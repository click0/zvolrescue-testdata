# Damage matrix run: image-v0-ztest

The damage matrix against the interim ztest-built image (no kernel, no
zvols — see [IMAGE.md](../../IMAGE.md)). Judged in *walk* mode: the
dataset list must match `zdb -d` and the object walker must read and
verify every block of every object, with the extracted content checked
against the checksums ZFS itself recorded in the block pointers.

*This run is tied to one particular ztest build (see the caveat in
[IMAGE.md](../../IMAGE.md)); the numbers describe that build, not a
fixture anyone else can reproduce byte for byte.* The image was rebuilt
for this run, so its geometry differs from the first: the mirror pool's
second top-level vdev is a log this time, and the draid1 is 16 children
in groups of `ndata` 2 + `nparity` 1.

| Pool | cases | pass | unexpected | defect | not applicable |
|---|---|---|---|---|---|
| mirror | 35 | 29 | 0 | 0 | 6 |
| raidz2 | 35 | 34 | 0 | 0 | 1 |
| draid1 | 35 | 31 | 0 | 0 | 4 |
| **total** | **105** | **94** | **0** | **0** | **11** |

## Every case

`—` means the manifest does not apply to that pool: it names a member or
a geometry the pool does not have.

| Manifest | mirror | raidz2 | draid1 |
|---|---|---|---|
| `combo-across-tops` | — | — | — |
| `combo-across-tops-one-past-budget` | — | refused | reconstructed |
| `combo-bitflips-three-members` | — | reconstructed | reconstructed |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | reconstructed |
| `combo-data-two-members-same-range` | refused | reconstructed | reconstructed |
| `combo-labels-plus-data` | bit-exact | reconstructed | reconstructed |
| `combo-missing-plus-unidentified` | refused | reconstructed | reconstructed |
| `combo-mos-copy-plus-member-gone` | — | reconstructed | — |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | reconstructed |
| `combo-rings-plus-data` | bit-exact | reconstructed | reconstructed |
| `combo-shift-plus-member-gone` | bit-exact | reconstructed | reconstructed |
| `combo-triple-labels-data-member` | — | refused | reconstructed |
| `combo-truncate-plus-data` | bit-exact | reconstructed | reconstructed |
| `combo-two-members-gone` | refused | reconstructed | reconstructed |
| `combo-unidentified-plus-data` | refused | reconstructed | reconstructed |
| `combo-vdev-phys-gone-and-member-missing` | refused | reconstructed | reconstructed |
| `data-bit-flips` | bit-exact | reconstructed | reconstructed |
| `data-gang-header` | bit-exact | bit-exact | bit-exact |
| `data-one-member` | bit-exact | reconstructed | reconstructed |
| `data-two-members-disjoint` | bit-exact | reconstructed | reconstructed |
| `data-two-members-same-range` | refused | reconstructed | reconstructed |
| `labels-all-four` | reconstructed | reconstructed | reconstructed |
| `labels-front-pair` | bit-exact | bit-exact | bit-exact |
| `labels-one-l0` | bit-exact | bit-exact | bit-exact |
| `labels-rear-pair` | bit-exact | bit-exact | bit-exact |
| `labels-rings-only` | bit-exact | bit-exact | bit-exact |
| `labels-vdev-phys-only` | reconstructed | reconstructed | reconstructed |
| `member-missing-one` | reconstructed | reconstructed | reconstructed |
| `member-missing-three` | — | refused | reconstructed |
| `member-missing-two` | refused | reconstructed | reconstructed |
| `metadata-mos-every-copy` | refused | refused | — |
| `metadata-mos-one-copy` | bit-exact | reconstructed | — |
| `partition-gpt-rewritten` | bit-exact | bit-exact | bit-exact |
| `partition-start-shifted` | bit-exact | bit-exact | bit-exact |
| `partition-tail-truncated` | bit-exact | bit-exact | bit-exact |

## Reading the result

Two damage classes changed meaning in this run, because the tool grew
the ability to answer them rather than merely survive them:

* **A member that starts somewhere else.** `combo-shift-plus-member-gone`
  used to expect a refusal on a two-way mirror: a shifted member was
  unusable, so with the other member gone there was nothing left. The
  zero point recovered from an uberblock's own offset verifier (SPEC
  F-61) puts the shifted member back, and the pool now reads bit-exact.
* **A member with no labels at all.**
  `combo-vdev-phys-gone-and-member-missing` is new: one member's four
  `vdev_phys` areas zeroed *and* another member absent, so redundancy
  alone no longer covers it. The manifest tells the tool the member
  belongs (`[recovery] assume_members`), and the tool works out which
  leaf by reading through it (SPEC F-62). On the two-way mirror there is
  no configuration left anywhere and the refusal is the right answer;
  on raidz2 and draid1 the pool comes back.

Both cases exposed something to fix in the tool, not in the manifests:

1. With no surviving label anywhere, `--assume-member` reported a usage
   error where the honest answer is unreadable evidence (exit 2).
2. Where several vacant leaves read equally well — a raidz2 or draid1
   that has lost one member reads whichever slot the label-less member
   is put in — refusing cost the recovery for nothing, since every block
   is checksum-verified either way. The tool now takes the first
   candidate, lists them all and says `=GUID` pins one.

A third correction was to the manifests themselves: `member-missing-three`
and `combo-across-tops-one-past-budget` expected a refusal after three
absent members, which holds for raidz but not for this image's dRAID —
its parity budget is per redundancy group of 3 columns out of 16
children, so three losses rarely collide in one group.
