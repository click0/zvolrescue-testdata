# Satellite `sat-slog` (sat-slog-v1)

Built 2026-11-27T14:57:33Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

A mirror with a separate intent log (`log-0`): after round 2 the pool frozen (`zpool freeze`, what the OpenZFS test suite does to the same end) and written to synchronously — 4 MiB of `vm/disk-sync` and files of `fs`, both `sync=always` — so that those writes are in the intent log alone, and exported so. What the members hold is the pool at the freeze: the volumes' `@export` hashes are taken right before it, and the oracle's readings of the exported pool are of it. `vm/disk-sync@replayed` is the same volume after an import that replays the log, on a copy of the members: what a reader that applies the log would give.

## Layout

Ashift 12, 12, as `zpool status` printed it at the end:

```
config:

	NAME                                    STATE     READ WRITE CKSUM
	sat-slog                                ONLINE       0     0     0
	  mirror-0                              ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0a.img  ONLINE       0     0     0
	    /var/tmp/sat/members/mirror-0b.img  ONLINE       0     0     0
	logs	
	  /var/tmp/sat/members/log-0.img        ONLINE       0     0     0

```

## Datasets

```
sat-slog	filesystem	4616652799847140674	Fri Nov 27 14:54 2026	42.5M	96K	-	-	on	lz4	off	none
sat-slog@s0	snapshot	14019008357848676241	Fri Nov 27 14:54 2026	0B	96K	-	-	-	-	off	-
sat-slog@s1	snapshot	16347375991440007903	Fri Nov 27 14:54 2026	0B	96K	-	-	-	-	off	-
sat-slog@s2	snapshot	17813912705948318438	Fri Nov 27 14:54 2026	0B	96K	-	-	-	-	off	-
sat-slog/fs	filesystem	17023871858234880166	Fri Nov 27 14:54 2026	1.34M	1.09M	-	-	on	lz4	off	none
sat-slog/fs@s0	snapshot	16772193739173529515	Fri Nov 27 14:54 2026	88K	1.03M	-	-	-	-	off	-
sat-slog/fs@s1	snapshot	8283983670327187694	Fri Nov 27 14:54 2026	80K	1.05M	-	-	-	-	off	-
sat-slog/fs@s2	snapshot	9620077638075133724	Fri Nov 27 14:54 2026	80K	1.07M	-	-	-	-	off	-
sat-slog/vm	filesystem	9149704847601211874	Fri Nov 27 14:54 2026	40.0M	96K	-	-	on	lz4	off	none
sat-slog/vm@s0	snapshot	6326853290465575112	Fri Nov 27 14:54 2026	0B	96K	-	-	-	-	off	-
sat-slog/vm@s1	snapshot	9279791749087940069	Fri Nov 27 14:54 2026	0B	96K	-	-	-	-	off	-
sat-slog/vm@s2	snapshot	3772370609617662851	Fri Nov 27 14:54 2026	0B	96K	-	-	-	-	off	-
sat-slog/vm/disk-16k	volume	5360358395618994946	Fri Nov 27 14:54 2026	18.4M	16.1M	24M	16K	sha256	off	off	none
sat-slog/vm/disk-16k@s0	snapshot	4168282288902327648	Fri Nov 27 14:54 2026	1.14M	16.1M	24M	-	-	-	off	-
sat-slog/vm/disk-16k@s1	snapshot	8597776979099957337	Fri Nov 27 14:54 2026	144K	16.1M	24M	-	-	-	off	-
sat-slog/vm/disk-16k@s2	snapshot	15548087085302443771	Fri Nov 27 14:54 2026	0B	16.1M	24M	-	-	-	off	-
sat-slog/vm/disk-8k	volume	7664694633393649092	Fri Nov 27 14:54 2026	9.66M	8.23M	24M	8K	fletcher4	lz4	off	none
sat-slog/vm/disk-8k@s0	snapshot	15895372902158925931	Fri Nov 27 14:54 2026	736K	8.22M	24M	-	-	-	off	-
sat-slog/vm/disk-8k@s1	snapshot	5524152911887432589	Fri Nov 27 14:54 2026	224K	8.22M	24M	-	-	-	off	-
sat-slog/vm/disk-8k@s2	snapshot	336141003560499145	Fri Nov 27 14:54 2026	0B	8.23M	24M	-	-	-	off	-
sat-slog/vm/disk-sync	volume	15354024951680838607	Fri Nov 27 14:54 2026	11.8M	8.22M	24M	8K	fletcher4	lz4	off	none
sat-slog/vm/disk-sync@s0	snapshot	3026317869916980020	Fri Nov 27 14:54 2026	728K	8.21M	24M	-	-	-	off	-
sat-slog/vm/disk-sync@s1	snapshot	14436179348092491316	Fri Nov 27 14:54 2026	216K	8.21M	24M	-	-	-	off	-
sat-slog/vm/disk-sync@s2	snapshot	13075225428702165149	Fri Nov 27 14:54 2026	136K	8.21M	24M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round. After round 2, the volumes hashed (`@export`), the pool frozen, 4 MiB of `vm/disk-sync` from offset 4 MiB and five files of `fs` written with every write synchronous. Deterministic content from seed `zvolrescue-sat-slog-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
cc96ba3f85467f602c311b6cbadb9b807fd29d68a1a633a29149ee663ee94966  log-0.img.zst
eda5738b3f9b0b2cb9e8a48ad4d6579b648d06ce90d7ded38270c94d45cc372a  mirror-0a.img.zst
16dfb81843eda7838e2a418ea838bdd84b12371923ccb969a9d23b7cc2b4e26e  mirror-0b.img.zst
```
