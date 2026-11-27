# Damage matrix: sat-ashift-v1

| Manifest | Expected | Actual | Files | Timeline | Datasets | Scan | Report | Carve | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `control-sat-ashift` | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | pass | yes |  |
| `data-sat-ashift-two-of-ashift13` | refused \| partial | partial | reconstructed | bit-exact | bit-exact | bit-exact | bit-exact | — | pass | yes | sat-ashift/vm/disk-8k: incomplete (blocks written as zeros); sat-ashift/vm/disk-16k: incomplete (blocks written as zeros) |
| `member-sat-ashift-one-of-each` | bit-exact \| reconstructed | reconstructed | reconstructed | bit-exact | bit-exact | refused | bit-exact | — | pass | yes | ; scan label t1-raidz1-2: refused; scan rings t1-raidz1-2: refused |
