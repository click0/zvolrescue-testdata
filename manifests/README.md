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
target = { object = "vm/disk-16k:dnode-block", copy = "all" }   # or copy = 0 / 1 / 2
pattern = "random"
```

`object` is `<dataset>:objset`, or `mos:objset`. The harness resolves it
to member/offset/size from the oracle's `zdb` captures — never from the
tool under test — and overwrites the chosen DVA copies.

`<dataset>` may be `any`, and usually should be: `ztest` creates and
destroys datasets as it runs, so which names reach a given capture is a
property of that build and a manifest naming one skips on every image
where the run went differently. `any` picks a dataset from the capture —
most block-pointer copies first, then by name, so the same image always
yields the same choice.

Two further shapes are described here because the format wants them and
**the harness refuses them by name until it can locate them honestly**:
`dnode-block` (the dnode array block holding object 1) and `crypto-key`
(the DSL crypto key ZAP). The first was resolved to the objset's own
block pointer, which meant a manifest using it damaged something other
than what it said.

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
| `metadata` | MOS objset, a dataset's own objset (dnode blocks, indirect blocks, property ZAPs and the crypto key object are not locatable yet — see above) |
| `data` | one RAIDZ column, both mirror halves in different places, a gang header, an encrypted block |
| `member` | whole member missing, member replaced by an older copy of itself |

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
| A DVA is not mapped through the **dRAID permutation**. Which child holds which column is a table derived from the pool, not arithmetic; reimplementing it inside the thing that is supposed to be the oracle is how a harness comes to be confidently wrong. | Every `target =` manifest skips on a dRAID pool — six cases in the current set. |
| A DVA is not mapped inside a **top-level vdev with more than one group**. The column arithmetic is one group wide and the member list is the whole top; with two groups they disagree. | No case today; the harness refuses rather than answering wrongly. |
| **`dnode-block`** and **`crypto-key`** targets are not located. | No manifest uses them. `dnode-block` used to resolve to the objset's own block pointer, so a manifest would have damaged something other than what it said. |
| **`older-self`** needs a member captured at two points of the same pool's life, which `ztest` cannot produce — it only continues a pool through a cachefile it does not leave behind. | Every `older-self` manifest skips on a ztest-built image. |

None of these is a tool limitation: they are places where the *test* side
cannot yet state the right answer, and they are listed so that an empty
cell is never mistaken for a pass.

The first set (22 manifests) covers each class at least once against the
`image-v1` layout: members `mirror-0a/0b`, `raidz2-0..3`, `draid1-0..3`
(see `oracle/layout.json` once the image is built). Expected outcomes are
stated from ZFS redundancy; where the current tool is known to fall short
(zero-point search, F-60..F-67), the manifest says so in a comment and the
run is a known defect until the feature lands.
