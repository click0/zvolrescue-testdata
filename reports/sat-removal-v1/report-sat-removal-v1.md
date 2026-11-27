# Damage matrix: sat-removal-v1

| Manifest | Expected | Actual | Files | Timeline | Datasets | Scan | Report | Carve | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `control-sat-removal` | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | pass | yes |  |
| `member-sat-removal-a-whole-mirror` | refused \| partial | partial | partial | bit-exact | bit-exact | bit-exact | bit-exact | — | pass | yes | sat-removal/vm/disk-8k: incomplete (blocks written as zeros); sat-removal/vm/disk-16k: incomplete (blocks written as zeros); files sat-removal/fs: incomplete (entries said not whole) |
| `member-sat-removal-one-of-each-mirror` | bit-exact \| reconstructed | reconstructed | reconstructed | bit-exact | bit-exact | refused | bit-exact | — | pass | yes | ; scan label t2-mirror-1: refused; scan rings t2-mirror-1: refused |
