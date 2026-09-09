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

The kernel-built golden image does not exist yet. In its place there is
**`image-v0-ztest`**, built with OpenZFS userland only (`ztest` + `zdb`, no
kernel module, no root, no disks): three pools — mirror, raidz2 inside a
mirror wrapper, draid1 — with genuine OpenZFS metadata but no zvols. Its
oracle is in `oracle/`, its description in [IMAGE.md](IMAGE.md), and the
first run of the damage matrix against it in
[reports/image-v0-ztest](reports/image-v0-ztest/README.md): 17 applicable
cases, all passed, no defects.

The member files themselves are not in git; rebuild them with
`tests/golden/build-ztest-image.sh` in zvolrescue (about three minutes) or
fetch them from the `image-v0-ztest` release. Their SHA-256 sums are in
`oracle/SHA256SUMS-release.txt`.

## Layout

| Path | What |
|---|---|
| GitHub Releases | image members, `zstd`-compressed, one file each, plus `SHA256SUMS` — never in git (see below) |
| `oracle/<pool>/` | dataset inventory, `zdb` captures, labels, layout, keys — the recorded truth of each pool |
| `reports/<tag>/` | damage-matrix runs against that image: what passed, what did not, what was not applicable |
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
