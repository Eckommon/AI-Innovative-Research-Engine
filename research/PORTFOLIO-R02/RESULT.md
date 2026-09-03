---
id: PORTFOLIO-R02-RESULT
type: portfolio-selection-result
created: 2026-09-03
issue: 71
state: COMPLETED_SELECTION
selected_candidate: C-US-002
selected_next_gate: US-PORT-F01
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R02 Result — Post-UK-Grid Mission-ROI Reselection
# PORTFOLIO-R02 결과 — UK Grid 이후 Mission-ROI 재선정

## Mission anchor / 목적 고정

**KO:** 본 재선정은 특정 branch 완주가 아니라, 공공·연구 데이터의 관계에서 새롭고 반증 가능하며 재현 가능하고 실용적인 혁신 기회 또는 구조적 병목을 발견·검증하는 `MEM-054` 목적을 최우선으로 적용한다.

**EN:** This reselection optimizes for `MEM-054`: discovering and testing new, falsifiable, reproducible, practically useful innovation opportunities or structural bottlenecks from relationships among public/research data, rather than finishing a particular branch.

## Trigger / 재선정 계기

`UK-GRID-E01` ended as `HOLD_E01_SOURCE_CARDINALITY`. Its frozen SCOTEX window contained 122 dates but 5,846 day-ahead structural rows rather than the preregistered 5,856; Stage B did not execute and no selected observation-level Flow/Limit/Cost values were opened. `DEC-101` forbids same-branch rescue without a new Stage 0 justification.

## Candidate review / 후보 재검토

| Candidate / 후보 | Mission value / 미션 가치 | Direct observable bottleneck/outcome / 직접 관측 병목·결과 | Access / 실행 접근성 | Current disposition / 현재 판단 |
|---|---|---|---|---|
| **`C-US-002` U.S. Port Weakest-Link Intelligence** | **HIGH** — logistics bottleneck, cross-agency operational relationship | **Strong:** BTS vessel berthing/dwell time and call counts; weather shock exposure can be joined separately | **Good:** current BTS public port-performance surfaces + NOAA public bulk Storm Events; no paid service required | **SELECT** |
| `C-US-003` Critical Mineral Resilience | HIGH — strategic supply-chain concentration/recycling leverage | Moderate/strong, but first join requires commodity/HTS concordance and resilience-index semantics | Good via USGS public MCS/data release and Census public bulk trade products; API itself now requires a key | `HOLD_READY_SECONDARY` |
| `C-EU-001` Cross-National Grid Stress | VERY HIGH cross-national value | Strong potential congestion/outage/resilience outcomes | Weaker near-term route: ENTSO-E automated access/token handling plus bidding-zone ↔ administrative/industrial mapping | `HOLD_READY_SECONDARY` |
| `C-JP-001` Japan Port Weather–Throughput Stress | HIGH cross-source national logistics value | MLIT/e-Stat port arrivals/cargo/container outcomes are official but primarily monthly aggregate | Public official files; JMA weather available, but monthly outcome reduces operational resolution | `HOLD_READY_SECONDARY` |
| `C-SG-001` Singapore Maritime Activity × Weather Regime | Moderate/high maritime value | MPA vessel-arrival/tonnage outcome is monthly aggregate; weather is much finer | Public data.gov.sg API/CSV, no key needed at normal public access | `HOLD_READY_SECONDARY` |
| `C-KR-003` Korea Port Weakest-Link | HIGH and event-level semantics | Strong in principle | `KR-PORT-F01` remained PARTIAL because record-level sample validation requires unavailable authenticated access in the current execution environment | `HOLD_ACCESS` |
| `C-EU-004` / `EU-ISR-F01` facility × climate asset | Strong reusable join asset | Facility point × daily climate join is PASS, but a sufficiently direct, low-confounder operational outcome has not yet been qualified | Good | `HOLD_ASSET_READY` |
| `C-UK-001` UK Grid Constraint Regime | Strong validated source semantics | Strong | Exact E01 route is structurally HOLD; automatic repair/substitution is prohibited | `HOLD_BRANCH` |
| AMBENCH P01/F46 | Preserved scientific history | Exact route dependency only | Repeated source/runtime/tooling burden | `DORMANT` |

## Current official-source refresh / 현재 공식 source 재확인

The portfolio decision rechecked official public surfaces on 2026-09-03 before selection:

- U.S. BTS Port Performance Freight Statistics Program continues to publish nationally consistent port capacity/throughput measures and identifies vessel berthing statistics as operational performance data: `https://www.bts.gov/ports`.
- BTS technical documentation defines vessel dwell/berthing time using AIS-derived vessel calls within port terminal geofences and describes dwell time as informative about port capacity and throughput: `https://www.bts.gov/PPFS-Tech-Docs`.
- BTS Data Inventory continues to expose the Vessel Berthing Times public surface: `https://data.bts.gov/stories/s/Vessel-Berthing-Times/4kd6-2t87/`.
- NOAA/NCEI Storm Events continues to expose public bulk CSV files and format documentation: `https://www.ncei.noaa.gov/pub/data/swdi/stormevents/csvfiles/`.
- U.S. Census 2026 merchandise-trade bulk products are now public at no cost, supporting future critical-mineral work without requiring the Census API route: `https://www.census.gov/foreign-trade/data/dataproducts.html`.
- Japan MLIT/e-Stat port statistics remain current but mainly monthly/port-aggregate for the screened route; Singapore MPA vessel-arrival series remains monthly.

## Selection / 선정

### **`SELECT_C_US_002_PORT_WEAKEST_LINK`**

`C-US-002` is selected because it currently offers the best combination of:

1. **direct operational bottleneck semantics** — actual vessel time at berth/dwell rather than a purely constructed proxy;
2. **cross-agency relationship value** — BTS/USCG/USACE-derived port-performance evidence can be related to NOAA weather-event evidence;
3. **falsifiability** — weather-exposed port-weeks can later be compared with non-exposed/baseline port-weeks using a prospectively defined design;
4. **practical utility** — port dwell is directly relevant to capacity, throughput, schedules and supply-chain costs;
5. **low immediate tooling burden** — public official sources, no paid API, no large model required for the next gate;
6. **portfolio independence** — it does not rescue UK-GRID, KR-PORT credential access, or AMBENCH P01.

This selection does **not** claim that weather causes longer vessel dwell. That relationship remains untested.

## Exact next bounded gate / 정확한 다음 제한 gate

### `US-PORT-F01 — BTS Berthing × NOAA Weather Join Feasibility`

The next gate is **source-semantic and join feasibility only**, not a numerical effect test.

Before opening any outcome-comparison experiment, qualify:

1. a stable official BTS row-level/tabular export or API surface for vessel berthing/dwell statistics;
2. exact BTS temporal grain, port identity fields, vessel-type fields, dwell/berthing metric fields, and call-count/support fields;
3. an official geographic anchor for the selected ports sufficient for an outcome-blind weather exposure mapping;
4. NOAA Storm Events temporal and geographic fields that can be deterministically mapped to the BTS port/week grain;
5. at least one non-credential, bounded overlap interval with sufficient port-week support;
6. duplicate/revision semantics and snapshot/hash requirements;
7. no outcome-effect statistic and no weather→dwell claim in F01.

### F01 stop rule / F01 중단 규칙

If BTS row-level/tabular export cannot be obtained through a stable public official route, or port geography/weather exposure cannot be defined without arbitrary manual interpretation, finalize F01 as HOLD/PARTIAL and return to Stage 0. Do **not** open a tooling descendant merely to scrape a dashboard.

## Held alternatives / 보류 후보

- `C-US-003` remains the strongest secondary strategic-supply-chain candidate. Its next useful gate would be official USGS-mineral ↔ Census-HTS commodity concordance feasibility, not an immediately fabricated resilience score.
- `C-EU-001` remains a high-value cross-national target but is deferred until a low-friction official route or token-authorized environment is justified by Mission-ROI.
- `C-JP-001` and `C-SG-001` remain viable, but monthly outcomes currently provide weaker operational resolution than BTS berthing data.
- UK-GRID E01 is preserved as HOLD and receives no automatic repair.

## Cost / 비용

Incremental monetary cost remained **0 USD**. No paid API, paid runner, commercial data, or billable service is authorized by this selection.
