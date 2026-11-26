#!/usr/bin/env python3
"""Check every damage manifest against the format and the oracle.

The harness that applies the manifests lives in zvolrescue
(`tests/golden/run-matrix.py`); a manifest it cannot place is reported
`n/a` there, and one with a key misspelt is a key left out, which is
worse: what stands for it is a default. This says so before a run does,
on every push here:

  * the file parses, and its `id` is its name;
  * every key is one the format has, at every level;
  * patterns, ranges and structure targets are in the format's grammar;
  * every member, top-level vdev, dataset and volume a manifest names is
    in the oracle of the pool it is written against: the one its `image`
    names, by the name that pool's `layout.json` gives, and `golden`
    where it names none;
  * an older copy is named only for a member the image's release holds
    one of;
  * expected outcomes are the format's, and never `defect`, for kinds of
    group ZFS has (a manifest may expect for a kind the published image
    lacks: it is also run on pools `ztest` builds);
  * the count `manifests/README.md` gives is the number of manifests.

Usage: tools/lint-manifests.py [ROOT]   (ROOT: this repository, default .)
Exit 0 when every manifest passes, 1 otherwise, with every finding listed.
"""

import json
import os
import re
import sys
import tomllib

CLASSES = {"labels", "partition", "metadata", "data", "member", "older-self"}
OUTCOMES = {"recovered", "bit-exact", "reconstructed", "refused"}
TOP_KEYS = {"id", "description", "classes", "damage", "expect", "held_out", "recovery", "image"}
DAMAGE_KEYS = {"member", "target", "pattern", "range"}
TARGET_KEYS = {"object", "block", "copy", "pieces", "level"}
EXPECT_KEYS = {"outcome", "volumes", "by_group_kind", "evidence"}
RECOVERY_KEYS = {"assume_members"}
MEMBER_KEYS = {"leaf", "top", "kind"}
SHAPES = {"objset", "dnode-block", "data", "indirect", "crypto-key"}
LABEL_PARTS = {"", "whole", "vdev_phys", "rings", "uberblocks"}
SIZE = re.compile(r"-?\d+\s*([KMG]i?B?)?")
PERCENT = re.compile(r"\d+(\.\d+)?%")
RING_SLOTS = 32
# The kinds of group a manifest may give an expectation for. A manifest
# is run against the published image and against the pools the harness
# builds with `ztest` on the spot, so it may name a kind the published
# image does not have.
GROUP_KINDS = {"mirror", "raidz1", "raidz2", "raidz3", "draid1", "draid2", "draid3"}


class Image:
    """What the oracle of one image says a manifest may name."""

    def __init__(self, oracle):
        self.dir = oracle
        layout = json.load(open(os.path.join(oracle, "layout.json")))
        self.tag = layout.get("image_tag", "")
        self.members = layout["members"]
        self.kinds = {m["group_kind"] for m in self.members.values()}
        self.tops = {m["top"] for m in self.members.values()}
        self.pool = pool = layout["pool"]
        # Without a `zfs list` capture (a pool `ztest` built) the names
        # of its datasets are not known here, and are not checked.
        self.datasets = None
        listed = os.path.join(oracle, "zfs-list.txt")
        if os.path.exists(listed):
            names = [line.split("\t")[0] for line in open(listed)]
            self.datasets = {n[len(pool) + 1:] for n in names if "@" not in n and n != pool}
        self.volumes = set()
        hashed = os.path.join(oracle, "volumes.sha256")
        if os.path.exists(hashed):
            for line in open(hashed):
                name = line.split()[1].split("@")[0]
                self.volumes |= {name, name[len(pool) + 1:]}
        self.older = set()
        release = os.path.join(oracle, "SHA256SUMS-release.txt")
        if os.path.exists(release):
            for line in open(release):
                f = line.split()[1]
                if f.startswith("round6-"):
                    self.older.add(f[len("round6-"):-len(".zst")])

    def member(self, spec):
        """The member a reference names, as the harness resolves it, or
        None. A string is a member's role or `<kind>-<i>[a-d]`; a table
        is {kind, leaf, top}, with the widest top-level vdev when it
        gives neither kind nor top."""
        if isinstance(spec, str):
            if spec in self.members:
                return spec
            m = re.fullmatch(r"([a-z0-9]+)-(\d+)([a-d])?", spec)
            if not m:
                return None
            leaf = int(m.group(2)) if not m.group(3) else "abcd".index(m.group(3))
            return self.member({"kind": m.group(1), "leaf": leaf})
        kind, leaf, top = spec.get("kind"), spec.get("leaf", 0), spec.get("top")
        if top is None and not kind:
            counts = {}
            for info in self.members.values():
                counts[info["top"]] = counts.get(info["top"], 0) + 1
            top = min(counts, key=lambda t: (-counts[t], t))
        for role, info in self.members.items():
            if kind and info["group_kind"] != kind:
                continue
            if top is not None and info["top"] != top:
                continue
            if info["index"] == leaf:
                return role
        return None


def check_range(spec):
    """None, or what is wrong with a `range`."""
    if not isinstance(spec, str):
        return "a range is a string"
    if spec.startswith("label:"):
        which, _, part = spec[len("label:"):].partition("/")
        if which not in ("all", ""):
            for name in which.split(","):
                if name.strip() not in ("L0", "L1", "L2", "L3"):
                    return f"label {name!r} is none of L0..L3"
        if part not in LABEL_PARTS:
            return f"label part {part!r} is none of {sorted(LABEL_PARTS - {''})}"
        return None
    for prefix in ("data:", "span:"):
        if spec.startswith(prefix):
            a, sep, b = spec[len(prefix):].partition("..")
            if not sep or not PERCENT.fullmatch(a) or (b and not PERCENT.fullmatch(b)):
                return f"{prefix} takes N%..M% or N%.."
            return None
    a, sep, b = spec.partition("..")
    if not sep:
        return "a byte range is start..end"
    for side in (a, b):
        if side and not SIZE.fullmatch(side.strip()):
            return f"{side!r} is not a size (N, with K/M/G, KiB/MiB/GiB)"
    return None


def check_pattern(pattern, image, role, rng):
    """Findings about one damage's pattern."""
    out = []
    name, _, arg = pattern.partition(":")
    if name in ("zeros", "random", "truncate", "missing") and not arg:
        if name == "missing" and rng is not None:
            out.append("`missing` takes no range: the member is not given at all")
    elif name in ("flip-bits", "shift") and arg.isdigit() and int(arg) > 0:
        pass
    elif name == "grow" and arg and SIZE.fullmatch(arg):
        pass
    elif name == "older-self" and arg:
        if image.tag and arg != f"{image.tag}-round6":
            out.append(f"older-self source {arg!r} is not this image's ({image.tag}-round6)")
        if role and image.members[role]["file"] not in image.older:
            out.append(f"no older copy of {image.members[role]['file']} in the release")
    elif name == "forged-txg" and arg.isdigit() and int(arg) > 0:
        if int(arg) % RING_SLOTS == 0:
            out.append(f"forged-txg:{arg} lands on the slot it came from")
        if not (isinstance(rng, str) and rng.startswith("label:")
                and rng.endswith(("/rings", "/uberblocks"))):
            out.append("forged-txg needs a `label:…/rings` range")
    else:
        out.append(f"pattern {pattern!r} is not in the format")
    return out


def check_target(target, image):
    out = []
    if not isinstance(target, dict):
        return ["a target is a table"]
    out += [f"target key {k!r} is not in the format" for k in target if k not in TARGET_KEYS]
    obj = target.get("object")
    if not isinstance(obj, str) or ":" not in obj:
        return out + ["a target names `object = \"<dataset>:<shape>\"`"]
    dataset, _, shape = obj.rpartition(":")
    if shape not in SHAPES:
        out.append(f"shape {shape!r} is none of {sorted(SHAPES)}")
    if dataset == "mos":
        if shape != "objset":
            out.append("of the MOS only `mos:objset` is a target")
    elif dataset != "any" and image.datasets is not None and dataset not in image.datasets:
        out.append(f"no dataset {dataset!r} in the oracle")
    elif (shape in ("data", "indirect") and dataset != "any" and image.datasets is not None
          and dataset not in image.volumes):
        out.append(f"{dataset!r} is not a volume: `{shape}` is a volume's")
    block = target.get("block")
    if block is not None and not (
        (isinstance(block, int) and not isinstance(block, bool) and block >= 0)
        or block == "all"
        or (isinstance(block, str) and block.startswith("on:") and block[3:] in image.kinds)
    ):
        out.append(f"block {block!r} is an index, `all` or on:<kind> of {sorted(image.kinds)}")
    copy = target.get("copy")
    if copy is not None and not (copy == "all" or (isinstance(copy, int) and 0 <= copy <= 2)):
        out.append(f"copy {copy!r} is 0, 1, 2 or `all`")
    if target.get("pieces", "all") not in ("all", "one"):
        out.append(f"pieces {target['pieces']!r} is `all` or `one`")
    level = target.get("level")
    if level is not None and not (isinstance(level, int) and level >= 0):
        out.append(f"level {level!r} is a level of the block tree, 0 and up")
    return out


def check_member_spec(spec, image):
    out = []
    if isinstance(spec, dict):
        out += [f"member key {k!r} is not in the format" for k in spec if k not in MEMBER_KEYS]
        if "top" in spec and spec["top"] not in image.tops:
            out.append(f"top-level vdev {spec['top']} is not in the image ({sorted(image.tops)})")
    elif not isinstance(spec, str):
        return ["a member is a name or {leaf, top, kind}"]
    role = image.member(spec)
    if role is None:
        out.append(f"no member {spec} in the image")
    return out, role


def check_outcome(value, where):
    values = [value] if isinstance(value, str) else value
    if not isinstance(values, list) or not values:
        return [f"{where} is an outcome or a list of them"]
    out = []
    for v in values:
        if v == "defect":
            out.append(f"{where}: `defect` is what a run outside its category is, never what one expects")
        elif v not in OUTCOMES:
            out.append(f"{where}: {v!r} is none of {sorted(OUTCOMES)}")
    return out


def lint(path, images):
    """Every finding about one manifest file."""
    stem = os.path.basename(path)[: -len(".toml")]
    try:
        m = tomllib.load(open(path, "rb"))
    except tomllib.TOMLDecodeError as e:
        return [f"does not parse: {e}"]
    out = [f"key {k!r} is not in the format" for k in m if k not in TOP_KEYS]
    pool = m.get("image", "golden")
    if not isinstance(pool, str) or pool not in images:
        return out + [f"image {pool!r} names no pool an oracle here describes ({sorted(images)})"]
    image = images[pool]
    if m.get("id") != stem:
        out.append(f"id {m.get('id')!r} is not the file's name {stem!r}")
    if not stem.startswith(tuple(f"{c}-" for c in CLASSES | {"combo"})):
        out.append("a manifest is named <class>-<variant> or combo-<variant>")
    if not isinstance(m.get("description"), str) or not m["description"].strip():
        out.append("no description")
    classes = m.get("classes")
    if not isinstance(classes, list) or not classes:
        out.append("no classes")
    else:
        out += [f"class {c!r} is none of {sorted(CLASSES)}" for c in classes if c not in CLASSES]
    if "held_out" in m and not isinstance(m["held_out"], bool):
        out.append("held_out is true or false")

    damage = m.get("damage")
    if not isinstance(damage, list) or not damage:
        out.append("no [[damage]]")
        damage = []
    for i, d in enumerate(damage, 1):
        at = f"damage {i}"
        out += [f"{at}: key {k!r} is not in the format" for k in d if k not in DAMAGE_KEYS]
        if ("member" in d) == ("target" in d):
            out.append(f"{at}: names a member or a target, one of the two")
            continue
        pattern = d.get("pattern")
        if not isinstance(pattern, str):
            out.append(f"{at}: no pattern")
            continue
        role = None
        if "target" in d:
            if "range" in d:
                out.append(f"{at}: a target is placed by the oracle, not by a range")
            out += [f"{at}: {e}" for e in check_target(d["target"], image)]
            if pattern not in ("zeros", "random") and not pattern.startswith("flip-bits:"):
                out.append(f"{at}: a target is overwritten (zeros, random, flip-bits), not {pattern!r}")
        else:
            found, role = check_member_spec(d["member"], image)
            out += [f"{at}: {e}" for e in found]
            if "range" in d:
                problem = check_range(d["range"])
                if problem:
                    out.append(f"{at}: {problem}")
        out += [f"{at}: {e}" for e in check_pattern(pattern, image, role, d.get("range"))]

    expect = m.get("expect")
    if not isinstance(expect, dict):
        out.append("no [expect]")
    else:
        out += [f"expect: key {k!r} is not in the format" for k in expect if k not in EXPECT_KEYS]
        if "outcome" not in expect:
            out.append("expect: no outcome")
        else:
            out += check_outcome(expect["outcome"], "expect.outcome")
        for kind, alt in expect.get("by_group_kind", {}).items():
            if kind not in GROUP_KINDS:
                out.append(f"expect.by_group_kind: {kind!r} is no kind of group ({sorted(GROUP_KINDS)})")
            out += check_outcome(alt, f"expect.by_group_kind.{kind}")
        volumes = expect.get("volumes", "all")
        if volumes != "all":
            if not isinstance(volumes, list) or not volumes:
                out.append("expect.volumes is `all` or a list of volumes")
            else:
                out += [f"expect.volumes: no volume {v!r} in the oracle"
                        for v in volumes if v not in image.volumes]
        evidence = expect.get("evidence", [])
        if not isinstance(evidence, list) or not all(isinstance(e, str) for e in evidence):
            out.append("expect.evidence is a list of strings")

    recovery = m.get("recovery", {})
    out += [f"recovery: key {k!r} is not in the format" for k in recovery if k not in RECOVERY_KEYS]
    for spec in recovery.get("assume_members", []):
        found, _ = check_member_spec(spec, image)
        out += [f"recovery.assume_members: {e}" for e in found]
    return out


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    # Every pool an oracle here describes, by the name its layout gives;
    # of several oracles of one pool, the one whose directory is named
    # after it.
    images = {}
    for d in sorted(os.listdir(os.path.join(root, "oracle"))):
        path = os.path.join(root, "oracle", d)
        if not os.path.exists(os.path.join(path, "layout.json")):
            continue
        image = Image(path)
        if image.pool not in images or d == image.pool:
            images[image.pool] = image
    folder = os.path.join(root, "manifests")
    files = sorted(f for f in os.listdir(folder) if f.endswith(".toml"))
    failed = 0
    for f in files:
        findings = lint(os.path.join(folder, f), images)
        for e in findings:
            print(f"manifests/{f}: {e}")
        failed += bool(findings)
    readme = open(os.path.join(folder, "README.md")).read()
    said = re.search(r"The (\d+) manifests", readme)
    if said and int(said.group(1)) != len(files):
        print(f"manifests/README.md: says {said.group(1)} manifests, and there are {len(files)}")
        failed += 1
    print(f"{len(files)} manifest(s), {failed} with findings")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
