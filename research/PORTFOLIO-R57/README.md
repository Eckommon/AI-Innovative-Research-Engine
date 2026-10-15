---
id: PORTFOLIO-R57
type: outcome-blind-parallel-stage0-contract
created: 2026-10-16
status: CONTRACT_FROZEN_PRE_ISSUE
reason: USER_APPROVED_TWO_TRACK_PARALLEL_EXECUTION_2026-10-16
independent_of: US-CMS-NPI-E01
candidate_future_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R57 — Parallel source-first reselection / 병렬 연구 후보 독립 재선정

## Mission and separation / 목적과 독립성

The user authorized parallel work while the locked `US-CMS-NPI-E01 / Issue #203` waits for its **first official future V2 weekly file**. This Stage 0 is **independent**, not an E01 rescue or outcome substitution. The canonical active checkpoint remains E01, while R57 is an explicitly separate screening Issue. No prospective candidate outcome memberships, event effect, entity ranking, or conditional association will be opened before an immutable selection.

**KO:** E01의 미래자료 대기 중에도 공공데이터 관계 탐색의 정보가치를 확보하기 위한 독립 사전등록 Stage-0입니다. E01의 출처·18개 게이트·346,859쌍·통계·checkpoint를 변경하지 않습니다.

## Frozen independent candidate universe / 사전 동결 후보군

**A. `US-FAA-AIR-003` — aircraft registry structure vs prospective source-native deregistration / FAA 항공기 구조 × 장래 등록말소**

- Unit prospect: **exact compound aircraft identity**, requiring aircraft serial number **and** official manufacturer/model code, with N-number treated as mutable registration label.
- Source: [FAA official daily full releasable aircraft bundle](https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download), which officially lists Master, Deregistered, make/model reference and engine reference files; source says refreshed daily at 11:30 pm Central.
- Exposure prospect: non-event structural manufacturer/model, engine category, manufacture age or non-outcome registration structure; forbid deregistration-related reason/status/date as exposures.
- Future event prospect: separately locked subsequent source-native deregistration event, conditional on proving true temporal aircraft identity.
- Blocking uncertainty: N-number reuse, serial collisions across manufacturers, model-code changes, loss of records and heterogeneous deregistration causes. **No automatic revival** of previous FAA-AIP (airport grants × delays), which is a different exact scientific route but had terminal 16/17 source-identity HOLD.

**B. `US-NHTSA-REC-002` — vehicle product attributes vs prospective recall / NHTSA 자동차 제품 구조 × 장래 리콜**

- Unit prospect: **source-verifiable product population** (make/model/model-year alone is **not presumed** a distinct engineering platform); no hypothetical VIN-denominator inference.
- Source: [NHTSA official datasets](https://www.nhtsa.gov/nhtsa-datasets-and-apis) offer downloadable full recall ZIPs, the `RCL.txt` schema dictionary and a campaign API; latest official portal independently documents daily updates.
- Exposure prospect: non-defect product type, independently documented platform/structural metadata **only if deterministic product identity linkage can be established**. Complaints/investigations/communications cannot be predictive features.
- Event prospect: source-native *future* new recall campaigns/affected product line, NOT a general failure frequency or a safety risk rate without population denominators.
- Blocking uncertainty: affected-product list many-to-many join, VIN/population denominator absent, campaign vs product temporal identity. F01 must fail closed rather than manufacture a platform bridge.

**C. `US-FDA-DEV-002` — registered device structure vs prospective recall / FDA 등록 의료기기 구조 × 장래 리콜**

- Unit prospect: exact **device listing/product code + establishment** only if official FDA identifier cardinality can be proved, otherwise **not selectable**.
- Official public sources to revalidate: [FDA openFDA device endpoints](https://open.fda.gov/apis/device/) and [FDA recall/enforcement API](https://open.fda.gov/apis/food/enforcement/) **(food endpoint not a device proxy; must independently locate and verify actual device enforcement path)**. No claim of joinability or updated datasets yet.
- Exposure prospect: source-native, non-adverse-event device class or listing metadata only.
- Blocking uncertainty: establishment-vs-product attribution, many-to-many mappings, recalls and adverse-event reporting semantics; prior R49 explicitly held FDA devices on source-join ambiguity. This is not an automatic rescue or selection.

## Frozen /45 selection criteria / /45 불변 선정 규칙

Score each candidate 0–5 **before any candidate's outcome distribution is opened**, with identical criteria:
1. public first-party machine-readable data accessibility, today;
2. exact, time-safe identity without fuzzy matching;
3. source-native prospective event with known date semantics;
4. structural exposure independent of event/near-event precursors;
5. denominator/observation opportunity and likely common support;
6. direct cross-table information gain;
7. mission-level innovation/bottleneck decision utility;
8. zero-cost deterministic runtime and reproducibility;
9. canonical novelty **after** terminal-branch-equivalence check.

Tie-break in order: (i) exact temporal identity, (ii) row access reliability, (iii) denominator, (iv) direct event, (v) novelty. A scorecard does **not** authorize a F01 if a fatal eligibility constraint persists. Select **at most one**, or **`HOLD_NO_ELIGIBLE_CANDIDATE`**.

## Hard exclusions / 금지

- No automatic resurrection of historical PHMSA F01 (two 403 transport failures), FCC ULS F01 (9/18 scientific HOLD), FRA (implementation block), old FAA-AIP (16/17 hold), or the active E01; even an identical label is not a scientific fix.
- No outcome data, effects, future event membership, ranking, causal claims, name/geo/fuzzy identity repair or post-score threshold tuning.
- No unaudited API limits, private/paid mirrors, paid GitHub compute, commercial data or unknown charges.
- No silent rewrite of the lone canonical active `US-CMS-NPI-E01` checkpoint.

## Ordered execution / 실행 순서

1. Freeze this candidate universe and /45 rubric in a distinct commit **before** creating the Stage-0 Issue. / Issue 전 사전 동결
2. Create **separate** R57 Stage-0 Issue, explicitly marked parallel and independent from active E01.
3. Official-source access, field/identity and prior terminal-equivalence revalidation, recording uncertainty rather than reading outcome counts.
4. Freeze one immutable /45 scorecard and select at most one F01 or HOLD. No runner-up rescue after observation.
5. If eligible: freeze a **new** outcome-blind F01 scientific contract in its own commit, then bind a separate F01 Issue. Gate against exact archival source/schema/identity with 0 USD.
6. Continue E01 six-hour first-source watch throughout; do not mutate E01 experiment authorization based on R57.

**Evidence class:** prospective `HYPOTHESIZED` candidates, not observed causal or empirical relationships.  
**Cost:** 0 USD.
