# Damage matrix: draid1

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-across-tops-one-past-budget` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-across-tops` | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 0, 'top': 1} |
| `combo-bitflips-three-members` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-data-two-members-same-range` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-labels-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-missing-plus-unidentified` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-mos-copy-plus-member-gone` | bit-exact | reconstructed | n/a | n/a | — | target mos:objset: DVA on a vdev this harness cannot map |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-rings-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-shift-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-triple-labels-data-member` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-truncate-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-two-members-gone` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-unidentified-plus-data` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `combo-vdev-phys-gone-and-member-missing` | bit-exact | reconstructed | reconstructed | pass | yes | told about t0-draid1-0.img; counts: 15 datasets, 293 objects, 297 blocks |
| `data-bit-flips` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `data-gang-header` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `data-one-member` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `data-two-members-same-range` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `labels-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `labels-rings-only` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `labels-vdev-phys-only` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `member-missing-one` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `member-missing-three` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `member-missing-two` | refused | bit-exact | reconstructed | reconstructed | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `metadata-mos-every-copy` | refused | bit-exact | reconstructed | n/a | n/a | — | target mos:objset: DVA on a vdev this harness cannot map |
| `metadata-mos-one-copy` | bit-exact | reconstructed | n/a | n/a | — | target mos:objset: DVA on a vdev this harness cannot map |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `partition-start-shifted` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes | counts: 15 datasets, 293 objects, 297 blocks |
