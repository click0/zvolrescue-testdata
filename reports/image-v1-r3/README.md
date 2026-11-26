# Damage matrix run: image-v1, run 3

The damage matrix against the published image `image-v1` (see
[IMAGE.md](../../IMAGE.md)), judged against the oracle in
`oracle/golden/`.

Run by hand in a Claude Code cloud container (no kernel ZFS: the tools
read the member files themselves), against the release files of
`image-v1` that `run-matrix.py --print-needs` names, each checked
against the pinned sums, on 2026-11-26. zvolrescue `7f5ef23`, manifests
at `b88c6ae`: **70 manifests: pass 70**; inputs unchanged in every run;
the held-out manifests not run; 2448 seconds.

Outcomes: 41 reconstructed, 16 bit-exact, 8 partial, 5 refused.

Files: 39 reconstructed, 22 bit-exact, 5 partial, 4 refused.

History: 68 bit-exact, 2 refused.

What is new since [the second run](../image-v1-r2/README.md):

* `zvolfiles` and `zvoltimeline` are judged in every case, against what
  the kernel read out of the pool's filesystems (`oracle/golden/files.json`)
  and against its own record of its history (`zpool-history-il.txt`) —
  every file's content, mode, owner, object number, mtime and extended
  attribute; every dataset and snapshot at its TXG, in its manner, with
  its GUID; every rename and destroy after the oldest TXG read. 26
  manifests say what the files and the history must come to, the others
  hold them to the rule that nothing is presented as right that is not.
  None was: every `partial` among the files is `zvolfiles` saying which
  entries did not read whole.
* `control-undamaged`, nothing damaged and nothing told: every volume,
  every file of every filesystem and of each of its twelve snapshots,
  and the history, bit-exact.
* `labels-metaslab-slack-every-member`, noise past the last metaslab of
  every member, bit-exact.
* Two findings, neither a wrong answer. With a forged uberblock in every
  ring (`labels-forged-txg`) `zvolfiles` passes the forged TXG over and
  ends 4 — what it read may be older than the pool's newest state —
  where `zvolrescue dump` ends 0 on the same members; which is the
  contract is open, and that case states no expectation for the files.
  And the first full run of the history judge called a defect where a
  stale member reached back before a rename and `zvoltimeline` named the
  volume as it was called then, rightly: the judge was taught that a
  dataset may be named by any name the record gives it.

| File | What |
|---|---|
| `report-image-v1.md`, `report-image-v1.json` | the verdict of every manifest, with the outcome per volume |
| `golden-matrix.log` | the matrix's own log |
