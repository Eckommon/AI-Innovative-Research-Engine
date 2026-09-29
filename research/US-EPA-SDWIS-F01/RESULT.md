---
id: US-EPA-SDWIS-F01-RESULT
type: structural-feasibility-result
created: 2026-09-30
issue: 182
research: US-EPA-SDWIS-F01
disposition: HOLD
attempt_01_commit: canonical-attempt-01
attempt_01_run: 36626153762
contract_commit: 5546edebea1c09f68eb98075b286b3f20bd69b46
gate: HOLD_US_EPA_SDWIS_F01_EXACT_PWSID_FUTURE_HEALTH_VIOLATION_DESIGN_NOT_READY
---

# US-EPA-SDWIS-F01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_EPA_SDWIS_F01_EXACT_PWSID_FUTURE_HEALTH_VIOLATION_DESIGN_NOT_READY`**

Attempt 01 is a valid national empirical execution of the frozen 18-gate contract and passes **15/18** requirements. Failed gates are **7, 9 and 13**. Because the pre-Issue rule requires exactly 18/18 PASS, this exact F01 is terminal scientific HOLD. No N01 or E01 is authorized.

Attempt 01은 고정된 18-gate 계약의 유효 national empirical 실행이며 **15/18**을 통과했습니다. 실패 gate는 **7, 9, 13**입니다. 사전계약이 18/18을 요구하므로 이 exact F01은 terminal scientific HOLD입니다.

## Baseline fingerprint / baseline 지문

Official EPA SDWA national ZIP:
- bytes: **423,774,232**
- last modified: **2026-07-09 19:39:37 GMT**
- SHA-256: `a18a20f9091c2e0466c91c83d0bac5651473441642331d09504e447a6e2ac7a4`
- maximum submission quarter: **2026Q2**
- later quarterly refresh opened: **false**
- future health-based membership opened: **false**

Required files were present:
- `SDWA_PUB_WATER_SYSTEMS.csv`
- `SDWA_FACILITIES.csv`
- `SDWA_VIOLATIONS_ENFORCEMENT.csv`
- `SDWA_REF_CODE_VALUES.csv`

Raw EPA bytes were transient only under RAW-001.

## Failed frozen gates / 실패 gate

### Gate 7 — exact PWSID syntax

- nonblank PWS rows: **434,040**
- exact-qualified PWSIDs under the frozen rule: **428,986**
- qualification rate: **98.8355912%**
- frozen threshold: **99.99%**

The contract may not be rescued by changing the exact PWSID grammar, padding/reconstructing IDs, substituting FRS/facility identifiers or using name/geography repair.

### Gate 9 — temporal lineage

The current national PWS table contains only **1 distinct SUBMISSIONYEARQUARTER: 2026Q2**, below the frozen minimum of **8** quarters.

This is independently decisive. The current ZIP is a latest-quarter national snapshot, not an eight-quarter history in the form prospectively required by this F01. After observing this result, the branch may not be rescued by adding an archive source, scraping prior quarterly files or redefining the temporal-lineage requirement.

### Gate 13 — violation identity/join support

Violation/enforcement rows: **15,432,737**

- nonblank violation PWSIDs: **15,432,737**
- exact-qualified under frozen PWSID grammar: **15,186,589**
- syntax rate: **98.4050269%**, below 99.90%
- distinct violation PWSIDs: **258,445**
- exact matched to current PWS table: **254,921**
- join rate: **98.6364604%**, below 99.00%

This is consistent with a violation history that contains records beyond the exact currently represented PWS universe, but the frozen contract does not permit post-observation threshold relaxation or alternate identity repair.

## Strong structural support that passed / 통과한 구조 지원

The branch nonetheless established substantial reusable evidence:

- PWS quarterly key duplicates: **0**
- latest-quarter active exact PWSIDs: **140,677** vs threshold 140,000
- latest active structural completeness (type + source + population): **99.9800962%**
- health-indicator semantic coverage: **100% Y/N**
- distinct historical health-based PWSID + VIOLATION_ID events: **557,102**
- health-based event date completeness: **100%**
- source-native health categories observed:
  - MCL: **1,634,410** rows
  - MRDL: **1,285**
  - TT: **338,078**
- later quarterly ZIP opened: **false**
- future event membership opened: **false**
- relationship/prediction/ranking/causal computation: **false**
- incremental monetary cost: **0 USD**

These facts establish source/event richness but do not authorize a prospective experiment under this frozen design.

## Consequence / 후속 조치

Do not authorize `US-EPA-SDWIS-N01` or `US-EPA-SDWIS-E01`.

Do not rescue this exact branch by:
- lowering PWSID syntax or join thresholds;
- introducing name/address/geographic/manual identity repair;
- adding historical quarterly archives after observing Gate 9;
- treating the current single-quarter ZIP as multi-quarter lineage;
- opening a later quarterly refresh.

Return to independent Stage-0 portfolio reselection. The SDWIS branch remains durable negative evidence showing that the current national download has excellent event semantics and scale but does not satisfy this preregistered temporal-lineage/identity design.

Incremental monetary cost: **0 USD**.
