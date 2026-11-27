# Coverage of the manifests

Written by `tools/coverage.py` from the manifests and the oracles —
do not edit by hand; the `Manifests` workflow fails when this file is
not what they make of it. The arithmetic is `tools/redundancy.py`'s:
every top-level vdev a manifest's damage reaches, on the image of its
pool it is written for (of `golden`, the newest), is placed against
the vdev's redundancy by the most of its members lost at any one
place — `none` (nothing of its data lost: labels, the boot area, the
slack), `within` (fewer than its parity), `at` (as many), `past`
(more) — or `?` where the arithmetic does not decide (a member moved,
grown or an older copy of itself, bits flipped over more members than
the parity, a slot under replacement). A block aimed at by its pointer
is counted by its case alone, and a class that damages no member
(the control; metadata, every case of which aims at a block) has no
rows here. An empty cell (—) is a combination no manifest tests.

121 manifests.

## Top-level vdevs, by class and position

| Class | Position | `draid1` | `file (log)` | `mirror` | `mirror (dedup)` | `mirror (special)` | `raidz1` | `raidz2` |
|---|---|---|---|---|---|---|---|---|
| labels | none | 9 | — | 10 | — | — | — | 16 |
| labels | within | — | — | — | — | — | — | — |
| labels | at | — | — | — | — | — | — | — |
| labels | past | — | — | — | — | — | — | — |
| labels | ? | — | — | — | — | — | — | — |
| partition | none | — | — | — | — | — | 1 | 1 |
| partition | within | — | — | — | — | — | — | — |
| partition | at | — | — | — | — | — | — | — |
| partition | past | — | — | — | — | — | — | — |
| partition | ? | — | — | — | — | — | — | 3 |
| data | none | — | — | — | — | — | — | — |
| data | within | — | — | — | — | — | — | 7 |
| data | at | 1 | — | 1 | — | — | 2 | 2 |
| data | past | 1 | — | 1 | — | — | 1 | — |
| data | ? | — | — | — | — | — | — | — |
| member | none | — | — | — | — | — | — | — |
| member | within | — | — | — | — | — | — | 1 |
| member | at | — | — | 6 | — | 1 | 5 | 3 |
| member | past | — | 2 | 1 | 1 | 1 | — | 1 |
| member | ? | — | — | — | — | — | — | 2 |
| older-self | none | — | — | — | — | — | — | — |
| older-self | within | — | — | — | — | — | — | — |
| older-self | at | — | — | — | — | — | — | — |
| older-self | past | — | — | — | — | — | — | — |
| older-self | ? | 1 | — | 2 | — | — | — | 1 |
| combo | none | — | — | — | — | — | — | 2 |
| combo | within | — | — | — | — | — | — | 12 |
| combo | at | — | — | 1 | — | — | — | 4 |
| combo | past | 1 | — | — | — | — | — | — |
| combo | ? | — | — | — | — | — | — | 5 |

## Cases, by class

The position of a case is its worst vdev's that holds data (a log
device or a dedup vdev does not); where it is `none`, `within` or
`at`, the arithmetic leaves the data recovered, and where it is
`past`, a refusal or a partial image — and the linter holds
`expect.outcome` to that, unless the case tells the tool something
(`[recovery]`), damages labels (which is about finding the pool, not
its data) or damages nothing (which is about whether the tool reads
the pool at all).

| Class | none | within | at | past | ? | outcome decided |
|---|---|---|---|---|---|---|
| labels | 17 | — | — | — | — | 2 |
| partition | 2 | — | — | — | 3 | 2 |
| metadata | 2 | — | — | — | 10 | 0 |
| data | — | 7 | 6 | 3 | 7 | 16 |
| member | 3 | 1 | 13 | 3 | 2 | 20 |
| older-self | — | — | — | — | 4 | 0 |
| combo | 2 | 8 | 5 | 1 | 8 | 6 |
| control | 14 | — | — | — | — | 0 |
