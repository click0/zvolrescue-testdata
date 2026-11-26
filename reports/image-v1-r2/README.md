# Damage matrix run: image-v1, second run

The damage matrix against the published golden image `image-v1` (see
[IMAGE.md](../../IMAGE.md)), judged against the oracle in
`oracle/golden/`: every volume of every damaged copy against the
kernel's hash, every expectation enforced, the inputs hashed before and
after every run.

Run by hand, 2026-11-26, in a Claude Code cloud container (no kernel
ZFS: the tool reads the member files itself, and needs none), against
the release files of `image-v1` that `run-matrix.py --print-needs`
names for these manifests — the ten members and six of the ten older
copies — each checked against the pinned `SHA256SUMS` and the
decompressed members against `oracle/golden/members.sha256`. zvolrescue
`9a04283`, manifests at `179b06c`: **68 manifests: pass 68**, none `n/a`,
none outside its expected category, inputs unchanged in every run; the
three `held_out` were not run. 1722 seconds.

Outcomes: 14 bit-exact, 41 reconstructed, 5 refused, 8 partial (the
lost blocks counted and written as zeros, accepted where `refused` is
expected).

What is new since [the first run](../image-v1/README.md) (41 manifests,
35 pass, 6 n/a):

* every manifest now applies to `image-v1`: the six that were `n/a`
  (structures the harness could not locate before the `zdb -dddddd`
  capture) are placed and pass;
* the ten cases of what the tool reads now — a pool no uberblock or no
  label is left of, read at the headers `zvolcarve roots` finds and
  through the layout given by hand, the member order searched; the boot
  area; an imager's map; a wrong key and none — all pass. The first of
  them to run, `labels-vdev-phys-every-member-hints`, found a defect
  before it passed: read through `--hints`, zvolrescue took no feature
  from the labels and read OpenZFS 2.4's gang headers at 512 bytes,
  giving nine of the eleven volumes partial. Fixed in `9a04283`, from
  the MOS's own `features_for_read`.

| File | What |
|---|---|
| `report-image-v1.md`, `report-image-v1.json` | the verdict of every manifest, with the outcome per volume |
| `golden-matrix.log` | the matrix's own log |
