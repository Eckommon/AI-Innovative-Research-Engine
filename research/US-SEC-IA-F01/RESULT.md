---
id: US-SEC-IA-F01-RESULT
type: structural-feasibility-result
created: 2026-10-01
issue: 187
research: US-SEC-IA-F01
disposition: HOLD
attempt_01_commit: a53611c003e96cbff112c22fec52ed20fe864a7e
attempt_01_run: 36652883210
contract_commit: 2734008b75116779d410ffec1e3ca44343e3e1f9
gate: HOLD_US_SEC_IA_F01_EXACT_CRD_FUTURE_FULL_ADVW_DESIGN_NOT_READY
---

# US-SEC-IA-F01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_SEC_IA_F01_EXACT_CRD_FUTURE_FULL_ADVW_DESIGN_NOT_READY`**

Attempt 01 is a valid empirical execution of the frozen source-lineage gate and passes **5/18** requirements. Gate 4 is the decisive scientific failure; gates 5–16 were not evaluated after that decisive failure. Because the pre-Issue contract requires exactly 18/18 PASS, this exact F01 is terminal scientific HOLD.

Attempt 01은 고정된 source-lineage gate의 유효 empirical 실행이며 **5/18**을 통과했습니다. Gate 4가 결정적 scientific failure이며, 그 이후 gate 5–16은 평가하지 않았습니다. 사전계약이 18/18을 요구하므로 이 exact F01은 terminal scientific HOLD입니다.

## Decisive Gate 4 failure / 결정적 Gate 4 실패

The frozen baseline required **exactly 12 official Registered Investment Adviser report ZIPs** for 2025-09 through 2026-08.

The official SEC report page resolved all 12 calendar slots, but the source-native formats were:

- 2025-09: **XLSX**
- 2025-10: **PDF — no data**
- 2025-11: **PDF — no data**
- 2025-12: ZIP
- 2026-01 through 2026-08: ZIP

Therefore the frozen criterion “12 official report ZIPs, all parseable as monthly baseline files” is false.

This is not a transport or parser defect. The runner successfully resolved the official SEC entries and their declared source formats. The October and November 2025 source objects are explicitly PDF `ia-no-data-*.pdf` entries, not missing ZIP links.

따라서 이는 transport/parser 문제가 아닙니다. 공식 SEC source 자체가 2025-10과 2025-11을 ZIP이 아닌 **no-data PDF**로 제공하고 있어, 사전고정 12개월 machine-readable lineage가 성립하지 않습니다.

## Why no rescue / 사후 구제 금지

Do not rescue this exact branch by:
- changing the frozen 12-month window;
- dropping October/November 2025 after observation;
- treating the no-data PDFs as equivalent row-bearing adviser reports;
- substituting a different SEC/IAPD month or source family;
- moving the baseline start to December 2025;
- lowering the 12-month resolution requirement.

Any such change would be a new hypothesis/contract, not a correction of Attempt 01.

## Preserved firewall / 유지된 방화벽

- historical ADV-W body opened: **false**
- post-cutoff ADV-W body opened: **false**
- future ADV-W membership opened: **false**
- withdrawal/business-failure relationship computed: **false**
- prediction/ranking/causal metric computed: **false**
- prohibited withdrawal exposure computed: **false**
- identity repair used: **false**
- incremental monetary cost: **0 USD**

Because Gate 4 failed decisively, the historical ADV-W body was not opened at all.

## Scientific meaning / 과학적 의미

This result does **not** show that CRD identity, ADV-W semantics, or adviser withdrawal analysis are weak in general. It shows that the specific preregistered prospective design depended on a continuous twelve-month machine-readable SEC Registered Investment Adviser baseline that is not actually available for the frozen window.

Full ADV-W withdrawal remains a registration event, not a business-failure label.

## Consequence / 후속 조치

- `US-SEC-IA-N01` is **not authorized**.
- `US-SEC-IA-E01` is **not authorized**.
- Do not open post-cutoff ADV-W membership.
- Return to independent Stage-0 portfolio reselection.
- Preserve the 2025-10/11 no-data gap as reusable source-lineage negative evidence.

Incremental monetary cost: **0 USD**.
