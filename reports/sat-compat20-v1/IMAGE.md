# Satellite `sat-compat20` (sat-compat20-v1)

Built 2026-11-27T16:36:03Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

One raidz1 of three disks created with `compatibility=openzfs-2.0-linux`: the features OpenZFS 2.0 on Linux knows and no later one — no block cloning, no RAIDZ expansion, no `zilsaxattr`, `head_errlog` or `vdev_zaps_v2` — as a pool made to be imported by 2.0, or made by it, has.

## Layout

Ashift 12, as `zpool status` printed it at the end:

```
config:

	NAME                                   STATE     READ WRITE CKSUM
	sat-compat20                           ONLINE       0     0     0
	  raidz1-0                             ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-0.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-1.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-2.img  ONLINE       0     0     0

```

## Datasets

```
sat-compat20	filesystem	13304454414257701462	Fri Nov 27 16:33 2026	36.2M	139K	-	-	on	lz4	off	none
sat-compat20@s0	snapshot	4495896154936489689	Fri Nov 27 16:33 2026	0B	139K	-	-	-	-	off	-
sat-compat20@s1	snapshot	3772377970317950184	Fri Nov 27 16:33 2026	0B	139K	-	-	-	-	off	-
sat-compat20@s2	snapshot	16845817322776341045	Fri Nov 27 16:33 2026	0B	139K	-	-	-	-	off	-
sat-compat20@s3	snapshot	942404192262027810	Fri Nov 27 16:33 2026	0B	139K	-	-	-	-	off	-
sat-compat20/fs	filesystem	15584052650798293438	Fri Nov 27 16:33 2026	1.58M	1.24M	-	-	on	lz4	off	none
sat-compat20/fs@s0	snapshot	2084358569929510617	Fri Nov 27 16:33 2026	117K	1.16M	-	-	-	-	off	-
sat-compat20/fs@s1	snapshot	13431833278039434434	Fri Nov 27 16:33 2026	107K	1.19M	-	-	-	-	off	-
sat-compat20/fs@s2	snapshot	3851930207132138971	Fri Nov 27 16:33 2026	117K	1.21M	-	-	-	-	off	-
sat-compat20/fs@s3	snapshot	10369528590839708609	Fri Nov 27 16:33 2026	0B	1.24M	-	-	-	-	off	-
sat-compat20/vm	filesystem	7500533562755095631	Fri Nov 27 16:33 2026	33.5M	128K	-	-	on	lz4	off	none
sat-compat20/vm@s0	snapshot	5383454511541627610	Fri Nov 27 16:33 2026	0B	128K	-	-	-	-	off	-
sat-compat20/vm@s1	snapshot	6613651161265509008	Fri Nov 27 16:33 2026	0B	128K	-	-	-	-	off	-
sat-compat20/vm@s2	snapshot	7377167465101690716	Fri Nov 27 16:33 2026	0B	128K	-	-	-	-	off	-
sat-compat20/vm@s3	snapshot	5159073012884721442	Fri Nov 27 16:33 2026	0B	128K	-	-	-	-	off	-
sat-compat20/vm/disk-16k	volume	16166292904442731049	Fri Nov 27 16:33 2026	19.6M	16.2M	24M	16K	sha256	off	off	none
sat-compat20/vm/disk-16k@s0	snapshot	16228940875558925900	Fri Nov 27 16:33 2026	1.17M	16.2M	24M	-	-	-	off	-
sat-compat20/vm/disk-16k@s1	snapshot	5823001913480530835	Fri Nov 27 16:33 2026	170K	16.2M	24M	-	-	-	off	-
sat-compat20/vm/disk-16k@s2	snapshot	5469346952545773915	Fri Nov 27 16:33 2026	170K	16.2M	24M	-	-	-	off	-
sat-compat20/vm/disk-16k@s3	snapshot	1174504696106651954	Fri Nov 27 16:33 2026	0B	16.2M	24M	-	-	-	off	-
sat-compat20/vm/disk-8k	volume	6526798736877178467	Fri Nov 27 16:33 2026	13.7M	10.9M	24M	8K	fletcher4	lz4	off	none
sat-compat20/vm/disk-8k@s0	snapshot	10257458624407429268	Fri Nov 27 16:33 2026	948K	10.9M	24M	-	-	-	off	-
sat-compat20/vm/disk-8k@s1	snapshot	8647265524659651031	Fri Nov 27 16:33 2026	266K	10.9M	24M	-	-	-	off	-
sat-compat20/vm/disk-8k@s2	snapshot	1547499566792999872	Fri Nov 27 16:33 2026	266K	10.9M	24M	-	-	-	off	-
sat-compat20/vm/disk-8k@s3	snapshot	11363210658903372810	Fri Nov 27 16:33 2026	0B	10.9M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round.  Deterministic content from seed `zvolrescue-sat-compat20-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
2255a9657ba5f78819fcc074b14d0cb462c88fe22b8f0c9d59cf3983a1d2fbc3  raidz1-0.img.zst
c015f49d2e12187a2d54fc4da1003b889c9422988e4369dc416f5247ac8c4119  raidz1-1.img.zst
a2733a63cb67cb47e68f08c9e59441c049600b4197ce64eabe30ef87c04606b0  raidz1-2.img.zst
```
