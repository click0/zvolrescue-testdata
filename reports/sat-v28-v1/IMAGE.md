# Satellite `sat-v28` (sat-v28-v1)

Built 2026-11-27T16:36:26Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

One raidz2 of four disks created with `-o version=28`: the last pool version before feature flags, with the ZPL of version 5 — its labels say version 28 and list no features, its MOS has no feature objects, and its volume is compressed with lzjb.

## Layout

Ashift 12, as `zpool status` printed it at the end:

```
config:

	NAME                                   STATE     READ WRITE CKSUM
	sat-v28                                ONLINE       0     0     0
	  raidz2-0                             ONLINE       0     0     0
	    /var/tmp/sat/members/raidz2-0.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz2-1.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz2-2.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz2-3.img  ONLINE       0     0     0

```

## Datasets

```
sat-v28	filesystem	11019915337993082754	Fri Nov 27 16:33 2026	41.3M	279K	-	-	on	lzjb	off	none
sat-v28@s0	snapshot	17662276737782598001	Fri Nov 27 16:33 2026	0B	279K	-	-	-	-	off	-
sat-v28@s1	snapshot	18441568694637993192	Fri Nov 27 16:33 2026	0B	279K	-	-	-	-	off	-
sat-v28@s2	snapshot	10205982219547918636	Fri Nov 27 16:33 2026	0B	279K	-	-	-	-	off	-
sat-v28@s3	snapshot	10493978807973620072	Fri Nov 27 16:33 2026	0B	279K	-	-	-	-	off	-
sat-v28/fs	filesystem	7023919989530861169	Fri Nov 27 16:33 2026	2.08M	1.46M	-	-	on	lzjb	off	none
sat-v28/fs@s0	snapshot	16104562609600736373	Fri Nov 27 16:33 2026	209K	1.37M	-	-	-	-	off	-
sat-v28/fs@s1	snapshot	5025669193279183296	Fri Nov 27 16:33 2026	198K	1.40M	-	-	-	-	off	-
sat-v28/fs@s2	snapshot	5208067825168554993	Fri Nov 27 16:33 2026	209K	1.43M	-	-	-	-	off	-
sat-v28/fs@s3	snapshot	16191092701313404728	Fri Nov 27 16:33 2026	0B	1.46M	-	-	-	-	off	-
sat-v28/vm	filesystem	15448665293044380853	Fri Nov 27 16:33 2026	37.0M	256K	-	-	on	lzjb	off	none
sat-v28/vm@s0	snapshot	11787903824565531259	Fri Nov 27 16:33 2026	0B	256K	-	-	-	-	off	-
sat-v28/vm@s1	snapshot	6065874476853439978	Fri Nov 27 16:33 2026	0B	256K	-	-	-	-	off	-
sat-v28/vm@s2	snapshot	16326120896960469889	Fri Nov 27 16:33 2026	0B	256K	-	-	-	-	off	-
sat-v28/vm@s3	snapshot	7789540511788503403	Fri Nov 27 16:33 2026	0B	256K	-	-	-	-	off	-
sat-v28/vm/disk-16k	volume	17434055734247719961	Fri Nov 27 16:33 2026	21.6M	17.7M	24M	16K	sha256	off	off	none
sat-v28/vm/disk-16k@s0	snapshot	15639370952296544036	Fri Nov 27 16:33 2026	1.32M	17.7M	24M	-	-	-	off	-
sat-v28/vm/disk-16k@s1	snapshot	17416853077386038921	Fri Nov 27 16:33 2026	232K	17.7M	24M	-	-	-	off	-
sat-v28/vm/disk-16k@s2	snapshot	17626013894133135394	Fri Nov 27 16:33 2026	232K	17.7M	24M	-	-	-	off	-
sat-v28/vm/disk-16k@s3	snapshot	9080208625389576666	Fri Nov 27 16:33 2026	0B	17.7M	24M	-	-	-	off	-
sat-v28/vm/disk-8k	volume	4874848789514195950	Fri Nov 27 16:33 2026	15.1M	12.0M	24M	8K	fletcher4	lzjb	off	none
sat-v28/vm/disk-8k@s0	snapshot	11283296496931767612	Fri Nov 27 16:33 2026	1.04M	12.0M	24M	-	-	-	off	-
sat-v28/vm/disk-8k@s1	snapshot	8344605921775399559	Fri Nov 27 16:33 2026	326K	12.0M	24M	-	-	-	off	-
sat-v28/vm/disk-8k@s2	snapshot	12106707361139328562	Fri Nov 27 16:33 2026	326K	12.0M	24M	-	-	-	off	-
sat-v28/vm/disk-8k@s3	snapshot	1871117671248808343	Fri Nov 27 16:33 2026	0B	12.0M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lzjb, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round.  Deterministic content from seed `zvolrescue-sat-v28-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
43d01b02cea7afaf4d90a54287cea9fafdab02197d43f35b605ef26c5aac23f8  raidz2-0.img.zst
e8d011c3597f981aae62fe6e9945ddd2a52af2ee1c2d2bca5c75799c09363512  raidz2-1.img.zst
b4cf1c49dff87b66b2be7a8ead27837765ab4b96f4fa6df1cabc3c1a6b7faaa0  raidz2-2.img.zst
b44819d3885fae6da4ac87a4fbc7ad9187ac88c9d11361a3a98e34faa492193d  raidz2-3.img.zst
```
