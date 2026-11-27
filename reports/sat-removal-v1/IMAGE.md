# Satellite `sat-removal` (sat-removal-v1)

Built 2026-11-27T14:58:28Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

Three two-way mirrors, the middle one removed after round 1: what it held copied onto the other two and found through the mapping the removal leaves (`com.delphix:device_removal`, the indirect vdev `indirect-1`), the snapshots of rounds 0 and 1 read through it. The removed disks are no members of the pool any more, and not in the release.

## Layout

Ashift 12, 12, 12, as `zpool status` printed it at the end:

```
config:

	NAME                                    STATE     READ WRITE CKSUM
	sat-removal                             ONLINE       0     0     0
	  mirror-0                              ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0a.img  ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0b.img  ONLINE       0     0     0
	  mirror-2                              ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-2a.img  ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-2b.img  ONLINE       0     0     0

```

## Datasets

```
sat-removal	filesystem	13046824310186909159	Fri Nov 27 14:55 2026	32.5M	104K	-	-	on	lz4	off	none
sat-removal@s0	snapshot	8214609942261880560	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-removal@s1	snapshot	17430581331572524076	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-removal@s2	snapshot	6285899927301798154	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-removal@s3	snapshot	332625149767327359	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-removal/fs	filesystem	15090041316912394134	Fri Nov 27 14:55 2026	1.34M	1.09M	-	-	on	lz4	off	none
sat-removal/fs@s0	snapshot	15668305818607517690	Fri Nov 27 14:55 2026	88K	1.03M	-	-	-	-	off	-
sat-removal/fs@s1	snapshot	16118673465750556335	Fri Nov 27 14:55 2026	72K	1.05M	-	-	-	-	off	-
sat-removal/fs@s2	snapshot	11873008826619868571	Fri Nov 27 14:55 2026	80K	1.07M	-	-	-	-	off	-
sat-removal/fs@s3	snapshot	17337530026851688281	Fri Nov 27 14:55 2026	0B	1.09M	-	-	-	-	off	-
sat-removal/vm	filesystem	1740823278239492750	Fri Nov 27 14:55 2026	30.1M	96K	-	-	on	lz4	off	none
sat-removal/vm@s0	snapshot	7510456470908225674	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-removal/vm@s1	snapshot	5791060765004111667	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-removal/vm@s2	snapshot	6133568750792931820	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-removal/vm@s3	snapshot	7896839770245613443	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-removal/vm/disk-16k	volume	9149612330153301822	Fri Nov 27 14:55 2026	19.6M	16.1M	24M	16K	sha256	off	off	none
sat-removal/vm/disk-16k@s0	snapshot	6109122060284723936	Fri Nov 27 14:55 2026	1.14M	16.1M	24M	-	-	-	off	-
sat-removal/vm/disk-16k@s1	snapshot	7672660393125257358	Fri Nov 27 14:55 2026	144K	16.1M	24M	-	-	-	off	-
sat-removal/vm/disk-16k@s2	snapshot	5747461212420142143	Fri Nov 27 14:55 2026	144K	16.1M	24M	-	-	-	off	-
sat-removal/vm/disk-16k@s3	snapshot	14177211100913944912	Fri Nov 27 14:55 2026	0B	16.1M	24M	-	-	-	off	-
sat-removal/vm/disk-8k	volume	18236641989068554287	Fri Nov 27 14:55 2026	10.4M	8.23M	24M	8K	fletcher4	lz4	off	none
sat-removal/vm/disk-8k@s0	snapshot	14689301649235924233	Fri Nov 27 14:55 2026	744K	8.23M	24M	-	-	-	off	-
sat-removal/vm/disk-8k@s1	snapshot	10857726670867419830	Fri Nov 27 14:55 2026	232K	8.23M	24M	-	-	-	off	-
sat-removal/vm/disk-8k@s2	snapshot	16850070620479028647	Fri Nov 27 14:55 2026	232K	8.23M	24M	-	-	-	off	-
sat-removal/vm/disk-8k@s3	snapshot	6500733457001108862	Fri Nov 27 14:55 2026	0B	8.23M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round. After round 1, `mirror-1` removed (`zpool remove`, waited for). Deterministic content from seed `zvolrescue-sat-removal-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
e2ab1d4798ed926736a7ec0f7e2c440ae074d2d2102a1b0e20dabe3318c1c6e7  mirror-0a.img.zst
d2ab6d19976080048f5026911888df445bab103df6cef9c841785c3abfbf6d3f  mirror-0b.img.zst
d08205a9503b1e685ff9b3539e82f10ee9adc4c054cffb2e86d5d0df8ea8044b  mirror-2a.img.zst
232726055a2ee25151579d08ef9b25490249b624ce806452f5d97829f48cc272  mirror-2b.img.zst
```
