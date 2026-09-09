# Damage matrix: draid1

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-1` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 1} |
| `data-bit-flips` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `data-mirror-both-halves` | bit-exact | n/a | n/a | — | no member matching {'kind': 'mirror', 'leaf': 0} |
| `data-raidz-column` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 1} |
| `labels-all-four` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 2} |
| `labels-front-pair` | bit-exact | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 1} |
| `labels-one-l0` | bit-exact | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 1} |
| `labels-rear-pair` | bit-exact | n/a | n/a | — | no member matching {'kind': 'mirror', 'leaf': 0} |
| `labels-rings-forged-txg` | bit-exact | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 0} |
| `labels-rings-only` | bit-exact | n/a | n/a | — | no member matching {'kind': 'mirror', 'leaf': 1} |
| `labels-vdev-phys-only` | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `member-missing-beyond-parity` | refused | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 0} |
| `member-missing-raidz2` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 0} |
| `member-missing-two-raidz2` | reconstructed | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 0} |
| `member-older-self` | reconstructed | n/a | n/a | — | this image has no older-self material |
| `metadata-crypto-key-object` | refused | n/a | n/a | — | target secret-raw:crypto-key: only objset/dnode-block are located from zdb |
| `metadata-dnode-block` | refused | n/a | n/a | — | target vm/disk-16k:dnode-block not found in the zdb capture |
| `metadata-mos-one-copy` | reconstructed | n/a | n/a | — | target mos:objset: DVA on a vdev this harness cannot map |
| `partition-gpt-rewritten` | bit-exact | n/a | n/a | — | no member matching {'kind': 'raidz2', 'leaf': 3} |
| `partition-start-shifted` | bit-exact | n/a | n/a | — | no member matching {'kind': 'mirror', 'leaf': 0} |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
