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
| `labels-uberblocks/` | the kernel-built image: `zdb -lu` of every member — its labels with every uberblock of their rings — captured offline from the published members (`oracle-capture.yml`, `what = labels-uberblocks`) |
| `zpool-status.txt` | `zpool status -v` before export |
| `keys/` | raw key file and passphrase file of the encrypted test datasets (they protect nothing) |
| `layout.json` | members, top-level vdevs, ashift, GUIDs — the machine-readable form of IMAGE.md |
| `members.sha256`, `SHA256SUMS-release.txt` | the uncompressed members, and the release's `zstd` files |
| `zdb-C.txt`, `zdb-u.txt`, `zdb-dddd.txt`, `zfs-list.txt`, `zfs-get-all.txt`, `zpool-get-all.txt`, `pool-facts.txt`, `datasets-exported.txt` | the kernel-built image only: the pool configuration, uberblocks, every object, every property, and what `zfs` listed at export. `zdb-u.txt`, `pool-facts.txt` and `datasets.txt` were taken while the pool was still imported, at TXG 4994 (the listing of `datasets.txt` is that of `datasets-by-txg/` from 4993 to 5014); `datasets-exported.txt` is the listing at the export's TXG 5015, the same as `datasets-by-txg/5015.txt` |
| `zdb-u-export.txt` | the kernel-built image: `zdb -e -u`, the uberblock zdb reads the exported pool at (TXG 5015), captured with `labels-uberblocks/` |
| `files.json`, `zpool-history-il.txt`, `files-capture.txt` | the kernel-built image only, captured later from the published members by `oracle-capture.yml` in zvolrescue (`what = files-history`, the pool imported read-only): every entry of every filesystem and snapshot as the VFS gives it, `zpool history -il`, and how they were taken |

## What each is judged by

`tests/golden/run-matrix.py` in zvolrescue holds a tool's answer
against these, in every case of the damage matrix:

| The oracle | What is held against it |
|---|---|
| `volumes.sha256` | every volume `zvolrescue dump` extracts |
| `files.json` | every entry `zvolfiles extract` writes |
| `zpool-history-il.txt`, `zfs-list.txt` (GUIDs) | the history `zvoltimeline` gives |
| `datasets-by-txg/` | the datasets `zvolrescue list -r` names, at the TXG it listed at, and the feature refcounts zdb verified there; on the control case at each TXG of the ring zdb recorded |
| `zpool-get-all.txt` | the state of every feature `zvolrescue list` reports, `active` or `enabled` |
| `labels/`, `labels-uberblocks/`, `zdb-u.txt`, `zdb-u-export.txt`, `zpool-status.txt`, `pool-facts.txt` | what `zvolrescue scan -vv` read of each member's label, of every slot of its uberblock rings, of the two uberblocks `zdb -u` printed, and of the top-level vdevs and the pool's version, GUID and ashifts |
| `volumes.sha256` and the evidence logs of a case | the report `zvolreport` builds of a case's runs and verifies: each extraction as the harness found it, every output hash as recorded |
| `layout.json`, `zdb-C.txt`, `zdb-dddd.txt`, `zdb-dddddd.txt`, `keys/`, `zfs-get-all.txt` | how damage is placed and what an operator would tell the tool: members, hints, metaslab ends, the block a `target` names, keys and their formats |
| `members.sha256`, `SHA256SUMS-release.txt` | the release files fetched, before any run |

Not held against anything: `datasets.txt` and `datasets-exported.txt`,
the same listings as `datasets-by-txg/` at the TXGs they were taken; the
pool properties of `zpool-get-all.txt` other than the features (size,
allocation, fragmentation: no tool reports them); and the three
`image-v0-ztest` pools, whose members were never published — the matrix
in CI rebuilds such a pool on each push — kept as the record the
reports `image-v0-ztest` and `-r2` were judged by.

