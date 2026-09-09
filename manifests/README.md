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

`object` is `<dataset>:<what>` with `what` one of `objset`, `dnode-block`
(the dnode array block holding object 1), `crypto-key` (the DSL crypto key
ZAP), or `mos:objset`. The harness resolves it to member/offset/size from
the oracle's `zdb` captures — never from the tool under test — and
overwrites the chosen DVA copies.

## Classes

| Class | Variants |
|---|---|
| `labels` | one, front pair, rear pair, all four, `vdev_phys` only, rings only, partial rings with a forged txg |
| `partition` | GPT rewritten, start shifted, tail truncated, re-created with another size |
| `metadata` | MOS, dnode blocks, indirect blocks, property ZAPs, the crypto key object |
| `data` | one RAIDZ column, both mirror halves in different places, a gang header, an encrypted block |
| `member` | whole member missing, member replaced by an older copy of itself |

Combinations are pairs and triples of variants across members and
top-level vdevs (`combo-<n>.toml`). A manifest with `held_out = true` is
not run during development, only before a release.

The first set (22 manifests) covers each class at least once against the
`image-v1` layout: members `mirror-0a/0b`, `raidz2-0..3`, `draid1-0..3`
(see `oracle/layout.json` once the image is built). Expected outcomes are
stated from ZFS redundancy; where the current tool is known to fall short
(zero-point search, F-60..F-67), the manifest says so in a comment and the
run is a known defect until the feature lands.
