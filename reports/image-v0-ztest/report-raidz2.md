# Damage matrix: raidz2

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-1` | reconstructed | n/a | n/a | — | no member matching {'kind': 'mirror', 'leaf': 1} |
| `data-bit-flips` | reconstructed | n/a | n/a | — | no member matching {'kind': 'draid1', 'leaf': 3} |
| `data-mirror-both-halves` | bit-exact | n/a | n/a | — | no member matching {'kind': 'mirror', 'leaf': 0} |
| `data-raidz-column` | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-all-four` | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-rear-pair` | bit-exact | n/a | n/a | — | no member matching {'kind': 'mirror', 'leaf': 0} |
| `labels-rings-forged-txg` | bit-exact | n/a | n/a | — | this image has no older-self material |
| `labels-rings-only` | bit-exact | n/a | n/a | — | no member matching {'kind': 'mirror', 'leaf': 1} |
| `labels-vdev-phys-only` | bit-exact | n/a | n/a | — | no member matching {'kind': 'draid1', 'leaf': 0} |
| `member-missing-beyond-parity` | refused | refused | pass | yes | blocks: refused; refused_detail: 32  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 3  fletcher4: ERROR not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 1  fletcher4: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; counts: 14 datasets, 283 objects, 333 blocks |
| `member-missing-raidz2` | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `member-missing-two-raidz2` | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `member-older-self` | reconstructed | n/a | n/a | — | no member matching {'kind': 'draid1', 'leaf': 1} |
| `metadata-crypto-key-object` | refused | n/a | n/a | — | target secret-raw:crypto-key: only objset/dnode-block are located from zdb |
| `metadata-dnode-block` | refused | n/a | n/a | — | target vm/disk-16k:dnode-block not found in the zdb capture |
| `metadata-mos-one-copy` | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `partition-start-shifted` | bit-exact | n/a | n/a | — | no member matching {'kind': 'mirror', 'leaf': 0} |
| `partition-tail-truncated` | bit-exact | n/a | n/a | — | no member matching {'kind': 'draid1', 'leaf': 2} |
