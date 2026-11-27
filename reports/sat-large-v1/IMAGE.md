# Satellite `sat-large` (sat-large-v1)

Built 2026-11-27T22:48:51Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

A large volume of content ZFS compresses: `vm/big`, 10 GiB of 8K blocks with zstd — the disk of a database's machine, 256 MiB of its system (text), 128 MiB of media (the keystream) and the rest the database's preallocated pages, each a header and a trailer with nothing between, which ZFS keeps in the block pointer itself (`embedded_data`), every 64th a page of rows; then three runs of 4 MiB written over it, one across the volume's 4 GiB. Over 1.3 million blocks under four levels of indirect blocks (8K blocks: a level-2 block spans 8 GiB), offsets past 4 GiB in the volume and in its members, on a mirror of two 12 GiB members of which the pool fills a twentieth, its blocks past the 4.5 GiB of zeros a filesystem took before it and gave back after (`ballast`, compression off, destroyed), as an old pool's sit where space was free when they were written. Its manifests are held out of the regular runs, and its oracle has no `zdb -dddddd` (a line a block would be over a million) and of `zdb -dddd` each dataset's own line alone.

## Layout

Ashift 12, as `zpool status` printed it at the end:

```
config:

	NAME                                    STATE     READ WRITE CKSUM
	sat-large                               ONLINE       0     0     0
	  mirror-0                              ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0a.img  ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0b.img  ONLINE       0     0     0

```

## Datasets

```
sat-large	filesystem	8574774686069230570	Fri Nov 27 22:41 2026	454M	104K	-	-	on	lz4	off	none
sat-large@s0	snapshot	7144800689452893962	Fri Nov 27 22:41 2026	0B	104K	-	-	-	-	off	-
sat-large@s1	snapshot	7191691045150286982	Fri Nov 27 22:41 2026	0B	104K	-	-	-	-	off	-
sat-large/fs	filesystem	5185417007138123686	Fri Nov 27 22:41 2026	1.14M	1.05M	-	-	on	lz4	off	none
sat-large/fs@s0	snapshot	18103425312461277651	Fri Nov 27 22:41 2026	88K	1.03M	-	-	-	-	off	-
sat-large/fs@s1	snapshot	14048273740854170543	Fri Nov 27 22:41 2026	0B	1.05M	-	-	-	-	off	-
sat-large/vm	filesystem	11472824990869217729	Fri Nov 27 22:41 2026	452M	96K	-	-	on	lz4	off	none
sat-large/vm@s0	snapshot	17253125705746290564	Fri Nov 27 22:41 2026	0B	96K	-	-	-	-	off	-
sat-large/vm@s1	snapshot	6880533119499186641	Fri Nov 27 22:41 2026	0B	96K	-	-	-	-	off	-
sat-large/vm/big	volume	6954111752289748636	Fri Nov 27 22:42 2026	426M	426M	10G	8K	on	zstd	off	none
sat-large/vm/disk-16k	volume	3342896285307605548	Fri Nov 27 22:41 2026	17.3M	16.1M	24M	16K	sha256	off	off	none
sat-large/vm/disk-16k@s0	snapshot	5415901333220681922	Fri Nov 27 22:41 2026	1.14M	16.1M	24M	-	-	-	off	-
sat-large/vm/disk-16k@s1	snapshot	15172227037045078265	Fri Nov 27 22:41 2026	0B	16.1M	24M	-	-	-	off	-
sat-large/vm/disk-8k	volume	8457070217050274266	Fri Nov 27 22:41 2026	8.94M	8.22M	24M	8K	fletcher4	lz4	off	none
sat-large/vm/disk-8k@s0	snapshot	2332986671204527350	Fri Nov 27 22:41 2026	736K	8.22M	24M	-	-	-	off	-
sat-large/vm/disk-8k@s1	snapshot	16341086951399664244	Fri Nov 27 22:41 2026	0B	8.22M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round. After the rounds, `ballast` created with 4.5 GiB of zeros in a file, then `vm/big` created and written whole, then three runs of 4 MiB of the keystream over it at 4094 MiB, 6 GiB and its last 4 MiB, a TXG each, then `ballast` destroyed; `vm/big` has no snapshot. Deterministic content from seed `zvolrescue-sat-large-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
e550dece540ab8ee819557ebb6526eff0974f20b40a3cc90a1218d4b58b2dbfb  mirror-0a.img.zst
cdefc020d5cf120cab7d07734cbd4b34d21133e42bcea9daaa37dc024ff046b6  mirror-0b.img.zst
```
