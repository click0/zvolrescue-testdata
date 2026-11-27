# Satellite `sat-mmp` (sat-mmp-v1)

Built 2026-11-27T14:56:26Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

One mirror with `multihost=on`: between the rounds the pool left imported for seconds at a time, so that the heartbeat of multi-modifier protection writes its uberblocks — the TXG of the last sync, a newer timestamp, the MMP fields — into the rings.

## Layout

Ashift 12, as `zpool status` printed it at the end:

```
config:

	NAME                                    STATE     READ WRITE CKSUM
	sat-mmp                                 ONLINE       0     0     0
	  mirror-0                              ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0a.img  ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0b.img  ONLINE       0     0     0

```

## Datasets

```
sat-mmp	filesystem	15046062988661417157	Fri Nov 27 14:54 2026	32.3M	104K	-	-	on	lz4	off	none
sat-mmp@s0	snapshot	1321651964176226715	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-mmp@s1	snapshot	8042668542451666596	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-mmp@s2	snapshot	515699723528014418	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-mmp@s3	snapshot	12482246010163515516	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-mmp/fs	filesystem	1848735812187787975	Fri Nov 27 14:54 2026	1.34M	1.09M	-	-	on	lz4	off	none
sat-mmp/fs@s0	snapshot	1042504604872953528	Fri Nov 27 14:55 2026	80K	1.03M	-	-	-	-	off	-
sat-mmp/fs@s1	snapshot	3516780973510689025	Fri Nov 27 14:55 2026	80K	1.05M	-	-	-	-	off	-
sat-mmp/fs@s2	snapshot	18153382015324998896	Fri Nov 27 14:55 2026	80K	1.07M	-	-	-	-	off	-
sat-mmp/fs@s3	snapshot	2414432040035633858	Fri Nov 27 14:55 2026	0B	1.09M	-	-	-	-	off	-
sat-mmp/vm	filesystem	1035660658322168182	Fri Nov 27 14:54 2026	30.1M	96K	-	-	on	lz4	off	none
sat-mmp/vm@s0	snapshot	16533640716861694529	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-mmp/vm@s1	snapshot	17890917491417312959	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-mmp/vm@s2	snapshot	4453096804411179552	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-mmp/vm@s3	snapshot	9112972676363310436	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-mmp/vm/disk-16k	volume	11627952256446423842	Fri Nov 27 14:54 2026	19.6M	16.1M	24M	16K	sha256	off	off	none
sat-mmp/vm/disk-16k@s0	snapshot	9076852969473822505	Fri Nov 27 14:55 2026	1.14M	16.1M	24M	-	-	-	off	-
sat-mmp/vm/disk-16k@s1	snapshot	4320969037301926610	Fri Nov 27 14:55 2026	144K	16.1M	24M	-	-	-	off	-
sat-mmp/vm/disk-16k@s2	snapshot	11796735895845018102	Fri Nov 27 14:55 2026	144K	16.1M	24M	-	-	-	off	-
sat-mmp/vm/disk-16k@s3	snapshot	1745746532729916316	Fri Nov 27 14:55 2026	0B	16.1M	24M	-	-	-	off	-
sat-mmp/vm/disk-8k	volume	4660413458060552613	Fri Nov 27 14:54 2026	10.4M	8.23M	24M	8K	fletcher4	lz4	off	none
sat-mmp/vm/disk-8k@s0	snapshot	4742209449304493118	Fri Nov 27 14:55 2026	744K	8.23M	24M	-	-	-	off	-
sat-mmp/vm/disk-8k@s1	snapshot	3366892221629009269	Fri Nov 27 14:55 2026	232K	8.23M	24M	-	-	-	off	-
sat-mmp/vm/disk-8k@s2	snapshot	15581377918674448059	Fri Nov 27 14:55 2026	232K	8.23M	24M	-	-	-	off	-
sat-mmp/vm/disk-8k@s3	snapshot	5181297944147773129	Fri Nov 27 14:55 2026	0B	8.23M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round. Five seconds of heartbeat after every round, and as many before the export. Deterministic content from seed `zvolrescue-sat-mmp-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
57e9d59935e5670a572f785737bc2b68c681909f52b3d26f3e8f0c6a1f52d5b6  mirror-0a.img.zst
0e0dc49b59e40cc52ee26b984730911738caf4b472b9dad986e8587135ab2a3c  mirror-0b.img.zst
```
