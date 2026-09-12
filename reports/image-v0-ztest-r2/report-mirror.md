# Damage matrix: mirror

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-across-tops-one-past-budget` | refused | n/a | n/a | — | no member matching {'leaf': 2, 'top': 0} |
| `combo-across-tops` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-bitflips-three-members` | refused | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-data-two-members-same-range` | refused | refused | pass | yes | blocks: refused; refused_detail: 32  dnode: every copy failed its checksum; 64  dnode: gang block: header checksum missing; 8192  locate: ERROR every copy failed its checksum; counts: 13 datasets, 251 objects, 210 blocks |
| `combo-label-flips-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-labels-plus-data` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-missing-plus-unidentified` | refused | refused | pass | yes | blocks: refused; refused_detail: 1  blake3: ERROR DVA names unknown top-level vdev 0; 160  dnode: DVA names unknown top-level vdev 0; 224  dnode: encrypted block: no key; counts: 13 datasets, 220 objects, 194 blocks |
| `combo-mos-copy-plus-member-gone` | bit-exact | reconstructed | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-objset-copy-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-rings-plus-data` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-shift-plus-member-gone` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-triple-labels-data-member` | refused | n/a | n/a | — | no member matching {'leaf': 2} |
| `combo-truncate-plus-data` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-two-members-gone` | refused | refused | pass | yes | blocks: refused; refused_detail: 1  blake3: ERROR DVA names unknown top-level vdev 0; 160  dnode: DVA names unknown top-level vdev 0; 224  dnode: encrypted block: no key; counts: 13 datasets, 220 objects, 194 blocks |
| `combo-unidentified-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `combo-vdev-phys-gone-and-member-missing` | refused | refused | pass | yes | told about t0-mirror-0.img; pool: refused |
| `data-bit-flips` | refused | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `data-gang-header` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `data-one-member` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `data-two-members-disjoint` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `data-two-members-same-range` | refused | refused | pass | yes | blocks: refused; refused_detail: 32  dnode: every copy failed its checksum; 64  dnode: gang block: header checksum missing; 8192  locate: ERROR every copy failed its checksum; counts: 13 datasets, 251 objects, 210 blocks |
| `data-zeros-one-member` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `data-zeros-two-members-same-range` | refused | refused | pass | yes | blocks: refused; refused_detail: 32  dnode: every copy failed its checksum; 64  dnode: gang block: header checksum missing; 8192  locate: ERROR every copy failed its checksum; counts: 13 datasets, 251 objects, 210 blocks |
| `labels-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `labels-bit-flips-all-four` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `labels-rings-only` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `labels-vdev-phys-only` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `member-missing-one` | bit-exact | reconstructed | reconstructed | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `member-missing-three` | refused | n/a | n/a | — | no member matching {'leaf': 2} |
| `member-missing-two` | refused | refused | pass | yes | blocks: refused; refused_detail: 1  blake3: ERROR DVA names unknown top-level vdev 0; 160  dnode: DVA names unknown top-level vdev 0; 224  dnode: encrypted block: no key; counts: 13 datasets, 220 objects, 194 blocks |
| `metadata-mos-every-copy` | refused | bit-exact | reconstructed | refused | pass | yes | pool: refused |
| `metadata-mos-one-copy` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `metadata-objset-one-copy` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `partition-start-shifted` | bit-exact | reconstructed | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes | counts: 13 datasets, 258 objects, 212 blocks |
