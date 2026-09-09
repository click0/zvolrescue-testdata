# Damage matrix run: image-v0-ztest

First run of the damage matrix, against the interim ztest-built image
(no kernel, no zvols — see [IMAGE.md](../../IMAGE.md)). Judged in *walk*
mode: the dataset list must match `zdb -d` and the object walker must read
and verify every block of every object.

| Pool | pass | unexpected | defect | not applicable |
|---|---|---|---|---|
| draid1 | 3 | 0 | 0 | 18 |
| mirror | 5 | 0 | 0 | 16 |
| raidz2 | 9 | 0 | 0 | 12 |
| **total** | **17** | **0** | **0** | **46** |

## What ran

| Manifest | mirror | raidz2 | draid1 |
|---|---|---|---|
| `combo-1` | — | — | — |
| `data-bit-flips` | pass (bit-exact) | — | — |
| `data-mirror-both-halves` | — | pass (bit-exact) | — |
| `data-raidz-column` | — | — | pass (reconstructed) |
| `labels-all-four` | — | — | pass (reconstructed) |
| `labels-front-pair` | — | — | pass (bit-exact) |
| `labels-one-l0` | — | — | pass (bit-exact) |
| `labels-rear-pair` | — | pass (bit-exact) | — |
| `labels-rings-forged-txg` | — | — | — |
| `labels-rings-only` | — | pass (bit-exact) | — |
| `labels-vdev-phys-only` | pass (reconstructed) | — | — |
| `member-missing-beyond-parity` | — | — | pass (refused) |
| `member-missing-raidz2` | — | — | pass (reconstructed) |
| `member-missing-two-raidz2` | — | — | pass (reconstructed) |
| `member-older-self` | — | — | — |
| `metadata-crypto-key-object` | — | — | — |
| `metadata-dnode-block` | — | — | — |
| `metadata-mos-one-copy` | — | pass (bit-exact) | pass (reconstructed) |
| `partition-gpt-rewritten` | — | — | pass (bit-exact) |
| `partition-start-shifted` | — | pass (bit-exact) | — |
| `partition-tail-truncated` | pass (bit-exact) | — | — |

## Reading the result

*This run is tied to one particular ztest build (see the caveat in
[IMAGE.md](../../IMAGE.md)); the numbers describe that build, not a
fixture anyone else can reproduce byte for byte.*

No defects: on every applicable case the tool either produced the data the
oracle recorded, or used redundancy and produced it, or refused with a
reason and offered nothing. Inputs were unchanged after every run.

The many *not applicable* cells are the interim image's limitation, not a
gap in the matrix: each ztest pool has one geometry, so a manifest naming
a `raidz2` member cannot run against the mirror pool. The kernel-built
image carries all three geometries in one pool and will run every manifest
against every one of them.

Two expectations were corrected while running, both mine rather than the
tool's: one MOS copy destroyed is transparent on a mirror but needs parity
on a raidz, and scattered bit flips may land in free space and need no
reconstruction at all. Both manifests now say so explicitly.

