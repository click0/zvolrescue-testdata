# Damage matrix run: image-v1, run 5

The damage matrix against the published image `image-v1` (see
[IMAGE.md](../../IMAGE.md)), judged against the oracle in
`oracle/golden/`.

Run by hand in a Claude Code cloud container (no kernel ZFS: the tools
read the member files themselves), against the release files of
`image-v1` that `run-matrix.py --print-needs` names, each checked
against the pinned sums, on 2026-11-26. zvolrescue `29ea950`, manifests
at `6eddaae`: **70 manifests: pass 70**; inputs unchanged in every run;
the held-out manifests not run; 2424 seconds.

Outcomes: 41 reconstructed, 16 bit-exact, 8 partial, 5 refused.

Files: 40 reconstructed, 22 bit-exact, 4 partial, 4 refused.

History: 68 bit-exact, 2 refused.

Datasets: 68 bit-exact, 2 refused.

Scan: 56 bit-exact, 14 refused.

What is new since [the fourth run](../image-v1-r4/README.md): two
answers more judged in every case, against what the build recorded
and nothing read before.

* The datasets `zvolrescue list -r` names, against `zdb -t T -d` at the
  TXG it listed at (`oracle/golden/datasets-by-txg/`): every dataset
  with its kind, object number, creation TXG and referenced size as zdb
  prints it, and nothing zdb does not name. 68 cases list every dataset
  as zdb named it; the two that refuse are those where every ring, or
  every label configuration, is gone, and `dump` refuses there too. On
  the control `list` read each of the 13 TXGs of the ring zdb recorded
  (4905 to 5015) with `--txg`, every one as zdb named it, and each TXG
  at which zdb's listing changes is one it names.
* What `zvolrescue scan -vv` read, against `zdb -l`, `zdb -u` and
  `zpool status` (`labels/`, `zdb-u.txt`, `zpool-status.txt`): the
  nvlist of the label it read of each member, every copy that verifies
  of the uberblock of TXG 4994, and each top-level vdev it assembled.
  56 cases bit-exact; in the other 14 a member none of whose labels
  read, or no copy of that uberblock left, is refused, never presented
  otherwise.

The judges were checked first against a tampered oracle — a creation
TXG changed and a dataset made up at a TXG, a label's `asize`, the
uberblock's timestamp and the dRAID's data disks in `zpool status`
changed — and each was a defect on the control.

| File | What |
|---|---|
| `report-image-v1.md`, `report-image-v1.json` | the verdict of every manifest, with the outcome per volume |
| `golden-matrix.log` | the matrix's own log |
