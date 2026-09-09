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
pattern = "zeros"             # zeros | random | flip-bits:<n> | shift:<sectors> | older-self:<image-tag>

[expect]
outcome = "bit-exact"         # bit-exact | reconstructed | refused | (never "defect")
volumes = "all"               # which oracle volumes are compared, or a list
evidence = ["label L0 missing", "label L2 used"]   # substrings the evidence log must contain (optional)
```

`expect.outcome` is derived from the redundancy ZFS guarantees for the
damage, not from what the tool does today. A run that lands anywhere else
is a tool defect. Every run also asserts that the SHA-256 of each damaged
copy is unchanged after the tool ran (read-only invariant).

`older-self:<tag>` overwrites the range with the same range taken from an
earlier image tag — the "member replaced by an older copy of itself" case,
where everything verifies but is not the newest.

## Classes

| Class | Variants |
|---|---|
| `labels` | one, front pair, rear pair, all four, `vdev_phys` only, rings only, partial rings with a forged txg |
| `partition` | GPT rewritten, start shifted, tail truncated, re-created with another size |
| `metadata` | MOS, dnode blocks, indirect blocks, property ZAPs, the crypto key object |
| `data` | one RAIDZ column, both mirror halves in different places, a gang header, an encrypted block |
| `member` | whole member missing, member replaced by an older copy of itself |

Combinations are pairs and triples of variants across members and
top-level vdevs. A subset marked `held_out = true` is not run during
development, only before a release.
