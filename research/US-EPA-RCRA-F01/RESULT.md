---
id: US-EPA-RCRA-F01-RESULT
type: structural-feasibility-result
created: 2026-10-08
issue: 198
research: US-EPA-RCRA-F01
disposition: PASS
contract_commit: ffbb1d89ea614c4c82cc39483383ccb09e23accf
attempt_01_commit: 4994dd3e0614d0c91e04b757d8e3dbe1fca6c335
attempt_01_run: 37669231109
incremental_monetary_cost_usd: 0
---

# US-EPA-RCRA-F01 Result / 결과

## Terminal disposition / 최종 판정

**`PASS_US_EPA_RCRA_F01_EXACT_HANDLER_FUTURE_EVALUATION_VIOLATION_DESIGN_READY`**

Attempt 01 validly passed **18/18** frozen structural gates. The official RCRAInfo baseline supports a deterministic exact-handler prospective design in which a later source-native evaluation is the observation opportunity and `FOUND_VIOLATION=Y` is the primary future event.

## Baseline fingerprint / baseline 지문

- official ZIP bytes: **119,521,531**
- last modified: **2026-10-04 13:45:03 GMT**
- SHA-256: `ef5f4e067c54647074cc11488f3c0c72519139c692cbf359b6b3b601af7a41e5`
- required six CSVs: all present
- later refresh opened: **false**
- future evaluation membership opened: **false**

## Structural evidence / 구조 근거

- Facility rows: **1,627,579**
- exact distinct handler keys: **1,627,578**
- ID syntax pass rate: **99.9999386%**
- ACTIVITY_LOCATION syntax: **100%**
- structurally usable handler keys: **1,627,578**
- VIO/SNC history: **2,686,277** rows
- valid monthly lineage: **322 months**, 2000-01 through 2026-10
- history→Facility exact key coverage: **100%**
- evaluation rows: **1,169,946**
- distinct evaluation opportunities: **1,124,301**
- distinct positive `Y` opportunities: **378,721**
- found-violation Y/N/U semantic coverage: **99.9986324%**
- evaluation-date completeness: **100%**
- distinct evaluation handler keys: **309,249**
- evaluation→Facility exact key coverage: **99.4590120%**

Actual CSV headers resolved cleanly as `EVALUATION_IDENTIFIER` and `FOUND_VIOLATION`.

## Scientific boundary / 과학 경계

F01 PASS establishes feasibility only. It does **not** establish that any structural handler characteristic predicts or causes later violations.

No later RCRAInfo weekly refresh body was opened. No relationship, prediction, ranking, causal metric, prohibited compliance exposure or identity repair was computed.

## Consequence / 후속 조치

Authorize exactly one separate outcome-blind `US-EPA-RCRA-N01` prospective-design gate.

N01 must freeze a non-tautological structural exposure, eligible handler cohort, future evaluation opportunity definition, matching/stratification and common-support rules before any later weekly refresh is opened.

E01 remains unauthorized until N01 passes.

Incremental monetary cost: **0 USD**.
