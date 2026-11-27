# Satellite `sat-spare` (sat-spare-v1)

Built 2026-11-27T14:56:58Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

One raidz2 of five disks with a hot spare: the third disk taken offline after round 0, written past for a round, and replaced by the spare after round 1 (`spare-2`, the spare resilvered whole, the disk left offline and stale); after round 2 the fifth disk replaced by a new one with the resilver held still (`zfs_scan_suspend_progress`), so that the pool is exported with `replacing-4` unfinished — the new disk holding only what was written after. Every device of both slots is a member (`t0-raidz2-2.1`, `t0-raidz2-4.1`).

## Layout

Ashift 12, as `zpool status` printed it at the end:

```
config:

	NAME                                     STATE     READ WRITE CKSUM
	sat-spare                                DEGRADED     0     0     0
	  raidz2-0                               DEGRADED     0     0     0
	    /var/tmp/sat/members/raidz2-0.img    ONLINE       0     0     0
	    /var/tmp/sat/members/raidz2-1.img    ONLINE       0     0     0
	    spare-2                              DEGRADED     0     0     0
	      /var/tmp/sat/members/raidz2-2.img  OFFLINE      0     0     0
	      /var/tmp/sat/members/spare-0.img   ONLINE       0     0     0
	    /var/tmp/sat/members/raidz2-3.img    ONLINE       0     0     0
	    replacing-4                          ONLINE       0     0     0
	      /var/tmp/sat/members/raidz2-4.img  ONLINE       0     0     0
	      /var/tmp/sat/members/new-0.img     ONLINE       0     0     0
	spares
	  /var/tmp/sat/members/spare-0.img       INUSE     currently in use

```

## Datasets

```
sat-spare	filesystem	5233430251100883933	Fri Nov 27 14:55 2026	47.7M	185K	-	-	on	lz4	off	none
sat-spare@s0	snapshot	1546393551516250572	Fri Nov 27 14:55 2026	0B	185K	-	-	-	-	off	-
sat-spare@s1	snapshot	5718822966391581470	Fri Nov 27 14:55 2026	0B	185K	-	-	-	-	off	-
sat-spare@s2	snapshot	8540995584331511593	Fri Nov 27 14:55 2026	0B	185K	-	-	-	-	off	-
sat-spare@s3	snapshot	15460320636582386565	Fri Nov 27 14:55 2026	0B	185K	-	-	-	-	off	-
sat-spare/fs	filesystem	9988273545160067415	Fri Nov 27 14:55 2026	1.80M	1.38M	-	-	on	lz4	off	none
sat-spare/fs@s0	snapshot	8889991231797737172	Fri Nov 27 14:55 2026	142K	1.29M	-	-	-	-	off	-
sat-spare/fs@s1	snapshot	16900658830842924205	Fri Nov 27 14:55 2026	128K	1.32M	-	-	-	-	off	-
sat-spare/fs@s2	snapshot	2510539920673601957	Fri Nov 27 14:55 2026	114K	1.35M	-	-	-	-	off	-
sat-spare/fs@s3	snapshot	1590675984689719796	Fri Nov 27 14:55 2026	0B	1.38M	-	-	-	-	off	-
sat-spare/vm	filesystem	16371788048294571651	Fri Nov 27 14:55 2026	44.3M	170K	-	-	on	lz4	off	none
sat-spare/vm@s0	snapshot	17408865942991098955	Fri Nov 27 14:55 2026	0B	170K	-	-	-	-	off	-
sat-spare/vm@s1	snapshot	13040215689041010315	Fri Nov 27 14:55 2026	0B	170K	-	-	-	-	off	-
sat-spare/vm@s2	snapshot	13977902553673642108	Fri Nov 27 14:55 2026	0B	170K	-	-	-	-	off	-
sat-spare/vm@s3	snapshot	5817235139765360617	Fri Nov 27 14:55 2026	0B	170K	-	-	-	-	off	-
sat-spare/vm/disk-16k	volume	15286671723850347201	Fri Nov 27 14:55 2026	26.1M	21.5M	24M	16K	sha256	off	off	none
sat-spare/vm/disk-16k@s0	snapshot	18369303150095017810	Fri Nov 27 14:55 2026	1.53M	21.5M	24M	-	-	-	off	-
sat-spare/vm/disk-16k@s1	snapshot	10945621038543018150	Fri Nov 27 14:55 2026	199K	21.5M	24M	-	-	-	off	-
sat-spare/vm/disk-16k@s2	snapshot	18442559523780442414	Fri Nov 27 14:55 2026	199K	21.5M	24M	-	-	-	off	-
sat-spare/vm/disk-16k@s3	snapshot	12308066538338089023	Fri Nov 27 14:55 2026	0B	21.5M	24M	-	-	-	off	-
sat-spare/vm/disk-8k	volume	10308582330306306289	Fri Nov 27 14:55 2026	18.0M	14.5M	24M	8K	fletcher4	lz4	off	none
sat-spare/vm/disk-8k@s0	snapshot	5213244167444409478	Fri Nov 27 14:55 2026	1.18M	14.5M	24M	-	-	-	off	-
sat-spare/vm/disk-8k@s1	snapshot	15427379768253595013	Fri Nov 27 14:55 2026	298K	14.5M	24M	-	-	-	off	-
sat-spare/vm/disk-8k@s2	snapshot	3230739208254403565	Fri Nov 27 14:55 2026	298K	14.5M	24M	-	-	-	off	-
sat-spare/vm/disk-8k@s3	snapshot	11987148306493927734	Fri Nov 27 14:55 2026	0B	14.5M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round. After round 0, `raidz2-2` taken offline; after round 1, replaced by `spare-0` and the resilver waited for; after round 2, `raidz2-4` replaced by `new-0` with the scan suspended. Deterministic content from seed `zvolrescue-sat-spare-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
38b0247670e11637b23bafd9767ca301ffde7ab2e9d21e658239508c8c229228  new-0.img.zst
2d31b41a6d273ea4001c31b1d2b673bdb6a0c80f8101c5d8a6abf87e610b0258  raidz2-0.img.zst
4ac9bcb98a7cc153ce7a8033c63ae45c4b37484d2ad42e99b25167ae9f401a04  raidz2-1.img.zst
25036f15ef6ba8ea348e6cae51c00b1ebd991b994cb82c4febed89d580a041af  raidz2-2.img.zst
7dfb4c086fe6885824e014f112da9e28601c1556e0fe118cfffe0406912cf091  raidz2-3.img.zst
a2f79f2090bd5775d648dac89a2098425e510c4437602ad9665741eaa699c606  raidz2-4.img.zst
beaa21a45f7815bd008b860e3acc94967f43a202fcb6d4e8e94b3995a9552d6a  spare-0.img.zst
```
