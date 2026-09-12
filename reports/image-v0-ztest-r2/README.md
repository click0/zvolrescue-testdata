# Damage matrix run: image-v0-ztest, second build

The damage matrix against a second `ztest`-built interim image (no
kernel, no zvols — see [IMAGE.md](../../IMAGE.md)). Judged in *walk*
mode: the dataset list must match `zdb -d` and the object walker must
read and verify every block of every object.

*Tied to one particular ztest build, like the first run. This build's
mirror pool has two data top-level vdevs rather than one and a log, which
changes what several manifests mean: losing "two members" can now mean
losing one whole top-level vdev while the other survives.*

**This run supersedes [image-v0-ztest](../image-v0-ztest/README.md),
whose draid1 column was void** — the layout generator read a member under
replacement as a group of its own and described that pool by its two
spare devices instead of its sixteen members.

| Pool | cases | pass | unexpected | defect | not applicable |
|---|---|---|---|---|---|
| mirror | 41 | 36 | 0 | 0 | 5 |
| raidz2 | 41 | 41 | 0 | 0 | 0 |
| draid1 | 41 | 35 | 0 | 0 | 6 |
| **total** | **123** | **112** | **0** | **0** | **11** |

Every applicable case landed where the redundancy ZFS guarantees says it
should. That was not true when this run was first made: it found one
defect, `combo-vdev-phys-gone-and-member-missing`, where a pool that had
lost every identifiable member of one top-level vdev was told
`--assume-member …: no scanned pool is missing a member` — which the
labels contradict, since they carry `vdev_children`. Refusing was right;
the reason given was not. The tool now names the vdev nothing describes
and points at what would help, and the case passes as `refused`.

## Why the eleven were not applicable

* **6** — no such member in this geometry.
* **5** — the dRAID permutation, which this harness does not map.

"No such member in this geometry" is the pool's shape answering: a mirror
group has two members, so a manifest that needs a third impaired one has
nothing to address, and a single-top dRAID has no second top-level vdev
to damage across. The dRAID permutation is a limit of this harness and
not of the tool — it is where the matrix cannot yet state the right
answer. Both are listed in
[manifests/README.md](../../manifests/README.md) with what they cost, so
an empty cell is never mistaken for a pass.

## Every case

`—` means the manifest does not apply: it names a member, a geometry or a
structure the pool or this harness does not have.

| Manifest | mirror | raidz2 | draid1 |
|---|---|---|---|
| `combo-across-tops` | reconstructed | reconstructed | — |
| `combo-across-tops-one-past-budget` | — | refused | refused |
| `combo-bitflips-three-members` | — | reconstructed | refused |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | reconstructed |
| `combo-data-two-members-same-range` | refused | reconstructed | reconstructed |
| `combo-label-flips-plus-data` | reconstructed | reconstructed | reconstructed |
| `combo-labels-plus-data` | bit-exact | reconstructed | reconstructed |
| `combo-missing-plus-unidentified` | refused | reconstructed | reconstructed |
| `combo-mos-copy-plus-member-gone` | — | reconstructed | — |
| `combo-objset-copy-plus-member-gone` | reconstructed | reconstructed | — |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | reconstructed |
| `combo-rings-plus-data` | bit-exact | reconstructed | reconstructed |
| `combo-shift-plus-member-gone` | bit-exact | reconstructed | reconstructed |
| `combo-triple-labels-data-member` | — | refused | reconstructed |
| `combo-truncate-plus-data` | bit-exact | reconstructed | reconstructed |
| `combo-two-members-gone` | refused | reconstructed | reconstructed |
| `combo-unidentified-plus-data` | reconstructed | reconstructed | reconstructed |
| `combo-vdev-phys-gone-and-member-missing` | refused | reconstructed | reconstructed |
| `data-bit-flips` | bit-exact | bit-exact | reconstructed |
| `data-gang-header` | bit-exact | reconstructed | bit-exact |
| `data-one-member` | bit-exact | reconstructed | reconstructed |
| `data-two-members-disjoint` | bit-exact | reconstructed | reconstructed |
| `data-two-members-same-range` | refused | reconstructed | reconstructed |
| `data-zeros-one-member` | bit-exact | reconstructed | reconstructed |
| `data-zeros-two-members-same-range` | refused | reconstructed | reconstructed |
| `labels-all-four` | reconstructed | reconstructed | reconstructed |
| `labels-bit-flips-all-four` | reconstructed | reconstructed | reconstructed |
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
| `metadata-objset-one-copy` | bit-exact | reconstructed | — |
| `partition-gpt-rewritten` | bit-exact | bit-exact | bit-exact |
| `partition-start-shifted` | bit-exact | bit-exact | bit-exact |
| `partition-tail-truncated` | bit-exact | bit-exact | bit-exact |
