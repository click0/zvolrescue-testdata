# Oracle

The recorded truth for the golden image, captured at build time on the
kernel that built it, before the pool was exported. Nothing here is ever
regenerated from the tool under test. One directory per pool:
`golden/` is the kernel-built image `image-v1` (one pool); `mirror/`,
`raidz2/` and `draid1/` are the three pools of the interim
`image-v0-ztest`, and `SHA256SUMS-release.txt` beside them is that
release's; `golden/SHA256SUMS-release.txt` is `image-v1`'s.

| File | Content |
|---|---|
| `volumes.sha256` | `sha256  dataset@snapshot` for every zvol at every snapshot and at export |
| `datasets.txt` | `zdb -d` at the final TXG: names, creation TXGs, types |
| `datasets-by-txg/` | `zdb -d` at every uberblock TXG that was still readable at capture |
| `labels/` | `zdb -l` of every member, verbatim |
| `zpool-status.txt` | `zpool status -v` before export |
| `keys/` | raw key file and passphrase file of the encrypted test datasets (they protect nothing) |
| `layout.json` | members, top-level vdevs, ashift, GUIDs — the machine-readable form of IMAGE.md |
| `members.sha256`, `SHA256SUMS-release.txt` | the uncompressed members, and the release's `zstd` files |
| `zdb-C.txt`, `zdb-u.txt`, `zdb-dddd.txt`, `zfs-list.txt`, `zfs-get-all.txt`, `zpool-get-all.txt`, `pool-facts.txt`, `datasets-exported.txt` | the kernel-built image only: the pool configuration, uberblocks, every object, every property, and what `zfs` listed at export |
