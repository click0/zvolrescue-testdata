# Damage matrix run: image-v1, run 4

The damage matrix against the published image `image-v1` (see
[IMAGE.md](../../IMAGE.md)), judged against the oracle in
`oracle/golden/`.

Run by hand in a Claude Code cloud container (no kernel ZFS: the tools
read the member files themselves), against the release files of
`image-v1` that `run-matrix.py --print-needs` names, each checked
against the pinned sums, on 2026-11-26. zvolrescue `4a95364`, manifests
at `83c8975`: **70 manifests: pass 70**; inputs unchanged in every run;
the held-out manifests not run; 2375 seconds.

Outcomes: 41 reconstructed, 16 bit-exact, 8 partial, 5 refused.

Files: 40 reconstructed, 22 bit-exact, 4 partial, 4 refused.

History: 68 bit-exact, 2 refused.

What is new since [the third run](../image-v1-r3/README.md): the open
question of that run is settled. `zvolrescue dump` and `list` now end
4, as `zvolfiles` does, when the newest TXG that names a volume, or the
pool or the tree it is under, does not read and an older one is used —
what is read may be older than the pool's newest state — and the
harness judges a run that ended 4 for that alone by its bytes, and
records the TXGs it passed over (`passed_over` in the report). Two cases
pass a TXG over:

* `labels-forged-txg`: the forged TXG 5018 on every member, its MOS
  matching no block, passed over by `dump` for every volume and by
  `zvolfiles` for every filesystem, each ending 4; every volume and
  every file as the oracle has it. Its
  files, `partial` in the third run, are `reconstructed`, and the
  manifest says what they must come to again.
* `metadata-dnode-block-every-copy`: for `golden/vm/disk-64k`, whose
  dnode block lost every copy, the newer TXGs that name it and do not
  read it (5015, 5006, 4994 and older) passed over at the dataset, and
  the volume read whole, as the oracle has it, at an older one.

| File | What |
|---|---|
| `report-image-v1.md`, `report-image-v1.json` | the verdict of every manifest, with the outcome per volume |
| `golden-matrix.log` | the matrix's own log |
