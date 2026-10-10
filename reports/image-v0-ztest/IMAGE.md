# The interim golden image (image-v0-ztest)

Built 2026-09-10T08:16:17Z on Linux 6.18.44-fc-v24 x86_64 with OpenZFS userland
OpenZFS (version not reported), **no kernel module**: `ztest` created and exercised the
pools entirely in user space.

## What this is and is not

A stopgap until the real golden image can be built on a host with a ZFS
kernel module (`tests/golden/build-image.sh` in zvolrescue). It carries
genuine OpenZFS metadata — MOS, DSL, dnodes, ZAPs, every checksum and
compression, encrypted datasets, gang blocks, hundreds of TXGs — but:

* **no zvols**: ztest creates filesystem-like datasets only, so damage runs
  are judged by walking every object of every dataset (the dataset list must
  match `zdb -d`, every block must read and verify) instead of by comparing
  volume hashes;
* **three pools, not one**: ztest cannot mix top-level vdev kinds, so the
  mirror, raidz2 and draid1 geometries live in separate pools; a manifest
  that spans geometries does not apply to any of them;
* **no `older-self` material**: ztest cannot be resumed on an existing pool
  without a cachefile it does not leave behind, so a member cannot be
  captured at two points of the same pool's life.

ztest also adds top-level vdevs while it runs, and wraps parity vdevs in a
mirror, so the topology below is what the pools ended up with, not what the
command line asked for. Roles name each member after its innermost
redundancy group.

## Pools

| Pool | Top-level vdev | Shape | Members (role → file) |
|---|---|---|---|
| mirror | 0 | mirror | `t0-mirror-0` → `ztest.0a`, `t0-mirror-1` → `ztest.1a` |
| raidz2 | 0 | mirror of raidz2 | `t0-raidz2-0` → `ztest.0a`, `t0-raidz2-1` → `ztest.1a`, `t0-raidz2-2` → `ztest.2a`, `t0-raidz2-3` → `ztest.3a` |
| draid1 | 0 | draid1 | `t0-draid1-0` → `ztest.0a`, `t0-draid1-1` → `ztest.1a`, `t0-draid1-2` → `ztest.2a`, `t0-draid1-3` → `ztest.3a`, `t0-draid1-4` → `ztest.4a`, `t0-draid1-5` → `ztest.5a`, `t0-draid1-6` → `ztest.6a`, `t0-draid1-7` → `ztest.7a`, `t0-draid1-8` → `ztest.8a`, `t0-draid1-9` → `ztest.9a`, `t0-draid1-10` → `ztest.10a`, `t0-draid1-11` → `ztest.11a`, `t0-draid1-12` → `ztest.12a`, `t0-draid1-13` → `ztest.13a`, `t0-draid1-14` → `ztest.14a`, `t0-draid1-15` → `ztest.15a` |

## Datasets

### mirror

```
ztest 1 0
ztest/ds_0 6 15
ztest/ds_0@0 782 15
ztest/ds_1 39 15
ztest/ds_1@1 1143 15
ztest/ds_2 40 15
ztest/ds_2@2 844 15
ztest/ds_3 41 14
ztest/ds_3@3 1431 14
ztest/temp_0 1024 5
ztest/temp_0@0 1026 5
ztest/temp_1 1138 1
ztest/temp_2 1228 5
ztest/temp_2@0 1255 5
ztest/temp_3 1755 5
ztest/temp_3@0 1775 5
ztest/temp_3@1 1783 5
ztest/temp_3@2 1796 5
```

### raidz2

```
ztest 1 0
ztest/ds_0 6 15
ztest/ds_1 73 15
ztest/ds_1@1 936 15
ztest/ds_2 75 14
ztest/ds_2@2 936 14
ztest/ds_3 77 14
ztest/ds_3@3 517 14
ztest/temp_0 993 5
ztest/temp_1 1041 5
ztest/temp_1@2 1052 5
ztest/temp_1@3 1068 5
ztest/temp_2 1161 5
ztest/temp_2@0 1162 5
ztest/temp_3 1272 5
```

### draid1

```
ztest 1 0
ztest/ds_0 6 16
ztest/ds_0@0 1122 16
ztest/ds_1 43 14
ztest/ds_1@1 619 14
ztest/ds_2 45 15
ztest/ds_3 47 14
ztest/ds_3@3 862 14
ztest/temp_0 1126 1
ztest/temp_1 1123 5
ztest/temp_1@0 1136 5
ztest/temp_2 1064 5
ztest/temp_2@0 1067 5
ztest/temp_3 965 5
ztest/temp_3@0 967 5
```

## Oracle

`oracle/<pool>/`: `inventory.txt` (dataset, creation TXG, object count — from
`zdb -d`), `datasets.txt`, `zdb-dddd.txt` (every object with its block
pointers and the checksums ZFS recorded), `zdb-C.txt`, `zdb-u.txt`,
`labels/<role>.txt` (`zdb -l`), `members.txt`, `layout.json`, `keys/raw.key`
(ztest's fixed wrapping key). Nothing here was produced by zvolrescue.

## Release files

`<pool>-<role>.img.zst` are the published members, one file per role.
There is no `older-self` material in this image: ztest cannot be resumed
on an existing pool without a cachefile it does not leave behind, so a
member cannot be captured at two points of the same pool\'s life. Manifests
using that pattern are skipped until the kernel-built image exists.

```
d2840d23316695e8ab2301c79dd6c6e314648911770d97e12b000107ab777e83  draid1-t0-draid1-0.img.zst
decb10a311db1c6a76fbd75a49d2e29125a8e123e944d38bb64f0d8a8d16b2da  draid1-t0-draid1-1.img.zst
7d890192bfd505ba49483292a9aaca9b675dd003bc3080f6f755e6d294dde7b6  draid1-t0-draid1-10.img.zst
0318d907530ac953dffe606d276c36152a215a134e79995b5da1152ed19cc06c  draid1-t0-draid1-11.img.zst
474f2ad4160f1d38af8f675c3cb2243eb46abb59b51c2449248f3f63cc922731  draid1-t0-draid1-12.img.zst
b212f36a0cc8494b3df1dd52905053789b741184c1b97ff1d4a610822b255d52  draid1-t0-draid1-13.img.zst
4026aa6a53e827455ffa3a71e938cb346a35b5540326a41e2b3c7d3856288d72  draid1-t0-draid1-14.img.zst
1ef1a6c602cc8729413e2c06c230c64c5aeb86d715263ed39234e63847164ee5  draid1-t0-draid1-15.img.zst
58e56ae7c534c3b775d807baeface01a9e504722cc501951d31a5b7025ecf539  draid1-t0-draid1-2.img.zst
c69dbd38944c069fefd046be7eeea11a5731b61820cb513f1914d6846c37e9f9  draid1-t0-draid1-3.img.zst
8b024dda9a602bcedb0abc2e1a6c38402cd56e686f2942a5f8d50fe05d9fa26d  draid1-t0-draid1-4.img.zst
7c272300727ce0f2e0edb9d1ac754993521ba1b52724e5ad0883dc13cdf9bb2c  draid1-t0-draid1-5.img.zst
fa7792e521ddfafabff55431527997c7efb6dc7a84a0ae8766e800f431a4aecd  draid1-t0-draid1-6.img.zst
d2ccdbffa6589ad1c258ca7829abce8e7f463d5980fc58e6dd6b9d57d91cf7cb  draid1-t0-draid1-7.img.zst
0391f5e15c39548245afcaf825b470dd39c6271fb726a4c0b937722fe501b8ce  draid1-t0-draid1-8.img.zst
2e6afdb532c65fc38dc47a33575e9fe5a43a0971c2bb5c634c407faabb28050e  draid1-t0-draid1-9.img.zst
6e35ef05bda5f355a2a25392a4ab828376ed0a189095039681aceb1afa2c073a  mirror-t0-mirror-0.img.zst
4b2eca9e08a302598f29a8dba6fe80304442639dbf6096cac76e0e23cb870a00  mirror-t0-mirror-1.img.zst
ec350e9a4102c3909c859dff5ac427778ae8f4518b4359eb7ea346a2211863b1  raidz2-t0-raidz2-0.img.zst
a148af6f2083d66ea102e2a50f376609519e8ca8df39cf342358031c3dc7e085  raidz2-t0-raidz2-1.img.zst
5c200c6771b183c342dcac429a1c2a74b6a1b792247cb2a92d17e2e4552387a4  raidz2-t0-raidz2-2.img.zst
affcf4817912a3a4037d03e5ea79a8c1e6a4602cc58c5a49ca10bc2e91c648e2  raidz2-t0-raidz2-3.img.zst
```
