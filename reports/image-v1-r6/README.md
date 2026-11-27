# Damage matrix run: image-v1, run 6

The damage matrix against the published image `image-v1` (see
[IMAGE.md](../../IMAGE.md)), judged against the oracle in
`oracle/golden/`.

Run by hand in a Claude Code cloud container (no kernel ZFS: the tools
read the member files themselves), against the release files of
`image-v1` that `run-matrix.py --print-needs` names, each checked
against the pinned sums, on 2026-11-27. zvolrescue `030aa5b`, manifests
at `f8892ee`: **70 manifests: pass 70**; inputs unchanged in every run;
the held-out manifests not run; 2643 seconds.

Outcomes: 41 reconstructed, 16 bit-exact, 8 partial, 5 refused.

Files: 40 reconstructed, 22 bit-exact, 4 partial, 4 refused.

History: 68 bit-exact, 2 refused.

Datasets: 68 bit-exact, 2 refused.

Scan: 49 bit-exact, 21 refused.

Report: 70 bit-exact.

Carve: 3 bit-exact, 1 partial, 1 refused.

What is new since [the fifth run](../image-v1-r5/README.md): every
one of the five programs is judged, and `list` and `scan` against more
of zdb's records.

* The features `zvolrescue list` names (new in `030aa5b`), against
  the refcounts zdb verified at the TXG it read and `zpool get all`
  (`datasets-by-txg/`, `zpool-get-all.txt`): each of the 47 with
  its state, and the 22 active with zdb's refcount. 68 cases bit-exact;
  the two that refuse are those `list` refuses.
* What `scan -vv` read of every slot of every label's uberblock ring,
  against `zdb -lu` of each member (`labels-uberblocks/`, captured
  offline from the published members), the uberblock of the export
  (`zdb-u-export.txt`), and the pool's version, GUID and ashifts
  (`pool-facts.txt`). Seven cases bit-exact in run 5 are refused here:
  a member put back as an older copy of itself (the five
  `older-self-*` and `combo-older-self-*` cases) holds the slots of
  other TXGs, which zdb's record says nothing of, and a member whose
  rings the damage wiped (`labels-rings-only`, `combo-rings-plus-data`) has
  none of zdb's slots to verify. Nothing read is presented otherwise.
  `scan --hints` now reports the pool the layout lays out, and where
  neither a label nor the MOS says its GUIDs the judge leaves them
  unjudged.
* `zvolreport` in every case: the report built of the case's runs, and
  verified, holds each output hash as the evidence logs recorded it,
  and verify fails on a tampered copy (on the control). 70 bit-exact.
* `zvolcarve` in the four cases whose damage leaves no ring, or no
  label configuration, to read, or the key wrong or missing, and on the
  control: the volumes it
  carves, dumped at their `volsize`, by their bytes against
  `volumes.sha256`. Bit-exact on the control and both key cases;
  partial where every ring is gone — the volumes under salted
  checksums (blake3, skein, edonr) cannot be verified with no MOS to
  give the salt, and are refused, saying so (new in `030aa5b`); refused
  where every label's configuration is gone.

The new judges were checked first against a tampered oracle — a
feature's refcount, a ring slot's `guid_sum`, a label's slot and
`ashift` — and each was a defect on the control.

| File | What |
|---|---|
| `report-image-v1.md`, `report-image-v1.json` | the verdict of every manifest, with the outcome per volume |
| `golden-matrix.log` | the matrix's own log |
