---
id: US-GRID-F01-RESULT
type: source-semantic-join-feasibility-result
created: 2026-09-04
issue: 77
state: COMPLETED_PASS
final_gate: PASS_US_GRID_QUEUE_BA_JOIN_READY
relationship_outcome_computed: false
eia_operating_values_opened: false
incremental_monetary_cost_usd: 0
---

# US-GRID-F01 Result — LBNL Queued Up × EIA-930 BA Join Feasibility
# US-GRID-F01 결과 — LBNL Queued Up × EIA-930 BA 조인 실행가능성

## Final gate / 최종 판정

**`PASS_US_GRID_QUEUE_BA_JOIN_READY`**

## Korean summary / 한국어 요약

LBNL Queued Up 2026의 project-level queue data와 EIA-930 balancing-authority operating-data bulk family를 결과 비사용 상태에서 검증했다.

전체 57개 LBNL `entity`를 EIA BA에 억지로 귀속하지 않고, exact identity / 공식 ISO alias / source-defined legal-name alias / 명시적 BA 운영관계만 허용하는 prospective rule을 적용했다.

최종적으로:
- **41/57 entity**가 deterministic BA mapping을 통과;
- **16/57 entity**는 many-to-many 또는 근거부족으로 사전 제외;
- 2019–2025 queue-entry rows **17,453 / 19,794 = 88.173184%**가 qualified subset에 남음;
- source-defined completed-project 조건을 적용하면 **447 unique projects / 11 EIA BAs**가 prospective IR→COD cohort를 구성;
- 이 cohort에는 duplicate `entity+q_id` 또는 semantic conflict가 **0건**;
- EIA EBA bulk bytes도 SHA-256으로 고정됨.

따라서 결과를 본 뒤 operator를 고르거나 지리적으로 BA를 추정하지 않고도, 후속 controlled experiment를 사전등록할 수 있는 deterministic cross-source unit이 존재한다.

## PASS basis / PASS 근거

### 1. LBNL source reproducibly frozen
- exact workbook URL and SHA-256 pinned;
- project sheet and codebook identified;
- `entity`, `q_id`, `q_status`, `q_date`, `on_date`, `wd_date`, `ia_date` semantics verified.

### 2. Direct queue bottleneck outcome frozen
Future primary outcome:
**IR→COD elapsed duration**, using source-defined `q_date` and `on_date`.

No duration result was computed in F01.

### 3. EIA-930 source reproducibly frozen
- keyless public EBA bulk route exists;
- EIA BA taxonomy frozen with official code/name evidence;
- current EBA ZIP pinned:
  `3b80081e3720e0075ca151bd81308cd548b076a436c9136baf8656b507a50bb1`.

No EBA numerical operating value was parsed for relationship analysis.

### 4. Deterministic prospective identity subset exists
Qualified:
**41 entities**.

Excluded:
**16 entities**.

Important exclusions include:
- `Duke` — one LBNL entity spans multiple EIA BA codes;
- `PacifiCorp` — EIA separates `PACE` and `PACW`;
- `WAPA-SN` — official WAPA material does not support one BA for the whole entity;
- other non-BA utilities/identities where assigning an EIA BA would require geography or service-territory inference.

### 5. Bounded common cohort exists
Frozen queue-entry window:
**2019-01-01 through 2025-12-31**.

Prospective completed-project cohort:
- qualified entity;
- operational status;
- explicit q_date/on_date;
- valid chronological order;
- on_date by 2025-12-31.

Structural cardinality:
**447 unique project keys across 11 EIA BAs**.

### 6. Integrity rules are fail-closed
- composite project key = `entity+q_id`;
- no preferred-row selection for conflicts;
- no synthetic duration for censored projects;
- no post-outcome alias restoration;
- no EIA metric selection before descendant preregistration.

## Scientific boundary / 과학적 경계

This PASS establishes **join and experiment readiness only**.

It does not establish:
- that higher EIA operating stress causes longer queue duration;
- that any BA/operator has longer queue times;
- that operating stress and interconnection delay are correlated;
- transmission-capacity causality;
- policy or investment superiority.

The 447-project cardinality is structural only; F01 did not calculate IR→COD duration values.

## Durable evidence / 영속 증거

- `research/US-GRID-F01/README.md`
- `research/US-GRID-F01/SOURCE_PREFLIGHT.md`
- `research/US-GRID-F01/IDENTITY_ADJUDICATION.md`
- `research/US-GRID-F01/STRUCTURAL_DIAGNOSTIC.md`
- `research/US-GRID-F01/COHORT_DIAGNOSTIC.md`
- `research/US-GRID-F01/ALIAS_ADJUDICATION.md`
- `research/US-GRID-F01/FINAL_SUPPORT_PREFLIGHT.md`
- `research/US-GRID-F01/EXECUTION_CONTRACT.md`

## Next authorization boundary / 다음 승인 경계

F01 authorizes only an **outcome-blind preregistration** of a bounded `US-GRID-E01` cross-source experiment.

The descendant must select the EIA-930 predictor, time window and statistic before opening EIA values or computing queue durations. If no scientifically defensible predictor can be frozen prospectively, return to Stage 0 rather than searching multiple EIA metrics for a significant result.

Incremental monetary cost remained **0 USD**.
