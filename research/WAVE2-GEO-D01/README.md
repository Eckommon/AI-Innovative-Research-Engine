---
id: WAVE2-GEO-D01
type: geographic-relationship-discovery
state: COMPLETED
created: 2026-09-03
mission_anchor: MEM-054
predecessor: EU-ISR-F01
incremental_monetary_cost_usd: 0
---

# WAVE2-GEO-D01 — Japan / UK / Singapore Relationship Candidate Discovery
# WAVE2-GEO-D01 — 일본 / 영국 / 싱가포르 데이터 관계 후보 탐색

## Purpose / 목적

Expand the candidate surface after Wave 1 without accumulating a broad catalogue for its own sake. Screen only official public-data combinations that can support a falsifiable bottleneck or decision question with a low-cost next feasibility gate.

Wave 1 이후 후보면을 확장하되 데이터 목록 자체를 늘리지 않는다. 공식 공공데이터 조합 중 반증 가능한 병목·의사결정 질문과 저비용 후속 feasibility gate를 만들 수 있는 후보만 선별한다.

## Fixed Mission-ROI dimensions / 고정 목적-ROI 기준

- cross-dataset / cross-agency relationship value;
- directness of bottleneck outcome;
- temporal/spatial join semantics;
- source accessibility without credential-provisioning work;
- falsifiability and practical utility;
- expected next-gate information gain;
- zero-cost feasibility;
- infrastructure-recursion risk.

No large downloads or predictive models are part of D01.

## Country findings / 국가별 결과

### United Kingdom / 영국 — Rank 1

Official NESO public CKAN surfaces provide:
- daily `Constraint Breakdown` with separate inertia, voltage and thermal constraint costs and volumes;
- half-hourly `Historic Demand Data` with national/transmission demand, embedded wind/solar generation, Scottish transfer and multiple interconnector flows;
- CKAN Data API and CSV access under NESO Open Data Licence.

The constraint outcome is unusually direct: NESO defines thermal constraint actions as actions taken when the energy that would naturally flow between regions exceeds the capacity of connecting circuits. This is an observed operational bottleneck outcome rather than an inferred stress proxy.

Relationship candidate:
**`C-UK-001 — GB Grid Constraint Regime Intelligence`**

Candidate relationship:
`half-hourly demand + embedded wind/solar + transfers/interconnectors → daily thermal/inertia/voltage constraint cost/volume regime`.

Key advantage: outcome and system-state sources share authoritative publisher/time semantics and are accessible through public CKAN without account/token provisioning.

### Japan / 일본 — Rank 2

Official JMA developer portal states that user registration is not required and provides AMeDAS observation data as machine-readable CSV. Historical observations can be downloaded by station/variable/period with quality and homogeneity flags.

MLIT/e-Stat Port Survey is Japan's core port statistics survey and publishes monthly port tables for vessel arrivals, maritime cargo and container counts; current 2026 port-level aggregates are published as Excel files.

Relationship candidate:
**`C-JP-001 — Port Weather–Throughput Stress`**

Candidate relationship:
`port-level monthly vessel/cargo/container activity + JMA weather exposure`.

Main limitation: operational outcome resolution is monthly/aggregate rather than event-level, and Japan's grid-data route is more decentralized across OCCTO/regional operators than the UK NESO route.

### Singapore / 싱가포르 — Rank 3

Official data.gov.sg provides MPA vessel-arrival datasets with long monthly history and public OpenAPI examples; base public access is available without an API key, while a key increases rate limits/support.

NEA/data.gov.sg provides station-level real-time rainfall, air temperature and wind speed with minute-level readings and 5-minute updates, also under the Open Data Licence.

Relationship candidate:
**`C-SG-001 — Maritime Activity × Weather Regime`**

Candidate relationship:
`monthly vessel arrivals/tonnage by type + aggregated station weather`.

Main limitation: MPA public outcome in the screened route is monthly aggregate, substantially coarser than the weather layer and weaker for identifying short disruption/recovery episodes.

## Ranking / 순위

1. **`C-UK-001 GB Grid Constraint Regime Intelligence` — SELECT**
2. `C-JP-001 Port Weather–Throughput Stress` — HOLD_READY_SECONDARY
3. `C-SG-001 Maritime Activity × Weather Regime` — HOLD_READY_SECONDARY

## Selection rationale / 선정 근거

C-UK-001 wins because it combines:
- a direct physical/operational bottleneck outcome;
- fine-grained system-state inputs;
- deterministic date/settlement-period semantics;
- no credential-provisioning dependency;
- low data/compute burden for a schema/alignment gate;
- strong practical relevance to renewable integration, transmission capacity and system operations.

This selection is based on source semantics and access structure, not observed model performance.

## Exact next action / 정확한 다음 행동

Open one feasibility gate:

**`UK-GRID-F01 — NESO Constraint × Demand/Renewables Alignment Feasibility`**

F01 must verify source identity, date overlap, aggregation semantics, type consistency, retrospective-correction rules and independent-unit definition before any association/model.

No weather source is required in F01; weather may be considered later only if a distinct incremental scientific question justifies it.

## Cost / 비용

Incremental monetary cost remained **0 USD**.
