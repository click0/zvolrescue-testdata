# Satellite `sat-ashift` (sat-ashift-v1)

Built 2026-11-27T14:58:12Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

Two raidz1 of three disks side by side, the first at ashift 9 and the second at 13 — the two sector sizes the golden image does not have, and two of them in one pool, where every top-level vdev has its own.

## Layout

Ashift 9, 13, as `zpool status` printed it at the end:

```
config:

	NAME                                      STATE     READ WRITE CKSUM
	sat-ashift                                ONLINE       0     0     0
	  raidz1-0                                ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1a9-0.img   ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1a9-1.img   ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1a9-2.img   ONLINE       0     0     0
	  raidz1-1                                ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1a13-0.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1a13-1.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1a13-2.img  ONLINE       0     0     0

```

## Datasets

```
sat-ashift	filesystem	11785390358093576744	Fri Nov 27 14:55 2026	50.2M	123K	-	-	on	lz4	off	none
sat-ashift@s0	snapshot	17350636191117101466	Fri Nov 27 14:55 2026	0B	123K	-	-	-	-	off	-
sat-ashift@s1	snapshot	7572826556593665771	Fri Nov 27 14:55 2026	0B	123K	-	-	-	-	off	-
sat-ashift@s2	snapshot	12240310187934259398	Fri Nov 27 14:55 2026	0B	123K	-	-	-	-	off	-
sat-ashift@s3	snapshot	2611611271386565106	Fri Nov 27 14:55 2026	0B	123K	-	-	-	-	off	-
sat-ashift/fs	filesystem	13944565575674359215	Fri Nov 27 14:55 2026	1.47M	1.10M	-	-	on	lz4	off	none
sat-ashift/fs@s0	snapshot	4180413273173487697	Fri Nov 27 14:55 2026	120K	1.02M	-	-	-	-	off	-
sat-ashift/fs@s1	snapshot	5474555037967164613	Fri Nov 27 14:55 2026	107K	1.05M	-	-	-	-	off	-
sat-ashift/fs@s2	snapshot	1317781730985970411	Fri Nov 27 14:55 2026	120K	1.07M	-	-	-	-	off	-
sat-ashift/fs@s3	snapshot	13490966928520193363	Fri Nov 27 14:55 2026	0B	1.10M	-	-	-	-	off	-
sat-ashift/vm	filesystem	15003240768648053990	Fri Nov 27 14:55 2026	47.6M	143K	-	-	on	lz4	off	none
sat-ashift/vm@s0	snapshot	5164677403022787315	Fri Nov 27 14:55 2026	0B	143K	-	-	-	-	off	-
sat-ashift/vm@s1	snapshot	8598400434149531700	Fri Nov 27 14:55 2026	0B	143K	-	-	-	-	off	-
sat-ashift/vm@s2	snapshot	12954388248635075280	Fri Nov 27 14:55 2026	0B	143K	-	-	-	-	off	-
sat-ashift/vm@s3	snapshot	2811755830823750376	Fri Nov 27 14:55 2026	0B	143K	-	-	-	-	off	-
sat-ashift/vm/disk-16k	volume	1450997518016859085	Fri Nov 27 14:55 2026	22.8M	18.7M	24M	16K	sha256	off	off	none
sat-ashift/vm/disk-16k@s0	snapshot	15420233247746757628	Fri Nov 27 14:55 2026	1.41M	18.7M	24M	-	-	-	off	-
sat-ashift/vm/disk-16k@s1	snapshot	7045285029679987885	Fri Nov 27 14:55 2026	178K	18.7M	24M	-	-	-	off	-
sat-ashift/vm/disk-16k@s2	snapshot	14174197326319392569	Fri Nov 27 14:55 2026	178K	18.7M	24M	-	-	-	off	-
sat-ashift/vm/disk-16k@s3	snapshot	11605893775303750817	Fri Nov 27 14:55 2026	0B	18.7M	24M	-	-	-	off	-
sat-ashift/vm/disk-8k	volume	8796844695387855612	Fri Nov 27 14:55 2026	24.7M	19.9M	24M	8K	fletcher4	lz4	off	none
sat-ashift/vm/disk-8k@s0	snapshot	10954669534807398363	Fri Nov 27 14:55 2026	1.60M	21.0M	24M	-	-	-	off	-
sat-ashift/vm/disk-8k@s1	snapshot	7136941251264638146	Fri Nov 27 14:55 2026	271K	20.7M	24M	-	-	-	off	-
sat-ashift/vm/disk-8k@s2	snapshot	13465842394674574464	Fri Nov 27 14:55 2026	271K	20.1M	24M	-	-	-	off	-
sat-ashift/vm/disk-8k@s3	snapshot	3475037341284286766	Fri Nov 27 14:55 2026	0B	19.9M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round.  Deterministic content from seed `zvolrescue-sat-ashift-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
a63ea05009e126e82d936a8368c924cc359feb2621ff7ebdb4c92a0d3f310870  raidz1a13-0.img.zst
30491fea6c247fb8619f6bfa0c9f3acae958035bc055bde5038bc994a78ce741  raidz1a13-1.img.zst
8bcc50ddd251902e9396e7504d495124c51caf5fe7111bc690143d8b8ec2cc28  raidz1a13-2.img.zst
030f1a9025446010260af30c07d928aaa652a32bb205703b22fd4d5d717ffce5  raidz1a9-0.img.zst
4dd5b77fb5a2b3585d208ebca4f9cf6a8c09f9ff7427599b1da7c0fe085da72f  raidz1a9-1.img.zst
5843c57998874c9a511dea39becd8183bf0e836c4b32fadc4276f51eeced6f8b  raidz1a9-2.img.zst
```
