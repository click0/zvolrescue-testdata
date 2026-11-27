#!/usr/bin/env python3
"""The coverage of the manifests, stated: COVERAGE.md, written from them
and the oracles by the redundancy arithmetic (redundancy.py).

For every manifest, against the image of its pool it is written for (of
`golden`, the newest: golden-v2), every top-level vdev its damage
reaches is placed against that vdev's redundancy — `none` where nothing
of its data is lost, `within`, `at` or `past` its parity, `?` where the
arithmetic does not decide — and counted by the manifest's class and the
kind of the vdev. An empty cell is a combination no manifest tests.

Usage: tools/coverage.py [ROOT]            writes ROOT/COVERAGE.md
       tools/coverage.py --check [ROOT]    exits 1 when it is not what
                                           the manifests make of it
"""

import collections
import importlib.util
import os
import sys
import tomllib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import redundancy  # noqa: E402

spec = importlib.util.spec_from_file_location("lint", os.path.join(HERE, "lint-manifests.py"))
lint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint)

POSITIONS = ["none", "within", "at", "past", "?"]
CLASSES = ["labels", "partition", "metadata", "data", "member", "older-self", "combo", "control"]


def images_of(root):
    """Every oracle here by pool and by tag, as the linter reads them."""
    images = {}
    for d in sorted(os.listdir(os.path.join(root, "oracle"))):
        path = os.path.join(root, "oracle", d)
        if os.path.exists(os.path.join(path, "layout.json")):
            image = lint.Image(path)
            images.setdefault(image.pool, []).append(image)
            if image.tag and image.tag != image.pool:
                images.setdefault(image.tag, []).append(image)
    return images


def table(root):
    images = images_of(root)
    folder = os.path.join(root, "manifests")
    cells = collections.Counter()      # (class, position, kind) -> tops
    cases = collections.Counter()      # (class, case position) -> manifests
    decided = collections.Counter()    # class -> manifests whose outcome the arithmetic decides
    kinds, total, skipped = set(), 0, []
    for name in sorted(f for f in os.listdir(folder) if f.endswith(".toml")):
        m = tomllib.load(open(os.path.join(folder, name), "rb"))
        stem = name[:-len(".toml")]
        cls = stem.split("-", 1)[0] if not stem.startswith("older-self") else "older-self"
        pool = m.get("image", "golden")
        if pool not in images:
            skipped.append(stem)
            continue
        image = images[pool][-1]       # of a pool's images, the newest
        total += 1
        tops, case = redundancy.assess(m, image.layout, image.member)
        cases[(cls, case)] += 1
        if redundancy.implied(case, m) is not None:
            decided[cls] += 1
        for t in tops.values():
            kinds.add(t["kind"])
            cells[(cls, t["position"], t["kind"])] += 1
    return cells, cases, decided, sorted(kinds), total, skipped


def render(root):
    cells, cases, decided, kinds, total, skipped = table(root)
    out = ["# Coverage of the manifests", "",
           "Written by `tools/coverage.py` from the manifests and the oracles —",
           "do not edit by hand; the `Manifests` workflow fails when this file is",
           "not what they make of it. The arithmetic is `tools/redundancy.py`'s:",
           "every top-level vdev a manifest's damage reaches, on the image of its",
           "pool it is written for (of `golden`, the newest), is placed against",
           "the vdev's redundancy by the most of its members lost at any one",
           "place — `none` (nothing of its data lost: labels, the boot area, the",
           "slack), `within` (fewer than its parity), `at` (as many), `past`",
           "(more) — or `?` where the arithmetic does not decide (a member moved,",
           "grown or an older copy of itself, bits flipped over more members than",
           "the parity, a slot under replacement). A block aimed at by its pointer",
           "is counted by its case alone, and a class that damages no member",
           "(the control; metadata, every case of which aims at a block) has no",
           "rows here. An empty cell (—) is a combination no manifest tests.", "",
           f"{total} manifests" + (f"; not counted, their pool having no oracle here: {', '.join(skipped)}" if skipped else "") + ".",
           "", "## Top-level vdevs, by class and position", "",
           "| Class | Position | " + " | ".join(f"`{k}`" for k in kinds) + " |",
           "|---|---|" + "---|" * len(kinds)]
    for cls in CLASSES:
        if not any(cells.get((cls, p, k)) for p in POSITIONS for k in kinds):
            continue               # no member damage at all: control, and blocks aimed at
        for pos in POSITIONS:
            row = [cells.get((cls, pos, k), 0) for k in kinds]
            out.append(f"| {cls} | {pos} | " + " | ".join(str(n) if n else "—" for n in row) + " |")
    out += ["", "## Cases, by class", "",
            "The position of a case is its worst vdev's that holds data (a log",
            "device or a dedup vdev does not); where it is `none`, `within` or",
            "`at`, the arithmetic leaves the data recovered, and where it is",
            "`past`, a refusal or a partial image — and the linter holds",
            "`expect.outcome` to that, unless the case tells the tool something",
            "(`[recovery]`), damages labels (which is about finding the pool, not",
            "its data) or damages nothing (which is about whether the tool reads",
            "the pool at all).", "",
            "| Class | " + " | ".join(POSITIONS) + " | outcome decided |",
            "|---|" + "---|" * (len(POSITIONS) + 1)]
    for cls in CLASSES:
        row = [cases.get((cls, p), 0) for p in POSITIONS]
        if not any(row):
            continue
        out.append(f"| {cls} | " + " | ".join(str(n) if n else "—" for n in row) + f" | {decided.get(cls, 0)} |")
    return "\n".join(out) + "\n"


def main():
    args = sys.argv[1:]
    check = "--check" in args
    args = [a for a in args if a != "--check"]
    root = args[0] if args else "."
    text = render(root)
    path = os.path.join(root, "COVERAGE.md")
    if check:
        have = open(path).read() if os.path.exists(path) else ""
        if have != text:
            print("COVERAGE.md is not what the manifests make of it: run tools/coverage.py", file=sys.stderr)
            sys.exit(1)
        print("COVERAGE.md is current")
        return
    open(path, "w").write(text)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
