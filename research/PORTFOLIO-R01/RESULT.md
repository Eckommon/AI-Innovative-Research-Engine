---
id: PORTFOLIO-R01-RESULT
type: portfolio-mission-roi-selection
state: COMPLETED
created: 2026-09-03
source_of_truth: github+current_official_metadata
incremental_monetary_cost_usd: 0
mission_anchor: MEM-054
branch_stop_control: DEC-093
---

# PORTFOLIO-R01 Result — Mission-Aligned Candidate Reselection
# PORTFOLIO-R01 결과 — 목적 정렬 후보 재선정

## 1. Decision frame / 판단 프레임

This reselection returns the engine from an over-deep AMBENCH descendant chain to the project mission:

> **Public/research data relationships → falsifiable hypotheses → controlled evidence → practically useful innovation/bottleneck discovery.**

Selection uses existing Wave 1 evidence first, then only minimal current official-source verification for the leading candidate. No large dataset, model, simulator, or F46 transport route was executed.

## 2. Ranked shortlist / 순위 후보

### Rank 1 — `C-KR-003 Port Weakest-Link Intelligence / 항만 최약고리 지능화` — **SELECT**

**Historical Combination IPS:** `95/100`.

Combination:
`PORT-MIS vessel/port-call timestamps + port-facility use + cargo/container + KMA weather`.

Mission-ROI strengths:
- directly targets a persistent operational bottleneck: vessel turnaround, berth/anchorage delay, congestion and disruption/recovery;
- event-level operational identifiers provide substantially finer resolution than aggregate port statistics;
- cross-dataset relationship is explicit rather than a single-dataset continuation;
- next uncertainty is scientific/semantic — whether a defensible port-call target and stable joins can be formed — rather than compute or transport engineering;
- immediate gate is metadata/schema/identity-first and low compute;
- high practical utility for port operations, logistics resilience, scheduling and congestion intelligence;
- no sunk-cost dependence on AMBENCH.

Minimal current official verification on 2026-09-03:
- Ministry of Oceans and Fisheries vessel-operation / vessel-entry data remain represented in the Public Data Portal with port, call sign, arrival count and arrival/departure time semantics;
- `항만시설사용정보` remains a free REST API, automatic approval, real-time, and explicitly queries by port authority code + arrival year + arrival count + call sign;
- its response includes the same identifiers plus berth/mooring-place code/name and entry/exit datetime;
- KMA ASOS hourly data remain a free REST JSON/XML API with time, station, temperature, precipitation, wind, humidity and related physical variables.

**Primary remaining uncertainty:** Can one deterministic `port_call_id` and one non-leaky operational turnaround/delay target be defined across the selected sources without ambiguous duplicate/correction semantics?

**Disposition:** `CONTINUE — SELECTED_PRIMARY`.

---

### Rank 2 — `C-EU-001 Cross-National Grid Stress Intelligence` — **HOLD_READY_SECONDARY**

Historical Combination IPS: `96/100`.

Strengths:
- strongest cross-national harmonization value;
- ENTSO-E + ERA5 + Eurostat can support multi-country stress/resilience relationships;
- strongly aligned with L3/L4 mission levels.

Why not first:
- current next gate must resolve ENTSO-E account/token access and bidding-zone/control-area ↔ NUTS semantics before a clean target is available;
- immediate mapping/access burden is higher than KR port-call identity/target qualification;
- port candidate offers faster scientific information gain at lower execution burden.

**Disposition:** `HOLD_READY_SECONDARY` — not rejected.

---

### Rank 3 — `C-EU-004 Industrial Site Climate Risk` — **HOLD_READY_SECONDARY**

Historical Combination IPS: `94/100`.

Strengths:
- direct facility-coordinate × physical-hazard relationship;
- EEA industrial sites + Copernicus/ERA5 creates strong cross-domain spatial stress-test potential;
- practical climate-resilience and industrial-risk utility.

Why not first:
- requires a fresh hazard/endpoint definition and spatial exposure contract;
- expected first-cycle information gain is good but lower than the already event-resolved Korean port route.

**Disposition:** `HOLD_READY_SECONDARY`.

---

### Rank 4 — `C-US-003 Critical Mineral Resilience` — **HOLD_READY_SECONDARY**

Historical Combination IPS: `92/100`.

Strengths:
- cross-agency/supply-chain mission fit;
- high practical value for import reliance, concentration and recycling leverage;
- domain diversification away from additive manufacturing.

Why not first:
- exact target/denominator/join design is less mature in current durable records than C-KR-003;
- would require broader fresh source discovery before a low-DOF experiment can be frozen.

**Disposition:** `HOLD_READY_SECONDARY`.

---

### Rank 5 — Wave 2 geographic discovery: Japan / UK / Singapore — **CONTINUE_AFTER_PRIMARY_GATE**

Strengths:
- high exploration value and directly advances L4 geographic expansion;
- reduces concentration on Wave 1/NIST domains.

Why not first:
- this is a discovery program, not yet one testable candidate;
- one low-cost scientific feasibility gate on the already strong C-KR-003 candidate has higher immediate information gain.

**Disposition:** `CONTINUE_AFTER_PRIMARY_GATE` — schedule portfolio return after the first KR-port feasibility result rather than allowing a long descendant chain.

---

### Rank 6 — Independent non-P01 test of `HYP-F37-01` thermal-history control — **HOLD_BRANCH_LEVEL**

Strengths:
- preserves a scientifically meaningful mechanism hypothesis from E29/E33/E36/F37.

Why not selected:
- additive-manufacturing branch has already accumulated substantial evidence and substantial queue share;
- F38 found only a narrow novelty gap with dense adjacent prior art;
- recent descendants moved into runtime/source infrastructure;
- current marginal mission value is below diversified cross-dataset candidates.

**Disposition:** `HOLD_BRANCH_LEVEL`. Reconsider only if a clean independent dataset appears with clearly superior Mission-ROI.

## 3. Existing branch dispositions / 기존 branch 처리

| Branch / Candidate | Disposition | Reason |
|---|---|---|
| AMBENCH P01 / E43-F46 route | **ARCHIVE_ROUTE / DORMANT** | >=2 infrastructure/source descendants without new scientific evidence; 18 MB archive is route-only dependency |
| F37 thermal-history mechanism | **PRESERVE / HOLD** | useful validated bounded mechanism hypothesis; no need to force immediate continuation |
| `C-US-004` registered manufacturing quality | **HOLD / NO SAME-REPRESENTATION ESCALATION** | already heavily explored via mds2-3761 E24/D25; same-representation escalation stopped |
| `C-KR-001` localized grid bottleneck | **HOLD_LOCALIZED / KEEP_SYSTEM_LEVEL_OPTION** | public bus-number asset/geographic mapping not established |
| `C-EU-002` industrial energy-emission efficiency | **HOLD_FACILITY_DENOMINATOR / KEEP_SECTOR_OPTION** | prior work established sector aggregate feasibility but generic facility production denominator gap |
| `C-KR-003` port weakest-link | **CONTINUE / PRIMARY** | high mission value, event-level joins, low immediate gate burden |

## 4. Mission-ROI check for the selected next gate / 선정 gate 목적-ROI

1. **Scientific vs tooling:** scientific/semantic. It asks whether a defensible operational target and event identity exist.
2. **Route uniqueness:** no single large file or proprietary route is required at this stage; multiple official metadata/API surfaces exist.
3. **Alternatives:** EU grid/site-climate and US critical-minerals remain credible, so branch continuation will be re-reviewed after one gate.
4. **Infrastructure streak:** reset to zero by leaving AMBENCH transport work.
5. **Stop-loss:** if the KR port identity/target gate fails, the candidate can be held with minimal sunk cost and portfolio selection resumes.

## 5. Exact next action / 정확한 다음 행동

Open a separately preregistered **`KR-PORT-F01 — Port-Call Identity & Turnaround-Target Feasibility Gate`**.

Before downloading a long history or training a model, verify only:
- current official source identities/access terms;
- exact candidate call-level identifiers across vessel-operation / vessel-entry and facility-use records;
- duplicate/correction/update semantics;
- whether arrival and departure timestamps support a deterministic nonnegative port-stay/turnaround target;
- whether berth/anchorage/facility-use categories can be attached without target leakage;
- whether weather can be joined prospectively by time + defensible station/port geography;
- sample-access feasibility under the free route;
- one frozen downstream target hierarchy if PASS.

No predictive model is authorized by PORTFOLIO-R01 itself.

## 6. Portfolio-return constraint / 포트폴리오 복귀 제약

Even if KR-PORT-F01 passes, do not allow an unlimited descendant chain. After the first controlled KR-port experiment or after any HOLD/REJECT, return to `MISSION-ROI` / Stage 0 and compare Wave 2 / EU / US alternatives again.

## 7. Cost / 비용

Incremental monetary cost: `0 USD`. No paid API, compute, storage, or data source used.
