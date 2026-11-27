#!/usr/bin/env python3
"""What a manifest's damage takes from each top-level vdev of an image,
against its redundancy: the arithmetic `expect.outcome` follows from.

A top-level vdev reads a block while no more of its members than its
parity are lost at the place the block is — a mirror of n members has
n - 1 to spare, a raidzN and a draidN N, a single device none. So what
counts is the most members lost at any one place:

  * a member absent, or overwritten over its whole span (`0..`, or the
    whole of its written space, `data:0%..100%`), is lost everywhere;
  * one overwritten, flipped or marked unreadable over part of its
    written space (`data:A%..B%`, `span:A%..B%`, a byte range) is lost
    there: two members of one raidz zeroed over the same percentages lose
    the same rows, over disjoint ones a row each;
  * damage to the labels, the boot area or the slack past the last
    metaslab takes no data.

Each top-level vdev the damage reaches is then `none` (nothing of it is
lost), `within` (fewer lost than its parity), `at` (as many) or `past`
(more), and the case as a whole is past where any vdev that holds data
is. A log device and a dedup vdev hold nothing a reader needs: past
them is still not past the pool's redundancy.

Where the arithmetic does not decide — a member moved within its device
or grown (where it is is the tool's to find), an older copy of a member
(stale for some blocks and right for others), flipped bits scattered
over more members than the parity (whether two of them meet is chance),
a slot under replacement (its devices stand in for one another), a block
aimed at by its pointer (its other copies, and the TXGs before it, are
the tool's to find) — the position is `?`. Label damage takes no data
and leaves the pool to be found, which is the tool's: its position is
`none`, and it decides no outcome.

Used by lint-manifests.py, which holds `expect.outcome` to it where it
decides, and by coverage.py, which tabulates it.
"""

import re

SIZE = re.compile(r"(-?\d+)\s*([KMG]i?B?)?$")
UNITS = {"K": 1 << 10, "M": 1 << 20, "G": 1 << 30}
LABEL_START = 4 << 20          # the two front labels and the boot area
REAR_LABELS = 512 << 10        # the two rear labels


def size(text):
    """Bytes of `512KiB`, `-8MiB`, `4096`.

    >>> size("512KiB"), size("-8MiB"), size("4096")
    (524288, -8388608, 4096)
    """
    m = SIZE.match(text.strip())
    if not m:
        raise ValueError(f"not a size: {text!r}")
    unit = (m.group(2) or "")[:1]
    return int(m.group(1)) * UNITS.get(unit, 1)


def member_loss(d):
    """What one damage of a member takes of its data: `whole`, a place
    (`(space, start, end)`, the space `pct` for the written space's
    percentages and `bytes` for a byte range), None for nothing, or `?`.
    And whether the loss is sparse (flipped bits: a few at random places).

    >>> [member_loss(d)[0] for d in (
    ...     {"pattern": "missing"},
    ...     {"pattern": "zeros", "range": "0.."},
    ...     {"pattern": "random", "range": "data:20%..30%"},
    ...     {"pattern": "zeros", "range": "label:all"},
    ...     {"pattern": "random", "range": "slack"},
    ...     {"pattern": "zeros", "range": "0..1MiB"},
    ...     {"pattern": "random", "range": "-512KiB.."},
    ...     {"pattern": "older-self:round6"},
    ...     {"pattern": "shift:2048"},
    ...     {"pattern": "unreadable", "range": "data:0%.."})]
    ['whole', 'whole', ('pct', 20.0, 30.0), None, None, None, None, '?', '?', 'whole']
    >>> member_loss({"pattern": "flip-bits:9", "range": "data:0%.."})
    ('whole', True)
    """
    pat = d.get("pattern", "")
    name = pat.split(":", 1)[0]
    if name == "missing":
        return "whole", False
    if name in ("older-self", "shift", "grow", "truncate", "forged-txg"):
        # Where the member is, how old it is, or what of its labels says
        # so is the tool's to find: not a loss this arithmetic counts.
        return ("?" if name != "forged-txg" else None), False
    if name not in ("zeros", "random", "flip-bits", "unreadable"):
        return "?", False
    sparse = name == "flip-bits"
    spec = d.get("range", "0..")
    if spec.startswith("label:") or spec == "slack":
        return None, sparse
    for prefix in ("data:", "span:"):
        if spec.startswith(prefix):
            a, _, b = spec[len(prefix):].partition("..")
            lo, hi = float(a.rstrip("%")), float(b.rstrip("%")) if b else 100.0
            if lo <= 0 and hi >= 100:
                return "whole", sparse
            return ("pct", lo, hi), sparse
    a, _, b = spec.partition("..")
    lo = size(a) if a else 0
    hi = size(b) if b else None
    if lo == 0 and hi is None:
        return "whole", sparse
    if lo >= 0 and hi is not None and hi <= LABEL_START:
        return None, sparse            # the front labels and the boot area
    if lo < 0 and hi is None and -lo <= REAR_LABELS:
        return None, sparse            # the rear labels
    return ("bytes", lo, hi if hi is not None else float("inf")), sparse


def parity(top):
    """How many members a top-level vdev can lose at one place.

    >>> parity({"kind": "mirror", "groups": [{"kind": "mirror", "count": 3}]})
    2
    >>> parity({"kind": "raidz2", "groups": [{"kind": "raidz2", "nparity": 2, "count": 4}]})
    2
    >>> parity({"kind": "file", "groups": [{"kind": "file", "count": 1}]})
    0
    """
    group = (top.get("groups") or [{}])[0]
    kind = group.get("kind", top.get("kind", ""))
    if kind == "mirror":
        return max(group.get("count", 1) - 1, 0)
    if "nparity" in group:
        return group["nparity"]
    m = re.match(r"(raidz|draid)(\d)", kind)
    return int(m.group(2)) if m else 0


def most_at_one_place(whole, places):
    """The most members lost at any one place: those lost everywhere and
    the most of the others whose places overlap.

    >>> most_at_one_place(1, [("pct", 20, 30), ("pct", 25, 40)]), most_at_one_place(0, [("pct", 0, 10), ("pct", 10, 20)])
    (3, 1)
    """
    best = 0
    for space in {p[0] for p in places}:
        spans = sorted((p[1], p[2]) for p in places if p[0] == space)
        events = sorted([(a, 1) for a, _ in spans] + [(b, -1) for _, b in spans])
        cur = 0
        for _, step in events:
            cur += step
            best = max(best, cur)
    return whole + best


def position(lost, spare):
    """`none`, `within`, `at` or `past`.

    >>> [position(n, 2) for n in (0, 1, 2, 3)]
    ['none', 'within', 'at', 'past']
    """
    if lost == 0:
        return "none"
    return "within" if lost < spare else "at" if lost == spare else "past"


def biases(status_text):
    """The class of each top-level vdev `zpool status` prints under a
    section of its own (`special`, `dedup`, `logs`), by id: what `zdb -C`
    does not print, and a layout made from it does not have.

    >>> biases("config:\\n\\n\\tNAME  STATE\\n\\tp  ONLINE\\n\\t  raidz1-0  ONLINE\\n\\t    /a  ONLINE\\n"
    ...        "\\tdedup\\t\\n\\t  mirror-2  ONLINE\\n\\t    /b  ONLINE\\n\\tspecial\\t\\n\\t  mirror-1  ONLINE\\n")
    {2: 'dedup', 1: 'special'}
    """
    out, section, inside = {}, None, False
    for raw in status_text.splitlines():
        if raw.startswith("config:"):
            inside = True
            continue
        if not inside or not raw.startswith("\t"):
            continue
        body = raw[1:]
        depth = (len(body) - len(body.lstrip(" "))) // 2
        name = body.strip().split()[0] if body.strip() else ""
        if depth == 0:
            section = name if name in ("special", "dedup", "logs") else None
        elif depth == 1 and section:
            m = re.search(r"-(\d+)$", name)
            if m:
                out[int(m.group(1))] = "log" if section == "logs" else section
    return out


def assess(manifest, layout, resolve):
    """Every top-level vdev the manifest's damage reaches, by index, with
    its kind, the members lost at its worst place, its parity and its
    position; and the case's: `none`, `within`, `at`, `past` or `?`.
    `resolve` turns a member reference into a role of the layout, or None.
    A target (a block aimed at by its pointer) is `?`: its copies, and
    the TXGs before it, are the tool's to find."""
    tops = {t["index"]: t for t in layout.get("tops", [])}
    members = layout.get("members", {})
    whole, places, sparse, unsure = {}, {}, {}, set()
    reached = set()
    case_unsure = False
    for d in manifest.get("damage", []):
        if "target" in d:
            case_unsure = True
            continue
        role = resolve(d.get("member"))
        if role is None or role not in members:
            case_unsure = True
            continue
        info = members[role]
        t = info["top"]
        reached.add(t)
        if "slot" in info or role in tops.get(t, {}).get("slot_devices", {}):
            unsure.add(t)              # a slot's devices stand in for one another
        loss, thin = member_loss(d)
        if loss == "?":
            unsure.add(t)
        elif loss == "whole":
            whole.setdefault(t, set()).add(role)
            sparse[t] = sparse.get(t, 0) + thin
        elif loss is not None:
            places.setdefault(t, []).append(loss)
            sparse[t] = sparse.get(t, 0) + thin
    out = {}
    for t in sorted(reached):
        top = tops.get(t, {})
        spare = parity(top)
        lost = most_at_one_place(len(whole.get(t, ())), places.get(t, []))
        pos = position(lost, spare)
        if t in unsure or (sparse.get(t, 0) and lost > spare):
            pos = "?"
        kind = top.get("kind", "?")
        if top.get("log"):
            kind += " (log)"
        elif top.get("alloc_bias"):
            kind += f" ({top['alloc_bias']})"
        out[t] = {"kind": kind, "lost": lost, "parity": spare, "position": pos,
                  "holds_data": not top.get("log") and top.get("alloc_bias") != "dedup"}
    order = ["none", "within", "at", "past"]
    if case_unsure or any(v["position"] == "?" for v in out.values() if v["holds_data"]):
        case = "?"
    else:
        case = max((v["position"] for v in out.values() if v["holds_data"]), key=order.index, default="none")
    return out, case


def implied(case, manifest):
    """The outcomes the arithmetic leaves a case: past the redundancy, a
    refusal (or the partial image it accepts); within or at it, the data
    back. None where the arithmetic does not decide — a case past its
    `?`, one that tells the tool something (`[recovery]`), or one whose
    labels are damaged, which is about finding the pool, not its data.

    A case that damages nothing has nothing to count: whether the tool
    reads the pool at all (an expanded raidz, which this build refuses)
    is no matter of redundancy.

    >>> d = {"damage": [{"member": "x", "pattern": "missing"}]}
    >>> implied("past", d), implied("at", d), implied("?", d), implied("within", {**d, "recovery": {"hints": "layout"}}), implied("none", {})
    ('refused', 'recovered', None, None, None)
    """
    if case == "?" or manifest.get("recovery") or not manifest.get("damage"):
        return None
    if any(d.get("range", "").startswith("label:") or d.get("pattern", "").startswith("forged-txg")
           for d in manifest.get("damage", [])):
        return None
    return "refused" if case == "past" else "recovered"


RECOVERED = {"recovered", "bit-exact", "reconstructed"}


def contradiction(implied_outcome, accepted):
    """What is wrong with the outcomes a manifest accepts, against the
    one the arithmetic leaves it, or None.

    >>> contradiction("recovered", ["refused"]), contradiction("refused", ["recovered", "refused"])
    ('the redundancy holds (within or at it), and it expects ["refused"]', None)
    >>> contradiction("refused", ["bit-exact"])
    'the damage is past the redundancy, and it expects ["bit-exact"] - a refusal, or a partial image, is what it leaves'
    """
    if implied_outcome == "recovered" and not RECOVERED & set(accepted):
        return f'the redundancy holds (within or at it), and it expects {accepted_text(accepted)}'
    if implied_outcome == "refused" and "refused" not in accepted:
        return (f"the damage is past the redundancy, and it expects {accepted_text(accepted)} - "
                "a refusal, or a partial image, is what it leaves")
    return None


def accepted_text(accepted):
    return "[" + ", ".join(f'"{a}"' for a in accepted) + "]"
