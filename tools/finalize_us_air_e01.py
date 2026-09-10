#!/usr/bin/env python3
"""Finalize US-AIR-E01 from already committed Stage B artifacts; no experiment rerun."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
E01 = ROOT / "research" / "US-AIR-E01"
REG = ROOT / "registry"
GATE = "PASS_US_AIR_E01_POSITIVE_MATERIAL_PRECIPITATION_DELAY_ASSOCIATION"
RUN = "34429684361"
CHECKPOINT = "CHK-20260911-US-AIR-E01-PASS-PORTFOLIO-RETURN"


def one_row(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 1, f"expected one row: {path}"
    return rows[0]


def read_rows(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


primary = one_row(E01 / "STAGE_B_PRIMARY_RESULT.csv")
source = read_rows(E01 / "STAGE_B_BTS_SOURCE_MANIFEST.csv")
sens = read_rows(E01 / "STAGE_B_SENSITIVITY_RESULT.csv")
stage_b = (E01 / "STAGE_B_RESULT.md").read_text(encoding="utf-8")

assert primary["gate"] == GATE
assert int(primary["n_airport_days"]) == 91687
assert int(primary["airports"]) == 255
assert int(primary["dates"]) == 365
assert float(primary["beta_log1p_precip"]) > 0
assert float(primary["ci95_low"]) > 0
assert float(primary["delta_0_to_10mm_minutes"]) >= 1.0
assert int(primary["negative_delay_rows"]) == 0
assert int(primary["nonfinite_delay_rows"]) == 0
assert primary["monthly_header_consistent"] == "True"
assert len(source) == 12
assert all(r["hash_match"] == "True" for r in source)
assert all(r["expected_sha256"] == r["actual_sha256"] for r in source)
assert all(r["expected_bytes"] == r["actual_bytes"] for r in source)
assert {r["analysis"] for r in sens} == {
    "S1_TRACE_0_1MM", "S2_EXCLUDE_DIVERTED", "S3_CLUSTER_AIRPORT_ISO_WEEK"
}
assert all(r["status"] == "OK" for r in sens)
assert GATE in stage_b

beta = float(primary["beta_log1p_precip"])
se = float(primary["se"])
ci_low = float(primary["ci95_low"])
ci_high = float(primary["ci95_high"])
p = float(primary["p_two_sided"])
delta = float(primary["delta_0_to_10mm_minutes"])
baseline_rmse = float(primary["baseline_rmse"])
weather_rmse = float(primary["weather_rmse"])
rmse_improvement = (baseline_rmse - weather_rmse) / baseline_rmse * 100.0

result = f'''---
id: US-AIR-E01-RESULT
type: preregistered-primary-relationship-result
created: 2026-09-11
issue: 90
state: COMPLETED_PASS
final_gate: {GATE}
decision: DEC-126
claim: CLM-137
relationship_outcome_computed: true
incremental_monetary_cost_usd: 0
---

# US-AIR-E01 Result
# US-AIR-E01 결과

## Final gate / 최종 판정

**`{GATE}`**

Under the prospectively frozen 2025 airport-day design, higher same-calendar-date NOAA LCDv2 `DailyPrecipitation` is positively associated with higher BTS mean `DepDelayMinutes` after airport fixed effects, FlightDate fixed effects and scheduled-departure-volume control. / 사전고정한 2025 공항-일 설계에서 동일 달력일 NOAA `DailyPrecipitation` 증가는 공항·FlightDate 고정효과와 예정 출발편수 통제 후 BTS 평균 `DepDelayMinutes` 증가와 양의 연관성을 보였다.

This is a contemporaneous association result, **not causal inference, advance prediction or delay propagation**. / 이는 당일 연관성 결과이며 인과·사전예측·지연전파 결과가 아니다.

## Integrity / 무결성

- Stage A: `PASS_US_AIR_E01_STAGE_A_PRECIPITATION_QUALITY` — 255 airports / 255 stations / 92,818 usable weather keys.
- Stage B Run: `{RUN}`.
- BTS 2025 frozen PREZIP hashes: **12/12 exact match before any ZIP CSV member was opened**.
- parsed source rows: **7,736,770**.
- rows belonging to the frozen Stage-A weather cohort: **6,726,149**.
- negative eligible `DepDelayMinutes` rows: **0**.
- non-finite/unparsed nonblank delay rows: **0**.
- monthly BTS header consistency: **True**.

## Realized panel / 실현 panel

- airport-day observations: **91,687**;
- unique airports: **255**;
- unique FlightDate levels: **365**;
- CR1 full parameter count K: **621**;
- FE alternating-projection iterations: **8**;
- final convergence change: **9.104e-15**.

The frozen support minimums of >=100 airports and >=30,000 airport-days pass without post-outcome subset selection. / 사전고정 support 기준을 outcome 사후선별 없이 통과했다.

## Primary preregistered estimate / 사전등록 주추정

- beta on `log1p(DailyPrecipitation_mm)`: **{beta:.12f} minutes**;
- two-way CR1 SE, AirportID × FlightDate: **{se:.12f}**;
- two-sided p-value: **{p:.12g}**;
- 95% CI: **[{ci_low:.12f}, {ci_high:.12f}]**;
- model-implied 0 mm → 10 mm contrast: **{delta:.6f} minutes**.

All three preregistered PASS conditions are satisfied: beta > 0, 95% CI lower bound > 0, and the 0→10 mm model-implied contrast >=1.0 minute. / 세 사전등록 PASS 조건을 모두 충족한다.

## Baseline comparison / baseline 비교

- baseline within-RMSE: **{baseline_rmse:.6f} min**;
- weather-model within-RMSE: **{weather_rmse:.6f} min**;
- descriptive in-sample RMSE reduction: **{rmse_improvement:.3f}%**.

RMSE was not a preregistered gate and is reported descriptively only. / RMSE는 gate가 아니며 기술적으로만 보고한다.

## Prespecified sensitivities / 사전 sensitivity

All three non-gate sensitivities completed `OK` and preserve a positive CI-excluding-zero coefficient with an approximately 11.68–11.87 minute 0→10 mm model-implied contrast:
- trace `T=0.1 mm`;
- Diverted exclusion;
- AirportID × ISO-week dependence stress test.

Sensitivities do not alter or rescue the primary gate. / sensitivity는 primary gate를 변경·구제하지 않는다.

## What this result does not establish / 본 결과가 입증하지 않는 것

It does not establish:
- precipitation **causes** 11.73 minutes of delay;
- advance forecast skill;
- network delay propagation;
- airport/carrier vulnerability rankings;
- an optimal precipitation threshold;
- external-year or out-of-sample generalization;
- novelty relative to prior aviation-weather research;
- operational/commercial decision utility;
- policy or investment superiority.

The coefficient is conditional on the frozen same-day panel specification and log precipitation transform. / 계수는 고정한 당일 panel specification과 log precipitation transform에 조건부이다.

## Mission disposition / 미션 처분

US-AIR advances from `JOIN_READY` to **`RELATIONSHIP_TESTED`** for this one preregistered precipitation-delay relationship. / US-AIR은 이 단일 사전등록 관계에 대해 `RELATIONSHIP_TESTED` 단계로 진입한다.

Do **not** automatically tune weather variables, thresholds, lags or airport subsets. Close Issue #90 and return to Stage 0 portfolio control. / 변수·threshold·lag·공항 subset 자동튜닝 없이 #90을 닫고 Stage 0로 복귀한다.

A later descendant must compete at Stage 0 and separately address generalization, novelty and named decision utility. / 후속은 Stage 0에서 다시 경쟁하고 일반화·신규성·구체적 의사결정 효익을 별도 검증해야 한다.

Incremental monetary cost remained **0 USD**.
'''

claim = f'''---
id: CLM-137
type: claim
created: 2026-09-11
state: OBSERVED_DERIVED_VALIDATED
---

# CLM-137 — Preregistered US-AIR precipitation-delay association passes
# CLM-137 — 사전등록 US-AIR 강수-출발지연 연관성 PASS

Under the frozen 2025 airport-day model, Run `{RUN}` estimates the coefficient on `log1p(DailyPrecipitation_mm)` at **{beta:.12f} minutes** with two-way AirportID/FlightDate CR1 SE **{se:.12f}**, 95% CI **[{ci_low:.12f}, {ci_high:.12f}]**, and a model-implied 0→10 mm contrast of **{delta:.6f} minutes** across **91,687 airport-days / 255 airports**. / 고정 2025 공항-일 모델에서 강수 log 변수는 평균 출발지연과 양의 연관성을 보이며 사전기준을 통과한다.

All preregistered PASS criteria are satisfied, so the exact gate is **`{GATE}`**. The three prespecified non-gate sensitivities are directionally consistent and do not determine the gate. / 세 PASS 조건을 모두 만족하며 sensitivity는 gate 결정에 사용되지 않았다.

Source integrity passed 12/12 frozen BTS ZIP hashes before delay parsing. / 지연값 파싱 전에 BTS frozen ZIP hash 12/12가 일치했다.

This claim is **association-only**. It does not establish causality, advance prediction, propagation, generalization, novelty, utility, rankings, policy superiority or investment superiority. / 본 주장은 연관성에 한정되며 인과·예측·전파·일반화·신규성·효용을 주장하지 않는다.

**Evidence / 근거**
- Run `{RUN}`;
- `research/US-AIR-E01/STAGE_B_PRIMARY_RESULT.csv`;
- `research/US-AIR-E01/STAGE_B_SENSITIVITY_RESULT.csv`;
- `research/US-AIR-E01/STAGE_B_BTS_SOURCE_MANIFEST.csv`;
- `research/US-AIR-E01/STAGE_B_RESULT.md`;
- `research/US-AIR-E01/RESULT.md`.

**Verification:** `V3_PREREGISTERED_RELATIONSHIP_REPRODUCED`.
'''

decision = f'''---
id: DEC-126
type: decision
created: 2026-09-11
status: ACTIVE
---

# DEC-126 — Finalize US-AIR-E01 as preregistered positive material association PASS
# DEC-126 — US-AIR-E01을 사전등록 양의 실질 연관성 PASS로 종료

## Decision / 결정

Finalize Issue #90 / `US-AIR-E01` as:

**`{GATE}`**

and close the issue as completed after this durable checkpoint is verified. / durable checkpoint 검증 후 #90을 completed로 종결한다.

## Basis / 근거

The frozen source, cohort, outcome, model, covariance and materiality contracts were established before Stage-B delay magnitudes were opened. Run `{RUN}` then produced:
- 12/12 exact BTS source hash matches;
- 91,687 realized airport-days across 255 airports and 365 dates;
- beta = {beta:.12f};
- 95% CI = [{ci_low:.12f}, {ci_high:.12f}];
- 0→10 mm model-implied contrast = {delta:.6f} minutes.

Thus beta > 0, CI lower > 0 and the >=1.0-minute materiality floor all pass. / 방향·95% CI·실질성 하한을 모두 충족한다.

## Evidence ladder / 증거 단계

US-AIR now qualifies as **`RELATIONSHIP_TESTED`** for one preregistered contemporaneous DailyPrecipitation→departure-delay relationship.

Do not promote it to:
- `GENERALIZATION_TESTED`;
- `NOVELTY_ASSESSED`;
- `UTILITY_TESTED`;
- `INNOVATION_CANDIDATE`.

Those remain separate unresolved stages. / 일반화·신규성·효용·혁신후보 승격은 별도 검증 전 금지한다.

## Branch-stop / 다음 분기

Do not automatically run another weather variable, threshold, lag, route, carrier or airport-subset analysis. Return to Stage 0 portfolio control after #90 closes. / 사후 튜닝 없이 Stage 0로 복귀한다.

Any descendant must compete against portfolio alternatives on expected information value, and a generalization descendant should use an untouched time/spatial period rather than refitting 2025 variants. / 후속은 portfolio 경쟁을 거치며 일반화 검증은 2025 변형 재적합보다 untouched 시공간을 사용해야 한다.

Incremental monetary cost remains **0 USD**. COST-001 and RAW-001 remain mandatory.
'''

(E01 / "RESULT.md").write_text(result, encoding="utf-8")
(REG / "CLM-137.md").write_text(claim, encoding="utf-8")
(REG / "DEC-126.md").write_text(decision, encoding="utf-8")

readme_path = E01 / "README.md"
readme = readme_path.read_text(encoding="utf-8")
readme = readme.replace("state: ACTIVE_STAGE_B", "state: COMPLETED_PASS")
readme = readme.replace("relationship_outcome_computed: false", "relationship_outcome_computed: true")
readme = readme.replace("delay_magnitudes_parsed: false", "delay_magnitudes_parsed: true")
if "final_gate:" not in readme.split("---", 2)[1]:
    readme = readme.replace(
        "primary_weather_variable: DailyPrecipitation\n",
        f"primary_weather_variable: DailyPrecipitation\nfinal_gate: {GATE}\n",
    )
if "## Final disposition / 최종 처분" not in readme:
    readme += f'''\n\n## Final disposition / 최종 처분\n\nRun `{RUN}` resolves the preregistered E01 as **`{GATE}`**.\n\nPrimary result: 91,687 airport-days / 255 airports; beta={beta:.12f}, 95% CI [{ci_low:.12f}, {ci_high:.12f}], 0→10 mm model-implied contrast={delta:.6f} minutes.\n\nUnder DEC-126 this branch is `RELATIONSHIP_TESTED` only. Close #90 and return to Stage 0; no automatic tuning or generalization claim.\n'''
readme_path.write_text(readme, encoding="utf-8")

ledger_path = REG / "CLAIM_LEDGER.md"
ledger = ledger_path.read_text(encoding="utf-8")
ledger_row = f'''| `CLM-137` | Under the frozen 2025 airport-day specification, NOAA DailyPrecipitation is positively associated with BTS mean departure delay: beta `{beta:.6f}`, 95% CI `[{ci_low:.6f}, {ci_high:.6f}]`, 0→10 mm model-implied contrast `{delta:.6f}` min over 91,687 airport-days/255 airports; exact primary gate `{GATE}`. Association only, not causal/generalization/utility evidence. / 고정 사전등록 모델에서 강수와 평균 출발지연의 양의 실질 연관성 PASS; 인과·일반화·효용 주장은 아님. | `OBSERVED/DERIVED/VALIDATED` | `V3_PREREGISTERED_RELATIONSHIP_REPRODUCED` | Run `{RUN}`; `research/US-AIR-E01/RESULT.md`; `registry/CLM-137.md`; Issue #90 | 2026-09-11 | active-relationship-tested |\n\n'''
if "`CLM-137`" not in ledger:
    marker = "## Rule / 규칙"
    assert marker in ledger
    ledger = ledger.replace(marker, ledger_row + marker)
ledger_path.write_text(ledger, encoding="utf-8")

dec_log_path = REG / "DECISION_LOG.md"
dec_log = dec_log_path.read_text(encoding="utf-8")
if "[DEC-126]" not in dec_log:
    anchor = "- [DEC-125](DEC-125.md): accept Stage-A precipitation-quality PASS and authorize frozen Stage B / 강수 기상품질 Stage A PASS 수용·고정 Stage B 승인."
    assert anchor in dec_log
    dec_log = dec_log.replace(
        anchor,
        anchor + "\n- [DEC-126](DEC-126.md): finalize US-AIR-E01 as preregistered positive material precipitation-delay association PASS; close #90 and return to Stage 0 / US-AIR-E01 양의 실질 연관성 PASS 확정·#90 종결·Stage 0 복귀.",
    )
dec_log_path.write_text(dec_log, encoding="utf-8")

status = f'''---
checkpoint_id: {CHECKPOINT}
active_issue: none
active_research: NONE
last_completed_issue: 90
last_completed_research: US-AIR-E01
last_decision: DEC-126
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_AIR_E01_RELATIONSHIP_TESTED_PASS__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

## Latest completed research / 최신 완료 연구

Issue #90 `US-AIR-E01` resolves to:

**`{GATE}`**

Primary preregistered result:
- Run `{RUN}`;
- 91,687 airport-days / 255 airports / 365 dates;
- beta on `log1p(DailyPrecipitation_mm)` = **{beta:.12f} min**;
- two-way CR1 95% CI = **[{ci_low:.12f}, {ci_high:.12f}]**;
- model-implied 0→10 mm contrast = **{delta:.6f} min**;
- 12/12 frozen BTS source hashes matched before outcome parsing.

The result satisfies the frozen positive-direction, CI and >=1-minute materiality gates. / 사전고정 방향·CI·실질성 gate를 모두 통과한다.

## Evidence status / 증거 상태

US-AIR is now **RELATIONSHIP_TESTED** for one contemporaneous precipitation-delay relationship.

It is **not** yet GENERALIZATION_TESTED, NOVELTY_ASSESSED, UTILITY_TESTED or an INNOVATION_CANDIDATE. The result is not causal or advance-predictive. / 일반화·신규성·효용·혁신후보 및 인과·사전예측 주장은 아직 없다.

## Exact next action / 정확한 다음 행동

**Return to Stage 0 portfolio control.** There is no active research Issue after #90 closes. / #90 종결 후 활성 연구 Issue 없이 Stage 0로 복귀한다.

Do not automatically test another weather variable, threshold, lag or 2025 subset. Compare portfolio alternatives before deciding whether the next uncertainty should be US-AIR external generalization, novelty/utility assessment, or another independent branch. / 자동 튜닝 금지, 다음 불확실성을 portfolio에서 다시 선택한다.

Incremental monetary cost remains **0 USD**.
'''
(ROOT / "STATUS.md").write_text(status, encoding="utf-8")

handoff = f'''---
checkpoint_id: {CHECKPOINT}
active_issue: none
active_research: NONE
last_completed_issue: 90
last_completed_research: US-AIR-E01
last_decision: DEC-126
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

US-AIR-E01 is complete under DEC-126 with:

**`{GATE}`**

Do not rerun Stage A or Stage B by default. / Stage A/B 기본 재실행 금지.

Canonical evidence:
- Run `{RUN}`;
- `research/US-AIR-E01/RESULT.md`;
- `research/US-AIR-E01/STAGE_B_PRIMARY_RESULT.csv`;
- `research/US-AIR-E01/STAGE_B_SENSITIVITY_RESULT.csv`;
- `registry/CLM-137.md`;
- `registry/DEC-126.md`.

Primary result: beta={beta:.12f}, 95% CI [{ci_low:.12f}, {ci_high:.12f}], 0→10 mm model-implied contrast={delta:.6f} minutes across 91,687 airport-days and 255 airports. / 주결과는 사전등록 PASS다.

## Boundary / 경계

This is one contemporaneous `RELATIONSHIP_TESTED` result only. No causal, advance-prediction, propagation, generalization, novelty or decision-utility claim is authorized. / 단일 당일 연관성 검증이며 더 높은 증거단계는 미승인이다.

## Exact next action / 정확한 다음 행동

Return to **Stage 0 portfolio control** with no active research Issue. / 활성 연구 Issue 없이 Stage 0로 복귀한다.

Do not automatically tune US-AIR. Recompare mission-level expected information value. A US-AIR generalization descendant, if selected, must use an untouched period/spatial holdout and be separately preregistered before outcomes. / US-AIR 자동튜닝 금지, 일반화 후속은 untouched holdout과 별도 사전등록이 필요하다.

Cost remains **0 USD**; potentially billable work requires explicit prior approval.
'''
(ROOT / "context" / "SESSION_HANDOFF.md").write_text(handoff, encoding="utf-8")

checkpoint = {
    "checkpoint_id": CHECKPOINT,
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 90,
    "last_completed_research": "US-AIR-E01",
    "last_decision": "DEC-126",
    "updated": "2026-09-11",
}
(ROOT / "context" / "checkpoint.json").write_text(json.dumps(checkpoint, indent=2) + "\n", encoding="utf-8")

print(
    f"FINALIZE_US_AIR_E01_READY;gate={GATE};N={primary['n_airport_days']};"
    f"airports={primary['airports']};beta={beta};ci_low={ci_low};delta10={delta}"
)
