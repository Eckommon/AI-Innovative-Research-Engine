---
id: US-FCC-ULS-F01-RESULT
type: structural-feasibility-result
created: 2026-09-21
issue: 166
research: US-FCC-ULS-F01
disposition: HOLD
attempt_02_commit: e78d0f64ebf37acc7c481628a415e68b0f69f7b3
workflow_run: 35555505050
contract_commit: 287f0e3dfe203beee3d9ca1f21e67e51ef2db6a5
gate: HOLD_US_FCC_ULS_F01_MICROWAVE_EXACT_SYSTEM_ID_FUTURE_EVENT_DESIGN_NOT_READY
---

# US-FCC-ULS-F01 Result / 결과

## Terminal disposition / 최종 판정

**`HOLD_US_FCC_ULS_F01_MICROWAVE_EXACT_SYSTEM_ID_FUTURE_EVENT_DESIGN_NOT_READY`**

Attempt 02 is the first valid empirical execution of the frozen 18-gate contract and passes **9/18** requirements. Because the pre-Issue rule requires exactly 18/18 PASS, this exact F01 is terminal scientific HOLD. No N01 or E01 is authorized.

Attempt 02는 고정된 18-gate 계약의 첫 유효 empirical 실행이며 **9/18**만 통과했습니다. 사전 계약은 18/18을 요구하므로 이 exact F01은 terminal scientific HOLD입니다. N01/E01은 허가하지 않습니다.

## Failed frozen gates / 실패 gate

Failed gates: **3, 8, 9, 10, 11, 12, 13, 14, 15**.

- **Gate 3 — documentation availability:** three frozen FCC PDF anchors were retrieved and fingerprinted, but the frozen FCC HTML download-page anchor remained HTTP 403 under the allowed transport resolution. The contract did not permit silently waiving this anchor.
- **Gate 8 — exact system-ID syntax:** HD contained **366,807 nonblank values** at the frozen documented Unique System Identifier position, but **0** satisfied the preregistered rule requiring lossless normalization to exactly nine decimal digits.
- **Gate 9 — independent license support:** therefore **0** distinct IDs met the frozen exact-ID rule, below the **20,000** minimum.
- **Gate 10 — active baseline support:** therefore **0** exact-qualified active IDs met the **10,000** minimum.
- **Gate 11 — status semantics:** **366,304 / 366,807 = 99.8628707%** of nonblank HD statuses were within the frozen `A/C/E/T` set, below **99.90%**. The remaining **503** rows were source status `P`; they were recorded and not remapped.
- **Gates 12–15:** the frozen exact-ID qualification left no active exact-ID cohort for date, HS-lineage and technical-table join support, so these gates failed under the unchanged contract.

중요한 해석 경계는 **FCC에 고유 식별자가 없다는 뜻이 아니라**, 이번 사전고정 규칙이 요구한 “exact 9-digit normalization”을 현재 baseline 표현에 그대로 적용했을 때 qualified cohort가 0이었다는 뜻입니다. 이 결과를 본 뒤 zero-padding, alternate identifier, field reinterpretation, threshold reduction 또는 다른 service family로 구제하지 않습니다.

## Valid baseline facts / 유효 baseline 사실

- official FCC `l_micro.zip`: HTTP 200, parseable ZIP
- baseline size: **211,037,826 bytes**
- baseline SHA-256: `3ade0c1fcf335fa9d50ce4ecc9bf11b53839d7a40de49baa8f8fa7877e636803`
- HD rows: **366,807**
- HS rows: **4,950,382**
- HD status counts: `A=165,713`, `C=132,479`, `E=48,865`, `P=503`, `T=19,247`
- required `HD.dat` and `HS.dat` were present
- multiple additional Microwave tables were present in the archive
- all five frozen daily `l_mw_xxx.zip` endpoints returned metadata-only HTTP 200

These are structural facts only. They do not establish a future cancellation/termination relationship, prediction, ranking, causal effect or regulatory conclusion.

## Implementation-correction provenance / 구현 보정 계보

Attempt 01 / Run `35555305664` ended before a valid empirical result because the GitHub-hosted Python urllib path received FCC HTTP 403. That attempt remains immutable.

Transport-only correction `486624cf803c291217baef97b8514294691fce82` changed only retrieval mechanics to curl plus FCC-owned endpoint variants. It changed no scientific threshold, service family, identity rule, source filename or future window. Attempt 02 then reached all 18 gates and is preserved at commit `e78d0f64ebf37acc7c481628a415e68b0f69f7b3` / Run `35555505050`.

## Future-outcome firewall / 미래 outcome 방화벽

- future daily transaction rows opened: **0**
- future cancelled/terminated membership opened: **false**
- daily entity-body bytes consumed: **0**
- prediction/ranking/causal metric computed: **false**
- name/address/call-sign-only/fuzzy/geospatial/manual identity repair: **false**

## Consequence / 후속 조치

This HOLD does **not** authorize `US-FCC-ULS-N01`. The failed exact design may not be rescued by redefining the ID syntax, lowering support thresholds, broadening the radio-service family, or opening future daily transaction bodies. Return to independent Stage-0 portfolio reselection.

이 HOLD는 `US-FCC-ULS-N01`을 허가하지 않습니다. ID 규칙·threshold·service family를 사후 변경하거나 future daily body를 열어 구제하지 않고 독립적인 Stage-0 portfolio reselection으로 복귀합니다.

Incremental monetary cost: **0 USD**.
