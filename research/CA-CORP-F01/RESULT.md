---
id: CA-CORP-F01-RESULT
type: structural-feasibility-result
created: 2026-09-29
issue: 173
research: CA-CORP-F01
disposition: HOLD
attempt_01_commit: 4d8c617a80aafbaf8200c859b5987776e6fe99db
contract_commit: b97728c4e6338386bf47ec28be0c34afdf7a4737
gate: HOLD_CA_CORP_F01_EXACT_ID_SECTION212_FUTURE_EVENT_DESIGN_NOT_READY
---

# CA-CORP-F01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_CA_CORP_F01_EXACT_ID_SECTION212_FUTURE_EVENT_DESIGN_NOT_READY`**

Attempt 01 is a valid empirical execution of the frozen 18-gate contract and passes **14/18** requirements. Failed gates are **5, 9, 10, 13**. Because the pre-Issue rule requires exactly 18/18 PASS, this exact F01 is terminal scientific HOLD. No N01 or E01 is authorized.

Attempt 01은 고정 18-gate 계약의 유효 empirical 실행이며 **14/18**을 통과했습니다. 실패 gate는 **5, 9, 10, 13**입니다. 사전계약이 18/18을 요구하므로 이 exact F01은 terminal scientific HOLD입니다.

## Decisive frozen failure / 결정적 고정 실패

**Gate 5 — Baseline parseability/schema**

The four official federal-corporation CSV resources expose Corporation Number, Governing legislation and Status, but none exposes an incorporation/continuance date concept required by the frozen contract. Observed active-CBCA headers include `Anniversary date`, `Year of last annual filing`, and `Date of last annual meeting`, but no incorporation/continuance date field.

공식 baseline CSV 4종에는 Corporation Number·Governing legislation·Status는 존재하지만, 사전고정 Gate 5가 요구한 incorporation/continuance date concept가 없습니다. 이는 parser alias 누락이 아니라 현재 공식 baseline schema 자체의 구조적 한계입니다.

Because Gate 5 independently fails, this exact design cannot reach 18/18 even if later parser/documentation clarifications changed Gates 9, 10 or 13. The contract therefore prohibits a rescue run that changes the baseline source, relaxes the required date concept or reinterprets unrelated date fields as incorporation/continuance.

## Other failed gates / 기타 실패 gate

- **Gate 9 — status semantics:** observed CBCA statuses were structurally recognizable, but the frozen documentation-label check did not find every exact required label in the current search-tips page.
- **Gate 10 — historical monthly lineage:** the current monthly landing page exposed only one month link inside the frozen 2025-01 through 2026-08 parsing rule, below the required 18 distinct publication months.
- **Gate 13 — event-class separation:** section 212 and section 210/211 labels were found, while amalgamation and discontinuance families were not established from the frozen monthly landing-page check.

These three failures are retained as observed evidence but are not used to justify an implementation-only rescue because Gate 5 already makes the exact preregistered design scientifically non-promotable.

## Strong support that did pass / 통과한 구조 지원

- exact-ID syntax: **1,569,191 / 1,569,191 = 100%**
- distinct active CBCA IDs: **644,887** vs threshold 250,000
- distinct complete federal IDs: **1,569,191** vs threshold 500,000
- historical section-212 support: **5,054** distinct IDs vs threshold 5,000
- exact baseline match of historical section-212 IDs: **5,045 / 5,054 = 99.8219%**
- API sample: **8 / 8 available responses concordant = 100%**
- future section-212 membership opened: **false**
- future rows opened: **0**
- prohibited trigger exposure computed: **false**
- incremental monetary cost: **0 USD**

These figures establish useful structural identity/event support only. They do not establish any corporate-dissolution relationship, prediction, ranking, causal effect or regulatory conclusion.

## Consequence / 후속 조치

Do not authorize `CA-CORP-N01` or `CA-CORP-E01`. Do not rescue this exact F01 by substituting another baseline, treating annual-filing/meeting dates as incorporation dates, loosening the date requirement, changing the legal population, or opening future section-212 membership.

Return to independent Stage-0 portfolio reselection. The CA-CORP branch remains durable negative evidence for future portfolio overlap scoring.

Incremental monetary cost: **0 USD**.
