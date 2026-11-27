# Damage matrix: sat-spare-v1

| Manifest | Expected | Actual | Files | Timeline | Datasets | Scan | Report | Carve | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `combo-sat-spare-three-columns` | refused \| partial | partial | partial | bit-exact | bit-exact | bit-exact | bit-exact | — | pass | yes | sat-spare/vm/disk-8k: incomplete (blocks written as zeros); sat-spare/vm/disk-16k: incomplete (blocks written as zeros); files sat-spare/fs: incomplete (entries said not whole) |
| `control-sat-spare` | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | pass | yes |  |
| `member-sat-spare-replacing-old-side-gone` | bit-exact \| reconstructed | reconstructed | reconstructed | bit-exact | bit-exact | bit-exact | bit-exact | — | pass | yes |  |
| `member-sat-spare-the-spare-gone` | bit-exact \| reconstructed | reconstructed | reconstructed | bit-exact | bit-exact | bit-exact | bit-exact | — | pass | yes |  |
| `member-sat-spare-two-gone` | bit-exact \| reconstructed | reconstructed | reconstructed | bit-exact | bit-exact | bit-exact | bit-exact | — | pass | yes |  |
