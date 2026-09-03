---
id: US-MINERAL-E01-SOURCE-MANIFEST
type: outcome-blind-stage-a-source-manifest
created: 2026-09-04
stage_a_pass: true
primary_values_parsed_in_stage_a: false
incremental_monetary_cost_usd: 0
---

# US-MINERAL-E01 Stage A Source Manifest / Stage A 소스 매니페스트

## Contract / 계약

- Frozen period: `2023-01` through `2023-12`.
- Frozen universe: `Antimony, Barite, Beryllium, Palladium, Phosphate, Potash, Rhodium, Tellurium`.
- Stage A parsed only fixed-width identity positions `1-28`; `gen_val_mo` positions `179-193` were not interpreted during Stage A.

## Source snapshots / 소스 스냅샷

| Month | HTTP | Content-Type | ZIP bytes | ZIP SHA-256 | Member | Member bytes | Member SHA-256 | Frozen mapped rows |
|---|---:|---|---:|---|---|---:|---|---:|
| 2023-01 | 200 | `application/zip` | 64301524 | `6b517fe8ae78c9b5675eab0ee6b63d2a3163e2e79a16e8dd0bbcb410df526a9e` | `IMP_DETL.txt` | 466564200 | `e7287bb47d5dd9a647ca27949541e1476af9d9068bf56aed7d2f5f150637df01` | 282 |
| 2023-02 | 200 | `application/zip` | 88808088 | `04f4428f1d8e64f8a4a9d1cc2b0e64036a3f89a772ed2d7b4a12eff5e86c0eee` | `IMP_DETL.txt` | 654511920 | `61d0762761e0bf01f7c3ea06af847d603a068685290efa4fd7c81f29dcc4981d` | 411 |
| 2023-03 | 200 | `application/zip` | 102105536 | `16d4b727973499dc19fa63d8d1b584da15eb5294175437bf768a360364cc3c53` | `IMP_DETL.txt` | 814817550 | `2347071acf87963bde72beae85a92541c80b85bd21ecf8346d2bccdfa4e988c8` | 542 |
| 2023-04 | 200 | `application/zip` | 111939419 | `af534410fcc903b48324c02929b9241ecd6a157d1f016b7d3366d46d50b991c8` | `IMP_DETL.txt` | 939025830 | `fcfb8c41d17307e0589a6d52c775f021278196a4fba3e210ca3498f424791ea5` | 613 |
| 2023-05 | 200 | `application/zip` | 121461519 | `64158ea1e757b98eee92b2b835c7344d5a28f0fc20a418abd00f000e842365f7` | `IMP_DETL.txt` | 1055893890 | `371e9c81ffc12a95994d0ce2ba33ac419e93edb6889428b87cbb3e7fed502e5a` | 679 |
| 2023-06 | 200 | `application/zip` | 129414795 | `15838b89a93359ac3f9b19f5d5d4899616c37d7b42c90e2c458e5929364056bd` | `IMP_DETL.txt` | 1161123030 | `09a89c98cb4d976a70f293c0f4ea47825416ee14beac0f4f67bafb4619635159` | 741 |
| 2023-07 | 200 | `application/zip` | 137139187 | `480a29a35b831c122695ce3442a87cfd629b001e0327d613870a55e210e9d87e` | `IMP_DETL.txt` | 1262902860 | `242b1671a62203e93fe3a9e0403d3b118152b135c46083ed1e6762e1d6ca9c6b` | 802 |
| 2023-08 | 200 | `application/zip` | 144804053 | `d3c32b9c582fc1c566e12a8cc4376f73473219034e0538e51d22ad0a398c85ec` | `IMP_DETL.txt` | 1359513210 | `4ea5121341ab86bd96379d561a3d33e14c229a5a0a63436e797ecee090d4cdfd` | 846 |
| 2023-09 | 200 | `application/zip` | 150688144 | `9c9d00628eadf3a9b58fb74af75881b5a25f70ed0428e5386bb01549c1d3fc0a` | `IMP_DETL.txt` | 1443585570 | `3dc56c5301584161d23821db267c6a7998afa4d1b06e6ef23d4523353342a8e7` | 898 |
| 2023-10 | 200 | `application/zip` | 157723124 | `29c189bc9bd5c76ffe600c4c71984a65cd70257af7d0955e0266be7057f169af` | `IMP_DETL.txt` | 1530757410 | `73b4ce70185b5a8eb9ec68e9d193b70cc3a896c9cb27f09738498b1a225afd81` | 948 |
| 2023-11 | 200 | `application/zip` | 162790072 | `704629afba8ca91343bd4a7bed053065b800fe888294b2ccfff5120c2f4397d8` | `IMP_DETL.txt` | 1609556790 | `6673a0525ca11488b386c40f4b3fa6a5e292d31b6d113dc5a8a7ccf6796105fa` | 984 |
| 2023-12 | 200 | `application/zip` | 167953446 | `6b29da2c27288487d8cbf1613f4910eac762fcdec0ed88b984ead54a0c2a5eef` | `IMP_DETL.txt` | 1682212410 | `ecc0f4c0034df2ada78ed38f46cd4528348db311a6eb85e27c6a30daa588756b` | 1033 |

## Frozen-universe structural counts / 고정 universe 구조 count

| Mineral | Mapped rows | Months with mapped rows |
|---|---:|---:|
| Antimony | 1041 | 12 |
| Barite | 695 | 12 |
| Beryllium | 422 | 12 |
| Palladium | 689 | 12 |
| Phosphate | 3113 | 12 |
| Potash | 2210 | 12 |
| Rhodium | 472 | 12 |
| Tellurium | 137 | 12 |

## Stage A gate / Stage A 게이트

**`PASS_E01_STAGE_A_SOURCE_IDENTITY_CARDINALITY`**

All 12 official carrier/member snapshots were pinned; mapped identities parsed; no repeated frozen raw full key was detected; every frozen mineral has at least one published mapped record in the 2023 window.

Incremental monetary cost remained **0 USD**.
