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
pattern = "zeros"             # zeros | random | flip-bits:<n> | shift:<sectors> | truncate | grow:<bytes> | missing | older-self:<source> | forged-txg:<bump> | unreadable

[expect]
outcome = "recovered"         # recovered (= bit-exact | reconstructed) | bit-exact | reconstructed | refused (partial accepted too) | a list of these; never "defect"
volumes = "all"               # which oracle volumes are compared, or a list
evidence = ["label L0 missing", "label L2 used"]   # substrings the evidence log must contain (optional)
files = "recovered"           # what the files of every filesystem come to (optional; see "The files")
timeline = "recovered"        # what the pool's history comes to (optional; see "The history")
```

`expect.outcome` is derived from the redundancy ZFS guarantees for the
damage, not from what the tool does today. `bit-exact` means every judged
volume hashed equal to the oracle without any use of redundancy;
`reconstructed` means the hashes are equal but the evidence log shows
redundancy at work (a member reported missing, a mirror half skipped, a
parity or combinatorial reconstruction); `recovered` means either of
those two — which one happens depends on member order and on where the
damage landed, and neither is a property worth pinning, so it is what
almost every manifest says; `refused` means the tool stopped with exit 3
for every judged volume and presented no partial output as good, and a
run that instead wrote an image with the lost blocks as zeros, counted
and announced (exit 4, `partial`), is accepted under it — it presents
nothing as good that is not. A list names several acceptable outcomes
where the damage does not deterministically hit live data. A run that
lands anywhere else is a tool defect. Every run also asserts that the SHA-256 of each damaged
copy is unchanged after the tool ran (read-only invariant).

A manifest written for one pool alone names it: `image = "<pool>"`, by
the name that pool's `oracle/<pool>/layout.json` gives (`golden`, and a
satellite's when there are satellites). It is then run against that
pool and no other, and the harness fetches nothing of another pool for
it. One that names none, as every manifest here does today, is run
against any pool the harness is given — the published image and the
pools it builds with `ztest` on the spot — and is checked here against
`golden`'s oracle.

Ranges are `start..end` in bytes with `KiB`/`MiB`/`GiB` suffixes; a
negative start counts from the end of the member (`-512KiB..` is the last
512 KiB), `0..` is the whole member. `slack` is the member's bytes past
the last metaslab of its top-level vdev, up to L2: a vdev allocates in
whole metaslabs, `asize >> metaslab_shift` of them, and what is left of
its `asize` — and of a dRAID child, everything past what the dRAID
addresses — is never written. The harness places it from the oracle's
`zdb -C` capture (`metaslab_shift`, `asize`, the geometry), mapped onto
the member the way the vdev maps any offset; a member whose metaslabs
reach L2 has none, and the case is n/a. Patterns: `zeros`, `random` (seeded per
manifest, so reproducible), `flip-bits:<n>` (n single-bit flips spread over
the range), `shift:<sectors>` (the member's content moved forward, the
image grows), `truncate` (the range is cut off, the image shrinks),
`unreadable` (the range zeroed, as an imager leaves what it could not
read, and marked bad, `-`, in a ddrescue map of the member that the tool
is given with `--map`: the range is known unread, not merely wrong),
`grow:<bytes>` (that much of nothing appended; no range: the partition
re-created larger, the rear labels no longer where the length puts
them), `missing` (the member is not passed to the tool at all; no
range), `older-self:<source>` — the range is replaced by the same range
of an earlier consistent copy of the member (`image-v1-round6` = the
`round6-*` release files of tag `image-v1`): the "member replaced by an
older copy of itself" case, where everything verifies but nothing is
current — and `forged-txg:<bump>`, on a `label:…/rings` range only: the
ring's newest verified uberblock copied into the slot ZFS would write
txg+bump to (txg modulo the ring's 32 slots, so a bump of 32 would land
on the slot it came from and is refused), with that txg, that birth in
its root pointer and the pointer's checksum words inverted, sealed for
its place. Every word of it verifies and no block is behind it: what a
sync leaves when its uberblocks reached the disks and its MOS did not.

A damage may also name a structure instead of a range:

```toml
[[damage]]
target = { object = "vm/disk-16k:dnode-block", block = 0, copy = "all" }   # or copy = 0 / 1 / 2
pattern = "random"
```

`object` is `mos:objset`, `<dataset>:objset`, or — from the oracle's
`zdb -dddddd` capture, where the image has one — `<dataset>:dnode-block`
(a block of the dataset's dnode array), `<volume>:data` (a data block of
the volume), `<volume>:indirect` (an indirect block of its data object)
or `<dataset>:crypto-key` (the MOS object its DSL directory names as
`com.datto:crypto_key_obj`: the ZAP holding its wrapped keys). `block`
picks which: an index in zdb's order (default 0; `all` for every block
of the level, which is what a crypto key means), or `on:<kind>` — the first block whose first copy lies on a top-level vdev
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

Every shape the format names is located now. `dnode-block` and
`crypto-key` were refused by name until the `zdb -dddddd` capture:
before it, `dnode-block` had been resolved to the objset's own block
pointer, which meant a manifest using it damaged something other than
what it said. A volume's **property ZAP** is not a shape of its own on
`image-v1`: with one entry (`size`) it is embedded in its dnode's block
pointer, so the dnode block *is* its block, and the `dnode-block` cases
cover it.

### The files

Where the oracle has a `files.json` — the kernel's reading of every
filesystem and snapshot of the pool, captured by `oracle-capture.yml`
in zvolrescue with `what = files-history`, the pool imported read-only
— every run also extracts every filesystem of the pool with `zvolfiles`
and holds the tree against it: each entry's type, mode, owner, object
number and mtime, a file's size and SHA-256, a link's target, each
extended attribute's size and SHA-256. An entry `zvolfiles` presents
as whole that is not, one missing that nothing it said accounts for,
or one the pool does not hold, makes the run a `defect` whatever the
manifest expects; an entry it says did not read whole (blocks written
as zeros, an attribute or a directory's contents unread, an entry that
failed — exit 4) is not compared, and the filesystem is `partial`.

`expect.files` says more where the redundancy does, in the vocabulary
of `outcome`. It is set where the damage is the pool's — labels, a
partition, a whole member, a key — rather than any block's, so that the
filesystems come to what the volumes come to; damage aimed at a range
or a block may or may not touch the files, and there only the rule
above holds. The control, `control-undamaged`, damages nothing and
tells the tool nothing: on it every snapshot of every filesystem is
judged as well, and everything must be bit-exact.

### The history

Where the oracle has `zpool-history-il.txt` — `zpool history -il`, taken
by the same capture — every run also asks `zvoltimeline` for the pool's
history and holds it against that record and the GUIDs in
`zfs-list.txt`: every dataset and snapshot it says came into being must
have, by that name, the TXG the record gives and the manner (created,
clone, snapshot) and the GUID; every one the pool holds must be there;
every rename, promotion and destroy the record has after the oldest TXG
it read must be there, at the first TXG it read from then on. What came
before that TXG — a destroy, a rename — is not asked for: nothing left
on the disks shows it. An event presented that the record contradicts
is a `defect`, whatever the manifest expects; one missing with exit 4,
the history said not to be whole, is `partial`. `expect.timeline` says
more, as `expect.files` does.

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

The rest of what an operator tells the tool, the harness passes on the
same way, to every run of the case:

```toml
[recovery]
hints = "layout"        # the pool's layout as the oracle records it, in --hints (SPEC F-65)
order = "reversed"      # every raidz and dRAID group of those hints the other way round
search_order = true     # --search-order: every order tried, the one the checksums accept kept (F-66)
roots = true            # zvolcarve roots on the damaged members, its headers in --roots (F-64)
key = "wrong"           # the encrypted volumes asked for with a key not theirs; "none": with none
```

`order` and `search_order` need `hints`. With `roots` the harness runs
`zvolcarve roots` over the members of the case first — with the hints
and maps, where the case has them — and passes its workspace on; a run
of it that finds nothing is noted, and the case goes on without. A case
that damages nothing and only tells the tool something (`key`) has no
`[[damage]]`. All of these but `assume_members` are the extraction's: a
pool with no volumes is judged by a walker that takes none of them, and
there such a case is `n/a`.

## Classes

| Class | Variants |
|---|---|
| `labels` | one, front pair, rear pair, all four, `vdev_phys` only, rings only, partial rings with a forged txg (`labels-forged-txg`: every ring three TXGs ahead of the pool, one member's rear rings gone) |
| `partition` | GPT rewritten, start shifted, tail truncated, re-created with another size (`partition-grown`) |
| `metadata` | MOS objset, a dataset's own objset, a dnode block of a volume's dataset, an indirect block of a volume's data object, the crypto key object of an encrypted volume — one copy and every copy (a volume's property ZAP on `image-v1` is embedded in its dnode's block pointer, so the dnode-block cases are its — see above) |
| `data` | one RAIDZ column, both mirror halves in different places, a gang header; one data block of a named volume — one piece, every piece — and every piece of an encrypted volume's block |
| `member` | whole member missing |
| `control` | nothing at all: the image as published, every volume and every file of every filesystem and snapshot (`control-undamaged`) |
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

The 73 manifests cover every class of SPEC §9.1's catalogue at least
once against the `image-v1` layout: members `mirror-0a/0b`,
`raidz2-0..3`, `draid1-0..3` (`oracle/golden/layout.json`). Expected
outcomes are stated from ZFS redundancy, and against the published
image every one applies and every one lands in its category: the
reports of the runs are in [`reports/`](../reports/), and the Results
table of zvolrescue's REALWORLD-TESTS.md has each run.

## Checked on every push

`tools/lint-manifests.py` reads every manifest the way the harness will
and says what it would not place, on every push here (the `Manifests`
workflow): a key the format does not have, at any level; a pattern, a
range or a structure target outside the grammar above; a member, a
top-level vdev, a dataset or a volume the oracle of its pool does not
have (`golden`'s, where it names none); an `image` no oracle here
describes; an older copy of a member its release holds none of; an outcome
that is not one of the four, or `defect`; an `id` that is not the
file's name; and a count in this file that is not the number of
manifests. Run it before a push: `python3 tools/lint-manifests.py`.
It knows the format and the oracle, not ZFS: whether an expectation
follows from the redundancy is still the writer's to get right.
