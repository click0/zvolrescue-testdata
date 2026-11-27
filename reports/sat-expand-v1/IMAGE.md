# Satellite `sat-expand` (sat-expand-v1)

Built 2026-11-27T14:57:42Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

One raidz1 of three disks expanded to four after round 1 (`zpool attach`, `org.openzfs:raidz_expansion`), the reflow waited for: the blocks born before it keep three disks' worth of columns laid over four, those after are four wide. zvolrescue does not read such a raidz and says so (SPEC F-70): the satellite is the case that holds it to that, and the pool a reader of it would be built against.

## Layout

Ashift 12, as `zpool status` printed it at the end:

```
config:

	NAME                                   STATE     READ WRITE CKSUM
	sat-expand                             ONLINE       0     0     0
	  raidz1-0                             ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-0.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-1.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-2.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-3.img  ONLINE       0     0     0

```

## Datasets

```
sat-expand	filesystem	3405676557151026387	Fri Nov 27 14:55 2026	36.2M	139K	-	-	on	lz4	off	none
sat-expand@s0	snapshot	3667334593175805596	Fri Nov 27 14:55 2026	0B	139K	-	-	-	-	off	-
sat-expand@s1	snapshot	17705093248264392571	Fri Nov 27 14:55 2026	0B	139K	-	-	-	-	off	-
sat-expand@s2	snapshot	13188335814778553650	Fri Nov 27 14:55 2026	0B	139K	-	-	-	-	off	-
sat-expand@s3	snapshot	8509416498595669039	Fri Nov 27 14:55 2026	0B	139K	-	-	-	-	off	-
sat-expand/fs	filesystem	8678153734105137381	Fri Nov 27 14:55 2026	1.55M	1.23M	-	-	on	lz4	off	none
sat-expand/fs@s0	snapshot	344227171213297718	Fri Nov 27 14:55 2026	107K	1.16M	-	-	-	-	off	-
sat-expand/fs@s1	snapshot	12143117706325957653	Fri Nov 27 14:55 2026	107K	1.19M	-	-	-	-	off	-
sat-expand/fs@s2	snapshot	9590842989880394774	Fri Nov 27 14:55 2026	107K	1.21M	-	-	-	-	off	-
sat-expand/fs@s3	snapshot	2121520591339984244	Fri Nov 27 14:55 2026	0B	1.23M	-	-	-	-	off	-
sat-expand/vm	filesystem	17106338898023393760	Fri Nov 27 14:55 2026	33.4M	128K	-	-	on	lz4	off	none
sat-expand/vm@s0	snapshot	2411880079331539703	Fri Nov 27 14:55 2026	0B	128K	-	-	-	-	off	-
sat-expand/vm@s1	snapshot	17605244819230189552	Fri Nov 27 14:55 2026	0B	128K	-	-	-	-	off	-
sat-expand/vm@s2	snapshot	16524232067228049054	Fri Nov 27 14:55 2026	0B	128K	-	-	-	-	off	-
sat-expand/vm@s3	snapshot	5308967135349692181	Fri Nov 27 14:55 2026	0B	128K	-	-	-	-	off	-
sat-expand/vm/disk-16k	volume	11859379581668134115	Fri Nov 27 14:55 2026	19.6M	16.1M	24M	16K	sha256	off	off	none
sat-expand/vm/disk-16k@s0	snapshot	6811298943539844618	Fri Nov 27 14:55 2026	1.17M	16.2M	24M	-	-	-	off	-
sat-expand/vm/disk-16k@s1	snapshot	461794977741960903	Fri Nov 27 14:55 2026	170K	16.2M	24M	-	-	-	off	-
sat-expand/vm/disk-16k@s2	snapshot	17301110000651193869	Fri Nov 27 14:55 2026	160K	16.1M	24M	-	-	-	off	-
sat-expand/vm/disk-16k@s3	snapshot	16262033411837589010	Fri Nov 27 14:55 2026	0B	16.1M	24M	-	-	-	off	-
sat-expand/vm/disk-8k	volume	10179385260670245275	Fri Nov 27 14:55 2026	13.7M	10.9M	24M	8K	fletcher4	lz4	off	none
sat-expand/vm/disk-8k@s0	snapshot	5767676213450014832	Fri Nov 27 14:55 2026	948K	10.9M	24M	-	-	-	off	-
sat-expand/vm/disk-8k@s1	snapshot	11813431285614954359	Fri Nov 27 14:55 2026	266K	10.9M	24M	-	-	-	off	-
sat-expand/vm/disk-8k@s2	snapshot	16133596275108834668	Fri Nov 27 14:55 2026	245K	10.9M	24M	-	-	-	off	-
sat-expand/vm/disk-8k@s3	snapshot	16886124491758628268	Fri Nov 27 14:55 2026	0B	10.9M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round. After round 1, `raidz1-3` attached to `raidz1-0` and the expansion waited for. Deterministic content from seed `zvolrescue-sat-expand-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
866c4b96f46b79cb97729b087294fc1c9d3716150535e8f9df53f3a3e8745e8c  raidz1-0.img.zst
fa84e7d24abaa1647a229d46e024fbdccdd8c56c0b2b2b80604fa706b3071db6  raidz1-1.img.zst
975c9268780fe035cf93935e56a7f21f9f60a0febdd03346f233bc12b7186255  raidz1-2.img.zst
a6743401026e359d6cc00b45d8b6c542a7dfea20d59e5037529ce967c4ac76c2  raidz1-3.img.zst
```
