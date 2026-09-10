# Damage matrix: mirror

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-across-tops-one-past-budget` | refused | n/a | n/a | — | no member matching {'leaf': 2, 'top': 0} |
| `combo-across-tops` | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 0, 'top': 1} |
| `combo-bitflips-three-members` | refused | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `combo-data-two-members-same-range` | refused | refused | pass | yes | blocks: refused; refused_detail: 4096  locate: ERROR every copy failed its checksum; 1  sha256 encrypted: ERROR every copy failed its checksum; 1  sha512: ERROR every copy failed its checksum; counts: 13 datasets, 245 objects, 200 blocks |
| `combo-held-front-labels-everywhere` | bit-exact | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-held-labels-plus-two-missing` | refused | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-held-rings-two-members` | refused | refused | pass | yes | pool: refused |
| `combo-labels-plus-data` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `combo-missing-plus-unidentified` | refused | refused | pass | yes | pool: refused |
| `combo-mos-copy-plus-member-gone` | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `combo-rings-plus-data` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `combo-shift-plus-member-gone` | refused | refused | pass | yes | pool: refused |
| `combo-triple-labels-data-member` | refused | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-truncate-plus-data` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `combo-two-members-gone` | refused | refused | pass | yes | pool: refused |
| `combo-unidentified-plus-data` | refused | refused | pass | yes | blocks: refused; refused_detail: 4096  locate: ERROR every copy failed its checksum; counts: 13 datasets, 245 objects, 200 blocks |
| `data-bit-flips` | refused | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `data-gang-header` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `data-one-member` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `data-two-members-disjoint` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `data-two-members-same-range` | refused | refused | pass | yes | blocks: refused; refused_detail: 4096  locate: ERROR every copy failed its checksum; 1  sha256 encrypted: ERROR every copy failed its checksum; 1  sha512: ERROR every copy failed its checksum; counts: 13 datasets, 245 objects, 200 blocks |
| `labels-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `labels-rings-only` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `labels-vdev-phys-only` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `member-missing-one` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `member-missing-three` | refused | n/a | n/a | — | no member matching {'leaf': 2} |
| `member-missing-two` | refused | refused | pass | yes | pool: refused |
| `metadata-mos-every-copy` | refused | bit-exact | reconstructed | refused | pass | yes | pool: refused |
| `metadata-mos-one-copy` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `partition-start-shifted` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 245 objects, 200 blocks |
