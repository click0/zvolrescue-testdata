# Damage matrix: raidz2

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-across-tops-one-past-budget` | refused | refused | pass | yes | blocks: refused; refused_detail: 128  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 224  dnode: not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; 1  fletcher4 gang: ERROR not recoverable: reconstruct: TooManyMissing { missing: 1, parities: 0 }; counts: 16 datasets, 296 objects, 276 blocks |
| `combo-across-tops` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-bitflips-three-members` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-data-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-label-flips-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-labels-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-missing-plus-unidentified` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-mos-copy-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-objset-copy-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-rings-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-shift-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-triple-labels-data-member` | refused | refused | pass | yes | blocks: refused; refused_detail: 8192  locate: ERROR every copy failed its checksum; counts: 16 datasets, 332 objects, 297 blocks |
| `combo-truncate-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-two-members-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-unidentified-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `combo-vdev-phys-gone-and-member-missing` | bit-exact | reconstructed | reconstructed | pass | yes | told about t0-raidz2-0.img; counts: 16 datasets, 332 objects, 299 blocks |
| `data-bit-flips` | refused | bit-exact | reconstructed | bit-exact | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `data-gang-header` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `data-one-member` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `data-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `data-zeros-one-member` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `data-zeros-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `labels-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `labels-bit-flips-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `labels-rings-only` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `labels-vdev-phys-only` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `member-missing-one` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `member-missing-three` | refused | refused | pass | yes | blocks: refused; refused_detail: 128  dnode: not recoverable: 1 data column(s) missing, only 0 parity column(s) readable; 224  dnode: not recoverable: 2 data column(s) missing, only 1 parity column(s) readable; 1  fletcher4 gang: ERROR not recoverable: reconstruct: TooManyMissing { missing: 1, parities: 0 }; counts: 16 datasets, 296 objects, 276 blocks |
| `member-missing-two` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `metadata-mos-every-copy` | refused | bit-exact | reconstructed | refused | pass | yes | pool: refused |
| `metadata-mos-one-copy` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `metadata-objset-one-copy` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `partition-start-shifted` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes | counts: 16 datasets, 332 objects, 299 blocks |
