# Roadmap

What this repository is to hold next, in the order it is to be done, and
how it is to be published so that a CI job fetches only what it tests.
The rules of [CLAUDE.md](CLAUDE.md) hold throughout: no binary in git,
the oracle from OpenZFS in a VM and never from the tool under test, an
image never rebuilt in place, expectations derived from ZFS redundancy.
`image-v1` stays as it is: zvolrescue's CI pins it.

## Where things stand

`image-v1` tests one program of five. The harness (`run-matrix.py` in
zvolrescue) judges `zvolrescue` only — the volumes `dump` writes and the
datasets a walk finds. Nothing here tells `zvolfiles` what the files of
`fs-largednode` hold, `zvoltimeline` what happened when, or `zvolcarve`
what the destroyed `vm/doomed` held last (`volumes.sha256` has it at
`s0`–`s2` only). And what zvolrescue has learned since the image was
built — reading a pool no uberblock is left of at the headers
`zvolcarve roots` finds, a pool no label is left of through `--hints`,
the member order of a raidz searched from either, a transaction group
from before a device removal, the pool checkpoint, a spare at work, an
intent log not applied — has no case here at all: it is tested on
synthetic fixtures and `libzpool` pools in zvolrescue's CI, not against
a pool whose answer is known.

## Publishing: one tag per pool, one download per need

| Rule | Why |
|---|---|
| A tag per pool, each with its own version: `golden-vN` for the main pool, `sat-<name>-vN` for each satellite. `image-v1` keeps its name. | Rebuilding one satellite touches no other; a job pins only the pools it reads. |
| Each tag has its own `SHA256SUMS`, and each pool its own `oracle/<pool>/`. | The pin in zvolrescue (`tests/golden/<tag>.SHA256SUMS`) stays one file per tag. |
| Within a tag, two sets: the members, and the older copies (`round6-*`). Older copies are published only for the members a manifest names. | `image-v1`'s older copies are 44% of its release, and the manifests use 6 of the 10. |
| A manifest names its pool: `image = "golden"` (the default) or `image = "sat-removal"`. The harness prints what the selected manifests need (`--print-needs`) and `fetch-image.sh` fetches that alone. | A run of manifests without older-self fetches no older copy; a satellite's run fetches nothing of `golden`. |
| A pool is fetched whole. | ZFS spreads every volume over every top-level vdev: no part of a pool reads without the rest. |
| The large `zdb` captures are split per dataset (`zdb-dddddd/<dataset>.txt`), every file under 50 MiB. | `oracle/golden/zdb-dddddd.txt` is 55 MiB already. |

### What a job fetches

| Job | Now | Planned |
|---|---|---|
| zvolrescue CI on every push | no image; the whole of this repository (18 MB packed, 65 MB checked out) | no image, or one satellite of 0.02–0.15 GB; `manifests/` only (sparse checkout, 0.3 MB) |
| `golden`, manifests without older-self | 2.51 GB (everything) | the members: 1.40 GB of `image-v1`, about 1.8 GB of `golden-v2` |
| `golden`, older-self manifests | (the same 2.51 GB) | the members and the older copies named, about 2.7 GB of `golden-v2` |
| a satellite | — | 0.02–0.18 GB |

The weekly and manual runs (`realworld.yml` in zvolrescue) become a
matrix: a job per pool, and `golden`'s manifests in a few shards, each
fetching its pool from the release.

### GitHub's limits, and what they mean here

| Limit | Value | Here |
|---|---|---|
| A release file | under 2 GiB; no limit on a release's total size or on downloads | the largest member is 194 MB; fetching from a release costs nothing, so the same pool may be fetched by every shard |
| A file in git | a warning above 50 MiB, refused above 100 MiB | `zdb-dddddd.txt` is past the warning: split it from `golden-v2` on |
| A repository | best under 1 GB, strongly under 5 GB | text only; `.git` is 18 MB today |
| Actions cache | 10 GB per repository; an entry not used for 7 days is evicted | a weekly run is at the edge of eviction, so the release, not the cache, is where a weekly run fetches from; drop an image's cache entry once its successor is pinned |
| A hosted runner (public repository) | 4 vCPU, 16 GB RAM, 14 GB SSD; a job up to 6 h; up to 256 jobs in a matrix, 20 at once | members decompress sparse — they take what is allocated — and a job holds one pool and the copies the harness damages |

## Stage 1 — on `image-v1`, no new image

Release: +0. Git: under 1 MB of text.

1. *Done.* **The push-time checkout narrowed to `manifests/`** in
   zvolrescue's CI (`sparse-checkout`): 0.3 MB instead of 18 MB packed.
2. *Done.* **A linter for the manifests**, run here on every push
   (`tools/lint-manifests.py`; its first run found a class the format
   does not have, now `member`): TOML that
   parses, `id` equal to the file name, members and top-level vdevs
   present in `oracle/<pool>/layout.json`, outcomes and patterns from
   the format, older copies only for members a release holds.
3. *Done.* **The harness fetches what the selected manifests need**: the
   `image` key, `run-matrix.py --print-needs`, `fetch-image.sh` taking
   that list.
4. *Done.* **Cases for what zvolrescue reads now**, with `[recovery]`
   keys the harness passes on (eleven manifests, all passing against
   `image-v1`; the hints case found that a pool read through `--hints`
   took no feature from its labels and read 2.4's gang headers at 512
   bytes, fixed in zvolrescue `9a04283`):
   * the uberblock rings of every member zeroed: refused without
     headers, recovered with `zvolcarve roots` and `--roots`;
   * the `vdev_phys` of every member zeroed: recovered through the
     layout in `oracle/golden/layout.json` given as `--hints`;
   * the same with a raidz's members out of order and `--search-order`;
   * both at once: hints, roots and the order searched;
   * a range a ddrescue map marks unreadable rather than overwritten
     (the pattern `unreadable`);
   * a wrong and a missing key for the encrypted volumes: refused;
   * negative controls, damage where ZFS reads nothing — the reserved
     boot area after L1, and the slack between the last metaslab and
     L2 (`range = "slack"`, placed from the `zdb -C` capture: 27.5 MiB
     on each mirror and raidz2 member of `image-v1`, 75.5 MiB on each
     dRAID child) — expected bit-exact.
5. *Done, but for zvolreport.* **The oracle extended from the published
   members** (`oracle-capture.yml` in zvolrescue with `what =
   files-history`: OpenZFS 2.4.1 in the ubuntu-26.04 runner's kernel,
   the members imported read-only and checked unchanged after the
   export): every entry of every filesystem and of each of its
   snapshots with its size, owner, mode, inode, mtime and the SHA-256
   of its content and of each extended attribute
   (`oracle/golden/files.json`); `zpool history -il`
   (`zpool-history-il.txt`); how, in `files-capture.txt`. The harness
   judges `zvolfiles` and `zvoltimeline` against them in every case
   (zvolrescue `7f5ef23`; `expect.files`, `expect.timeline` and the
   control case in the manifests; `reports/image-v1-r3`, 70 of 70). The
   exit status after a TXG passed over, 4 from `zvolfiles` where
   `zvolrescue dump` gave 0, is settled: 4 from every tool, the bytes
   judged (zvolrescue `4a95364`, `reports/image-v1-r4`, 70 of 70).
   Left: `zvolreport`, judged by building and verifying a report of the
   matrix's own evidence logs.
6. *Done.* **Every matrix run's report kept here**
   (`reports/<tag>-rN/`), not only the first: `tools/add-report.py`
   lays a report out as the next run, with a README written from its
   JSON, and the published image's job of `realworld.yml` in zvolrescue
   calls it after every run on `main` and pushes the result with the
   token `publish-golden.yml` uses. `reports/image-v1-r2` was the
   second, kept by hand.

## Stage 2 — `golden-v2` and the satellites

Release: about 3.6 GB in all — `golden-v2` 2.8 GB with the older copies
the manifests name, the satellites 0.8 GB — beside `image-v1`'s 2.51 GB,
which stays. Git: 20–40 MB of oracle text.

**`golden-v2`**: `image-v1`'s recipe with, besides —
a filesystem with a tree in it (directories, symbolic and hard links,
sparse files, a file of 4K records deep enough for two levels of
indirect blocks, system-attribute spill blocks, `casesensitivity=mixed`
and `normalization=formD`), a filesystem destroyed, `zfs promote`,
`rollback` and a snapshot destroyed, volumes of `volblocksize` 128K, of
`copies=2`, of `checksum=off` and of `zstd-fast`, a block-cloned file,
and the hash of every volume taken just before it is destroyed. About
330 MiB more data; the members of 512 MiB go from 36% to about 48% full.

**Satellites**, one pool-level feature each, small members, no older
copies:

| Tag | What | ≈ |
|---|---|---|
| `sat-removal-v1` | two mirrors, one removed: the indirect vdev, and the removed disks still members | 0.16 GB |
| `sat-checkpoint-v1` | a volume written, the pool checkpointed, the volume destroyed and the space written again | 0.14 GB |
| `sat-spare-v1` | raidz2 with a hot spare at work, and a replacing that did not finish | 0.18 GB |
| `sat-expand-v1` | raidz1 expanded from three disks to four (OpenZFS 2.3 and later) | 0.12 GB |
| `sat-special-v1` | special and dedup vdevs | 0.08 GB |
| `sat-ashift9-v1`, `sat-ashift13-v1` | raidz1 at the two ashifts `image-v1` does not have | 0.08 GB |
| `sat-slog-v1`, `sat-mmp-v1` | an intent log not applied; `multihost=on` | 0.06 GB |

A dRAID of more than one group waits until the harness maps a DVA
inside a top-level vdev of several groups; until then it refuses such a
case rather than answering wrongly.

## Stage 3 — other systems and versions

* **A pool made on FreeBSD** (its base OpenZFS, GPT and `gptid` as
  FreeBSD writes them), on a slimmed recipe: 0.3–0.5 GB.
* **The feature sets of older pools** without older kernels:
  `zpool create -o compatibility=openzfs-2.0-linux`, `-d` and
  `-o version=28` on the current OpenZFS — three small pools, about
  0.15 GB.
* **A pool at scale**, `held_out` and in a tag of its own that a
  regular run never fetches: thousands of snapshots and datasets
  (0.2–0.4 GB), or a large volume of content ZFS compresses
  (1–3 GB).

## Stage 4 — coverage, stated

Release: +0.

* A table generated from the manifests: class × kind of top-level vdev ×
  where the damage sits against the redundancy (within it, at it, one
  past it), so that an empty cell shows.
* The redundancy arithmetic in the manifests themselves — what is lost
  per top-level vdev against its parity — so that the linter can check
  that `expect.outcome` follows from it.

All sizes above are estimates from `image-v1`'s release: the volumes'
content is pseudo-random and does not compress, so a compressed member
is what is allocated on it, 1.22 bytes of release per byte the pool
reports used. The numbers that count are the ones each build writes into
its `IMAGE.md`.
