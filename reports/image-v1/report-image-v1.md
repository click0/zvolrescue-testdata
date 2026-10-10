# Damage matrix: image-v1

| Manifest | Expected | Actual | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|
| `combo-across-tops-one-past-budget` | refused | partial | n/a | n/a | yes | no member matching {'leaf': 2, 'top': 0} |
| `combo-across-tops` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-bitflips-three-members` | refused | bit-exact | reconstructed | partial | partial | pass | yes | golden/vm/disk-16k: incomplete (blocks written as zeros); golden/vm/disk-blake3: incomplete (blocks written as zeros); golden/vm/disk-sparse: incomplete (blocks written as zeros); golden/secret-raw/disk: incomplete (blocks written as zeros); golden/vm/newname: incomplete (blocks written as zeros) |
| `combo-data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-data-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-label-flips-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-labels-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-missing-plus-unidentified` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-mos-copy-plus-member-gone` | bit-exact | reconstructed | n/a | n/a | yes | top-level vdev 2 is draid1: this harness does not map a DVA through the dRAID permutation, so structure-targeted damage is not placed on it |
| `combo-objset-copy-plus-member-gone` | bit-exact | reconstructed | n/a | n/a | yes | top-level vdev 2 is draid1: this harness does not map a DVA through the dRAID permutation, so structure-targeted damage is not placed on it |
| `combo-partition-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-rings-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-shift-plus-member-gone` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-triple-labels-data-member` | refused | partial | partial | pass | yes | golden/vm/disk-16k: incomplete (blocks written as zeros); golden/vm/disk-64k: incomplete (blocks written as zeros); golden/vm/disk-skein: incomplete (blocks written as zeros); golden/vm/disk-edonr: incomplete (blocks written as zeros); golden/secret-raw/disk: incomplete (blocks written as zeros); golden/vm/newname: incomplete (blocks written as zeros) |
| `combo-truncate-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-two-members-gone` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-unidentified-plus-data` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `combo-vdev-phys-gone-and-member-missing` | bit-exact | reconstructed | reconstructed | pass | yes | told about t1-raidz2-0.img |
| `data-bit-flips` | refused | bit-exact | reconstructed | partial | reconstructed | pass | yes |  |
| `data-gang-header` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `data-one-member` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `data-two-members-disjoint` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `data-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `data-zeros-one-member` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `data-zeros-two-members-same-range` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `labels-all-four` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `labels-bit-flips-all-four` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `labels-front-pair` | bit-exact | bit-exact | pass | yes |  |
| `labels-one-l0` | bit-exact | bit-exact | pass | yes |  |
| `labels-rear-pair` | bit-exact | bit-exact | pass | yes |  |
| `labels-rings-only` | bit-exact | reconstructed | bit-exact | pass | yes |  |
| `labels-vdev-phys-only` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `member-missing-one` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `member-missing-three` | refused | partial | partial | pass | yes | golden/vm/disk-8k: incomplete (blocks written as zeros); golden/vm/disk-16k: incomplete (blocks written as zeros); golden/vm/disk-64k: incomplete (blocks written as zeros); golden/vm/disk-skein: incomplete (blocks written as zeros); golden/vm/disk-edonr: incomplete (blocks written as zeros); golden/vm/disk-blake3: incomplete (blocks written as zeros); golden/vm/disk-sparse: incomplete (blocks written as zeros); golden/secret-raw/disk: incomplete (blocks written as zeros); golden/secret-pw/disk: incomplete (blocks written as zeros); golden/vm/newname: incomplete (blocks written as zeros); golden/vm/clone-of-16k: incomplete (blocks written as zeros) |
| `member-missing-two` | bit-exact | reconstructed | reconstructed | pass | yes |  |
| `metadata-mos-every-copy` | refused | bit-exact | reconstructed | partial | n/a | n/a | yes | top-level vdev 2 is draid1: this harness does not map a DVA through the dRAID permutation, so structure-targeted damage is not placed on it |
| `metadata-mos-one-copy` | bit-exact | reconstructed | n/a | n/a | yes | top-level vdev 2 is draid1: this harness does not map a DVA through the dRAID permutation, so structure-targeted damage is not placed on it |
| `metadata-objset-one-copy` | bit-exact | reconstructed | n/a | n/a | yes | top-level vdev 2 is draid1: this harness does not map a DVA through the dRAID permutation, so structure-targeted damage is not placed on it |
| `partition-gpt-rewritten` | bit-exact | bit-exact | pass | yes |  |
| `partition-start-shifted` | bit-exact | reconstructed | bit-exact | pass | yes |  |
| `partition-tail-truncated` | bit-exact | bit-exact | pass | yes |  |
