# Damage matrix run: image-v0-ztest

The damage matrix against the interim ztest-built image (no kernel, no
zvols — see [IMAGE.md](../../IMAGE.md)). Judged in *walk* mode: the
dataset list must match `zdb -d` and the object walker must read and
verify every block of every object, with the extracted content checked
against the checksums ZFS itself recorded in the block pointers.

*This run is tied to one particular ztest build (see the caveat in
[IMAGE.md](../../IMAGE.md)); the numbers describe that build, not a
fixture anyone else can reproduce byte for byte.*

| Pool | cases | pass | unexpected | defect | not applicable |
|---|---|---|---|---|---|
| mirror | 37 | 29 | 0 | 0 | 8 |
| raidz2 | 37 | 37 | 0 | 0 | 0 |
| draid1 | 37 | 33 | 0 | 0 | 4 |
| **total** | **111** | **99** | **0** | **0** | **12** |

## Every case

`—` means the manifest does not apply to that pool: it names a member or
a geometry the pool does not have.

| Manifest | mirror | raidz2 | draid1 |
|---|---|---|---|
| `combo-across-tops` | — | reconstructed | — |
| `combo-across-tops-one-past-budget` | — | refused | refused |
| `combo-bitflips-three-members` | — | reconstructed | refused |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | reconstructed |
| `combo-data-two-members-same-range` | refused | reconstructed | reconstructed |
| `combo-held-front-labels-everywhere` | — | bit-exact | bit-exact |
| `combo-held-labels-plus-two-missing` | — | refused | refused |
| `combo-held-rings-two-members` | refused | bit-exact | bit-exact |
| `combo-labels-plus-data` | bit-exact | reconstructed | reconstructed |
| `combo-missing-plus-unidentified` | refused | reconstructed | reconstructed |
| `combo-mos-copy-plus-member-gone` | — | reconstructed | — |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | reconstructed |
| `combo-rings-plus-data` | bit-exact | reconstructed | reconstructed |
| `combo-shift-plus-member-gone` | refused | reconstructed | reconstructed |
| `combo-triple-labels-data-member` | — | refused | reconstructed |
| `combo-truncate-plus-data` | bit-exact | reconstructed | reconstructed |
| `combo-two-members-gone` | refused | reconstructed | reconstructed |
| `combo-unidentified-plus-data` | refused | reconstructed | reconstructed |
| `data-bit-flips` | bit-exact | reconstructed | reconstructed |
| `data-gang-header` | bit-exact | reconstructed | bit-exact |
| `data-one-member` | bit-exact | reconstructed | bit-exact |
| `data-two-members-disjoint` | bit-exact | reconstructed | reconstructed |
| `data-two-members-same-range` | refused | reconstructed | reconstructed |
| `labels-all-four` | reconstructed | reconstructed | reconstructed |
| `labels-front-pair` | bit-exact | bit-exact | bit-exact |
| `labels-one-l0` | bit-exact | bit-exact | bit-exact |
| `labels-rear-pair` | bit-exact | bit-exact | bit-exact |
| `labels-rings-only` | bit-exact | bit-exact | bit-exact |
| `labels-vdev-phys-only` | reconstructed | reconstructed | reconstructed |
| `member-missing-one` | reconstructed | reconstructed | reconstructed |
| `member-missing-three` | — | refused | refused |
| `member-missing-two` | refused | reconstructed | reconstructed |
| `metadata-mos-every-copy` | refused | refused | — |
| `metadata-mos-one-copy` | bit-exact | reconstructed | — |
| `partition-gpt-rewritten` | bit-exact | bit-exact | bit-exact |
| `partition-start-shifted` | bit-exact | reconstructed | reconstructed |
| `partition-tail-truncated` | bit-exact | bit-exact | bit-exact |

## Reading the result

No defects: on every applicable case the tool either produced the data
the oracle recorded, or refused with a reason and offered nothing.
Inputs were unchanged after every run, checked by hashing each damaged
copy before and after.

What the combinations found was never a wrong answer from the tool; it
was three wrong assumptions in the matrix itself, which is what an
oracle-driven matrix is for:

* **Rear labels are not at the end of the file.** ZFS places L2 and L3
  relative to the member size rounded down to a whole 256 KiB label. One
  member of this image is not label-aligned, so a naive "last 512 KiB"
  range left its L2 nvlist intact and the whole damage class silently
  missed. Manifests now say `label:L2,L3` and the harness computes the
  offsets.
* **Damage must land where the data is.** These members are sparse; a
  range picked by eye mostly hit holes. `data:30%..40%` now addresses the
  written space, and `span:5%..25%` the same byte range on every member
  when the point is to destroy both copies of the same blocks.
* **dRAID parity is per group, not per vdev.** A group here is three
  columns wide out of sixteen children, so two or three impaired members
  rarely collide in one group and most rows keep a rebuildable column.
  Expecting a flat refusal after two losses was wrong.

The remaining *not applicable* cells are the interim image's shape: each
ztest pool carries one geometry, so a manifest naming a second top-level
vdev, or a fourth member, has nothing to bind to on some of them. The
kernel-built image will carry all three geometries in one pool.

