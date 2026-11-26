#!/usr/bin/env python3
"""Keep a damage-matrix run's report here, as the next `reports/<tag>-rN/`.

The harness (`tests/golden/run-matrix.py` in zvolrescue) writes its
verdicts to `report-<label>.json` and `.md` in its `--out` directory;
`realworld.yml` there runs it against a published image every week and
calls this to keep what came of it, and a run made by hand is kept the
same way. The first run against a tag is `reports/<tag>/`, every later
one `reports/<tag>-r<N>/`, N one more than the highest there is. Into
it go the two report files, the matrix's log when there is one, and a
README.md written from the JSON: who ran it, against what, with which
commits, the counts, and every run that was not a plain pass.

Usage:
  tools/add-report.py REPORT_DIR --tag TAG [--root ROOT] [--by TEXT]
                      [--run-url URL] [--tool-commit SHA]
                      [--manifests-commit SHA] [--seconds N] [--held-out]
                      [--date YYYY-MM-DD]

Prints the directory it made, relative to ROOT (this repository,
default .). Exit 1, with nothing written, when the report is not there
or not the harness's.
"""

import argparse
import collections
import datetime
import json
import os
import re
import shutil
import sys


def next_dir(names, tag):
    """The directory the next run against `tag` goes in, given the names
    already in `reports/`.

    >>> next_dir([], "image-v1")
    'image-v1'
    >>> next_dir(["image-v1", "image-v1-r2", "image-v0-ztest-r2"], "image-v1")
    'image-v1-r3'
    >>> next_dir(["image-v1-r2"], "image-v1")
    'image-v1-r3'
    >>> next_dir(["image-v1", "image-v10"], "image-v1")
    'image-v1-r2'
    """
    runs = [1 for n in names if n == tag]
    runs += [int(m.group(1)) for n in names
             if (m := re.fullmatch(re.escape(tag) + r"-r(\d+)", n))]
    return tag if not runs else f"{tag}-r{max(runs) + 1}"


def pool_of(root, tag):
    """The pool whose oracle here names `tag` as its image, or None."""
    oracle = os.path.join(root, "oracle")
    for pool in sorted(os.listdir(oracle)) if os.path.isdir(oracle) else []:
        try:
            layout = json.load(open(os.path.join(oracle, pool, "layout.json")))
        except (OSError, ValueError):
            continue
        if layout.get("image_tag") == tag:
            return pool
    return None


def plural(n, one, many):
    """
    >>> plural(1, "manifest", "manifests"), plural(3, "manifest", "manifests")
    ('1 manifest', '3 manifests')
    """
    return f"{n} {one if n == 1 else many}"


def summary(records, tag, pool, number, run, by, tool, manifests, seconds, held_out, date):
    """The README of a run, from the harness's records.

    >>> recs = [
    ...     {"id": "a", "expected": "bit-exact", "actual": "bit-exact", "verdict": "pass",
    ...      "inputs_unchanged": True, "image": "golden"},
    ...     {"id": "b", "expected": "refused", "actual": "partial", "verdict": "pass",
    ...      "inputs_unchanged": True, "image": "golden"},
    ...     {"id": "c", "expected": "—", "actual": "n/a", "verdict": "n/a",
    ...      "notes": ["no such member"], "inputs_unchanged": True},
    ... ]
    >>> text = summary(recs, "image-v1", "golden", 3, "", "`realworld.yml` in zvolrescue, the weekly run",
    ...                "abcdef0123", "0123456789", 1722, False, "2026-11-30")
    >>> print(text.split("## ")[0].strip())  # doctest: +NORMALIZE_WHITESPACE
    # Damage matrix run: image-v1, run 3
    <BLANKLINE>
    The damage matrix against the published image `image-v1` (see
    [IMAGE.md](../../IMAGE.md)), judged against the oracle in
    `oracle/golden/`.
    <BLANKLINE>
    Run by `realworld.yml` in zvolrescue, the weekly run, on 2026-11-30.
    zvolrescue `abcdef0`, manifests at `0123456`: **3 manifests: pass 2,
    n/a 1**; inputs unchanged in every run; the held-out manifests not
    run; 1722 seconds.
    <BLANKLINE>
    Outcomes: 1 bit-exact, 1 partial.
    >>> "* `c` n/a: no such member" in text
    True
    """
    verdicts = collections.Counter(r["verdict"] for r in records)
    order = ["pass", "n/a", "unexpected", "defect"]
    counted = ", ".join(f"{v} {verdicts[v]}" for v in order + sorted(set(verdicts) - set(order))
                        if verdicts[v])
    actual = collections.Counter(r["actual"] for r in records if r["verdict"] != "n/a")
    wrote = [r["id"] for r in records if r.get("inputs_unchanged") is False]

    who = f"Run by {by}" if by else "Run"
    who += f", on {date}" + (f": {run}" if run else "") + "."
    what = []
    if tool:
        what.append(f"zvolrescue `{tool[:7]}`")
    if manifests:
        what.append(f"manifests at `{manifests[:7]}`")
    facts = (", ".join(what) + ": " if what else "") + \
        f"**{plural(len(records), 'manifest', 'manifests')}: {counted}**"
    facts += "; inputs unchanged in every run" if not wrote else \
        f"; **a run changed its inputs**: {', '.join(f'`{w}`' for w in wrote)}"
    facts += "; the held-out manifests run too" if held_out else "; the held-out manifests not run"
    if seconds:
        facts += f"; {seconds} seconds"
    facts += "."

    out = [f"# Damage matrix run: {tag}, run {number}", ""]
    oracle = f", judged against the oracle in `oracle/{pool}/`" if pool else ""
    out.append(wrap(f"The damage matrix against the published image `{tag}` (see "
                    f"[IMAGE.md](../../IMAGE.md)){oracle}."))
    out.append("")
    out.append(wrap(f"{who} {facts}"))
    out.append("")
    if actual:
        out.append(wrap("Outcomes: " + ", ".join(f"{n} {k}" for k, n in sorted(
            actual.items(), key=lambda kv: (-kv[1], kv[0]))) + "."))
        out.append("")
    # The files (zvolfiles), the history (zvoltimeline), the datasets
    # listed (list against zdb -d) and what scan read (against zdb -l,
    # zdb -u, zpool status), where the oracle had them to judge by.
    for side, what in (("files", "Files"), ("timeline", "History"), ("datasets", "Datasets"),
                       ("scan", "Scan")):
        got = collections.Counter(r[side]["actual"] for r in records if side in r)
        if got:
            out.append(wrap(f"{what}: " + ", ".join(f"{n} {k}" for k, n in sorted(
                got.items(), key=lambda kv: (-kv[1], kv[0]))) + "."))
            out.append("")

    notable = [r for r in records if r["verdict"] != "pass" or r.get("inputs_unchanged") is False]
    if notable:
        out.append("## Not a plain pass")
        out.append("")
        for r in notable:
            notes = "; ".join(r.get("notes") or [])
            if r["verdict"] == "n/a":
                out.append(f"* `{r['id']}` n/a" + (f": {notes}" if notes else ""))
            else:
                line = f"* **`{r['id']}`** {r['verdict']}: expected {r['expected']}, got {r['actual']}"
                out.append(line + (f" — {notes}" if notes else ""))
                for k, v in (r.get("outcomes") or {}).items():
                    if k != "refused_detail" and v != "ok":
                        out.append(f"  * {k}: {v}")
                for side in ("files", "timeline", "datasets", "scan"):
                    if r.get(side, {}).get("verdict", "pass") != "pass":
                        out.append(f"  * {side}: expected {r[side]['expected']}, got {r[side]['actual']}")
        out.append("")

    out += ["| File | What |", "|---|---|",
            f"| `report-{tag}.md`, `report-{tag}.json` | the verdict of every manifest, "
            "with the outcome per volume |"]
    return "\n".join(out) + "\n"


def wrap(text, width=72):
    """Lines of at most `width`, broken at spaces outside backticks.

    >>> wrap("a `b c` d", 5)
    'a\\n`b c`\\nd'
    """
    words, cur, inside = [], "", False
    for ch in text:
        if ch == "`":
            inside = not inside
        if ch == " " and not inside:
            words.append(cur)
            cur = ""
        else:
            cur += ch
    words.append(cur)
    lines, line = [], ""
    for w in words:
        if line and len(line) + 1 + len(w) > width:
            lines.append(line)
            line = w
        else:
            line = f"{line} {w}" if line else w
    lines.append(line)
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("report", help="the harness's --out directory")
    ap.add_argument("--tag", required=True, help="the image's tag; the report is report-<tag>.json")
    ap.add_argument("--root", default=".", help="this repository (default .)")
    ap.add_argument("--by", default="", help="who ran it, as the README says it")
    ap.add_argument("--run-url", default="")
    ap.add_argument("--tool-commit", default="")
    ap.add_argument("--manifests-commit", default="")
    ap.add_argument("--seconds", type=int, default=0)
    ap.add_argument("--held-out", action="store_true")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args()

    src = os.path.join(a.report, f"report-{a.tag}.json")
    try:
        records = json.load(open(src))
        if not isinstance(records, list) or not all(
                isinstance(r, dict) and {"id", "verdict", "actual", "expected"} <= r.keys()
                for r in records):
            raise ValueError("not a list of the harness's records")
    except (OSError, ValueError) as e:
        print(f"add-report: {src}: {e}", file=sys.stderr)
        return 1

    reports = os.path.join(a.root, "reports")
    os.makedirs(reports, exist_ok=True)
    name = next_dir(os.listdir(reports), a.tag)
    number = 1 if name == a.tag else int(name.rsplit("-r", 1)[1])
    dst = os.path.join(reports, name)
    os.mkdir(dst)

    pool = pool_of(a.root, a.tag)
    text = summary(records, a.tag, pool, number, a.run_url, a.by, a.tool_commit,
                   a.manifests_commit, a.seconds, a.held_out, a.date)
    shutil.copyfile(src, os.path.join(dst, f"report-{a.tag}.json"))
    md = os.path.join(a.report, f"report-{a.tag}.md")
    if os.path.exists(md):
        shutil.copyfile(md, os.path.join(dst, f"report-{a.tag}.md"))
    log = f"{pool or a.tag}-matrix.log"
    for have in ("matrix.log", log):
        if os.path.exists(os.path.join(a.report, have)):
            shutil.copyfile(os.path.join(a.report, have), os.path.join(dst, log))
            text += f"| `{log}` | the matrix's own log |\n"
            break
    with open(os.path.join(dst, "README.md"), "w") as f:
        f.write(text)
    print(os.path.relpath(dst, a.root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
