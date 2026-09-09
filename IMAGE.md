# The interim golden image (image-v0-ztest)

Built 2026-09-09T21:49:32Z on Linux 6.18.44-fc-v24 x86_64 with OpenZFS userland
(OpenZFS (version not reported)), **no kernel module**: `ztest` created and exercised the pools
entirely in user space, `zdb` recorded the oracle.

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
| mirror | 0 | mirror | `t0-mirror-0` → `ztest.0a`, `t0-mirror-1` → `ztest.1b` |
| raidz2 | 0 | mirror of raidz2 | `t0-raidz2-0` → `ztest.0a`, `t0-raidz2-1` → `ztest.1a`, `t0-raidz2-2` → `ztest.2a`, `t0-raidz2-3` → `ztest.3a` |
| raidz2 | 1 | mirror of raidz2 | `t1-raidz2-0` → `ztest.4a`, `t1-raidz2-1` → `ztest.5a`, `t1-raidz2-2` → `ztest.6a`, `t1-raidz2-3` → `ztest.7a` |
| draid1 | 0 | draid1 | `t0-draid1-0` → `ztest.0a`, `t0-draid1-1` → `ztest.1a`, `t0-draid1-2` → `ztest.2a`, `t0-draid1-3` → `ztest.3a`, `t0-draid1-4` → `ztest.4a`, `t0-draid1-5` → `ztest.5a`, `t0-draid1-6` → `ztest.6a`, `t0-draid1-7` → `ztest.7a`, `t0-draid1-8` → `ztest.8a`, `t0-draid1-9` → `ztest.9a`, `t0-draid1-10` → `ztest.10a`, `t0-draid1-11` → `ztest.11a`, `t0-draid1-12` → `ztest.12a`, `t0-draid1-13` → `ztest.13a`, `t0-draid1-14` → `ztest.14a`, `t0-draid1-15` → `ztest.15a` |

## Datasets

### mirror

| Dataset | Creation TXG | Objects |
|---|---|---|
| `ztest` | 1 | 0 |
| `ztest/ds_0` | 6 | 15 |
| `ztest/ds_1` | 67 | 15 |
| `ztest/ds_1@1` | 1051 | 15 |
| `ztest/ds_2` | 68 | 15 |
| `ztest/ds_2@2` | 1210 | 15 |
| `ztest/ds_3` | 70 | 15 |
| `ztest/temp_0` | 1398 | 5 |
| `ztest/temp_0@0` | 1406 | 5 |
| `ztest/temp_1` | 1558 | 5 |
| `ztest/temp_1@2` | 1600 | 5 |
| `ztest/temp_2` | 1369 | 5 |
| `ztest/temp_3` | 1541 | 1 |

### raidz2

| Dataset | Creation TXG | Objects |
|---|---|---|
| `ztest` | 1 | 0 |
| `ztest/ds_0` | 6 | 16 |
| `ztest/ds_0@0` | 833 | 16 |
| `ztest/ds_1` | 41 | 15 |
| `ztest/ds_2` | 43 | 15 |
| `ztest/ds_3` | 45 | 15 |
| `ztest/ds_3@3` | 425 | 15 |
| `ztest/temp_0` | 949 | 1 |
| `ztest/temp_1` | 965 | 5 |
| `ztest/temp_1@2` | 971 | 5 |
| `ztest/temp_2` | 914 | 5 |
| `ztest/temp_2@3` | 956 | 5 |
| `ztest/temp_3` | 942 | 5 |
| `ztest/temp_3@1` | 952 | 5 |

### draid1

| Dataset | Creation TXG | Objects |
|---|---|---|
| `ztest` | 1 | 0 |
| `ztest/ds_0` | 6 | 16 |
| `ztest/ds_0@0` | 423 | 15 |
| `ztest/ds_1` | 46 | 15 |
| `ztest/ds_1@1` | 324 | 14 |
| `ztest/ds_2` | 48 | 15 |
| `ztest/ds_3` | 50 | 15 |
| `ztest/ds_3@3` | 586 | 15 |
| `ztest/temp_0` | 634 | 1 |
| `ztest/temp_1` | 630 | 5 |
| `ztest/temp_1@2` | 648 | 5 |
| `ztest/temp_2` | 643 | 5 |
| `ztest/temp_3` | 632 | 1 |

## Oracle

`oracle/<pool>/`:

| File | Content |
|---|---|
| `inventory.txt` | dataset, creation TXG, object count — from `zdb -d` |
| `datasets.txt` | `zdb -d` verbatim |
| `zdb-dddd.txt` | every object with its block pointers and the checksums ZFS recorded |
| `zdb-C.txt`, `zdb-u.txt` | pool configuration and uberblock |
| `labels/<role>.txt` | `zdb -l` of that member |
| `layout.json`, `members.txt` | roles, files, GUIDs, topology |
| `keys/raw.key` | ztest's fixed wrapping key (it protects nothing) |

Nothing here was produced by zvolrescue.

## A caveat about this particular build

`ztest` picks its topology, datasets and writes at random, so a rebuild
produces a *different* image. The oracle in `oracle/` and the sums below
describe exactly the build listed here. If those member files are never
published, treat this image as a record of one run rather than a fixture:
rebuild with `tests/golden/build-ztest-image.sh`, and the new oracle
replaces this one. The kernel-built golden image (`image-v1`) will be the
first fixture worth pinning, because it is built by a script that decides
the layout instead of ztest.

## Release files

`<pool>-<role>.img.zst` — the members, one file per role. Unpack with
`zstd -d` into a directory per pool and point the harness at it.

```
c5123326163eb35eb978132a66ec6f6d820f960fbe1b85853d014cd924fa3d60  draid1-t0-draid1-0.img.zst
549abbb6c3337096e723bd5aa716d441693643d1c579de9f9f997b8ba400fbed  draid1-t0-draid1-1.img.zst
ac528a86faf115215c966b3933bd2ad7e47d31220b8f1c4acc21dea76827a281  draid1-t0-draid1-10.img.zst
84a795ba9c64badf79558e3620307d080d88036a5cbc5bc880998b3e4eacfd26  draid1-t0-draid1-11.img.zst
506e34772e3adb4a615fc4c131db9763ea7e6094dc9617cb2bcc4e3db137a090  draid1-t0-draid1-12.img.zst
f24e2a22468d16dd9e22ff23b71a7a20c90978def57bebf3a36aea867b8eb5ce  draid1-t0-draid1-13.img.zst
a73e83ee3a8dab1951eda80a5892199f99e1226111a752e2a6fd35fe511800dc  draid1-t0-draid1-14.img.zst
329eeb7b226872a9467c5313e8385ccea678bf2ac7ba968ccb082b26ae3beaa2  draid1-t0-draid1-15.img.zst
44e464e9d32ea2a8ae886249f2387926c6ed96ee2f2d90e545e63a3bb3db43f2  draid1-t0-draid1-2.img.zst
c817bcc9705aef710b0ed0dfab092ea77068185d889321dcd22446f5c680f3ca  draid1-t0-draid1-3.img.zst
b2fda7e3eecf5cc3b45086adcbe462ae20d98a104b16c97ce1e637eb3b8d25e0  draid1-t0-draid1-4.img.zst
3ed3586d45f11101abe4a3d05e75ffd2cd5bc141166d7acc428a6f7fb048c09b  draid1-t0-draid1-5.img.zst
0bd8e92b7741ba875ebf6f0e2bfdeaa520b967d2a14d87aa095bf8ff6339d82d  draid1-t0-draid1-6.img.zst
9295aa7cac29a9d54dde8db2e5964f6002c62e936c55a201c2b6beb25c47eae9  draid1-t0-draid1-7.img.zst
70bab9c6e7e3df6de71ae40b88ef622678a6801ad3ca7e81c50e75863b127c49  draid1-t0-draid1-8.img.zst
b2d1c0a635b4a42ba88bb989ea71dec7f0d471c18ef9398bf7555cd43273ffe2  draid1-t0-draid1-9.img.zst
eaa77c98112f9f00b4d821c4dce9538fbba1b1ac4cdd1726f9f1b5b6214f4aeb  mirror-t0-mirror-0.img.zst
ad8ba475f1ddda5fb0c7ed881cee8b71f145c280aa9614f7965dbb9f0d2c270e  mirror-t0-mirror-1.img.zst
450f30ebfc866e8059a3707c0063f51ac11f2f004f359abbca6ba8f6cb7ba060  raidz2-t0-raidz2-0.img.zst
a00d87c052de3cd9c1ad1530f3f5b3391ada13218b64ee6be5ae3194da61bd96  raidz2-t0-raidz2-1.img.zst
f191c00385e4b0869488306679c472576cffbb57a2ce54afba4db5350c4d18a6  raidz2-t0-raidz2-2.img.zst
bb1cc770e486f6abe31b3478e123ab7895fa6d13e8935375b3e96ff0b7a81f64  raidz2-t0-raidz2-3.img.zst
e9f581d182e3e1f07c2e8d876625ac4ed803e2bc24aee7225feae047a028be2c  raidz2-t1-raidz2-0.img.zst
7d24ebf763eabeb320fa047f8362f329106fcc240e4797eb82d3c24ccfa699a3  raidz2-t1-raidz2-1.img.zst
85ee4d7548c9bd81c461fb606483ef7abd0e3528f3b0c4631343bc57800f71f4  raidz2-t1-raidz2-2.img.zst
ca13190c9827007481066e62504c2c258acfb5a763cd46ad612265260234beff  raidz2-t1-raidz2-3.img.zst
```
