---
checkpoint_id: CHK-20260905-US-AIR-F01-SOURCE-PREFLIGHT
active_issue: 88
active_research: US-AIR-F01
last_completed_issue: 87
last_completed_research: PORTFOLIO-R08
last_decision: DEC-120
updated: 2026-09-05
---

# Project Status / 프로젝트 상태

**Project / 프로젝트:** AI-Innovative-Research-Engine / AI 기반 혁신 탐색 연구 엔진  
**State / 상태:** `MISSION_ANCHOR_FIXED__US_AIR_F01_SOURCE_ROUTE_VERIFIED__MAPPING_CARDINALITY_PENDING`  
**Active Work Queue / 활성 작업 큐:** Issue #88 `US-AIR-F01 — BTS On-Time airport/flight identity × NOAA LCDv2 weather-station join feasibility`.

## Fixed Mission / 고정 목적

Discover and validate **new, falsifiable, reproducible and practically useful innovation opportunities or structural bottlenecks from relationships among public/research data**. `MEM-054` remains mandatory.

## Last completed research / 마지막 완료 연구

`PORTFOLIO-R08` completed as:

**`SELECT_C_US_004_AVIATION_WEATHER_DELAY_PROPAGATION`**

Selected next branch:

**C-US-004 — U.S. Aviation Weather–Delay Propagation Intelligence**.

Durable decision:
- `research/PORTFOLIO-R08/RESULT.md`
- `registry/DEC-120.md`
- `registry/CLM-133.md`

Issue #87 is completed/closed.

## Active US-AIR-F01 / 활성 US-AIR-F01

Issue #88 is active.

Frozen:
- period = calendar year 2025;
- primary future outcome family to qualify = BTS `DepDelayMinutes`;
- BTS `WeatherDelay` is not an eligible primary outcome;
- minimum structural PASS support = >=50 qualified origin airports and >=40 unique NOAA stations;
- flights sharing one station-time exposure are nested observations, not independent weather replications.

## Source preflight completed / source 사전검증 완료

Interim gate:

**`CONTINUE_US_AIR_F01_BYTE_AND_MAPPING_CARDINALITY`**

Verified without weather values or delay magnitudes:
- BTS current On-Time field/source semantics;
- all twelve 2025 Marketing Carrier monthly PREZIP files are present in the official directory;
- directory-listed total compressed size across those 12 files = 412,308,983 bytes;
- BTS Master Coordinate schema exposes AirportID/SeqID, latitude/longitude, UTC/local variation and time-valid airport attributes;
- NOAA LCDv2 is current, LCDv1 is deprecated, and LCDv2 provides station metadata plus bulk CSV;
- the official LCDv2 station list is live and includes airport-coincident U.S. station identities.

Durable preflight:
- `research/US-AIR-F01/SOURCE_PREFLIGHT.md`

## Not yet proven / 아직 미확정

Do not declare F01 PASS yet.

Pending:
1. materialize a bounded official BTS 2025 monthly ZIP and record byte hash/header;
2. reproduce the complete BTS Master Coordinate row payload;
3. construct actual 2025 origin AirportID/SeqID support;
4. freeze time-valid 2025 airport coordinates;
5. construct prospective airport→LCDv2 station map;
6. prove >=50 qualified airports and >=40 unique NOAA stations;
7. verify 2025 station-time support;
8. freeze DST/time-zone alignment and station-day/hour exposure keys.

No weather–delay association or effect estimate is authorized.

## Preserved AU-NEM boundary / 보존된 AU-NEM 경계

`AU-NEM-F01` remains:

**`PASS_AU_NEM_WEATHER_CONGESTION_JOIN_READY`**.

Do not automatically launch broad-region AU-NEM E01 because six interconnectors collapse to four broad region-pair weather exposures.

## Exact next action / 정확한 다음 행동

Continue Issue #88 with one bounded zero-cost source-execution step that emits only:
- source bytes/hashes;
- CSV headers/schema;
- airport/station identity and coordinate support;
- time-support diagnostics;
- prospective mapping cardinality.

Fail closed rather than rescue if public deterministic mapping or the frozen independent-unit minimum cannot be met.

Incremental monetary cost remains **0 USD**. Any potentially billable action requires explicit prior approval.
