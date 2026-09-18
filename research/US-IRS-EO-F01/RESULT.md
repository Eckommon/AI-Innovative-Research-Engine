---
id: US-IRS-EO-F01-RESULT
type: structural-feasibility-result
created: 2026-09-18
issue: 163
research: US-IRS-EO-F01
disposition: PASS
attempt_02_commit: ab7651c49e2c739734c6330d9d239201514d21e3
workflow_run: 35282837658
contract_commit: 689a00db411b650defcb679bef998beeb55a57da
gate: PASS_US_IRS_EO_F01_EXACT_EIN_JOIN_READY
---

# US-IRS-EO-F01 Result / 결과

## Terminal disposition / 최종 판정

**`PASS_US_IRS_EO_F01_EXACT_EIN_JOIN_READY`**

The final immutable outcome-blind evidence passes **18/18** frozen requirements. Official IRS Form-990-series index data for posting years 2022–2024 provide exact nine-digit EIN identity, large longitudinal filed-organization support, documented filing/event semantics, and a still-sealed Automatic Revocation outcome source sufficient to proceed to one separately preregistered N01 design.

최종 immutable outcome-blind evidence는 고정된 **18/18** 요구조건을 모두 통과했습니다. 2022–2024 IRS Form-990-series 공식 index는 exact 9-digit EIN 식별자, 충분한 종단 filing support, 문서화된 filing/event semantics를 제공하며 Automatic Revocation outcome은 계속 봉인되어 있어 별도 사전등록 N01 설계로 진행할 수 있습니다.

## Structural support / 구조적 support

- combined 2022–2024 historical index rows: **2,090,378**
- valid exact 9-digit EIN rows: **2,090,378 / 2,090,378 (100%)**
- distinct valid EINs: **742,646**
- EINs present in at least two posting-year indexes: **641,705**
- parseable Tax Period: **100%**
- nonblank Object ID: **100%**
- duplicate nonblank Object ID rate: **0%**
- parseable Submission Date representation after the documented parser-only correction: **2,090,378 / 2,090,378 (100%)**
- Submission Date source precision in Attempt 02: **2,090,378 exact `YYYY` year-precision values**
- Automatic Revocation ZIP metadata access: **HEAD, HTTP 200, 0 entity-body bytes consumed**

These are structural feasibility facts only. They are not revocation-risk, financial-weakness, governance-effect, causal, predictive, ranking, compliance, or novelty results.

위 수치는 구조적 실행가능성 사실일 뿐이며 revocation risk, 재무취약성, governance effect, 인과·예측·순위·compliance·신규성 결과가 아닙니다.

## Implementation-correction provenance / 구현 보정 계보

Attempt 01 commit `814f4da6a6050bb3e61908c01807eb769a017553` / Run `35257875153` is preserved unchanged. It returned 17/18 because the original parser accepted full calendar-date/timestamp forms but not the source's exact four-digit `YYYY` Submission Date representation, producing a uniform 0 / 2,090,378 Gate-11 parse result.

Correction `d3026031bb7e5b90e63709589e226cd99babc590` changed **no scientific threshold, source year, identity rule, or outcome firewall**. Attempt 02 accepted exact `YYYY` only as a year-precision source representation. The internal `YYYY-01-01` value is an ordering sentinel and does not assert an observed month/day. Attempt 02 then passed all 18 frozen gates and is preserved at `ab7651c49e2c739734c6330d9d239201514d21e3` / Run `35282837658`.

Attempt 01은 삭제·덮어쓰기하지 않으며, 이번 PASS는 source representation에 대한 parser-only correction 이후 동일한 scientific contract를 재실행한 결과입니다.

## Future-outcome and anti-tautology firewall / 미래 outcome·순환성 방화벽

- Automatic Revocation data rows opened: **0**
- 2025/2026 Form-990 index rows opened: **0**
- Automatic Revocation entity-body bytes consumed: **0**
- missed-filing/nonfiling streak exposure variables constructed: **0**
- name/address/fuzzy/geospatial/manual identity repair used: **false**

Automatic revocation is mechanically tied to three consecutive missed required filings. Therefore descendant work remains prohibited from using missed-filing/nonfiling streaks or equivalent statutory-trigger encodings as exposure variables.

## Consequence / 후속 조치

This PASS authorizes **only** a separately preregistered outcome-blind `US-IRS-EO-N01` design stage. Before any Automatic Revocation membership row is opened, N01 must freeze the filed-return cohort, substantive non-tautological exposure, return/amendment deduplication, temporal risk window, reinstatement handling, matching/comparator rules, support/balance gates, and future event adjudication.

이 PASS는 별도 outcome-blind `US-IRS-EO-N01` 설계만 허가합니다. Automatic Revocation membership을 열기 전에 cohort·비순환 substantive exposure·중복처리·시간창·reinstatement·비교군·support/balance·event adjudication을 먼저 고정해야 합니다. E01은 아직 허가되지 않습니다.

Incremental monetary cost: **0 USD**.
