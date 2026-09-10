# Damage matrix: draid1

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-across-tops-one-past-budget` | refused | refused | pass | yes | blocks: refused; refused_detail: 192  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 1  fletcher4 gang: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; 1  fletcher4: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; counts: 13 datasets, 267 objects, 268 blocks |
| `combo-across-tops` | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 0, 'top': 1} |
| `combo-bitflips-three-members` | refused | bit-exact | reconstructed | refused | pass | yes | blocks: refused; refused_detail: 32  dnode: every copy failed its checksum; counts: 13 datasets, 289 objects, 294 blocks |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-data-two-members-same-range` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-held-front-labels-everywhere` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-held-labels-plus-two-missing` | refused | refused | pass | yes | blocks: refused; refused_detail: 192  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 1  fletcher4 gang: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; 1  fletcher4: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; counts: 13 datasets, 267 objects, 268 blocks |
| `combo-held-rings-two-members` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-labels-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-missing-plus-unidentified` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-mos-copy-plus-member-gone` | bit-exact | reconstructed | n/a | n/a | — | target mos:objset: DVA on a vdev this harness cannot map |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-rings-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-shift-plus-member-gone` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-triple-labels-data-member` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-truncate-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-two-members-gone` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `combo-unidentified-plus-data` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `data-bit-flips` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `data-gang-header` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `data-one-member` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `data-two-members-same-range` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `labels-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `labels-rings-only` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `labels-vdev-phys-only` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `member-missing-one` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `member-missing-three` | refused | refused | pass | yes | blocks: refused; refused_detail: 192  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 1  fletcher4 gang: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; 1  fletcher4: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; counts: 13 datasets, 267 objects, 268 blocks |
| `member-missing-two` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `metadata-mos-every-copy` | refused | bit-exact | reconstructed | n/a | n/a | — | target mos:objset: DVA on a vdev this harness cannot map |
| `metadata-mos-one-copy` | bit-exact | reconstructed | n/a | n/a | — | target mos:objset: DVA on a vdev this harness cannot map |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `partition-start-shifted` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 290 objects, 295 blocks |
