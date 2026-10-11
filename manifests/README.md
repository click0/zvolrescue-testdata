# Damage manifests

A manifest describes one test case: which members of the golden image are
copied, what is overwritten in the copies, and which outcome category the
run must land in. Manifests are applied by zvolrescue's test harness to
temporary copies; the golden image itself is never modified.

## Format

One manifest per file, TOML, named `<class>-<variant>.toml` for single
classes and `combo-<n>.toml` for combinations.

```toml
# manifests/labels-front-pair.toml
id = "labels-front-pair"
description = "Both front labels (L0, L1) of one RAIDZ2 member zeroed"
classes = ["labels"]          # for combination bookkeeping

[[damage]]
member = "raidz2-1"           # member name from IMAGE.md
range = "0..512KiB"           # byte range in the member; sizes in KiB/MiB/GiB
pattern = "zeros"             # zeros | random | flip-bits:<n> | shift:<sectors> | truncate | missing | older-self:<source>

[expect]
outcome = "bit-exact"         # bit-exact | reconstructed | refused | (never "defect")
volumes = "all"               # which oracle volumes are compared, or a list
evidence = ["label L0 missing", "label L2 used"]   # substrings the evidence log must contain (optional)
```

`expect.outcome` is derived from the redundancy ZFS guarantees for the
damage, not from what the tool does today. `bit-exact` means every judged
volume hashed equal to the oracle without any use of redundancy;
`reconstructed` means the hashes are equal but the evidence log shows
redundancy at work (a member reported missing, a mirror half skipped, a
parity or combinatorial reconstruction); `refused` means the tool stopped
with exit 3 for every judged volume and presented no partial output as
good. A run that lands anywhere else
is a tool defect. Every run also asserts that the SHA-256 of each damaged
copy is unchanged after the tool ran (read-only invariant).

Ranges are `start..end` in bytes with `KiB`/`MiB`/`GiB` suffixes; a
negative start counts from the end of the member (`-512KiB..` is the last
512 KiB), `0..` is the whole member. Patterns: `zeros`, `random` (seeded per
manifest, so reproducible), `flip-bits:<n>` (n single-bit flips spread over
the range), `shift:<sectors>` (the member's content moved forward, the
image grows), `truncate` (the range is cut off, the image shrinks),
`missing` (the member is not passed to the tool at all; no range), and
`older-self:<source>` — the range is replaced by the same range of an
earlier consistent copy of the member (`image-v1-round6` = the `round6-*`
release files of tag `image-v1`): the "member replaced by an older copy of
itself" case, where everything verifies but nothing is current.

A damage may also name a structure instead of a range:

```toml
[[damage]]
target = { object = "vm/disk-16k:dnode-block", block = 0, copy = "all" }   # or copy = 0 / 1 / 2
pattern = "random"
```

`object` is `mos:objset`, `<dataset>:objset`, or — from the oracle's
`zdb -dddddd` capture, where the image has one — `<dataset>:dnode-block`
(a block of the dataset's dnode array), `<volume>:data` (a data block of
the volume) or `<volume>:indirect` (an indirect block of its data
object). `block` picks which: an index in zdb's order (default 0), or
`on:<kind>` — the first block whose first copy lies on a top-level vdev
of that kind (`on:mirror`, `on:raidz2`, `on:draid1`), so that a case
asks for a block the harness can place without naming an index that is
one image's alone. `copy` is a DVA copy or `all`. `pieces` is `all` (the
chosen copies whole: both mirror halves, every raidz column) or `one`:
one piece of the first copy — a mirror half, one raidz data column, one
dRAID column — the loss every geometry survives once. The harness
resolves all of it to member/offset/size from the oracle's `zdb`
captures — never from the tool under test — and overwrites that.

`<dataset>` may be `any`, and usually should be: `ztest` creates and
destroys datasets as it runs, so which names reach a given capture is a
property of that build and a manifest naming one skips on every image
where the run went differently. `any` picks a dataset from the capture —
most block-pointer copies first, then by name, so the same image always
yields the same choice.

One further shape is described here because the format wants it and
**the harness refuses it by name until it can locate it honestly**:
`crypto-key` (the DSL crypto key ZAP of an encrypted dataset). `dnode-block`
was in that list until the `zdb -dddddd` capture: before it, the shape
had been resolved to the objset's own block pointer, which meant a
manifest using it damaged something other than what it said.

### Telling the tool something

Some damage leaves a member carrying nothing that says whose it is: with
all four `vdev_phys` areas gone, only its siblings' configuration knows
that leaf exists. An operator in that position asserts the member belongs
to the pool, and a manifest says the same:

```toml
[recovery]
assume_members = [{ leaf = 0 }]
```

The harness passes each named member as `--assume-member PATH`. That is
the whole assertion: which leaf it is, the tool works out by reading
through it, and every block is still verified by its checksum, so a
member that does not hold this pool's data is refused. Use it only for
classes where the member genuinely cannot identify itself — never to
help the tool past damage it should be answering on its own.

## Classes

| Class | Variants |
|---|---|
| `labels` | one, front pair, rear pair, all four, `vdev_phys` only, rings only, partial rings with a forged txg |
| `partition` | GPT rewritten, start shifted, tail truncated, re-created with another size |
| `metadata` | MOS objset, a dataset's own objset, a dnode block of a volume's dataset, an indirect block of a volume's data object — one copy and every copy (property ZAPs and the crypto key object are not locatable yet — see above) |
| `data` | one RAIDZ column, both mirror halves in different places, a gang header; one data block of a named volume — one piece, every piece — and every piece of an encrypted volume's block |
| `member` | whole member missing |
| `older-self` | a member replaced by a consistent copy of itself from round 6 of the fill (the `round6-*` files of the release): one mirror half, both halves, two raidz2 columns, one dRAID child, and one stale beside one missing (`older-self-*.toml`, `combo-older-self-plus-member-gone.toml`) |

Combinations are pairs and triples of variants across members and
top-level vdevs (`combo-<n>.toml`). A manifest with `held_out = true` is
not run during development, only before a release.

## What the harness cannot place, and what that costs

A manifest that addresses something the harness cannot resolve is
reported `n/a` and shown as `—` in a run's table. That is the honest
answer — a skipped case is visible, a wrong one is not — but it is worth
knowing which cells are empty for a reason other than the pool's shape.

| Limitation | Cost |
|---|---|
| A copy on a **dRAID top** is placed by content, not arithmetic: the block's bytes (read from a copy on a mirror, or put back together from a raidz's data columns, and checked against the pointer's checksum where it is fletcher4 or sha256) are searched for on the dRAID's children. What that places is the data columns, and a parity column only where it equals a data column (one data sector in the row, the rest padding); other parity columns stay. | A "copy destroyed" on dRAID is its data columns destroyed; the copy stays rebuildable from parity where ZFS would rebuild it. A block whose bytes are found at more than one row offset, or all zeros, is not placed, and the case is n/a with the reason. |
| A DVA is not mapped inside a **top-level vdev with more than one group**. The column arithmetic is one group wide and the member list is the whole top; with two groups they disagree. | No case today; the harness refuses rather than answering wrongly. |
| The **`crypto-key`** target is not located. | No manifest uses it. |
| A block **below the object set** (`dnode-block`, `data`, `indirect`) needs the oracle's `zdb -dddddd` capture; `image-v1` got it after publication (`oracle-capture.yml` in zvolrescue, OpenZFS's zdb offline over the released members), the builder keeps it for every image since. A **data block whose one copy lies on the dRAID top** has no second copy to read its bytes from, so content cannot place it; a **gang block** (most lower indirect blocks of a volume filled with ganging forced) is not aimed at, since its pointer names the whole tree's size and not the header's — `indirect` therefore means the topmost level unless `level` says otherwise. | Without the capture every such case is n/a. A data case names `block = "on:mirror"` or `"on:raidz2"` for that reason. |
| **`older-self`** needs the members captured at an earlier point of the same pool's life: the `round6-*` files of the release, decompressed beside the members as `<image>-round6` (or named with `--older`). `ztest` cannot produce such a capture — it only continues a pool through a cachefile it does not leave behind. | Every `older-self` manifest is n/a on a ztest-built image, and on a kernel-built one whose round-6 copies were not fetched. |

None of these is a tool limitation: they are places where the *test* side
cannot yet state the right answer, and they are listed so that an empty
cell is never mistaken for a pass.

## An expectation must not depend on where the blocks landed

`span:` and `data:` take percentages, and it is tempting to write
`span:5%..25%` and expect `refused` because "both copies of the block
are gone". They are gone only if they were in that slice. Where a pool
puts its blocks is a property of the `ztest` run that built the image —
how long it ran, how much it wrote, which metaslabs it opened — not a
property of the pool's redundancy. Three manifests were written this way
and passed for two months against one image; on an image built with a
shorter run the same slice missed the volume entirely and the extraction
came back bit-exact, which the run correctly reported as `unexpected`.
The manifests were wrong, not the tool.

So: an expectation may rest on **what was damaged** (labels, a located
structure, a whole member, every written byte), never on a percentage
happening to contain something. `data:0%..100%` is every block a member
has, on any image; a middle slice is whatever that run put there.

And it may rest on the **geometry** only where the geometry is known.
Against the published image it is: the layout is recorded beside it and
does not change. Against an image built on the spot it is not, and the
difference is larger than it sounds. `ztest` attaches and detaches
devices while it runs, so a pool asked for as a two-way mirror comes out
two, three or four leaves wide; it removes vdevs, leaving an `indirect`
top behind; and it makes datasets with `checksum=off`, where damaged
bytes reach the decompressor with nothing to have caught them. Six
builds from the same command gave `data-zeros-two-members-same-range`
three different answers — `refused` on a two-way mirror, `bit-exact` on
a three-way one — and all three were the tool behaving correctly.

A manifest is written against the published image. A run against a
freshly built pool can say whether the tool broke or wrote to its
evidence, because neither depends on the shape; it cannot say whether
the redundancy verdict is right.

Nothing in the harness enforces any of this — there is no cheap way to
ask "did this damage touch anything the extraction reads", and the
expectations do not yet carry the redundancy arithmetic that would let
them be judged against any shape — so these are rules for writing
manifests, and the only place they are written down is here.

The first set (22 manifests) covers each class at least once against the
`image-v1` layout: members `mirror-0a/0b`, `raidz2-0..3`, `draid1-0..3`
(see `oracle/layout.json` once the image is built). Expected outcomes are
stated from ZFS redundancy; where the current tool is known to fall short
(zero-point search, F-60..F-67), the manifest says so in a comment and the
run is a known defect until the feature lands.
