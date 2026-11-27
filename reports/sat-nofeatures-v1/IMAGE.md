# Satellite `sat-nofeatures` (sat-nofeatures-v1)

Built 2026-11-27T16:36:13Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

One mirror created with `zpool create -d`: pool version 5000 with every feature disabled — no hole birth, no embedded data, no lz4 (its volume compressed with lzjb), no large dnodes, no spacemap histogram — what a pool upgraded from a legacy version and never given a feature looks like.

## Layout

Ashift 12, as `zpool status` printed it at the end:

```
config:

	NAME                                    STATE     READ WRITE CKSUM
	sat-nofeatures                          ONLINE       0     0     0
	  mirror-0                              ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0a.img  ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0b.img  ONLINE       0     0     0

```

## Datasets

```
sat-nofeatures	filesystem	6182129524173359235	Fri Nov 27 16:33 2026	33.7M	200K	-	-	on	lzjb	off	none
sat-nofeatures@s0	snapshot	8088027261209068424	Fri Nov 27 16:33 2026	0B	200K	-	-	-	-	off	-
sat-nofeatures@s1	snapshot	7980461011245038411	Fri Nov 27 16:33 2026	0B	200K	-	-	-	-	off	-
sat-nofeatures@s2	snapshot	2697923325172293103	Fri Nov 27 16:33 2026	0B	200K	-	-	-	-	off	-
sat-nofeatures@s3	snapshot	5337467743565085770	Fri Nov 27 16:33 2026	0B	200K	-	-	-	-	off	-
sat-nofeatures/fs	filesystem	3159907796441499058	Fri Nov 27 16:33 2026	1.62M	1.22M	-	-	on	lzjb	off	none
sat-nofeatures/fs@s0	snapshot	10985323726119608029	Fri Nov 27 16:33 2026	136K	1.16M	-	-	-	-	off	-
sat-nofeatures/fs@s1	snapshot	11876400122841265615	Fri Nov 27 16:33 2026	136K	1.18M	-	-	-	-	off	-
sat-nofeatures/fs@s2	snapshot	949330963117178188	Fri Nov 27 16:33 2026	136K	1.20M	-	-	-	-	off	-
sat-nofeatures/fs@s3	snapshot	16124991179622521696	Fri Nov 27 16:33 2026	0B	1.22M	-	-	-	-	off	-
sat-nofeatures/vm	filesystem	2944086123422780520	Fri Nov 27 16:33 2026	30.6M	176K	-	-	on	lzjb	off	none
sat-nofeatures/vm@s0	snapshot	5838450102125019864	Fri Nov 27 16:33 2026	0B	176K	-	-	-	-	off	-
sat-nofeatures/vm@s1	snapshot	5674753208979662060	Fri Nov 27 16:33 2026	0B	176K	-	-	-	-	off	-
sat-nofeatures/vm@s2	snapshot	10455189288651133936	Fri Nov 27 16:33 2026	0B	176K	-	-	-	-	off	-
sat-nofeatures/vm@s3	snapshot	17069713021079540943	Fri Nov 27 16:33 2026	0B	176K	-	-	-	-	off	-
sat-nofeatures/vm/disk-16k	volume	10059301909881469232	Fri Nov 27 16:33 2026	19.8M	16.2M	24M	16K	sha256	off	off	none
sat-nofeatures/vm/disk-16k@s0	snapshot	1516715059115521654	Fri Nov 27 16:33 2026	1.19M	16.2M	24M	-	-	-	off	-
sat-nofeatures/vm/disk-16k@s1	snapshot	2425861939890785580	Fri Nov 27 16:33 2026	192K	16.2M	24M	-	-	-	off	-
sat-nofeatures/vm/disk-16k@s2	snapshot	16694351405317914265	Fri Nov 27 16:33 2026	192K	16.2M	24M	-	-	-	off	-
sat-nofeatures/vm/disk-16k@s3	snapshot	2647322837454064491	Fri Nov 27 16:33 2026	0B	16.2M	24M	-	-	-	off	-
sat-nofeatures/vm/disk-8k	volume	15838417472241304697	Fri Nov 27 16:33 2026	10.6M	8.29M	24M	8K	fletcher4	lzjb	off	none
sat-nofeatures/vm/disk-8k@s0	snapshot	5003758652974615118	Fri Nov 27 16:33 2026	800K	8.29M	24M	-	-	-	off	-
sat-nofeatures/vm/disk-8k@s1	snapshot	9348094200736483932	Fri Nov 27 16:33 2026	288K	8.29M	24M	-	-	-	off	-
sat-nofeatures/vm/disk-8k@s2	snapshot	14683906723946341429	Fri Nov 27 16:33 2026	288K	8.29M	24M	-	-	-	off	-
sat-nofeatures/vm/disk-8k@s3	snapshot	8613957187839409562	Fri Nov 27 16:33 2026	0B	8.29M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lzjb, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round.  Deterministic content from seed `zvolrescue-sat-nofeatures-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
3c290a3bb7988e873f89c12ac02991d8f197008fce8be85392b86b225c4efbd7  mirror-0a.img.zst
ee3104c89036688227486b9010aeea090ced282cab0e9b5ff4bf8a7384fd7740  mirror-0b.img.zst
```
