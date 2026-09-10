# Damage matrix: raidz2

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-across-tops-one-past-budget` | refused | refused | pass | yes | blocks: refused; refused_detail: 32  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 3  fletcher4: ERROR not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 1  fletcher4: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; counts: 14 datasets, 283 objects, 333 blocks |
| `combo-across-tops` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-bitflips-three-members` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-data-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-held-front-labels-everywhere` | bit-exact | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-held-labels-plus-two-missing` | refused | refused | pass | yes | blocks: refused; refused_detail: 32  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 3  fletcher4: ERROR not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 1  fletcher4: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; counts: 14 datasets, 283 objects, 333 blocks |
| `combo-held-rings-two-members` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-labels-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-missing-plus-unidentified` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-mos-copy-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-rings-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-shift-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-triple-labels-data-member` | refused | refused | pass | yes | blocks: refused; refused_detail: 14  sha256: ERROR every copy failed its checksum; counts: 14 datasets, 296 objects, 338 blocks |
| `combo-truncate-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-two-members-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `combo-unidentified-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `data-bit-flips` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `data-gang-header` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `data-one-member` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `data-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-rings-only` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `labels-vdev-phys-only` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `member-missing-one` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `member-missing-three` | refused | refused | pass | yes | blocks: refused; refused_detail: 32  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 3  fletcher4: ERROR not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 1  fletcher4: ERROR not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; counts: 14 datasets, 283 objects, 333 blocks |
| `member-missing-two` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `metadata-mos-every-copy` | refused | bit-exact | reconstructed | refused | pass | yes | pool: refused |
| `metadata-mos-one-copy` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `partition-start-shifted` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes | counts: 14 datasets, 296 objects, 338 blocks |
