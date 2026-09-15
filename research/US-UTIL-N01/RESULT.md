---
id: US-UTIL-N01-RESULT
type: outcome-blind-design-identifiability-result
created: 2026-09-16
issue: 137
state: COMPLETED_HOLD
final_gate: HOLD_US_UTIL_N01_SOURCE_OR_DESIGN_SUPPORT
decision: DEC-189
claim: CLM-175
corrected_run: 35008869612
superseded_runs: [35007853296, 35007936755]
reliability_magnitudes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-N01 Result / 결과

## Final gate / 최종 판정

**`HOLD_US_UTIL_N01_SOURCE_OR_DESIGN_SUPPORT`**

US-UTIL-N01 does not reach a separately authorized Reliability-outcome experiment. The prospectively frozen AMI-ramp matched design fails multiple support requirements before any SAIDI magnitude is opened. / US-UTIL-N01은 별도 Reliability outcome 실험 단계로 승격되지 않는다. SAIDI 값을 열기 전에 사전 고정된 AMI-ramp matched design의 여러 support 요건이 충족되지 않았다.

## Corrected outcome-blind support / 교정된 outcome-blind support

Corrected execution Run `35008869612` reused the already prospectively adjudicated F02 largest-identity worksheet rule and the primary IEEE-with-MED rule excluding LOS variants. No scientific threshold, denominator, year, state rule or caliper changed. / 교정 실행은 F02에서 이미 사전 판정된 parser 규칙만 재사용했으며 과학적 기준은 변경하지 않았다.

- eligible utility-state transitions: **1,279**
- distinct eligible Utility Numbers: **408** vs frozen minimum **500**
- exposed candidates: **259** vs frozen minimum **300**
- control candidates: **499** vs frozen minimum **300**
- conflicting exact utility-state-year AMI records: **87** vs frozen requirement **0**
- deterministic matched pairs: **13** vs frozen minimum **150**
- matched states: **9** vs frozen minimum **25**
- pairs by exposure year: **{'2020': 1, '2021': 2, '2022': 8, '2023': 2}**; represented-year minimum was **30 pairs each**
- frozen pair fingerprint: `9210dcdadc76ba3c33963a18f29eb5b6afb5f39350f662fd8b8354f19e45037d`

The control-candidate minimum and all-year exposed/control existence tests pass, but the design still terminates because multiple mandatory frozen requirements fail. / control 후보 수와 모든 exposure year의 양 역할 존재는 통과하지만, 여러 필수 고정요건이 실패하므로 design은 종료된다.

## Execution lineage / 실행 계보

- Run `35007853296`: environment dependency failure (`openpyxl` absent), before support calculation.
- Run `35007936755`: `EXECUTION_PARSER_INVALID_FOR_GATE`; wrong base F02 worksheet/header resolver and an unregistered hard condition were detected before terminalization.
- Run `35008869612`: corrected execution under unchanged Issue #137 contract; this is the terminal evidence-bearing N01 run.

## Evidence boundary / 증거 경계

This HOLD means **design/support identifiability failed**. It is not evidence that AMI does or does not improve reliability. Specifically:
- SAIDI/SAIFI/CAIDI magnitudes remain unopened;
- no AMI→Reliability relationship was computed;
- no NOAA storm magnitude was used;
- no customer-weighted county exposure was invented;
- no post-execution threshold/caliper/aggregation rescue is permitted;
- no causal or resilience claim is supported.

A future US-UTIL descendant requires a new Stage-0/portfolio authorization rather than modifying N01 after seeing support. / 후속 US-UTIL 연구는 N01 기준을 사후 변경하지 않고 Stage 0/portfolio에서 새로 승인되어야 한다.

Incremental monetary cost remained **0 USD**.
