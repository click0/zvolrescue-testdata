# Satellite `sat-checkpoint` (sat-checkpoint-v1)

Built 2026-11-27T14:57:43Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

One raidz1, checkpointed after round 1 (`zpool checkpoint`) and exported with the checkpoint in place: the volume `vm/precious` destroyed right after it, and rounds 2 and 3 written over the others. What the pool held at the checkpoint is every volume's `@checkpoint` hash in `volumes.sha256`, `vm/precious`'s among them; its TXG is `checkpoint_txg` in `zdb-u-export.txt`.

## Layout

Ashift 12, as `zpool status` printed it at the end:

```
config:

	NAME                                   STATE     READ WRITE CKSUM
	sat-checkpoint                         ONLINE       0     0     0
	  raidz1-0                             ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-0.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-1.img  ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-2.img  ONLINE       0     0     0

```

## Datasets

```
sat-checkpoint	filesystem	8652489913046024403	Fri Nov 27 14:54 2026	36.2M	139K	-	-	on	lz4	off	none
sat-checkpoint@s0	snapshot	4378816044759505677	Fri Nov 27 14:54 2026	0B	139K	-	-	-	-	off	-
sat-checkpoint@s1	snapshot	9014765356779952651	Fri Nov 27 14:54 2026	0B	139K	-	-	-	-	off	-
sat-checkpoint@s2	snapshot	3735295624543192282	Fri Nov 27 14:54 2026	0B	139K	-	-	-	-	off	-
sat-checkpoint@s3	snapshot	2177178534145203023	Fri Nov 27 14:54 2026	0B	139K	-	-	-	-	off	-
sat-checkpoint/fs	filesystem	2664839224889238444	Fri Nov 27 14:54 2026	1.57M	1.22M	-	-	on	lz4	off	none
sat-checkpoint/fs@s0	snapshot	1353222862576308786	Fri Nov 27 14:54 2026	95.9K	1.16M	-	-	-	-	off	-
sat-checkpoint/fs@s1	snapshot	1733227171929653831	Fri Nov 27 14:54 2026	95.9K	1.19M	-	-	-	-	off	-
sat-checkpoint/fs@s2	snapshot	833278986594455836	Fri Nov 27 14:54 2026	107K	1.19M	-	-	-	-	off	-
sat-checkpoint/fs@s3	snapshot	3306827026856481609	Fri Nov 27 14:54 2026	0B	1.22M	-	-	-	-	off	-
sat-checkpoint/vm	filesystem	17745615263374508672	Fri Nov 27 14:54 2026	33.5M	128K	-	-	on	lz4	off	none
sat-checkpoint/vm@s0	snapshot	3898551006235709056	Fri Nov 27 14:54 2026	0B	128K	-	-	-	-	off	-
sat-checkpoint/vm@s1	snapshot	15201333157831500878	Fri Nov 27 14:54 2026	0B	128K	-	-	-	-	off	-
sat-checkpoint/vm@s2	snapshot	13828411774907962118	Fri Nov 27 14:54 2026	0B	128K	-	-	-	-	off	-
sat-checkpoint/vm@s3	snapshot	13064819551623530949	Fri Nov 27 14:54 2026	0B	128K	-	-	-	-	off	-
sat-checkpoint/vm/disk-16k	volume	13836496392625494764	Fri Nov 27 14:54 2026	19.6M	16.2M	24M	16K	sha256	off	off	none
sat-checkpoint/vm/disk-16k@s0	snapshot	14537822966138673498	Fri Nov 27 14:54 2026	1.17M	16.2M	24M	-	-	-	off	-
sat-checkpoint/vm/disk-16k@s1	snapshot	1399073210967446930	Fri Nov 27 14:54 2026	170K	16.2M	24M	-	-	-	off	-
sat-checkpoint/vm/disk-16k@s2	snapshot	12386932952696551366	Fri Nov 27 14:54 2026	170K	16.2M	24M	-	-	-	off	-
sat-checkpoint/vm/disk-16k@s3	snapshot	5155316827886791737	Fri Nov 27 14:54 2026	0B	16.2M	24M	-	-	-	off	-
sat-checkpoint/vm/disk-8k	volume	17216375072363581568	Fri Nov 27 14:54 2026	13.7M	10.9M	24M	8K	fletcher4	lz4	off	none
sat-checkpoint/vm/disk-8k@s0	snapshot	12030172397952915701	Fri Nov 27 14:54 2026	948K	10.9M	24M	-	-	-	off	-
sat-checkpoint/vm/disk-8k@s1	snapshot	5921578637765688671	Fri Nov 27 14:54 2026	266K	10.9M	24M	-	-	-	off	-
sat-checkpoint/vm/disk-8k@s2	snapshot	17528904286627070606	Fri Nov 27 14:54 2026	266K	10.9M	24M	-	-	-	off	-
sat-checkpoint/vm/disk-8k@s3	snapshot	5940519596564549613	Fri Nov 27 14:54 2026	0B	10.9M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round. After round 1, every volume hashed (`@checkpoint`), the pool checkpointed, `vm/precious` hashed again (`@destroyed`) and destroyed with its snapshots, two files of `fs` removed. `datasets-checkpoint.txt` is `zdb -e -k -d`, the datasets of the checkpointed state. Deterministic content from seed `zvolrescue-sat-checkpoint-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
225a07d40923ca46ac33a02cb5be30cb2f1d5e6516a5b5c04effdb36e3a189be  raidz1-0.img.zst
d52a2a600418905b25aac02945d2f9a4c90569f0fee06404dac704c152b78f12  raidz1-1.img.zst
0eee86eee213d6654a9250b50bdad1c91edd0285a5ab7153482d461d1a62ad74  raidz1-2.img.zst
```
