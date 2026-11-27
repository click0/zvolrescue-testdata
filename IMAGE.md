# The golden image (golden-v2)

Built 2026-11-27T12:06:03Z on Linux 7.0.0-1020-azure x86_64 with zfs-2.4.1-1ubuntu5.1.

## Layout

One pool `golden`, ashift 12, three top-level vdevs on 512M file members:

| Top-level vdev | Members |
|---|---|
| mirror-0 | mirror-0a mirror-0b |
| raidz2-1 | raidz2-0 raidz2-1 raidz2-2 raidz2-3 |
| draid1:2d:4c:1s-2 | draid1-0 draid1-1 draid1-2 draid1-3 |

## Datasets

```
golden	filesystem	17580028663218866002	Fri Nov 27 11:55 2026	1.43G	198K	-	-	on	lz4	off	none
golden@s0	snapshot	8151619710064643754	Fri Nov 27 11:55 2026	0B	160K	-	-	-	-	off	-
golden@s1	snapshot	1348233921717220851	Fri Nov 27 11:55 2026	0B	160K	-	-	-	-	off	-
golden@s2	snapshot	14718958550085142202	Fri Nov 27 11:55 2026	0B	194K	-	-	-	-	off	-
golden@s3	snapshot	15219157387462315028	Fri Nov 27 11:55 2026	0B	194K	-	-	-	-	off	-
golden@s4	snapshot	15515917945492284891	Fri Nov 27 11:56 2026	0B	194K	-	-	-	-	off	-
golden@s5	snapshot	1003629375115513046	Fri Nov 27 11:56 2026	0B	194K	-	-	-	-	off	-
golden@s6	snapshot	5361913143468993713	Fri Nov 27 11:56 2026	0B	194K	-	-	-	-	off	-
golden@s7	snapshot	1556536958388282463	Fri Nov 27 11:56 2026	0B	194K	-	-	-	-	off	-
golden@s8	snapshot	11956233354728221034	Fri Nov 27 11:56 2026	0B	194K	-	-	-	-	off	-
golden@s9	snapshot	17338095889275281440	Fri Nov 27 11:56 2026	0B	194K	-	-	-	-	off	-
golden@s10	snapshot	71579702613625647	Fri Nov 27 11:56 2026	0B	194K	-	-	-	-	off	-
golden@s11	snapshot	14021004234362263350	Fri Nov 27 11:56 2026	0B	198K	-	-	-	-	off	-
golden/fs-base	filesystem	17563480194253145312	Fri Nov 27 11:55 2026	102K	10.1M	-	-	on	lz4	off	none
golden/fs-base@s2	snapshot	2839769816484794489	Fri Nov 27 11:55 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-base@s3	snapshot	15895941541233042097	Fri Nov 27 11:55 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-base@s4	snapshot	1894762751055048699	Fri Nov 27 11:56 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-base@s5	snapshot	10148272234730880094	Fri Nov 27 11:56 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-base@s6	snapshot	11803079760423271910	Fri Nov 27 11:56 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-base@s7	snapshot	11315173138870852488	Fri Nov 27 11:56 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-base@s8	snapshot	13236372479292680672	Fri Nov 27 11:56 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-base@s9	snapshot	93885563558797681	Fri Nov 27 11:56 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-base@s10	snapshot	3717788458565627101	Fri Nov 27 11:56 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-base@s11	snapshot	7925013891861279162	Fri Nov 27 11:56 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-largednode	filesystem	9169163388873587755	Fri Nov 27 11:55 2026	11.1M	11.1M	-	-	on	lz4	off	none
golden/fs-largednode@s0	snapshot	3931876494281920976	Fri Nov 27 11:55 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s1	snapshot	8054901975574271438	Fri Nov 27 11:55 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s2	snapshot	12313195784892219142	Fri Nov 27 11:55 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s3	snapshot	4045770976191018561	Fri Nov 27 11:55 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s4	snapshot	1227427598051708885	Fri Nov 27 11:56 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s5	snapshot	15477238689862412971	Fri Nov 27 11:56 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s6	snapshot	6739543668057365230	Fri Nov 27 11:56 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s7	snapshot	11904917711480923048	Fri Nov 27 11:56 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s8	snapshot	4984524462783192387	Fri Nov 27 11:56 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s9	snapshot	11391930906366968423	Fri Nov 27 11:56 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s10	snapshot	14721399562828005882	Fri Nov 27 11:56 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-largednode@s11	snapshot	3423102503294747271	Fri Nov 27 11:56 2026	0B	11.1M	-	-	-	-	off	-
golden/fs-promoted	filesystem	9156757318307389597	Fri Nov 27 11:55 2026	10.5M	10.4M	-	-	on	lz4	off	none
golden/fs-promoted@s0	snapshot	4090557113965355631	Fri Nov 27 11:55 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-promoted@s1	snapshot	10914382961629031278	Fri Nov 27 11:55 2026	0B	10.1M	-	-	-	-	off	-
golden/fs-promoted@s2	snapshot	2204376169923395899	Fri Nov 27 11:55 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-promoted@s3	snapshot	14728845661988098158	Fri Nov 27 11:55 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-promoted@s4	snapshot	6937952329654893695	Fri Nov 27 11:56 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-promoted@s5	snapshot	16196699778243830243	Fri Nov 27 11:56 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-promoted@s6	snapshot	3950063992899354182	Fri Nov 27 11:56 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-promoted@s7	snapshot	8638870901279742788	Fri Nov 27 11:56 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-promoted@s8	snapshot	2275309032383321308	Fri Nov 27 11:56 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-promoted@s9	snapshot	4732597303257155953	Fri Nov 27 11:56 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-promoted@s10	snapshot	9716279710801774661	Fri Nov 27 11:56 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-promoted@s11	snapshot	13646678285759602398	Fri Nov 27 11:56 2026	0B	10.4M	-	-	-	-	off	-
golden/fs-tree	filesystem	18056700070671754620	Fri Nov 27 11:55 2026	38.7M	38.0M	-	-	on	lz4	off	none
golden/fs-tree@s0	snapshot	3755729709250027901	Fri Nov 27 11:55 2026	0B	37.9M	-	-	-	-	off	-
golden/fs-tree@s1	snapshot	6894865197692385522	Fri Nov 27 11:55 2026	0B	37.9M	-	-	-	-	off	-
golden/fs-tree@s2	snapshot	18008214799357321640	Fri Nov 27 11:55 2026	0B	37.9M	-	-	-	-	off	-
golden/fs-tree@s3	snapshot	13781188094112875386	Fri Nov 27 11:55 2026	0B	38.0M	-	-	-	-	off	-
golden/fs-tree@s4	snapshot	16059030841330920396	Fri Nov 27 11:56 2026	0B	38.0M	-	-	-	-	off	-
golden/fs-tree@s5	snapshot	6663835550058326164	Fri Nov 27 11:56 2026	0B	38.0M	-	-	-	-	off	-
golden/fs-tree@s6	snapshot	11962632932366233281	Fri Nov 27 11:56 2026	0B	38.0M	-	-	-	-	off	-
golden/fs-tree@s7	snapshot	4760261579522406567	Fri Nov 27 11:56 2026	0B	38.0M	-	-	-	-	off	-
golden/fs-tree@s8	snapshot	2035781410504559379	Fri Nov 27 11:56 2026	0B	38.0M	-	-	-	-	off	-
golden/fs-tree@s9	snapshot	9160320760503911708	Fri Nov 27 11:56 2026	0B	38.0M	-	-	-	-	off	-
golden/fs-tree@s10	snapshot	14378814364972193879	Fri Nov 27 11:56 2026	0B	38.0M	-	-	-	-	off	-
golden/fs-tree@s11	snapshot	3451225905450129973	Fri Nov 27 11:56 2026	0B	38.0M	-	-	-	-	off	-
golden/secret-pw	filesystem	11988151321770365656	Fri Nov 27 11:55 2026	122M	256K	-	-	on	lz4	aes-128-ccm	passphrase
golden/secret-pw@s0	snapshot	1010328141126121286	Fri Nov 27 11:55 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s1	snapshot	13281951937779473259	Fri Nov 27 11:55 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s2	snapshot	10417294407996624029	Fri Nov 27 11:55 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s3	snapshot	15084828801530094038	Fri Nov 27 11:55 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s4	snapshot	6800384986153720151	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s5	snapshot	16666159611371788203	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s6	snapshot	5958760873894092984	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s7	snapshot	8949578352087789925	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s8	snapshot	2478230870819433108	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s9	snapshot	16606733200323162461	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s10	snapshot	14102248836899647902	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw@s11	snapshot	18333004728415675721	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-128-ccm	-
golden/secret-pw/disk	volume	412966478571761356	Fri Nov 27 11:55 2026	121M	25.8M	48M	8K	skein	zstd	aes-128-ccm	passphrase
golden/secret-pw/disk@s0	snapshot	11076099625643570689	Fri Nov 27 11:55 2026	2.15M	25.9M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s1	snapshot	3383006103904186353	Fri Nov 27 11:55 2026	382K	25.7M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s2	snapshot	4247333954817895571	Fri Nov 27 11:55 2026	396K	25.7M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s3	snapshot	8730072134027608401	Fri Nov 27 11:55 2026	382K	25.6M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s4	snapshot	4457727085578057825	Fri Nov 27 11:56 2026	372K	25.7M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s5	snapshot	11439283578711627952	Fri Nov 27 11:56 2026	378K	25.8M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s6	snapshot	12239686144450212752	Fri Nov 27 11:56 2026	372K	25.8M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s7	snapshot	3870693197614072571	Fri Nov 27 11:56 2026	378K	25.8M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s8	snapshot	1340645794477682721	Fri Nov 27 11:56 2026	358K	25.7M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s9	snapshot	3716440069207488309	Fri Nov 27 11:56 2026	372K	25.8M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s10	snapshot	17079503052952161728	Fri Nov 27 11:56 2026	378K	25.8M	48M	-	-	-	aes-128-ccm	-
golden/secret-pw/disk@s11	snapshot	8131022132993564562	Fri Nov 27 11:56 2026	0B	25.8M	48M	-	-	-	aes-128-ccm	-
golden/secret-raw	filesystem	18438227061229879867	Fri Nov 27 11:55 2026	91.9M	256K	-	-	on	lz4	aes-256-gcm	raw
golden/secret-raw@s0	snapshot	155656886128714376	Fri Nov 27 11:55 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s1	snapshot	16661571834044416275	Fri Nov 27 11:55 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s2	snapshot	13054730254262336739	Fri Nov 27 11:55 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s3	snapshot	6369552212474709598	Fri Nov 27 11:55 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s4	snapshot	13491926347694320034	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s5	snapshot	12949947986905475905	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s6	snapshot	15218002951498209904	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s7	snapshot	9229583366639819729	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s8	snapshot	3076894870234891505	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s9	snapshot	579184472211088406	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s10	snapshot	5298523947317006124	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw@s11	snapshot	1877538698544426168	Fri Nov 27 11:56 2026	0B	256K	-	-	-	-	aes-256-gcm	-
golden/secret-raw/disk	volume	5838533146485032327	Fri Nov 27 11:55 2026	91.6M	19.2M	48M	16K	sha256	lz4	aes-256-gcm	raw
golden/secret-raw/disk@s0	snapshot	781675339059113167	Fri Nov 27 11:55 2026	1.47M	19.1M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s1	snapshot	10294411082137409766	Fri Nov 27 11:55 2026	426K	19.3M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s2	snapshot	6143555989342542719	Fri Nov 27 11:55 2026	368K	19.3M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s3	snapshot	10663693972157732140	Fri Nov 27 11:55 2026	386K	19.4M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s4	snapshot	6390308483504918937	Fri Nov 27 11:56 2026	356K	19.3M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s5	snapshot	1756705620752303034	Fri Nov 27 11:56 2026	368K	19.4M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s6	snapshot	71527461958862696	Fri Nov 27 11:56 2026	356K	19.3M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s7	snapshot	1035580088424455544	Fri Nov 27 11:56 2026	368K	19.3M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s8	snapshot	14839996292427443955	Fri Nov 27 11:56 2026	356K	19.4M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s9	snapshot	9310144231872799619	Fri Nov 27 11:56 2026	368K	19.2M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s10	snapshot	13247237589735338122	Fri Nov 27 11:56 2026	368K	19.4M	48M	-	-	-	aes-256-gcm	-
golden/secret-raw/disk@s11	snapshot	16687098804285425265	Fri Nov 27 11:56 2026	0B	19.2M	48M	-	-	-	aes-256-gcm	-
golden/vm	filesystem	12486820899186734467	Fri Nov 27 11:55 2026	1.15G	144K	-	-	on	lz4	off	none
golden/vm@s0	snapshot	6364917314628535451	Fri Nov 27 11:55 2026	0B	144K	-	-	-	-	off	-
golden/vm@s1	snapshot	14645046332668790726	Fri Nov 27 11:55 2026	0B	144K	-	-	-	-	off	-
golden/vm@s2	snapshot	10839576484253954624	Fri Nov 27 11:55 2026	0B	144K	-	-	-	-	off	-
golden/vm@s3	snapshot	8761327244009213941	Fri Nov 27 11:55 2026	0B	144K	-	-	-	-	off	-
golden/vm@s4	snapshot	14079954227361468190	Fri Nov 27 11:56 2026	0B	144K	-	-	-	-	off	-
golden/vm@s5	snapshot	15140771190786869205	Fri Nov 27 11:56 2026	0B	144K	-	-	-	-	off	-
golden/vm@s6	snapshot	10123221841499201790	Fri Nov 27 11:56 2026	0B	144K	-	-	-	-	off	-
golden/vm@s7	snapshot	11242862220542488526	Fri Nov 27 11:56 2026	0B	144K	-	-	-	-	off	-
golden/vm@s8	snapshot	12172810461772777427	Fri Nov 27 11:56 2026	0B	144K	-	-	-	-	off	-
golden/vm@s9	snapshot	17683708941584600799	Fri Nov 27 11:56 2026	0B	144K	-	-	-	-	off	-
golden/vm@s10	snapshot	9393505489177605140	Fri Nov 27 11:56 2026	0B	144K	-	-	-	-	off	-
golden/vm@s11	snapshot	14668134888933619867	Fri Nov 27 11:56 2026	0B	144K	-	-	-	-	off	-
golden/vm/clone-of-16k	volume	2859332922515262995	Fri Nov 27 11:55 2026	12.0M	20.0M	48M	16K	on	lz4	off	none
golden/vm/clone-of-16k@s4	snapshot	8892747740523751230	Fri Nov 27 11:56 2026	270K	19.9M	48M	-	-	-	off	-
golden/vm/clone-of-16k@s5	snapshot	11568055861224974220	Fri Nov 27 11:56 2026	291K	19.9M	48M	-	-	-	off	-
golden/vm/clone-of-16k@s6	snapshot	1088015684242833636	Fri Nov 27 11:56 2026	270K	19.9M	48M	-	-	-	off	-
golden/vm/clone-of-16k@s7	snapshot	1515737873547297875	Fri Nov 27 11:56 2026	282K	20.0M	48M	-	-	-	off	-
golden/vm/clone-of-16k@s8	snapshot	5898852859320370358	Fri Nov 27 11:56 2026	283K	20.0M	48M	-	-	-	off	-
golden/vm/clone-of-16k@s9	snapshot	5391661606356927073	Fri Nov 27 11:56 2026	254K	20.1M	48M	-	-	-	off	-
golden/vm/clone-of-16k@s10	snapshot	6411341465208006067	Fri Nov 27 11:56 2026	282K	20.0M	48M	-	-	-	off	-
golden/vm/clone-of-16k@s11	snapshot	5399584903168333941	Fri Nov 27 11:56 2026	0B	20.0M	48M	-	-	-	off	-
golden/vm/disk-128k	volume	7428789855559082725	Fri Nov 27 11:55 2026	89.5M	32.2M	48M	128K	sha256	lz4	off	none
golden/vm/disk-128k@s0	snapshot	8755838636319599647	Fri Nov 27 11:55 2026	2.13M	32.2M	48M	-	-	-	off	-
golden/vm/disk-128k@s1	snapshot	2591851618278217723	Fri Nov 27 11:55 2026	98.1K	32.1M	48M	-	-	-	off	-
golden/vm/disk-128k@s2	snapshot	1187066408165190379	Fri Nov 27 11:55 2026	98.1K	32.2M	48M	-	-	-	off	-
golden/vm/disk-128k@s3	snapshot	16439595398889643268	Fri Nov 27 11:55 2026	98.1K	32.1M	48M	-	-	-	off	-
golden/vm/disk-128k@s4	snapshot	979684171380179786	Fri Nov 27 11:56 2026	130K	32.2M	48M	-	-	-	off	-
golden/vm/disk-128k@s5	snapshot	3314269673012193515	Fri Nov 27 11:56 2026	98.1K	32.1M	48M	-	-	-	off	-
golden/vm/disk-128k@s6	snapshot	9971701273688053428	Fri Nov 27 11:56 2026	130K	32.2M	48M	-	-	-	off	-
golden/vm/disk-128k@s7	snapshot	7397818778565432393	Fri Nov 27 11:56 2026	130K	32.2M	48M	-	-	-	off	-
golden/vm/disk-128k@s8	snapshot	14379893170264659815	Fri Nov 27 11:56 2026	112K	32.1M	48M	-	-	-	off	-
golden/vm/disk-128k@s9	snapshot	18368806516887949603	Fri Nov 27 11:56 2026	112K	32.1M	48M	-	-	-	off	-
golden/vm/disk-128k@s10	snapshot	16398474708939211520	Fri Nov 27 11:56 2026	98.1K	32.1M	48M	-	-	-	off	-
golden/vm/disk-128k@s11	snapshot	14644439292617704760	Fri Nov 27 11:56 2026	0B	32.2M	48M	-	-	-	off	-
golden/vm/disk-16k	volume	7324933601684738320	Fri Nov 27 11:55 2026	81.7M	19.9M	48M	16K	sha256	zstd	off	none
golden/vm/disk-16k@s0	snapshot	910541474132800030	Fri Nov 27 11:55 2026	1.55M	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s1	snapshot	11334691736551760077	Fri Nov 27 11:55 2026	268K	19.8M	48M	-	-	-	off	-
golden/vm/disk-16k@s2	snapshot	15648214358209265049	Fri Nov 27 11:55 2026	270K	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s3	snapshot	11996318836647196640	Fri Nov 27 11:55 2026	268K	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s4	snapshot	6526631850418526578	Fri Nov 27 11:56 2026	283K	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s5	snapshot	11424236686828694459	Fri Nov 27 11:56 2026	284K	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s6	snapshot	6029946794281120014	Fri Nov 27 11:56 2026	283K	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s7	snapshot	15918358838373054067	Fri Nov 27 11:56 2026	270K	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s8	snapshot	4794683137600223345	Fri Nov 27 11:56 2026	286K	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s9	snapshot	9000753798449656398	Fri Nov 27 11:56 2026	283K	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s10	snapshot	14743196479142707730	Fri Nov 27 11:56 2026	270K	19.9M	48M	-	-	-	off	-
golden/vm/disk-16k@s11	snapshot	16464053618684501250	Fri Nov 27 11:56 2026	0B	19.9M	48M	-	-	-	off	-
golden/vm/disk-64k	volume	406025738756282991	Fri Nov 27 11:55 2026	65.5M	11.8M	48M	64K	sha512	gzip	off	none
golden/vm/disk-64k@s0	snapshot	8369961508810782337	Fri Nov 27 11:55 2026	885K	11.9M	48M	-	-	-	off	-
golden/vm/disk-64k@s1	snapshot	7543292180767860914	Fri Nov 27 11:55 2026	132K	11.9M	48M	-	-	-	off	-
golden/vm/disk-64k@s2	snapshot	13130351356656524344	Fri Nov 27 11:55 2026	132K	11.9M	48M	-	-	-	off	-
golden/vm/disk-64k@s3	snapshot	8825728806667408786	Fri Nov 27 11:55 2026	132K	11.9M	48M	-	-	-	off	-
golden/vm/disk-64k@s4	snapshot	11065520732073082589	Fri Nov 27 11:56 2026	144K	11.9M	48M	-	-	-	off	-
golden/vm/disk-64k@s6	snapshot	4170244421229002354	Fri Nov 27 11:56 2026	144K	11.8M	48M	-	-	-	off	-
golden/vm/disk-64k@s7	snapshot	7962674260852823175	Fri Nov 27 11:56 2026	132K	11.8M	48M	-	-	-	off	-
golden/vm/disk-64k@s8	snapshot	7324414323995699277	Fri Nov 27 11:56 2026	144K	11.8M	48M	-	-	-	off	-
golden/vm/disk-64k@s9	snapshot	7004962118221656707	Fri Nov 27 11:56 2026	144K	11.8M	48M	-	-	-	off	-
golden/vm/disk-64k@s10	snapshot	7042291982011718399	Fri Nov 27 11:56 2026	132K	11.8M	48M	-	-	-	off	-
golden/vm/disk-64k@s11	snapshot	14292686957082140549	Fri Nov 27 11:56 2026	0B	11.8M	48M	-	-	-	off	-
golden/vm/disk-8k	volume	7345759356079952279	Fri Nov 27 11:55 2026	121M	25.9M	48M	8K	fletcher4	lz4	off	none
golden/vm/disk-8k@s0	snapshot	12288134088391839177	Fri Nov 27 11:55 2026	2.00M	25.9M	48M	-	-	-	off	-
golden/vm/disk-8k@s1	snapshot	3178846698014141425	Fri Nov 27 11:55 2026	270K	26.0M	48M	-	-	-	off	-
golden/vm/disk-8k@s2	snapshot	13243069304192755154	Fri Nov 27 11:55 2026	281K	26.0M	48M	-	-	-	off	-
golden/vm/disk-8k@s3	snapshot	10016808325728576510	Fri Nov 27 11:55 2026	282K	26.2M	48M	-	-	-	off	-
golden/vm/disk-8k@s4	snapshot	13412890724800225206	Fri Nov 27 11:56 2026	294K	26.1M	48M	-	-	-	off	-
golden/vm/disk-8k@s5	snapshot	11836197629086281167	Fri Nov 27 11:56 2026	285K	25.8M	48M	-	-	-	off	-
golden/vm/disk-8k@s6	snapshot	15808581398103800068	Fri Nov 27 11:56 2026	294K	25.8M	48M	-	-	-	off	-
golden/vm/disk-8k@s7	snapshot	5707761955408108081	Fri Nov 27 11:56 2026	285K	25.8M	48M	-	-	-	off	-
golden/vm/disk-8k@s8	snapshot	7734277327482417888	Fri Nov 27 11:56 2026	295K	25.9M	48M	-	-	-	off	-
golden/vm/disk-8k@s9	snapshot	1186979500499030475	Fri Nov 27 11:56 2026	294K	26.0M	48M	-	-	-	off	-
golden/vm/disk-8k@s10	snapshot	6396392655555682158	Fri Nov 27 11:56 2026	312K	26.0M	48M	-	-	-	off	-
golden/vm/disk-8k@s11	snapshot	1420684696658087436	Fri Nov 27 11:56 2026	0B	25.9M	48M	-	-	-	off	-
golden/vm/disk-blake3	volume	8007773066019074833	Fri Nov 27 11:55 2026	116M	34.6M	48M	16K	blake3	off	off	none
golden/vm/disk-blake3@s0	snapshot	10147032863306321680	Fri Nov 27 11:55 2026	2.40M	34.6M	48M	-	-	-	off	-
golden/vm/disk-blake3@s1	snapshot	4750323676800708356	Fri Nov 27 11:55 2026	270K	34.6M	48M	-	-	-	off	-
golden/vm/disk-blake3@s2	snapshot	12392512559767808207	Fri Nov 27 11:55 2026	270K	34.6M	48M	-	-	-	off	-
golden/vm/disk-blake3@s3	snapshot	7250771446443004823	Fri Nov 27 11:55 2026	270K	34.7M	48M	-	-	-	off	-
golden/vm/disk-blake3@s4	snapshot	4356597597661540879	Fri Nov 27 11:56 2026	282K	34.6M	48M	-	-	-	off	-
golden/vm/disk-blake3@s5	snapshot	10304613150414114715	Fri Nov 27 11:56 2026	270K	34.6M	48M	-	-	-	off	-
golden/vm/disk-blake3@s6	snapshot	1177327930356573743	Fri Nov 27 11:56 2026	282K	34.7M	48M	-	-	-	off	-
golden/vm/disk-blake3@s7	snapshot	16889328844370176850	Fri Nov 27 11:56 2026	254K	34.6M	48M	-	-	-	off	-
golden/vm/disk-blake3@s8	snapshot	17126847037278597396	Fri Nov 27 11:56 2026	282K	34.7M	48M	-	-	-	off	-
golden/vm/disk-blake3@s9	snapshot	5798176971506942995	Fri Nov 27 11:56 2026	282K	34.7M	48M	-	-	-	off	-
golden/vm/disk-blake3@s10	snapshot	9853674794513479553	Fri Nov 27 11:56 2026	268K	34.6M	48M	-	-	-	off	-
golden/vm/disk-blake3@s11	snapshot	16426158777946830293	Fri Nov 27 11:56 2026	0B	34.6M	48M	-	-	-	off	-
golden/vm/disk-copies2	volume	16915484739506572096	Fri Nov 27 11:55 2026	175M	68.3M	48M	16K	fletcher4	lz4	off	none
golden/vm/disk-copies2@s0	snapshot	9253255258596599305	Fri Nov 27 11:55 2026	4.72M	68.5M	48M	-	-	-	off	-
golden/vm/disk-copies2@s1	snapshot	3176747172136248325	Fri Nov 27 11:55 2026	410K	68.5M	48M	-	-	-	off	-
golden/vm/disk-copies2@s2	snapshot	14971241260324641587	Fri Nov 27 11:55 2026	410K	68.5M	48M	-	-	-	off	-
golden/vm/disk-copies2@s3	snapshot	14162008245250264980	Fri Nov 27 11:55 2026	410K	68.4M	48M	-	-	-	off	-
golden/vm/disk-copies2@s4	snapshot	3957231418197572129	Fri Nov 27 11:56 2026	410K	68.3M	48M	-	-	-	off	-
golden/vm/disk-copies2@s5	snapshot	3222821194158885750	Fri Nov 27 11:56 2026	410K	68.3M	48M	-	-	-	off	-
golden/vm/disk-copies2@s6	snapshot	15959457846623463581	Fri Nov 27 11:56 2026	410K	68.1M	48M	-	-	-	off	-
golden/vm/disk-copies2@s7	snapshot	9361946613694094523	Fri Nov 27 11:56 2026	410K	68.2M	48M	-	-	-	off	-
golden/vm/disk-copies2@s8	snapshot	15932979220732004111	Fri Nov 27 11:56 2026	410K	68.2M	48M	-	-	-	off	-
golden/vm/disk-copies2@s9	snapshot	14953071377759355726	Fri Nov 27 11:56 2026	410K	68.2M	48M	-	-	-	off	-
golden/vm/disk-copies2@s10	snapshot	3363551338104415488	Fri Nov 27 11:56 2026	410K	68.3M	48M	-	-	-	off	-
golden/vm/disk-copies2@s11	snapshot	18221082964951638866	Fri Nov 27 11:56 2026	0B	68.3M	48M	-	-	-	off	-
golden/vm/disk-edonr	volume	6138055654929209280	Fri Nov 27 11:55 2026	96.9M	32.7M	48M	16K	edonr	zle	off	none
golden/vm/disk-edonr@s0	snapshot	11490307987833758976	Fri Nov 27 11:55 2026	2.26M	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s1	snapshot	14405549193399847523	Fri Nov 27 11:55 2026	266K	32.8M	48M	-	-	-	off	-
golden/vm/disk-edonr@s2	snapshot	18176884727207306280	Fri Nov 27 11:55 2026	270K	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s3	snapshot	3747324109673790538	Fri Nov 27 11:55 2026	266K	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s4	snapshot	16114206972972729826	Fri Nov 27 11:56 2026	282K	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s5	snapshot	17823400382952357957	Fri Nov 27 11:56 2026	270K	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s6	snapshot	17700522844912162292	Fri Nov 27 11:56 2026	282K	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s7	snapshot	16037763644321751316	Fri Nov 27 11:56 2026	267K	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s8	snapshot	2638305239164578342	Fri Nov 27 11:56 2026	270K	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s9	snapshot	878014251750061406	Fri Nov 27 11:56 2026	282K	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s10	snapshot	13456619704005022868	Fri Nov 27 11:56 2026	270K	32.7M	48M	-	-	-	off	-
golden/vm/disk-edonr@s11	snapshot	2676419971083441949	Fri Nov 27 11:56 2026	0B	32.7M	48M	-	-	-	off	-
golden/vm/disk-nocsum	volume	9389260330494728597	Fri Nov 27 11:55 2026	114M	34.3M	48M	16K	off	off	off	none
golden/vm/disk-nocsum@s0	snapshot	6683068474423190613	Fri Nov 27 11:55 2026	2.24M	34.3M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s1	snapshot	15816875182925975247	Fri Nov 27 11:55 2026	136K	34.3M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s2	snapshot	2806073255556160087	Fri Nov 27 11:55 2026	132K	34.3M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s3	snapshot	6209559752399325138	Fri Nov 27 11:55 2026	136K	34.3M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s4	snapshot	13424709791521827192	Fri Nov 27 11:56 2026	120K	34.3M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s5	snapshot	15748724666018375157	Fri Nov 27 11:56 2026	132K	34.3M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s6	snapshot	17624464460493769246	Fri Nov 27 11:56 2026	136K	34.3M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s7	snapshot	16675809180001462119	Fri Nov 27 11:56 2026	132K	34.4M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s8	snapshot	9633407473601583771	Fri Nov 27 11:56 2026	120K	34.3M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s9	snapshot	2029513292279731995	Fri Nov 27 11:56 2026	120K	34.3M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s10	snapshot	8378677476125628509	Fri Nov 27 11:56 2026	132K	34.4M	48M	-	-	-	off	-
golden/vm/disk-nocsum@s11	snapshot	16123537029711689270	Fri Nov 27 11:56 2026	0B	34.3M	48M	-	-	-	off	-
golden/vm/disk-skein	volume	14907099764968780040	Fri Nov 27 11:55 2026	81.2M	19.6M	48M	16K	skein	lzjb	off	none
golden/vm/disk-skein@s0	snapshot	2060824511892356572	Fri Nov 27 11:55 2026	1.39M	19.5M	48M	-	-	-	off	-
golden/vm/disk-skein@s1	snapshot	2688967257586613430	Fri Nov 27 11:55 2026	266K	19.6M	48M	-	-	-	off	-
golden/vm/disk-skein@s2	snapshot	10052680034947167359	Fri Nov 27 11:55 2026	282K	19.6M	48M	-	-	-	off	-
golden/vm/disk-skein@s3	snapshot	14663793128091684797	Fri Nov 27 11:55 2026	266K	19.5M	48M	-	-	-	off	-
golden/vm/disk-skein@s4	snapshot	6407307920721158282	Fri Nov 27 11:56 2026	282K	19.6M	48M	-	-	-	off	-
golden/vm/disk-skein@s5	snapshot	10430844364823014489	Fri Nov 27 11:56 2026	270K	19.5M	48M	-	-	-	off	-
golden/vm/disk-skein@s6	snapshot	14063662531449272564	Fri Nov 27 11:56 2026	282K	19.6M	48M	-	-	-	off	-
golden/vm/disk-skein@s7	snapshot	2205951879325647082	Fri Nov 27 11:56 2026	254K	19.5M	48M	-	-	-	off	-
golden/vm/disk-skein@s8	snapshot	15696664192011368442	Fri Nov 27 11:56 2026	286K	19.6M	48M	-	-	-	off	-
golden/vm/disk-skein@s9	snapshot	9657153939126967811	Fri Nov 27 11:56 2026	283K	19.6M	48M	-	-	-	off	-
golden/vm/disk-skein@s10	snapshot	6538048628009716917	Fri Nov 27 11:56 2026	270K	19.5M	48M	-	-	-	off	-
golden/vm/disk-skein@s11	snapshot	17013705018111540581	Fri Nov 27 11:56 2026	0B	19.6M	48M	-	-	-	off	-
golden/vm/disk-sparse	volume	8645215191594876224	Fri Nov 27 11:55 2026	43.8M	23.5M	256M	16K	fletcher4	lz4	off	none
golden/vm/disk-sparse@s0	snapshot	13486051283867619729	Fri Nov 27 11:55 2026	955K	18.5M	256M	-	-	-	off	-
golden/vm/disk-sparse@s1	snapshot	1903574924758701274	Fri Nov 27 11:55 2026	149K	19.9M	256M	-	-	-	off	-
golden/vm/disk-sparse@s2	snapshot	14365777192441846643	Fri Nov 27 11:55 2026	176K	21.5M	256M	-	-	-	off	-
golden/vm/disk-sparse@s3	snapshot	4268772300618374202	Fri Nov 27 11:55 2026	185K	23.7M	256M	-	-	-	off	-
golden/vm/disk-sparse@s4	snapshot	5811715331091306065	Fri Nov 27 11:56 2026	205K	23.6M	256M	-	-	-	off	-
golden/vm/disk-sparse@s5	snapshot	5105802760429107385	Fri Nov 27 11:56 2026	164K	23.5M	256M	-	-	-	off	-
golden/vm/disk-sparse@s6	snapshot	4581732425149133981	Fri Nov 27 11:56 2026	205K	23.5M	256M	-	-	-	off	-
golden/vm/disk-sparse@s7	snapshot	11125995940654818407	Fri Nov 27 11:56 2026	204K	23.5M	256M	-	-	-	off	-
golden/vm/disk-sparse@s8	snapshot	16487847849087980618	Fri Nov 27 11:56 2026	185K	23.5M	256M	-	-	-	off	-
golden/vm/disk-sparse@s9	snapshot	7151633570335050032	Fri Nov 27 11:56 2026	201K	23.5M	256M	-	-	-	off	-
golden/vm/disk-sparse@s10	snapshot	16799569630339861241	Fri Nov 27 11:56 2026	164K	23.4M	256M	-	-	-	off	-
golden/vm/disk-sparse@s11	snapshot	4763810191415107413	Fri Nov 27 11:56 2026	0B	23.5M	256M	-	-	-	off	-
golden/vm/disk-zstdfast	volume	3418504286682905919	Fri Nov 27 11:55 2026	82.1M	20.1M	48M	16K	sha256	zstd-fast	off	none
golden/vm/disk-zstdfast@s0	snapshot	11008717025309189779	Fri Nov 27 11:55 2026	1.57M	20.3M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s1	snapshot	8877514236635050135	Fri Nov 27 11:55 2026	286K	20.2M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s2	snapshot	13025067034884046204	Fri Nov 27 11:55 2026	283K	20.2M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s3	snapshot	650510949472656623	Fri Nov 27 11:55 2026	299K	20.2M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s4	snapshot	9427647982570063556	Fri Nov 27 11:56 2026	270K	20.1M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s5	snapshot	6608069029639779914	Fri Nov 27 11:56 2026	283K	20.2M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s6	snapshot	13067291931502830044	Fri Nov 27 11:56 2026	270K	20.1M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s7	snapshot	4550835462212887083	Fri Nov 27 11:56 2026	283K	20.2M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s8	snapshot	8093203690028768289	Fri Nov 27 11:56 2026	270K	20.1M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s9	snapshot	3980613715516763141	Fri Nov 27 11:56 2026	270K	20.1M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s10	snapshot	8334213436759555292	Fri Nov 27 11:56 2026	283K	20.2M	48M	-	-	-	off	-
golden/vm/disk-zstdfast@s11	snapshot	11159369527172377855	Fri Nov 27 11:56 2026	0B	20.1M	48M	-	-	-	off	-
golden/vm/newname	volume	10917120096066213306	Fri Nov 27 11:55 2026	98.4M	34.3M	32M	16K	fletcher4	lz4	off	none
golden/vm/newname@s0	snapshot	14664585624468730677	Fri Nov 27 11:55 2026	2.39M	34.5M	32M	-	-	-	off	-
golden/vm/newname@s1	snapshot	3755530858704768215	Fri Nov 27 11:55 2026	283K	34.6M	32M	-	-	-	off	-
golden/vm/newname@s2	snapshot	4161533425269844731	Fri Nov 27 11:55 2026	283K	34.5M	32M	-	-	-	off	-
golden/vm/newname@s3	snapshot	14448535233397947935	Fri Nov 27 11:55 2026	286K	34.5M	32M	-	-	-	off	-
golden/vm/newname@s4	snapshot	8404538457426609673	Fri Nov 27 11:56 2026	270K	34.5M	32M	-	-	-	off	-
golden/vm/newname@s5	snapshot	5611799047394590815	Fri Nov 27 11:56 2026	283K	34.5M	32M	-	-	-	off	-
golden/vm/newname@s6	snapshot	10348102490375400431	Fri Nov 27 11:56 2026	270K	34.5M	32M	-	-	-	off	-
golden/vm/newname@s7	snapshot	4336138265259630112	Fri Nov 27 11:56 2026	282K	34.5M	32M	-	-	-	off	-
golden/vm/newname@s8	snapshot	18391293861524464412	Fri Nov 27 11:56 2026	251K	34.5M	32M	-	-	-	off	-
golden/vm/newname@s9	snapshot	12464674437847150403	Fri Nov 27 11:56 2026	270K	34.4M	32M	-	-	-	off	-
golden/vm/newname@s10	snapshot	6834077108419491585	Fri Nov 27 11:56 2026	282K	34.4M	32M	-	-	-	off	-
golden/vm/newname@s11	snapshot	15263933993362271785	Fri Nov 27 11:56 2026	0B	34.3M	32M	-	-	-	off	-
```

## What is in it

* Volumes over every checksum and compression, of volblocksize 8K to 128K, one sparse, one of `copies=2`, one of `checksum=off`, two encrypted (a raw key and a passphrase). Where a volume's compression is on, it is written with content that compression shrinks — the hex dump of a keystream, every line twice; for `zle`, the keystream with every other 2 KiB zeroed — and with the keystream itself where it is off.
* `fs-largednode`: 400 files with an extended attribute each, large dnodes.
* `fs-tree`, `casesensitivity=mixed`, `normalization=formD`, `xattr=sa`, legacy dnodes: nine levels of directories, a fat-ZAP directory of 300 long names, names differing in case alone, a name written composed and decomposed (one file under formD), a Cyrillic name, a name of 255 bytes, hard links in one directory and across two, symbolic links short, of 1009 bytes, to a directory and to nothing, a sparse file of 1100 MiB with three records of data, a file that is all hole, a file of 1536 records of 4 KiB (two level-1 blocks under a level-2 block), attributes that spill out of the dnode, one in a directory of attributes, one on a directory, unusual owners and modes, a FIFO and two device nodes; and cloned blocks (`cp --reflink`), within the dataset and into `fs-base`.
* `fs-base` and `fs-promoted`: a clone of `fs-base@s1`, written to, promoted at round 4.

## History

12 rounds of 8 TXGs with 256 KiB writes to every volume, a recursive snapshot `s<round>` after each round. After round 1, `fs-base@s1` cloned to `fs-promoted`; 2, a file of the tree grown and one added; 3, `vm/disk-16k@s3` cloned to `vm/clone-of-16k`; 4, `fs-promoted` promoted; 5, a directory of the tree removed with its files and a hard link undone; 6, `vm/oldname` renamed to `vm/newname`; 7, `vm/disk-64k@s5` destroyed; 8, `vm/disk-8k` and `fs-tree` written to and rolled back to `s8`; 9, `vm/doomed@s2` then `vm/doomed` destroyed, its bytes hashed just before (`vm/doomed@destroyed` in `volumes.sha256`); 10, 64 KiB of the 4K-record file rewritten, a file of the tree moved, `fs-doomed` destroyed. Gang blocks forced (threshold 16 KiB) from the volumes' first fill to the end of the history; the tree was written before. Deterministic content from seed `zvolrescue-golden-2026`. The `round6-*` release files are a consistent copy of members taken right after round 6 (the `older-self:round6` pattern of the damage manifests): draid1-3 mirror-0a mirror-0b raidz2-0 raidz2-1 raidz2-2.

## Oracle

See `oracle/`: `volumes.sha256` (every volume at every snapshot, at export, and just before it was destroyed), `zfs-get-destroyed.txt` (the properties of what was destroyed, just before), `datasets*.txt`, `datasets-by-txg/`, `labels/`, `labels-uberblocks/`, `zdb-u-export.txt`, `zdb-*.txt` and `zdb-dddddd/` (offline, over the exported members; the last one file a dataset), `files.json`, `zpool-history-il.txt` and `files-capture.txt` (the kernel, read-only), `zpool-status.txt`, `keys/`, `layout.json`, `members.sha256` and `members-round6.sha256` (uncompressed).

## Release files

```
e2fc014fb0bad31c415da45aeb4f0c4ca23e51f3fc26daf07370ac5a47d36f7e  draid1-0.img.zst
05ee7574718ad5cfde806fb022e49b4028443f57949d86c4c369a365eca1a551  draid1-1.img.zst
a0f067d88d79862b12a17c0adcdc54e3eb458a4ef444cca36fecfe33d3588ab8  draid1-2.img.zst
08e70d0fb124634843b5e39b00198b1a78446b446873697f539c86544070d03d  draid1-3.img.zst
f6a5dd692d3657517f3d53bf7cea0874f6b4b7d4464227f9ea73562707365de2  mirror-0a.img.zst
99797cbc4c49f98671f5752ecc26942fec0d90462239d4b27e2bbdadc083dc22  mirror-0b.img.zst
891f709f12ae0d2977723fb1cc5616d3eba27aecfe1887e0a27af2b9c017fe9e  raidz2-0.img.zst
efc70e3077814a1d18d6bb831f8c3cdecb2e41aa3cd643edc3607711650f6a1b  raidz2-1.img.zst
bebc9544e5553fbdb90fa90582198d5d2748ea63ec3e460024549f0dd3033095  raidz2-2.img.zst
4d3f8a9ca8181a3d2b21c9991a72be231b9d01edac40f606b1a8940c03855bd0  raidz2-3.img.zst
ee9ad663975ffdcc28dbcd9f1e2478b50679e0e5da4e7d799f021adc821568a8  round6-draid1-3.img.zst
585355bde7bb80d7fb92fc5c9ee3a9caf74542c044e79f79b432d69de78134e8  round6-mirror-0a.img.zst
406fcd0c8468c8c7c25e0ff8372c353588ed7bf5c336d2c1d2ef8ae6f7dd07fb  round6-mirror-0b.img.zst
8e3525054687a785079c7397d79df0e11d42ec349ea8999d001e4c764022cefc  round6-raidz2-0.img.zst
719c72b74ed72d5a53b48e5474a0fbcc28509d21ee8d6bf67ef216b50b968cff  round6-raidz2-1.img.zst
487364fa256e84c119af1b5425a58483d1d65ede86ba6e2779d0767f4111eca9  round6-raidz2-2.img.zst
```
