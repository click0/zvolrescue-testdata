# zvolrescue-testdata

Test data for [zvolrescue](https://github.com/click0/zvolrescue), the
read-only ZFS zvol recovery tool. This repository holds what zvolrescue's
[SPEC §9.1](https://github.com/click0/zvolrescue/blob/main/docs/SPEC.md)
calls the golden image and the damage matrix:

* **one golden pool image** — a single pool with mirror, RAIDZ2 and dRAID1
  top-level vdevs, zvols, snapshots, clones, encrypted datasets, every
  checksum and compression, gang blocks, hundreds of TXGs — built once by
  a script in a real-kernel VM and then immutable;
* **the oracle** — SHA-256 of every volume at every snapshot, `zdb` output
  for every TXG and member, keys: the "how it should be" every recovery is
  compared against;
* **damage manifests** — declarative descriptions of what to overwrite
  (member, byte range, pattern), applied to temporary copies at test time,
  singly and in combinations.

Recovery is only testable when the right answer is known in advance. The
diversity here comes from the kinds and combinations of damage, not from
more images with different content.

Українською: [README_UK.md](README_UK.md).

## What is here now

**`image-v1`**, the kernel-built golden image: one pool, `golden`, with
mirror-2, raidz2-4 and draid1 top-level vdevs at `ashift` 12, eleven
volumes over every checksum and compression and three block sizes, a
clone, raw-key and passphrase encryption, snapshots after each of twelve
rounds of writes, a rename, a destroy, gang blocks forced, 5015 TXGs —
built by `tests/golden/build-image.sh` in zvolrescue on the OpenZFS 2.4.1
of a GitHub `ubuntu-26.04` runner (the `golden` job of
`realworld.yml`), described in [IMAGE.md](IMAGE.md). Its oracle is in
`oracle/golden/`; the damage matrix against it, run on the same kernel
right after the build, is in [reports/image-v1](reports/image-v1/README.md):
41 manifests, 35 passed, 6 not applicable, none outside its expected
category. Its first build was refused whole by zvolrescue v0.9.8, which
did not know `dynamic_gang_header`; v0.9.9 reads it.

The member files are the `image-v1` release here — twenty `zstd` files,
the ten members and a consistent copy of each taken after round 6 of
the fill (the manifests' older-self pattern), with `SHA256SUMS`; the
sums of the uncompressed members are in `oracle/golden/members.sha256`.
Published by `publish-golden.yml` in zvolrescue from the run that built
and judged the image, never by hand.

Before it there was **`image-v0-ztest`**, built with OpenZFS userland
only (`ztest` + `zdb`, no kernel module, no root, no disks): three pools
— mirror, raidz2, draid1 — with genuine OpenZFS metadata but no zvols. It
stays: its oracle in `oracle/mirror/`, `oracle/raidz2/` and
`oracle/draid1/`, its description in
[reports/image-v0-ztest/IMAGE.md](reports/image-v0-ztest/IMAGE.md), its
members in no release — `tests/golden/build-ztest-image.sh` in zvolrescue
rebuilds pools of that kind in about three minutes, differently each
time — and the matrix against it in
[reports/image-v0-ztest-r2](reports/image-v0-ztest-r2/README.md): 44
manifests over three pools, 112 applicable runs, all passed, one defect
found and fixed on the way (`--assume-member` answered "no scanned pool
is missing a member" about a pool missing a whole top-level vdev). The
[first run](reports/image-v0-ztest/README.md) is kept as a record; its
draid1 column was judged against that pool's spares rather than its
members and does not count. zvolrescue's CI still builds one pool of it
for the pinned subset of the matrix it runs on every push.

## Layout

| Path | What |
|---|---|
| GitHub Releases | image members, `zstd`-compressed, one file each, plus `SHA256SUMS` — never in git (see below) |
| `oracle/<pool>/` | dataset inventory, `zdb` captures, labels, layout, keys — the recorded truth of each pool |
| `reports/<tag>/` | damage-matrix runs against that image: what passed, what did not, what was not applicable |
| `manifests/` | damage manifests, one file per class and per combination set; format in [manifests/README.md](manifests/README.md) |
| `IMAGE.md` | how the current image was built (the script lives in zvolrescue), tool versions, pool layout, TXG history; an earlier image's copy sits under its `reports/<tag>/` |

## Versioning

Each image version is a release tag here (`image-v1`, `image-v2`, …);
zvolrescue pins the tag and the `SHA256SUMS` it expects. Images are never
edited by hand: a change means a new build and a new tag. Manifests and the
oracle are versioned in git alongside.

## Why not in git

A GitHub repository limits files to 100 MiB and Git LFS bandwidth is
metered; release assets allow 2 GiB per file and unmetered downloads. Image
members compress well (unused space is zeros), so a release holds a few
hundred MiB in total. CI in zvolrescue downloads the assets once and keeps
them in the Actions cache.

## Licence

BSD 3-Clause, as zvolrescue. The pool content is synthetic and carries no
real data; the encryption keys in `oracle/` protect nothing.
