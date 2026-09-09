# Damage matrix: mirror

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-1` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 1} |
| `data-bit-flips` | reconstructed | n/a | n/a | — | no member matching {'kind': 'draid1', 'leaf': 3} |
| `data-mirror-both-halves` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `data-raidz-column` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 1} |
| `labels-all-four` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 2} |
| `labels-front-pair` | bit-exact | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 1} |
| `labels-one-l0` | bit-exact | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 1} |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `labels-rings-forged-txg` | bit-exact | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 0} |
| `labels-rings-only` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `labels-vdev-phys-only` | bit-exact | n/a | n/a | — | no member matching {'kind': 'draid1', 'leaf': 0} |
| `member-missing-beyond-parity` | refused | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 0} |
| `member-missing-raidz2` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 0} |
| `member-missing-two-raidz2` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 0} |
| `member-older-self` | reconstructed | n/a | n/a | — | no member matching {'kind': 'draid1', 'leaf': 1} |
| `metadata-crypto-key-object` | refused | n/a | n/a | — | target secret-raw:crypto-key: only objset/dnode-block are located from zdb |
| `metadata-dnode-block` | refused | n/a | n/a | — | target vm/disk-16k:dnode-block not found in the zdb capture |
| `metadata-mos-one-copy` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `partition-gpt-rewritten` | bit-exact | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 3} |
| `partition-start-shifted` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `partition-tail-truncated` | bit-exact | n/a | n/a | — | no member matching {'kind': 'draid1', 'leaf': 2} |
