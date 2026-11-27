# Satellite `sat-freebsd` (sat-freebsd-v1)

Built 2026-11-27T16:59:17Z on FreeBSD 15.1-RELEASE-p6 amd64 with zfs-2.4.2-1-FreeBSD_g6330a45b0.

One raidz1 of three disks made on FreeBSD 15.1-RELEASE-p6 with the OpenZFS of its base system (zfs-2.4.2-1-FreeBSD_g6330a45b0), each disk laid out as FreeBSD's installer lays one out — a GPT with a freebsd-boot partition of 512 KiB and a freebsd-zfs one aligned to 1 MiB, labelled `gpt/<disk>` — and the pool made on the labels. The members are the whole disks, partition table and all, and `layout.json` gives each the offset of its vdev.

## Layout

Ashift 12, as `zpool status` printed it at the end:

```
config:

	NAME           STATE     READ WRITE CKSUM
	sat-freebsd    ONLINE       0     0     0
	  raidz1-0     ONLINE       0     0     0
	    gpt/fbsd0  ONLINE       0     0     0
	    gpt/fbsd1  ONLINE       0     0     0
	    gpt/fbsd2  ONLINE       0     0     0

```

## Datasets

```
sat-freebsd	filesystem	13899658244382871654	Fri Nov 27 16:56 2026	36.0M	139K	-	-	on	lz4	off	none
sat-freebsd@s0	snapshot	13948786386220139358	Fri Nov 27 16:56 2026	0B	139K	-	-	-	-	off	-
sat-freebsd@s1	snapshot	726517546943239026	Fri Nov 27 16:56 2026	0B	139K	-	-	-	-	off	-
sat-freebsd@s2	snapshot	13456990150769006422	Fri Nov 27 16:56 2026	0B	139K	-	-	-	-	off	-
sat-freebsd@s3	snapshot	17419463803905205882	Fri Nov 27 16:56 2026	0B	139K	-	-	-	-	off	-
sat-freebsd/fs	filesystem	17712468838891193288	Fri Nov 27 16:56 2026	1.49M	1.17M	-	-	on	lz4	off	none
sat-freebsd/fs@s0	snapshot	5696839640834293048	Fri Nov 27 16:56 2026	117K	1.09M	-	-	-	-	off	-
sat-freebsd/fs@s1	snapshot	5345889300981594591	Fri Nov 27 16:56 2026	107K	1.12M	-	-	-	-	off	-
sat-freebsd/fs@s2	snapshot	4704063502683263142	Fri Nov 27 16:56 2026	85.2K	1.14M	-	-	-	-	off	-
sat-freebsd/fs@s3	snapshot	6096357574392397290	Fri Nov 27 16:56 2026	0B	1.17M	-	-	-	-	off	-
sat-freebsd/vm	filesystem	6551477737972354355	Fri Nov 27 16:56 2026	33.5M	128K	-	-	on	lz4	off	none
sat-freebsd/vm@s0	snapshot	964754164771583752	Fri Nov 27 16:56 2026	0B	128K	-	-	-	-	off	-
sat-freebsd/vm@s1	snapshot	6534561925644537239	Fri Nov 27 16:56 2026	0B	128K	-	-	-	-	off	-
sat-freebsd/vm@s2	snapshot	4366598879641137865	Fri Nov 27 16:56 2026	0B	128K	-	-	-	-	off	-
sat-freebsd/vm@s3	snapshot	7879041786846226127	Fri Nov 27 16:56 2026	0B	128K	-	-	-	-	off	-
sat-freebsd/vm/disk-16k	volume	11340929292501162573	Fri Nov 27 16:56 2026	19.6M	16.2M	24M	16K	sha256	off	off	none
sat-freebsd/vm/disk-16k@s0	snapshot	3873379490651029173	Fri Nov 27 16:56 2026	1.17M	16.2M	24M	-	-	-	off	-
sat-freebsd/vm/disk-16k@s1	snapshot	17145565352516026955	Fri Nov 27 16:56 2026	170K	16.2M	24M	-	-	-	off	-
sat-freebsd/vm/disk-16k@s2	snapshot	13141374180880222637	Fri Nov 27 16:56 2026	170K	16.2M	24M	-	-	-	off	-
sat-freebsd/vm/disk-16k@s3	snapshot	15921580897495859317	Fri Nov 27 16:56 2026	0B	16.2M	24M	-	-	-	off	-
sat-freebsd/vm/disk-8k	volume	2370346691962085533	Fri Nov 27 16:56 2026	13.7M	10.9M	24M	8K	fletcher4	lz4	off	none
sat-freebsd/vm/disk-8k@s0	snapshot	5179585002660423189	Fri Nov 27 16:56 2026	948K	10.9M	24M	-	-	-	off	-
sat-freebsd/vm/disk-8k@s1	snapshot	8120603359357860977	Fri Nov 27 16:56 2026	266K	10.9M	24M	-	-	-	off	-
sat-freebsd/vm/disk-8k@s2	snapshot	14368019740639187965	Fri Nov 27 16:56 2026	266K	10.9M	24M	-	-	-	off	-
sat-freebsd/vm/disk-8k@s3	snapshot	1504161266989918928	Fri Nov 27 16:56 2026	0B	10.9M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round.  Deterministic content from seed `zvolrescue-sat-freebsd-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
5df834c973335858fbd4637f142952044fa6dc94293536a7d01a27ad06927207  fbsd0.img.zst
0bcfdb60e6a8f40ad7ea673c25aeeb22f522bcec8c45dbf225c3c9158d4b9ee3  fbsd1.img.zst
2389df296e3d7af1f783ab5a7b9af8dffa84c59cfdd376e0444c397266465d3e  fbsd2.img.zst
```
