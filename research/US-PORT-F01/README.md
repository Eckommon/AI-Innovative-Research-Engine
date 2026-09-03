---
id: US-PORT-F01
type: source-semantic-join-feasibility
created: 2026-09-03
issue: 72
state: PREREGISTERED_ACTIVE
parent_candidate: C-US-002
incremental_monetary_cost_usd: 0
---

# US-PORT-F01 — BTS Berthing × NOAA Weather Join Feasibility
# US-PORT-F01 — BTS 선박 접안시간 × NOAA 기상 join 가능성

## Mission / 목적

Qualify whether current official U.S. public data can support a deterministic and reproducible **port-time vessel berthing/dwell × weather-event** relationship suitable for a later controlled bottleneck experiment.

본 gate는 공공데이터 간 관계를 검증 가능한 연구단위로 만들 수 있는지만 판정한다. **기상이 dwell time을 증가시킨다는 효과를 검정하거나 주장하지 않는다.**

Authorized by `PORTFOLIO-R02` and `DEC-102` under `MEM-054` / `DEC-093`.

## Outcome-blind/source exposure disclosure / 결과 비사용·source 노출 고지

Before this README was persisted, portfolio/source-refresh work had already exposed the following **source-semantic metadata only**:

- BTS Port Performance defines vessel dwell/berthing as an operational port-performance metric and relates it to capacity/throughput.
- Official Data.gov metadata exposed a public BTS dataset identifier `abu9-jbyq`, titled `Tanker/Liquid Bulk Vessel Dwell Times at the Top U.S. Ports January 2019 to June 2023`, with public CSV/JSON/XML distributions and metadata modified `2026-06-16`.
- No weather→dwell effect statistic was computed.
- No preregistered future effect window, port, weather threshold, or outcome direction was selected from observed dwell/weather values.

These metadata exposures are permanently disclosed and may not later be represented as newly outcome-blind discoveries.

## Frozen F01 questions / 고정 F01 질문

F01 may answer only:

1. **Stable BTS table:** Does at least one official BTS dwell/berthing dataset have a stable public tabular/API distribution without dashboard scraping?
2. **BTS semantics:** What are the exact time, port identity, vessel type, dwell/berthing metric and support/call-count fields?
3. **Port geography:** Can BTS port identity be anchored deterministically to an official geographic unit or coordinate source without manual arbitrary matching?
4. **NOAA semantics:** Do NOAA/NCEI Storm Events provide temporal and geographic fields that can be mapped prospectively to the BTS time/geography grain?
5. **Overlap:** Is there at least one bounded common coverage interval suitable for later analysis?
6. **Integrity:** Can source revisions/snapshots and payload/schema hashes be preserved reproducibly?

F01 shall not select a weather threshold by observed dwell response and shall not calculate a weather→dwell association.

## Preferred source route / 우선 source 경로

### BTS

Prefer machine-readable official BTS/Data.gov distributions over dashboards.

Known qualified metadata candidate before preregistration:
- dataset ID: `abu9-jbyq`;
- official catalog landing: `https://catalog.data.gov/dataset/tanker-liquid-bulk-vessel-dwell-times-at-the-top-u-s-ports-january-2019-to-june-2023`;
- publisher: Bureau of Transportation Statistics;
- access level: public;
- title coverage semantics: January 2019 through June 2023;
- official metadata advertises direct CSV/JSON/XML distributions.

F01 may discover a newer/better official BTS tabular dataset only if selection is based on source semantics/access and not on weather-effect performance.

### NOAA

Use official NOAA/NCEI Storm Events bulk distribution/documentation only:
`https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/`

No commercial weather source is authorized.

## Bounded empirical access / 제한된 empirical 접근

F01 may retrieve only what is required to validate schema, source identity, time/geography semantics and bounded overlap. It should avoid large historical downloads when metadata/header/sample access is sufficient.

If a small sample is required, selection must be deterministic from source ordering or a prospectively fixed source interval and must not be selected for a favorable dwell/weather relationship.

## Gate / 판정

### `PASS_US_PORT_BTS_NOAA_JOIN_READY`
Require all:
- stable official machine-readable BTS dwell/berthing table available without opaque dashboard scraping;
- exact time/port/dwell/support semantics identifiable;
- deterministic official port geographic anchor available;
- NOAA temporal/geographic exposure fields are compatible with a prospectively specified port-time mapping;
- at least one bounded common period exists;
- revision/snapshot/hash plan can be specified without paid services or arbitrary manual mapping.

### `PARTIAL_US_PORT_SOURCE_SEMANTICS_READY__JOIN_COMPONENT_PENDING`
Use only when core BTS and NOAA semantics are qualified but one bounded join component remains empirically unresolved without opening an effect test.

### `HOLD_US_PORT_PUBLIC_JOIN_ROUTE`
Use when stable official tabular access, deterministic geography, bounded overlap, or zero-cost source route cannot be established in the current environment.

### `REJECT_US_PORT_WEATHER_DWELL_FRAME`
Use when official source semantics demonstrate that the proposed port-time weather exposure relationship is invalid as framed.

## Branch-stop / branch 중단

If the needed data require opaque dashboard scraping/reverse engineering, credential-heavy work, arbitrary manual geography, or a tooling descendant, stop and return to Stage 0. Do not rescue F01 merely because a workaround exists.

## Future experiment boundary / 후속 실험 경계

A F01 PASS does **not** authorize a weather-effect test. Any later experiment must separately preregister:
- port(s) and vessel class;
- independent time unit;
- weather exposure definition;
- baseline/comparator;
- confounder controls;
- outcome metric and support thresholds;
- materiality/statistical gate;
- source snapshot/version hashes.

No such choices may be tuned from F01 outcome-effect observations because F01 is not permitted to calculate them.

## Cost / 비용

Incremental monetary cost must remain **0 USD**. No paid API, paid runner, commercial dataset, or billable external service is authorized.
