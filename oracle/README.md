# Oracle

The recorded truth for the golden image, captured at build time on the
kernel that built it, before the pool was exported. Nothing here is ever
regenerated from the tool under test. One directory per pool:
`golden/` is the kernel-built image `image-v1` (one pool), with the
sums of its release files in `golden/SHA256SUMS-release.txt`; `mirror/`,
`raidz2/` and `draid1/` are the three pools of the interim
`image-v0-ztest`, which has no release — its builder makes a different
pool each time.

| File | Content |
|---|---|
| `volumes.sha256` | `sha256  dataset@snapshot` for every zvol at every snapshot and at export |
| `datasets.txt` | `zdb -d` at the final TXG: names, creation TXGs, types |
| `datasets-by-txg/` | `zdb -t T -d` for each of the newest TXGs (the kernel-built image: the newest 128, read at the newest uberblock at or before each) |
| `labels/` | `zdb -l` of every member, verbatim |
| `zpool-status.txt` | `zpool status -v` before export |
| `keys/` | raw key file and passphrase file of the encrypted test datasets (they protect nothing) |
| `layout.json` | members, top-level vdevs, ashift, GUIDs — the machine-readable form of IMAGE.md |
| `members.sha256`, `SHA256SUMS-release.txt` | the uncompressed members, and the release's `zstd` files |
| `zdb-C.txt`, `zdb-u.txt`, `zdb-dddd.txt`, `zfs-list.txt`, `zfs-get-all.txt`, `zpool-get-all.txt`, `pool-facts.txt`, `datasets-exported.txt` | the kernel-built image only: the pool configuration, uberblocks, every object, every property, and what `zfs` listed at export |
| `files.json`, `zpool-history-il.txt`, `files-capture.txt` | the kernel-built image only, captured later from the published members by `oracle-capture.yml` in zvolrescue (`what = files-history`, the pool imported read-only): every entry of every filesystem and snapshot as the VFS gives it, `zpool history -il`, and how they were taken |

## What each is judged by

`tests/golden/run-matrix.py` in zvolrescue holds a tool's answer
against these, in every case of the damage matrix:

| The oracle | What is held against it |
|---|---|
| `volumes.sha256` | every volume `zvolrescue dump` extracts |
| `files.json` | every entry `zvolfiles extract` writes |
| `zpool-history-il.txt`, `zfs-list.txt` (GUIDs) | the history `zvoltimeline` gives |
| `datasets-by-txg/` | the datasets `zvolrescue list -r` names, at the TXG it listed at; on the control case at each TXG of the ring zdb recorded |
| `labels/`, `zdb-u.txt`, `zpool-status.txt` | what `zvolrescue scan -vv` read of each member's label, of the uberblock `zdb -u` printed, and of the top-level vdevs |
| `layout.json`, `zdb-C.txt`, `zdb-dddd.txt`, `zdb-dddddd.txt`, `keys/`, `zfs-get-all.txt` | how damage is placed and what an operator would tell the tool: members, hints, metaslab ends, the block a `target` names, keys and their formats |
| `members.sha256`, `SHA256SUMS-release.txt` | the release files fetched, before any run |

Not held against anything yet: `datasets.txt` and `datasets-exported.txt`
(the same listing as `datasets-by-txg/` at the TXG they were taken),
`zpool-get-all.txt` and `pool-facts.txt` (pool properties and feature
states, which no tool reports), and the three `image-v0-ztest` pools,
which the matrix in CI rebuilds on each push rather than reads.

