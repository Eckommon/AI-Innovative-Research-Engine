---
id: CA-RAIL-E01-RESULT
type: preregistered-experiment-result
created: 2026-09-04
issue: 84
state: COMPLETED_HOLD
final_gate: HOLD_CA_RAIL_E01_WEATHER_SOURCE_INTEGRITY
stage_a_gate: HOLD_CA_RAIL_E01_WEATHER_SOURCE_INTEGRITY
stage_b_executed: false
rail_dwell_relationship_computed: false
incremental_monetary_cost_usd: 0
---

# CA-RAIL-E01 Result — Stage A Weather-Source HOLD
# CA-RAIL-E01 결과 — Stage A 기상 source HOLD

## Final gate / 최종 판정

**HOLD_CA_RAIL_E01_WEATHER_SOURCE_INTEGRITY**

The preregistered Stage A source/completeness gate failed before any rail dwell magnitude was opened for association analysis.

Stage B was therefore not authorized and no extreme-cold/dwell coefficient was calculated.

## Frozen experiment that was tested / 검증한 고정 실험

Primary weather variable:
**ECCC daily Minimum Temperature (°C)** only.

Weekly exposure candidate:
minimum daily Min Temp over the Monday–Sunday rail reporting week.

Completeness:
**7/7 valid daily Min Temp values required**.

Frozen parent universe:
- 14 ECCC stations;
- 105 reporting weeks;
- 1,470 possible station-weeks;
- 19 carrier-terminal series / maximum 1,995 rail panel keys.

## Source identity / source 식별

All 14 frozen ECCC Climate IDs resolved deterministically to one official Station ID from the F01-pinned station inventory.

The exact station-inventory snapshot matched the F01 hash:

`72751e152ba3206f74bbff6eac689ea209d93cab7b26428519088f72bbf38a1c`

Stage A downloaded and hash-pinned exactly 28 official ECCC daily CSV responses:
14 stations × calendar years 2024 and 2025.

No alternate weather variable was requested.

## Frozen time boundary / 고정 시간 경계

The final rail reporting week begins 2025-12-29 and extends through 2026-01-04.

The preregistration authorized only calendar-year 2024–2025 weather acquisition.

Therefore that final reporting week is structurally ineligible at every station and 2026 weather was not opened to rescue it.

## Preregistered completeness result / 사전등록 완전성 결과

Possible station-weeks: **1,470**

Eligible 7/7 station-weeks: **1,143**

Eligible share: **77.755102%**

Frozen Stage-A requirement: **>=90% overall**

Per-station requirement: **>=90 qualified weeks**

This requirement was not met.

### Qualified weeks by station

| Climate ID | City | Qualified weeks / 105 |
|---|---|---:|
| 1066488 | Prince Rupert | **0** |
| 1096454 | Prince George | **86** |
| 110Q44V | Vancouver | 103 |
| 1163842 | Kamloops | 90 |
| 3012209 | Edmonton | 97 |
| 3025484 | Red Deer | 93 |
| 3031094 | Calgary | 97 |
| 3033892 | Lethbridge | **0** |
| 4015322 | Moose Jaw | 95 |
| 4057152 | Saskatoon | 100 |
| 5023262 | Winnipeg | 97 |
| 6127510 | Sarnia | 92 |
| 6158355 | Toronto | 98 |
| 7024745 | Montreal | 95 |

The two zero-support stations had full daily date rows but **zero numeric Min Temp values** in both 2024 and 2025 official daily files under the frozen station identities.

Prince George also failed the frozen per-station >=90-week floor.

## Why the branch stops / 왜 여기서 중단하는가

The preregistration explicitly prohibited:
- changing to snow, precipitation, wind, gust, mean temperature or another weather variable;
- remapping a terminal to another station;
- relaxing 7/7 completeness;
- dropping weak-support stations after opening weather data;
- changing the terminal universe to rescue the result.

Therefore the scientifically valid action is **HOLD**, not redesign inside E01.

A different weather variable, station rule or terminal subset would constitute a new hypothesis and must compete again at Stage 0.

## What this HOLD means / HOLD 의미

This HOLD does **not** mean:
- extreme cold is unrelated to rail dwell;
- weather is irrelevant to Canadian rail operations;
- another ECCC variable would fail.

It means only:

**the exact preregistered Minimum-Temperature × frozen-station experiment does not have sufficient source completeness to proceed under its own precommitted integrity rules.**

## Durable evidence / 영속 증거

- `research/CA-RAIL-E01/README.md`
- `research/CA-RAIL-E01/STAGE_A_TIME_BOUNDARY.md`
- `research/CA-RAIL-E01/STAGE_A_SOURCE_MANIFEST.md`
- `research/CA-RAIL-E01/STAGE_A_STATION_WEEK_ELIGIBILITY.csv`

No Transport Canada dwell magnitude was opened for the association and no Stage-B relationship statistic was calculated.

Incremental monetary cost remained **0 USD**.
