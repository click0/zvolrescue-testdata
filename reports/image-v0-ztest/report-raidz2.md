# Damage matrix: raidz2

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-across-tops-one-past-budget` | refused | refused | pass | yes | blocks: refused; refused_detail: 2  blake3: ERROR not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 2272  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 96  dnode: not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; counts: 15 datasets, 198 objects, 193 blocks |
| `combo-across-tops` | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 0, 'top': 1} |
| `combo-bitflips-three-members` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-data-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-labels-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-missing-plus-unidentified` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-mos-copy-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-rings-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-shift-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-triple-labels-data-member` | refused | refused | pass | yes | blocks: refused; refused_detail: 1  objset ztest/ds_3@3: every copy failed its checksum; counts: 15 datasets, 280 objects, 238 blocks |
| `combo-truncate-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-two-members-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-unidentified-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `combo-vdev-phys-gone-and-member-missing` | bit-exact | reconstructed | reconstructed | pass | yes | told about t0-raidz2-0.img; counts: 15 datasets, 294 objects, 244 blocks |
| `data-bit-flips` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `data-gang-header` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `data-one-member` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `data-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `labels-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `labels-rings-only` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `labels-vdev-phys-only` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `member-missing-one` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `member-missing-three` | refused | refused | pass | yes | blocks: refused; refused_detail: 2  blake3: ERROR not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 2272  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 96  dnode: not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; counts: 15 datasets, 198 objects, 193 blocks |
| `member-missing-two` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `metadata-mos-every-copy` | refused | bit-exact | reconstructed | refused | pass | yes | pool: refused |
| `metadata-mos-one-copy` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `partition-start-shifted` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 294 objects, 244 blocks |
