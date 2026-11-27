# Damage matrix: sat-slog-v1

| Manifest | Expected | Actual | Files | Timeline | Datasets | Scan | Report | Carve | Verdict | Inputs unchanged | Detail |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `control-sat-slog` | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | pass | yes |  |
| `member-sat-slog-log-gone` | bit-exact \| reconstructed | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | bit-exact | — | pass | yes |  |
| `member-sat-slog-log-zeroed` | bit-exact \| reconstructed | bit-exact | bit-exact | bit-exact | bit-exact | refused | bit-exact | — | pass | yes | ; scan label t1-file-0: refused; scan rings t1-file-0: refused |
| `member-sat-slog-mirror-half` | bit-exact \| reconstructed | reconstructed | reconstructed | bit-exact | bit-exact | bit-exact | bit-exact | — | pass | yes |  |
