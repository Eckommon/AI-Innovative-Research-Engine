---
id: CA-RAIL-E01-STAGE-A-SOURCE-MANIFEST
type: preregistered-weather-source-integrity-result
created: 2026-09-04
stage_a_gate: HOLD_CA_RAIL_E01_WEATHER_SOURCE_INTEGRITY
rail_dwell_relationship_computed: false
rail_dwell_magnitudes_opened: false
primary_weather_variable_opened: true
alternate_weather_variables_opened: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-E01 Stage A Source / Completeness Manifest

## Stage A gate: **HOLD_CA_RAIL_E01_WEATHER_SOURCE_INTEGRITY**

Stage A opened only the preregistered ECCC daily Minimum Temperature field and its flag for source/completeness qualification. No Transport Canada dwell magnitude was parsed for association analysis, and no weather-dwell statistic was computed.

## A. Frozen parent identity

- F01 support-key SHA-256: 454bce3a77510cedbe4ff0f81cdc561500ec40462396e63f6f36ef8ebaf361e7
- frozen reporting weeks: **105**
- frozen ECCC Climate IDs: **14**
- weather acquisition calendar years: **2024 and 2025 only**
- final 2025-12-29 reporting week is structurally ineligible because it extends into 2026, which is outside the preregistered acquisition window.

## B. Frozen ECCC station inventory

- URL: https://collaboration.cmc.ec.gc.ca/cmc/climate/Get_More_Data_Plus_de_donnees/Station%20Inventory%20EN.csv
- bytes: **1309532**
- SHA-256: 72751e152ba3206f74bbff6eac689ea209d93cab7b26428519088f72bbf38a1c
- encoding: utf-8-sig
- Stage-A extraction timestamp UTC: 2026-09-04T14:08:55+00:00

| Climate ID | Station ID | City | Inventory station | DLY first | DLY last |
|---|---:|---|---|---:|---:|
| 1066488 | 424 | Prince Rupert | PRINCE RUPERT MONT CIRC | 1959 | 2026 |
| 1096454 | 50169 | Prince George | PRINCE GEORGE MASSEY AUTO | 2018 | 2026 |
| 110Q44V | 55438 | Vancouver | VANCOUVER HARBOUR | 2023 | 2026 |
| 1163842 | 42203 | Kamloops | KAMLOOPS AUT | 2006 | 2026 |
| 3012209 | 27214 | Edmonton | EDMONTON BLATCHFORD | 1996 | 2026 |
| 3025484 | 55018 | Red Deer | RED DEER REGIONAL A | 2020 | 2026 |
| 3031094 | 27211 | Calgary | CALGARY INT'L CS | 1999 | 2026 |
| 3033892 | 46867 | Lethbridge | LETHBRIDGE CDA 2 | 2004 | 2026 |
| 4015322 | 27476 | Moose Jaw | MOOSE JAW CS | 1998 | 2026 |
| 4057152 | 50091 | Saskatoon | SASKATOON INTL A | 2018 | 2026 |
| 5023262 | 28051 | Winnipeg | WINNIPEG THE FORKS | 1999 | 2026 |
| 6127510 | 48373 | Sarnia | SARNIA | 2009 | 2026 |
| 6158355 | 31688 | Toronto | TORONTO CITY | 2002 | 2026 |
| 7024745 | 10761 | Montreal | MCTAVISH | 1994 | 2026 |

## C. Raw ECCC daily-response manifest

Only 2024 and 2025 daily files were requested. Hashes below identify the exact Stage-A weather snapshot.

| Climate ID | Station ID | Year | Bytes | SHA-256 | Parsed date rows | Numeric Min Temp | Min Temp flag counts |
|---|---:|---:|---:|---|---:|---:|---|
| 1066488 | 424 | 2024 | 58975 | 77f8cfbd3700c7e51a8b5042698e1e114fb55d4a059c01734aa6ca6a1df1a9df | 366 | 0 | {} |
| 1066488 | 424 | 2025 | 57845 | f4c4633ac70173fd84f04e18dbd66ecc70e4f98adbebfffc691ca7d425ca2d5e | 365 | 0 | {} |
| 1096454 | 50169 | 2024 | 65820 | f9b66f72dedae7231207f6dcc3ebf3e58c3af63c3a95b89b8af01894b115b3d3 | 366 | 357 | {'M': 9} |
| 1096454 | 50169 | 2025 | 65272 | 0f1c748cbfe24b2a82726a457065c5f2a8794d7e076b83e97b8020b7a0651591 | 365 | 339 | {'M': 20} |
| 110Q44V | 55438 | 2024 | 62241 | 80956c839909f65696b350a9d3fd52c5ce8916c3bc616c4d8da9faac6a06dcc2 | 366 | 366 | {} |
| 110Q44V | 55438 | 2025 | 62065 | bb6fc22169d85061e242ec6f47d1ac8fb1a68e2a702b8e9e480c2482b2b676c8 | 365 | 364 | {'M': 1} |
| 1163842 | 42203 | 2024 | 61044 | 1842e85ccd9fef3964dfce2c7933c17da81be99b8cd39f552c3962fb70ec8f85 | 366 | 357 | {'M': 9} |
| 1163842 | 42203 | 2025 | 61060 | 8aa1ab176631f0b3c1b83b0ef6396e20c43e908cb85684bc41d534ab9dc132f6 | 365 | 355 | {'M': 10} |
| 3012209 | 27214 | 2024 | 63816 | 44118cbe9e43c55a8c33dd4cc792aadd5107814bff67b8115d2aac68b71ef642 | 366 | 364 | {'M': 2} |
| 3012209 | 27214 | 2025 | 63704 | 11806c9c9bd2839a71071b547578afd3d6bdb20a9e048a5b71f85656a8b3871b | 365 | 358 | {'M': 7} |
| 3025484 | 55018 | 2024 | 64288 | b6b7e132c33af4824e5a099a866b572c169b7335859757e3c0c48f2bb070125a | 366 | 359 | {'M': 7} |
| 3025484 | 55018 | 2025 | 64091 | d0426cdfb2acd4b373f63715942e5ab203ee28c628a56c0826c77d33b755960d | 365 | 356 | {'M': 9} |
| 3031094 | 27211 | 2024 | 63184 | 3fc50c376495622e37a0920514b6fbc73c89fc95038344f288cc2d8237b8fde2 | 366 | 362 | {'M': 4} |
| 3031094 | 27211 | 2025 | 62974 | e69e13f90ba25ffa5f123080bbeb157eaaea1d7b5909d1e2315f3d79511259cd | 365 | 361 | {'M': 4} |
| 3033892 | 46867 | 2024 | 59190 | 58149e65a44e113f58e0c540e4ae58ac3aee896455446df4c2ae38a8dbd5fec9 | 366 | 0 | {} |
| 3033892 | 46867 | 2025 | 59037 | 9974e089bf4d258c85d2c79dd0e1ca82f8c89a89dba0231c1c0e1a61675ebcc8 | 365 | 0 | {} |
| 4015322 | 27476 | 2024 | 61868 | 5eadfcbbd9a3ff0009b4e1905d572e2e367549df429b688453ce3149ff444ebc | 366 | 365 | {'M': 1} |
| 4015322 | 27476 | 2025 | 61733 | 32ff56846805f47d8d0cd4f8877d693a5feecb762355381793415c7de8275204 | 365 | 355 | {'M': 10} |
| 4057152 | 50091 | 2024 | 63178 | cc6a67df285d08b08d57ac3704738125184bd8acac8011c3409590b162ad8a18 | 366 | 365 | {'M': 1} |
| 4057152 | 50091 | 2025 | 63039 | 50dda186388100dbba13fc47ea005d7cf1615fd194ded17af3e7af3fe7f69ac2 | 365 | 362 | {'M': 3} |
| 5023262 | 28051 | 2024 | 62953 | 422cc84e585d79aebae1d652cc12c67eed3198e02effe7cdabf108883189a766 | 366 | 364 | {'M': 2} |
| 5023262 | 28051 | 2025 | 62810 | a3cec46681f645bd7617a1b56c89da9ce7f208bf87d8c21cc13e3e20aeac1ff0 | 365 | 358 | {'M': 7} |
| 6127510 | 48373 | 2024 | 58705 | 8bdd525bde243b9b9c5d8e0d0556d2bd162c6b6ff9d7f21a02693f0603f9a423 | 366 | 340 | {'M': 26} |
| 6127510 | 48373 | 2025 | 58837 | edea793863622bf16eddedc00eb16d71c31709fd68dd3b380699fc83d507c382 | 365 | 353 | {'M': 12} |
| 6158355 | 31688 | 2024 | 60762 | 2c0c5a3395b2e10f91092ea5a3db5b56e8823a8b25803de1b342460861891a45 | 366 | 363 | {'M': 3} |
| 6158355 | 31688 | 2025 | 60744 | b5597a92cc067317511bf1d4471d8c5ce5b906b4ba1ae2caf9607a91d4c5df5d | 365 | 359 | {'M': 6} |
| 7024745 | 10761 | 2024 | 59251 | d73af2726fcaec4b5c973e245ceee7b009275c7b362434c466e94bb302cd2b6d | 366 | 364 | {'M': 2} |
| 7024745 | 10761 | 2025 | 59233 | 3eaa16964c64270e1d30c2ce3aee7a0369991ba89612c94a412588b13dd8e818 | 365 | 358 | {'M': 7} |

## D. Preregistered 7/7 station-week completeness

- possible station-weeks: **1470**
- eligible 7/7 station-weeks: **1143**
- eligible share: **77.755102%**
- required overall share: **>=90%**
- per-station minimum requirement: **>=90 qualified weeks**
- all stations satisfy per-station floor: **NO**

| Climate ID | City | Qualified weeks / 105 |
|---|---|---:|
| 1066488 | Prince Rupert | 0 |
| 1096454 | Prince George | 86 |
| 110Q44V | Vancouver | 103 |
| 1163842 | Kamloops | 90 |
| 3012209 | Edmonton | 97 |
| 3025484 | Red Deer | 93 |
| 3031094 | Calgary | 97 |
| 3033892 | Lethbridge | 0 |
| 4015322 | Moose Jaw | 95 |
| 4057152 | Saskatoon | 100 |
| 5023262 | Winnipeg | 97 |
| 6127510 | Sarnia | 92 |
| 6158355 | Toronto | 98 |
| 7024745 | Montreal | 95 |

## E. Eligibility manifest

- file: research/CA-RAIL-E01/STAGE_A_STATION_WEEK_ELIGIBILITY.csv
- SHA-256: 5e78e0672b2233e8cf5ca5608eb86ea9a58ea91af9082555a4bfe80e67c9d9ce
- fields contain station/week identity, valid-day count and eligibility only; no Min Temp magnitude is persisted.

## F. Stage-B authorization

Stage A HOLD. Stage B is not authorized and the weather variable, station universe or completeness rule may not be changed to rescue this E01.

Incremental monetary cost remained **0 USD**.
