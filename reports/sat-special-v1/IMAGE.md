# Satellite `sat-special` (sat-special-v1)

Built 2026-11-27T14:58:27Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

One raidz1 with a special mirror and a dedup mirror beside it (`org.zfsonlinux:allocation_classes`): the metadata on the special vdev, and `fs`'s blocks up to 16K (`special_small_blocks`); `vm/disk-small`, all of whose 8K blocks go there too; `vm/disk-dedup`, written the same 256 KiB at every offset with `dedup=on`, its table on the dedup vdev.

## Layout

Ashift 12, 12, 12, as `zpool status` printed it at the end:

```
config:

	NAME                                     STATE     READ WRITE CKSUM
	sat-special                              ONLINE       0     0     0
	  raidz1-0                               ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-0.img    ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-1.img    ONLINE       0     0     0
	    /var/tmp/sat/members/raidz1-2.img    ONLINE       0     0     0
	dedup	
	  mirror-2                               ONLINE       0     0     0
	    /var/tmp/sat/members/dedup-0a.img    ONLINE       0     0     0
	    /var/tmp/sat/members/dedup-0b.img    ONLINE       0     0     0
	special	
	  mirror-1                               ONLINE       0     0     0
	    /var/tmp/sat/members/special-0a.img  ONLINE       0     0     0
	    /var/tmp/sat/members/special-0b.img  ONLINE       0     0     0

```

## Datasets

```
sat-special	filesystem	3174360211909820709	Fri Nov 27 14:55 2026	66.3M	104K	-	-	on	lz4	off	none
sat-special@s0	snapshot	12448252049729910254	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-special@s1	snapshot	2448077148073866584	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-special@s2	snapshot	16835069985038314338	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-special@s3	snapshot	3188758987331876873	Fri Nov 27 14:55 2026	0B	104K	-	-	-	-	off	-
sat-special/fs	filesystem	6483176187749577037	Fri Nov 27 14:55 2026	1.40M	1.13M	-	-	on	lz4	off	none
sat-special/fs@s0	snapshot	5671039263869350980	Fri Nov 27 14:55 2026	88K	1.07M	-	-	-	-	off	-
sat-special/fs@s1	snapshot	2940094363998832762	Fri Nov 27 14:55 2026	88K	1.09M	-	-	-	-	off	-
sat-special/fs@s2	snapshot	13512780102804079312	Fri Nov 27 14:55 2026	88K	1.11M	-	-	-	-	off	-
sat-special/fs@s3	snapshot	12234790559077472563	Fri Nov 27 14:55 2026	0B	1.13M	-	-	-	-	off	-
sat-special/vm	filesystem	3384499084285095225	Fri Nov 27 14:55 2026	63.1M	96K	-	-	on	lz4	off	none
sat-special/vm@s0	snapshot	1529854425325963006	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-special/vm@s1	snapshot	3234265768059164590	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-special/vm@s2	snapshot	3874689959828375436	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-special/vm@s3	snapshot	3825952840036678016	Fri Nov 27 14:55 2026	0B	96K	-	-	-	-	off	-
sat-special/vm/disk-16k	volume	17470777198913193491	Fri Nov 27 14:55 2026	19.5M	16.1M	24M	16K	sha256	off	off	none
sat-special/vm/disk-16k@s0	snapshot	6937089190883603461	Fri Nov 27 14:55 2026	1.14M	16.1M	24M	-	-	-	off	-
sat-special/vm/disk-16k@s1	snapshot	17404791851527097030	Fri Nov 27 14:55 2026	144K	16.1M	24M	-	-	-	off	-
sat-special/vm/disk-16k@s2	snapshot	8090614102031184378	Fri Nov 27 14:55 2026	144K	16.1M	24M	-	-	-	off	-
sat-special/vm/disk-16k@s3	snapshot	7990739129394261751	Fri Nov 27 14:55 2026	0B	16.1M	24M	-	-	-	off	-
sat-special/vm/disk-8k	volume	18070248665480379357	Fri Nov 27 14:55 2026	13.6M	10.9M	24M	8K	fletcher4	lz4	off	none
sat-special/vm/disk-8k@s0	snapshot	12353226801283990926	Fri Nov 27 14:55 2026	914K	10.9M	24M	-	-	-	off	-
sat-special/vm/disk-8k@s1	snapshot	511700634126043585	Fri Nov 27 14:55 2026	232K	10.9M	24M	-	-	-	off	-
sat-special/vm/disk-8k@s2	snapshot	9040994197739600957	Fri Nov 27 14:55 2026	232K	10.9M	24M	-	-	-	off	-
sat-special/vm/disk-8k@s3	snapshot	8038174646249510875	Fri Nov 27 14:55 2026	0B	10.9M	24M	-	-	-	off	-
sat-special/vm/disk-dedup	volume	536620940977944976	Fri Nov 27 14:55 2026	19.5M	16.1M	24M	16K	sha256	off	off	none
sat-special/vm/disk-dedup@s0	snapshot	3679479982909486699	Fri Nov 27 14:55 2026	1.13M	16.1M	24M	-	-	-	off	-
sat-special/vm/disk-dedup@s1	snapshot	16552822892767364712	Fri Nov 27 14:55 2026	136K	16.1M	24M	-	-	-	off	-
sat-special/vm/disk-dedup@s2	snapshot	15976264562022295253	Fri Nov 27 14:55 2026	136K	16.1M	24M	-	-	-	off	-
sat-special/vm/disk-dedup@s3	snapshot	4813222611301006305	Fri Nov 27 14:55 2026	0B	16.1M	24M	-	-	-	off	-
sat-special/vm/disk-small	volume	9001899316021314157	Fri Nov 27 14:55 2026	10.4M	8.23M	16M	8K	sha256	lz4	off	none
sat-special/vm/disk-small@s0	snapshot	16269146711902738025	Fri Nov 27 14:55 2026	744K	8.23M	16M	-	-	-	off	-
sat-special/vm/disk-small@s1	snapshot	13016725825203593380	Fri Nov 27 14:55 2026	232K	8.23M	16M	-	-	-	off	-
sat-special/vm/disk-small@s2	snapshot	2809091690497052633	Fri Nov 27 14:55 2026	232K	8.23M	16M	-	-	-	off	-
sat-special/vm/disk-small@s3	snapshot	4951539810761857168	Fri Nov 27 14:55 2026	0B	8.23M	16M	-	-	-	off	-
```

## History

`vm/disk-8k` (8K blocks, lz4, written with content it shrinks) and `vm/disk-16k` (16K blocks, sha256, the keystream), 16 MiB of each, and `fs`, twenty text files, twenty of the keystream in a directory, a symbolic and a hard link. Then rounds of four TXGs with 256 KiB written to every volume and a file to `fs` in each, a recursive snapshot `s<round>` after each round.  Deterministic content from seed `zvolrescue-sat-special-2026`.

## Oracle

As the golden image's, without older copies: `volumes.sha256`, `zfs-get-destroyed.txt` where something was destroyed, `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/`, `files.json`, `zpool-history-il.txt`, `files-capture.txt`, `zpool-status.txt`, `layout.json` (`satellite`: the manifests that name no pool are not run against it), `members.sha256`.

## Release files

```
d79c48a87c6d4dbe94106618c22750a8d2f1a11d2f81049881b24fe79c0ecf73  dedup-0a.img.zst
ba17a0daaa74150b5685973e03c98ee71c69526841eea1714ab875b2a84a006c  dedup-0b.img.zst
807d18046df31798e97e5c76e4ee4ad9240b97f4302d50647155b76f32f5c238  raidz1-0.img.zst
dfd486e61998b16e2958e5434ef76823b5ba95622334b118a40282402039b417  raidz1-1.img.zst
b3314391526b91983cd14fb9b062bb72c78a92cf8ee7519756700ce700d05c47  raidz1-2.img.zst
bab6626fc497ac85505b2cfc3ab98a1156b0ec312318505e724aafe3419f07a7  special-0a.img.zst
cd1a359fe535c3c135fc1064784ba5e552373fb9443c679aa1bc36a111c91223  special-0b.img.zst
```
