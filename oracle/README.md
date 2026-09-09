# Oracle

The recorded truth for the golden image, captured at build time in the VM
before the pool was exported. Nothing here is ever regenerated from the
tool under test.

| File | Content |
|---|---|
| `volumes.sha256` | `sha256  dataset@snapshot` for every zvol at every snapshot and at export |
| `datasets.txt` | `zdb -d` at the final TXG: names, creation TXGs, types |
| `datasets-by-txg/` | `zdb -d` at every uberblock TXG that was still readable at capture |
| `labels/` | `zdb -l` of every member, verbatim |
| `zpool-status.txt` | `zpool status -v` before export |
| `keys/` | raw key file and passphrase file of the encrypted test datasets (they protect nothing) |
| `layout.json` | members, top-level vdevs, ashift, GUIDs — the machine-readable form of IMAGE.md |
