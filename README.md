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

## Layout

| Path | What |
|---|---|
| GitHub Releases | image members, `zstd`-compressed, one file each, plus `SHA256SUMS` — never in git (see below) |
| `oracle/` | volume hashes per snapshot, `zdb -d`/`zdb -l` captures, `zpool status`, key material of the test datasets |
| `manifests/` | damage manifests, one file per class and per combination set; format in [manifests/README.md](manifests/README.md) |
| `IMAGE.md` | how the image was built (the script lives in zvolrescue), tool versions, pool layout, TXG history |

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
