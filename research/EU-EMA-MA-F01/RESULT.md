---
id: EU-EMA-MA-F01-RESULT
type: structural-feasibility-result
created: 2026-09-29
issue: 175
research: EU-EMA-MA-F01
disposition: HOLD
attempt_02_commit: fe07b9ef39db42758c16612d202f29235be88b6c
attempt_02_run: 36545759009
contract_commit: 215cd9dd74a358e412a86de5d41a039c2f8186cb
gate: HOLD_EU_EMA_MA_F01_EXACT_PRODUCT_FUTURE_WITHDRAWAL_SUSPENSION_DESIGN_NOT_READY
---

# EU-EMA-MA-F01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_EU_EMA_MA_F01_EXACT_PRODUCT_FUTURE_WITHDRAWAL_SUSPENSION_DESIGN_NOT_READY`**

Attempt 02 is the first valid empirical execution of the frozen 18-gate contract and passes **15/18** requirements. Failed gates are **9, 12, 14**. Because the pre-Issue rule requires exactly 18/18 PASS, this exact F01 is terminal scientific HOLD. No N01 or E01 is authorized.

Attempt 02는 고정 18-gate 계약의 첫 유효 empirical 실행이며 **15/18**을 통과했습니다. 실패 gate는 **9, 12, 14**입니다. 사전계약이 18/18을 요구하므로 이 exact F01은 terminal scientific HOLD입니다.

## Decisive frozen failure / 결정적 고정 실패

**Gate 9 — Decision-date support**

The current official EMA medicines table produced **2,351** qualified human EMA product IDs under the exact frozen `EMEA/H/C/######` identity rule. Only **92.0459379%** of focal rows had a parseable nonblank European Commission decision/authorisation date under the preregistered gate, below the frozen **99.00%** threshold.

This is sufficient by itself to make the exact preregistered design non-promotable. The population or threshold may not now be narrowed to authorised-only rows, status-specific subsets or another date field to rescue Gate 9.

Gate 9의 실제 관측치는 **92.0459379% < 99.00%**입니다. 이 실패만으로도 18/18은 불가능하며, 결과 확인 후 authorised-only subset이나 다른 날짜 필드로 모집단을 바꾸는 구제는 금지합니다.

## Other failed gates / 기타 실패 gate

- **Gate 12 — historical event-date support:** 93 historical withdrawn-authorisation products were identified; only **54 / 93 = 58.0645%** met the frozen requirement that both authorisation-issued date and withdrawal date be parsed and chronologically sane.
- **Gate 14 — event-class separation:** suspension, expiry and post-authorisation procedure semantics were detected in the frozen documentation surfaces, but the exact required initial-application-withdrawal wording was not established by the preregistered documentation check.

These failures are retained as evidence. Even if later parser/documentation improvements affected Gates 12 or 14, Gate 9 independently prevents promotion under the unchanged contract.

## Strong support that passed / 통과한 구조 지원

- official EMA baseline: `medicines-output-medicines-report_en.xlsx`
- baseline SHA-256: `5a9c27c2a91282b6305b7721c3458638e0d08a2618dc0b327dcec18d4002cdcf`
- exact ID syntax: **2,351 / 2,351 = 100%**
- distinct qualified human product IDs: **2,351**
- authorised/current IDs: **1,573**
- official medicine URL coverage: **100%**
- historical withdrawn-authorisation support: **93** qualified products from the deterministic baseline-derived candidate pages
- withdrawal reason support: **93 / 93 = 100%**
- reason classes observed: **69 VOLUNTARY_COMMERCIAL**, **24 OTHER_UNKNOWN**
- historical identity concordance: **100%**
- future event membership opened: **false**
- future entity pages consumed for membership: **0**
- relationship/prediction/ranking/causal metric computed: **false**
- incremental monetary cost: **0 USD**

These are structural source facts only. They do not establish a medicine-withdrawal relationship, safety signal, prediction, ranking, causal effect, prescribing recommendation or regulatory conclusion.

## Attempt provenance / 시도 계보

Attempt 01 / Run `36529679263` was implementation-blocked after Gates 1–4 because a valid official XLSX body was stored under a temporary `.bin` filename and rejected by `openpyxl`. Attempt 01 remains immutable at commit `56c557a334ee82401217e99d4700825889f248a9`.

Implementation correction `04c6a70767ebfca5bcf9c369a938ae0b0d888950` changed only temporary filename extension preservation. Attempt 02 / Run `36545759009` completed successfully and is preserved at commit `fe07b9ef39db42758c16612d202f29235be88b6c`.

## Consequence / 후속 조치

Do not authorize `EU-EMA-MA-N01` or E01. Do not rescue this exact F01 by narrowing the focal population after observation, lowering the 99% date threshold, substituting another date field, weakening historical-date support, collapsing event classes, or opening future withdrawal/suspension membership.

Return to independent Stage-0 portfolio reselection. The EMA branch remains durable negative evidence for future overlap scoring.

Incremental monetary cost: **0 USD**.
