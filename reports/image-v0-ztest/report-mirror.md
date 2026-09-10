# Damage matrix: mirror

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-across-tops-one-past-budget` | refused | n/a | n/a | — | no member matching {'leaf': 2, 'top': 0} |
| `combo-across-tops` | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 0, 'top': 1} |
| `combo-bitflips-three-members` | refused | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `combo-data-two-members-same-range` | refused | refused | pass | yes | blocks: refused; refused_detail: 2  blake3: ERROR every copy failed its checksum; 640  dnode: every copy failed its checksum; 1  fletcher4: ERROR every copy failed its checksum; counts: 18 datasets, 286 objects, 248 blocks |
| `combo-labels-plus-data` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `combo-missing-plus-unidentified` | refused | refused | pass | yes | pool: refused |
| `combo-mos-copy-plus-member-gone` | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `combo-rings-plus-data` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `combo-shift-plus-member-gone` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `combo-triple-labels-data-member` | refused | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-truncate-plus-data` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `combo-two-members-gone` | refused | refused | pass | yes | pool: refused |
| `combo-unidentified-plus-data` | refused | refused | pass | yes | blocks: refused; refused_detail: 16384  locate: ERROR every copy failed its checksum; counts: 18 datasets, 306 objects, 259 blocks |
| `combo-vdev-phys-gone-and-member-missing` | refused | refused | pass | yes | told about t0-mirror-0.img; pool: refused |
| `data-bit-flips` | refused | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `data-gang-header` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `data-one-member` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `data-two-members-disjoint` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `data-two-members-same-range` | refused | refused | pass | yes | blocks: refused; refused_detail: 2  blake3: ERROR every copy failed its checksum; 640  dnode: every copy failed its checksum; 1  fletcher4: ERROR every copy failed its checksum; counts: 18 datasets, 286 objects, 248 blocks |
| `labels-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `labels-rings-only` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `labels-vdev-phys-only` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `member-missing-one` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `member-missing-three` | refused | n/a | n/a | — | no member matching {'leaf': 2} |
| `member-missing-two` | refused | refused | pass | yes | pool: refused |
| `metadata-mos-every-copy` | refused | bit-exact | reconstructed | refused | pass | yes | pool: refused |
| `metadata-mos-one-copy` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `partition-start-shifted` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes | counts: 18 datasets, 306 objects, 263 blocks |
