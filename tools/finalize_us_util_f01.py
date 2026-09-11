#!/usr/bin/env python3
"""Finalize US-UTIL-F01 JOIN_READY from already-derived outcome-blind artifacts.

This script does not download sources, read SAIDI/SAIFI magnitudes, parse AMI meter
magnitudes, or estimate any relationship. It only validates the durable F01 join
qualification and synchronizes the canonical SoT.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JOIN = ROOT / "research" / "US-UTIL-F01" / "JOIN_QUALIFICATION.md"
README = ROOT / "research" / "US-UTIL-F01" / "README.md"
RESULT = ROOT / "research" / "US-UTIL-F01" / "RESULT.md"
STATUS = ROOT / "STATUS.md"
HANDOFF = ROOT / "context" / "SESSION_HANDOFF.md"
CHECKPOINT = ROOT / "context" / "checkpoint.json"
DECISION_LOG = ROOT / "registry" / "DECISION_LOG.md"
CLAIM_LEDGER = ROOT / "registry" / "CLAIM_LEDGER.md"
DECISION = ROOT / "registry" / "DEC-130.md"
CLAIM = ROOT / "registry" / "CLM-139.md"

GATE = "PASS_US_UTIL_F01_JOIN_READY"


def require_once(text: str, needle: str, label: str) -> None:
    if text.count(needle) != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence of {needle!r}")


def main() -> None:
    join = JOIN.read_text(encoding="utf-8")
    required = [
        GATE,
        "Reliability IDs: **908**",
        "Advanced Metering IDs: **2,379**",
        "Service Territory IDs: **2,907**",
        "**842**",
        "**6,341**",
        "NOAA 2024 FIPS route reproducible: **True**",
        "reliability_magnitudes_parsed: false",
        "ami_meter_magnitudes_parsed: false",
        "relationship_computed: false",
    ]
    for token in required:
        if token not in join:
            raise RuntimeError(f"JOIN_QUALIFICATION missing required token: {token}")

    cp = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    expected_cp = {
        "checkpoint_id": "CHK-20260911-US-UTIL-F01-ACTIVE",
        "active_issue": 94,
        "active_research": "US-UTIL-F01",
        "last_completed_issue": 93,
        "last_completed_research": "PORTFOLIO-R11",
        "last_decision": "DEC-129",
        "updated": "2026-09-11",
    }
    if cp != expected_cp:
        raise RuntimeError(f"checkpoint drift before finalization: {cp}")

    result = f'''---
id: US-UTIL-F01-RESULT
type: outcome-blind-join-feasibility-result
created: 2026-09-11
issue: 94
state: COMPLETED_PASS
final_gate: {GATE}
decision: DEC-130
claim: CLM-139
reliability_magnitudes_parsed: false
ami_meter_magnitudes_parsed: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-UTIL-F01 Result
# US-UTIL-F01 결과

## Final gate / 최종 판정

**`{GATE}`**

The frozen source/identity/cardinality gate passes without opening SAIDI/SAIFI magnitudes, AMI meter magnitudes, or any AMI × storm × reliability relationship. / SAIDI·SAIFI 값, AMI meter 값, AMI×폭풍×신뢰도 관계를 열지 않고 source·identity·cardinality gate를 통과했다.

## Qualified structure / 검증된 구조

- EIA-861 2024 final Reliability utility IDs: **908**
- Advanced Metering utility IDs: **2,379**
- Service Territory utility IDs: **2,907**
- Reliability ∩ AMI ∩ Service Territory IDs entering county qualification: **907**
- utilities with complete deterministic county qualification: **842**
- utilities excluded because at least one reported county was unmatched/ambiguous: **65**
- qualified utility×county mappings: **6,341**
- qualified mappings with zero NOAA 2024 county-event rows: **279**
- NOAA county event rows attached for source-key support diagnostics: **85,232**

The frozen minimums were >=300 county-qualified reliability utilities, >=250 with AMI support, >=1,000 qualified utility×county mappings, and a reproducible NOAA county route. All pass. / 고정 최소기준을 모두 통과한다.

## Join rule / 결합 규칙

EIA Service Territory uses exact EIA utility identity and preserves the many-to-many utility↔county structure. County names are deterministically normalized and matched by USPS state × normalized county name to the official 2024 Census county Gazetteer, yielding Census GEOID; NOAA county exposure uses `STATE_FIPS + CZ_FIPS` for `CZ_TYPE=C`. No fuzzy utility-name matching or customer allocation across counties is introduced. / utility·county 다대다 구조를 보존하고 fuzzy utility matching 및 county별 고객 가중치를 만들지 않는다.

A valid Census county with no NOAA 2024 event row is retained as a zero-recorded-event county, not treated as an unmapped geography. / Census상 유효하지만 NOAA event가 없는 county는 미매핑이 아니라 0-event로 보존한다.

## Evidence boundary / 증거 경계

This PASS means **JOIN_READY only**. It does not establish:
- an AMI effect on reliability;
- a storm effect on SAIDI/SAIFI;
- causal resilience;
- predictive utility;
- generalization, novelty, or decision utility;
- independent exposure for counties shared by multiple utilities.

Any relationship test must be separately selected and preregistered after Stage 0, with explicit treatment of storm aggregation, major-event-day definitions, reliability-reporting comparability, many-to-many exposure and dependence. / 효과실험은 Stage 0 재선정과 별도 사전등록이 필요하다.

## Durable evidence / 영속 근거

- `research/US-UTIL-F01/JOIN_QUALIFICATION.md`
- `research/US-UTIL-F01/UTILITY_COUNTY_JOIN_MAP.csv`
- `research/US-UTIL-F01/COUNTY_CROSSWALK_DIAGNOSTIC.csv`
- `research/US-UTIL-F01/JOIN_SOURCE_MANIFEST.csv`
- `research/US-UTIL-F01/SOURCE_CARDINALITY_PREFLIGHT.md`

Incremental monetary cost remained **0 USD**.
'''
    RESULT.write_text(result, encoding="utf-8")

    claim = f'''---
id: CLM-139
type: claim
created: 2026-09-11
state: OBSERVED_DERIVED_VALIDATED
---

# CLM-139 — US-UTIL-F01 passes deterministic nationwide utility-county join feasibility
# CLM-139 — US-UTIL-F01 전국 utility-county 결정론적 결합 feasibility PASS

Under the frozen outcome-blind gate, EIA-861 2024 final Reliability / Advanced Metering / Service Territory identities and NOAA 2024 Storm Events can be joined through an explicit utility→county→Census GEOID→NOAA county-FIPS route. / 고정 결과비사용 gate에서 EIA utility→county→Census GEOID→NOAA county-FIPS 경로가 성립한다.

Verified support:
- **842** reliability utilities have complete deterministic county qualification and AMI support;
- **6,341** qualified utility×county mappings remain;
- the frozen >=300 / >=250 / >=1,000 thresholds all pass;
- NOAA 2024 county-key route is reproducible;
- no SAIDI/SAIFI magnitude, AMI meter magnitude, or relationship was used for qualification.

**Gate:** `{GATE}`

**Verification:** `V3_OUTCOME_BLIND_JOIN_REPRODUCED`

This claim is JOIN_READY only and authorizes no AMI/reliability effect claim. / JOIN_READY 주장일 뿐 효과 주장을 승인하지 않는다.
'''
    CLAIM.write_text(claim, encoding="utf-8")

    decision = f'''---
id: DEC-130
type: decision
created: 2026-09-11
status: ACTIVE
---

# DEC-130 — Accept US-UTIL-F01 JOIN_READY and return to Stage 0
# DEC-130 — US-UTIL-F01 JOIN_READY 수용 및 Stage 0 복귀

## Decision / 결정

Accept **`{GATE}`** for Issue #94 and classify `C-US-005` as `JOIN_READY` only. / #94를 JOIN_READY로 확정한다.

## Basis / 근거

The frozen structural thresholds all pass prospectively:
- 842 fully county-qualified reliability utilities (minimum 300);
- 842 with AMI support (minimum 250);
- 6,341 qualified utility×county mappings (minimum 1,000);
- reproducible NOAA 2024 county FIPS route.

The join uses EIA utility IDs, deterministic county qualification through Census GEOID, and preserves utility↔county many-to-many exposure. No outcome magnitude or relationship was used to select or repair mappings. / 결과값 없이 identity·county 구조만으로 통과했다.

## Branch boundary / 분기 경계

Do **not** automatically start an AMI × storm × SAIDI/SAIFI relationship test. Return to Stage 0 portfolio control. / 효과실험 자동진입 금지, Stage 0로 복귀한다.

Any descendant must compete against independent portfolio candidates and, if selected, preregister before outcomes:
- one reliability outcome/denominator and reporting-comparability rule;
- one storm exposure aggregation and time window;
- major-event-day treatment;
- county-sharing/dependence handling;
- minimum useful effect and falsification rule.

Incremental monetary cost remains **0 USD**.
'''
    DECISION.write_text(decision, encoding="utf-8")

    readme = README.read_text(encoding="utf-8")
    readme = readme.replace("state: ACTIVE_SOURCE_PREFLIGHT", "state: COMPLETED_JOIN_READY")
    readme = readme.replace("decision: DEC-129", "decision: DEC-130")
    old_next = "## Exact next action / 정확한 다음 행동\n\nRun source-byte/schema/cardinality preflight. Persist hashes, member/sheet names, selected non-outcome headers, identity counts, county-key counts and exclusions. / source hash·schema·identity cardinality만 기록한다."
    new_next = f'''## Final disposition / 최종 처분

**`{GATE}`**

Verified: **842** completely county-qualified reliability utilities with AMI support and **6,341** qualified utility×county mappings under the deterministic Census GEOID→NOAA FIPS route. No reliability/AMI magnitude or relationship was opened. / 결과값 비사용 JOIN_READY다.

## Exact next action / 정확한 다음 행동

Return to **Stage 0 portfolio control**. Do not automatically fit an AMI × storm × reliability model. Any relationship descendant requires separate portfolio selection and preregistration. / Stage 0로 복귀하며 효과실험 자동진입을 금지한다.'''
    require_once(readme, old_next, "README next-action replacement")
    readme = readme.replace(old_next, new_next)
    README.write_text(readme, encoding="utf-8")

    ledger = CLAIM_LEDGER.read_text(encoding="utf-8")
    claim_row = "| `CLM-139` | Outcome-blind US-UTIL-F01 deterministically qualifies 842 EIA-861 reliability utilities with AMI support and 6,341 utility×county mappings through Census GEOID to NOAA 2024 county FIPS; frozen structural gate `PASS_US_UTIL_F01_JOIN_READY`. No SAIDI/SAIFI, AMI magnitude or relationship was used. / 결과값 비사용 상태에서 842개 utility·6,341개 utility×county 결합으로 JOIN_READY PASS. | `OBSERVED/DERIVED/VALIDATED` | `V3_OUTCOME_BLIND_JOIN_REPRODUCED` | `research/US-UTIL-F01/RESULT.md`; `JOIN_QUALIFICATION.md`; `registry/CLM-139.md`; Issue #94 | 2026-09-11 | active-join-ready |\n\n"
    if "`CLM-139`" not in ledger:
        require_once(ledger, "## Rule / 규칙", "claim-ledger insertion anchor")
        ledger = ledger.replace("## Rule / 규칙", claim_row + "## Rule / 규칙")
    CLAIM_LEDGER.write_text(ledger, encoding="utf-8")

    dlog = DECISION_LOG.read_text(encoding="utf-8")
    dec_line = "- [DEC-130](DEC-130.md): accept US-UTIL-F01 as `PASS_US_UTIL_F01_JOIN_READY`; classify C-US-005 JOIN_READY only and return to Stage 0 without automatic AMI×storm×reliability effect testing. / JOIN_READY만 수용하고 효과실험 자동진입 없이 Stage 0 복귀.\n"
    if "[DEC-130]" not in dlog:
        anchor = "- [DEC-129](DEC-129.md): R11 selects C-US-005 / US-UTIL-F01 fresh utility AMI × storm × reliability join feasibility; first gate remains outcome-blind. / 신규 utility AMI×폭풍×신뢰도 결합 feasibility 선정·첫 gate 효과값 비사용.\n"
        require_once(dlog, anchor, "decision-log insertion anchor")
        dlog = dlog.replace(anchor, anchor + dec_line)
    DECISION_LOG.write_text(dlog, encoding="utf-8")

    STATUS.write_text(f'''---
checkpoint_id: CHK-20260911-US-UTIL-F01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 94
last_completed_research: US-UTIL-F01
last_decision: DEC-130
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_UTIL_F01_JOIN_READY_PASS__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

## Latest completed research / 최신 완료 연구

Issue #94 `US-UTIL-F01` resolves to:

**`{GATE}`**

Outcome-blind verified structure:
- 842 fully county-qualified reliability utilities with AMI support;
- 6,341 qualified utility×county mappings;
- deterministic EIA utility ID → Service Territory county → Census GEOID → NOAA county-FIPS route;
- frozen source/cardinality thresholds all pass;
- no SAIDI/SAIFI magnitude, AMI magnitude, or relationship opened.

## Evidence status / 증거 상태

`C-US-005` is **JOIN_READY only**. It is not RELATIONSHIP_TESTED, GENERALIZATION_TESTED, NOVELTY_ASSESSED, UTILITY_TESTED, or an INNOVATION_CANDIDATE. / 효과·일반화·신규성·효용은 미검증이다.

## Exact next action / 정확한 다음 행동

Return to **Stage 0 portfolio control** with no active research Issue. / 활성 연구 Issue 없이 Stage 0로 복귀한다.

Do not automatically open AMI × storm × reliability outcomes. Recompare this descendant against independent opportunities; any selected experiment must preregister outcome comparability, storm aggregation/MED treatment, many-to-many dependence and materiality before values are opened. / 효과실험 자동진입 금지.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    HANDOFF.write_text(f'''---
checkpoint_id: CHK-20260911-US-UTIL-F01-PASS-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 94
last_completed_research: US-UTIL-F01
last_decision: DEC-130
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

US-UTIL-F01 is complete under DEC-130 with:

**`{GATE}`**

Do not rerun the F01 source/county qualification by default. / F01 기본 재실행 금지.

Canonical evidence:
- `research/US-UTIL-F01/RESULT.md`;
- `research/US-UTIL-F01/JOIN_QUALIFICATION.md`;
- `research/US-UTIL-F01/UTILITY_COUNTY_JOIN_MAP.csv`;
- `registry/CLM-139.md`;
- `registry/DEC-130.md`.

Verified support: **842** complete reliability+AMI utility identities and **6,341** utility×county mappings. / 구조 gate PASS다.

## Boundary / 경계

This is JOIN_READY only. No SAIDI/SAIFI magnitude, AMI magnitude, storm-reliability coefficient, causality, predictive utility or resilience benefit has been established. / 효과·인과·예측·효용 주장은 없다.

## Exact next action / 정확한 다음 행동

Return to **Stage 0 portfolio control** with no active research Issue. / 활성 연구 Issue 없이 Stage 0로 복귀한다.

A US-UTIL relationship descendant may re-enter only through a fresh portfolio selection and a preregistered outcome/exposure/dependence contract. / 후속 효과실험은 새 portfolio 선정·사전등록 필요.

Cost remains **0 USD**; potentially billable work requires explicit prior approval.
''', encoding="utf-8")

    CHECKPOINT.write_text(json.dumps({
        "checkpoint_id": "CHK-20260911-US-UTIL-F01-PASS-PORTFOLIO-RETURN",
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 94,
        "last_completed_research": "US-UTIL-F01",
        "last_decision": "DEC-130",
        "updated": "2026-09-11",
    }, indent=2) + "\n", encoding="utf-8")

    print(GATE)
    print("qualified_utilities=842;qualified_utility_county=6341;relationship_computed=false")


if __name__ == "__main__":
    main()
