---
id: JP-PORT-E01-STAGE-A-SOURCE-MANIFEST
created: 2026-09-04
stage_a_gate: PASS_E01_STAGE_A_SOURCE_IDENTITY_QUALITY
relationship_outcome_computed: false
primary_weather_summary_computed: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-E01 Stage A Source / Identity / Quality Manifest

## Stage A gate: **PASS_E01_STAGE_A_SOURCE_IDENTITY_QUALITY**

Stage A opened only the preregistered JMA daily maximum-wind variable to validate source identity, quality, homogeneity and monthly completeness. It did not compute monthly wind maxima, read cargo magnitudes for relationship analysis, or calculate beta.

## A. MLIT source revalidation

| Year | Bytes | SHA-256 | Port total rows |
|---:|---:|---|---:|
| 2019 | 1056222 | c9b52effc6939080290f9cd2d1eaad894769d5a0af8f5c268bd18dce5218bebf | 161 |
| 2020 | 1048653 | 9ee04b6f968fa475f004c7e397cb74303d6bd3498972ef040c12f3414b1fbe46 | 166 |
| 2021 | 1045142 | de510a1510a178a9dc3d3d0dce9ed5ea8da165929ccb0d381458f2005571dd68 | 166 |
| 2022 | 1045714 | f5e1402c0fba0afa2b8a74f8e463638c9dc6ef141ed9c08355f39125b6fa61c4 | 166 |
| 2023 | 1044224 | 4670b2ac230cae5b2bdc6a50ae03c72001137ca24b9c023a6f90e28e77156d04 | 166 |
| 2024 | 1056705 | 830c2173b19f9ea106596e043730bd93616dafe93ef0c6a385d633335cef0200 | 166 |

## B. E01 transport crosswalk

- F01-qualified port mappings: **149**
- exact one-to-one obsdl station transport identities: **126**
- ambiguous obsdl station names excluded before values: **5 station IDs**
- ports retained before quality/completeness: **143**
- ports excluded because their station transport identity is ambiguous: **6**

Excluded transport-ambiguous port mappings:
下関→81428 下関, 伏木富山→55091 伏木, 北九州→81428 下関, 直江津→54586 大潟, 石狩湾新→14116 山口, 高松→72086 高松

## C. Raw JMA CSV manifest

- root-session SHA-256: 78e5d9e76d1e3dfb240cda4d837d9a870a8cbc3ae58a8b8ff20b4bee842ad2f9
- requested element only: 302 最大風速
- period per request: 2019-01-01..2024-12-31
- deterministic batch size: **8 stations**
- number of requests: **16**
- 5-second pause between requests
- one bounded retry only for HTTP 502/503/504, after 15 seconds

| Batch | History station IDs | obsdl IDs | Bytes | SHA-256 | Rows | Attempt |
|---:|---|---|---:|---|---:|---:|
| 1 | 11016 13277 16091 17112 17341 18273 19432 20751 | s47401 s47406 s47411 s47435 s47409 s47420 s47418 s47440 | 300283 | 03d6e9876881910b4fc8b5aed01b1ebe42bac45b24cf1fa66c6a69dfcc400839 | 2198 | 1 |
| 2 | 21187 21323 23232 31121 31312 31336 31602 32111 | s47424 s47423 s47430 a1122 s47575 a1027 s47581 a0183 | 299716 | bf64c5520a5ed469e4b5e4f54516b288a7c43796080c2bbec0f18308a666be5a | 2198 | 1 |
| 3 | 32286 32402 33146 33472 33751 33877 34331 35052 | a1036 s47582 a0209 s47585 a0233 s47512 a1030 s47587 | 298538 | 9c823897e7085b7ca6ea8a8340a746195364412347b32dd527f907790ff58409 | 2198 | 1 |
| 4 | 36151 36846 40201 44166 45212 45282 46106 46211 | a0285 s47598 s47629 a0371 s47682 a0382 s47670 a0392 | 299695 | 3e34dccb536bf1eb45e0df153c2220b738da396d4b9555e093f3f87746929c7c | 2198 | 1 |
| 5 | 50196 50206 50477 50551 51216 51311 51331 53061 | a0442 s47657 a1601 s47655 a1638 a0984 a0470 s47684 | 298530 | bd8f7ed0cbce9d9aa3ea41a4cc4026ca9dc74b76469585c4fda7499ae451c516 | 2198 | 1 |
| 6 | 53133 53296 53378 54166 54236 54541 54711 56146 | s47651 a1258 s47663 a0518 a1469 a0532 a0539 a0565 | 300921 | 6ba9f4cd4902fd17abba72fc6b0bebdc16b897a261aa051a719a8d71c56bea2f | 2198 | 1 |
| 7 | 56227 57001 57248 61076 61111 62091 62101 62131 | s47605 a1071 s47631 a0589 s47750 a1062 a1471 a0606 | 300886 | 07d2ad956d2e5eb6e921b37a0e50da87855db995f9b643f25115d796a22bab16 | 2198 | 1 |
| 8 | 63383 63491 63496 63518 65042 65201 65276 66408 | s47769 a0624 a0625 s47770 s47777 a1485 a0649 s47768 | 299795 | 49662a35711e135d169a13ffa3c67614a3a7cf190c607144fa728aac220d3e2d | 2198 | 1 |
| 9 | 66421 66446 66481 66501 67401 67437 67461 67496 | a0668 a0669 a0919 a0670 s47767 s47765 a0686 a0688 | 293680 | dbc6d6ccb7b1f2f0f788ec95a4a51ef772fbd1c3a9ec9256aaf470aff00368fb | 2198 | 1 |
| 10 | 67511 68376 68431 69006 69052 71106 71231 72111 | s47766 s47755 a1321 s47742 a1519 s47895 a1242 s47890 | 296449 | d66a515f37b399110d30f378955c106cd9e2fb3a541e7945b2a9429f054e51a7 | 2198 | 1 |
| 11 | 73076 73126 73141 73151 73168 73442 74188 74311 | a1077 a0958 a0734 a0735 a1521 s47892 a1476 a0756 | 299038 | 4b44acf274602c6649cb6ed6e452d947f6bbadc322a8a3dea1a3f454fd18bdea | 2198 | 2 |
| 12 | 74447 81321 81371 81386 81436 81481 82068 82182 | s47897 a0940 a0775 a0776 a0778 a0942 a1590 s47807 | 297150 | 312068c5a93ca6a219033b46721bc7450cc019264a8e950f7c4a2b15ce88bdd5 | 2198 | 1 |
| 13 | 83051 83216 83401 84072 84121 84183 84266 84496 | a0794 s47815 a0808 s47800 a1144 a0814 s47812 s47817 | 297971 | 11d752d9d0f32836272416f79079b5d5971d528e160a5b42aec53f4f2d0cf510 | 2198 | 1 |
| 14 | 84523 85033 85116 86141 86216 86271 86451 87181 | a0962 a1610 a1075 s47819 a1081 a0843 a0924 a0857 | 294867 | a8d9fa166a9dc51463d22d42b85b847ae37e1e93fb4485895aa43a3e44058445 | 2198 | 2 |
| 15 | 87412 87492 88166 88317 88406 88432 88612 88821 | a1481 s47835 a0881 s47827 a0936 a0890 s47837 a1520 | 298758 | 17f7f97d04bdf4baa8aaefe77b450bf89c3cc8ec035102f4ae761c4d4fb2f7ca | 2198 | 1 |
| 16 | 91107 91166 91197 91241 93041 94081 | s47940 a1596 s47936 a0909 s47927 s47918 | 230615 | cb3e512b7ce3ad3f3394d558625016e2edda9d27f57e61aec3d01ab1fc41aba8 | 2198 | 1 |

## D. Quality / homogeneity

- stations requested: **126**
- stations with >1 homogeneity number during 2019–2024: **0**
- stations surviving homogeneity rule: **126**

## E. 90% monthly completeness

- eligible station-month keys: **8950**
- station-month failures: **122**

## F. Frozen eligible panel-key manifest

- panel-key rows: **10165**
- unique ports: **143**
- unique JMA history stations: **126**
- unique year-months: **72**
- panel-key file SHA-256: **7831034401647ef1602ea8db6f6445206df4b3954ef3bae010dd8e2cd3587486**
- file: research/JP-PORT-E01/STAGE_A_PANEL_KEYS.csv

## Raw cache handoff

The exact raw CSV bytes used for Stage A remain only in the current workflow runner under /tmp and are not committed to the repository. Stage B is not executed by this workflow; a future Stage-B run must explicitly re-pin its own raw inputs or use an approved artifact handoff.

## Stage B authorization

Stage A PASS. Stage B may compute only the preregistered monthly maximum wind, MLIT log1p cargo outcome, fixed-effects model and frozen gate.

Incremental monetary cost remained **0 USD**.
