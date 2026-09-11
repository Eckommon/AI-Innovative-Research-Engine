#!/usr/bin/env python3
"""Finalize US-UTIL-F02 from already committed outcome-blind artifacts.

No source is downloaded and no Reliability/AMI magnitude is parsed here.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research" / "US-UTIL-F02"
REG = ROOT / "registry"

RESULT = RESEARCH / "RESULT.md"
README = RESEARCH / "README.md"
CLAIM_LEDGER = REG / "CLAIM_LEDGER.md"
DECISION_LOG = REG / "DECISION_LOG.md"
STATUS = ROOT / "STATUS.md"
HANDOFF = ROOT / "context" / "SESSION_HANDOFF.md"
CHECKPOINT = ROOT / "context" / "checkpoint.json"

GATE = "PASS_US_UTIL_F02_PANEL_DESIGN_READY"
RUN = "34553499300"
RESULT_COMMIT = "65cebe8cc2feb6ccdc4193469a541b500ee62e2b"


def require(text: str, token: str) -> None:
    if token not in text:
        raise RuntimeError(f"Required token missing: {token}")


def main() -> None:
    result = RESULT.read_text(encoding="utf-8")
    for token in [
        GATE,
        "**883** (threshold 500)",
        "**819** (threshold 300)",
        "**4,857** (threshold 2,000)",
        "**37,156** (threshold 8,000)",
        "Reliability basis route identifiable all six years: **True**",
        "AMI numerator/denominator header route identifiable all six years: **True**",
        "NOAA county-key route reproducible all six years: **True**",
        "reliability_magnitudes_parsed: false",
        "ami_magnitudes_parsed: false",
        "relationship_computed: false",
    ]:
        require(result, token)

    claim = f'''---
id: CLM-140
type: claim
created: 2026-09-11
state: OBSERVED_DERIVED_VALIDATED
---

# CLM-140 — US-UTIL-F02 2019–2024 panel design is source-comparable
# CLM-140 — US-UTIL-F02 2019–2024 panel 설계 source 비교가능성 PASS

Under the prospectively frozen, outcome-blind 2019–2024 contract, official EIA-861 final annual files plus year-matched Census county Gazetteers and NOAA Storm Events support a reproducible longitudinal utility-panel design. / 사전고정 결과 비사용 계약에서 다년 utility panel 설계가 재현 가능하다.

Validated support from Run `{RUN}`:
- **883** utilities have Reliability + Advanced Metering + Service Territory support in at least 4 of 6 years;
- **819** utilities have at least 4 years with prospectively identifiable IEEE-with-MED SAIDI/SAIFI support plus complete deterministic geography;
- **4,857** repeated-support utility-year observations;
- **37,156** qualified utility-year×county mappings;
- Reliability-basis, AMI numerator/denominator header, and NOAA county-key routes are identifiable/reproducible in all six years.

The gate is **`{GATE}`**.

No SAIDI/SAIFI/CAIDI magnitude, AMI/AMR/standard-meter count magnitude, storm severity/damage magnitude, or relationship coefficient was used to qualify the panel. / 효과값은 자격판정에 사용하지 않았다.

This claim is **PANEL_DESIGN_READY only**. It does not establish an AMI effect, storm effect, resilience benefit, causality, novelty, predictive utility, or innovation status.

**Verification:** `V3_PREREGISTERED_LONGITUDINAL_SOURCE_AND_CARDINALITY_REPRODUCED`

Evidence:
- GitHub Actions Run `{RUN}`;
- result commit `{RESULT_COMMIT}`;
- `research/US-UTIL-F02/RESULT.md`;
- `research/US-UTIL-F02/YEAR_SCHEMA_SUPPORT.csv`;
- `research/US-UTIL-F02/UTILITY_YEAR_SUPPORT.csv`;
- `research/US-UTIL-F02/QUALIFIED_UTILITY_YEAR_COUNTY.csv`.
'''
    (REG / "CLM-140.md").write_text(claim, encoding="utf-8")

    decision = f'''---
id: DEC-133
type: decision
created: 2026-09-11
status: ACTIVE
---

# DEC-133 — Accept US-UTIL-F02 PANEL_DESIGN_READY PASS and return to Stage 0
# DEC-133 — US-UTIL-F02 PANEL_DESIGN_READY PASS 수용 및 Stage 0 복귀

## Decision / 결정

Accept Run `{RUN}` as:

**`{GATE}`**

and complete Issue #96 after this durable checkpoint is committed. / durable checkpoint 반영 후 #96을 완료 종결한다.

## Basis / 근거

All frozen DEC-132 thresholds pass without opening Reliability or AMI magnitudes:
- 883 >=4/6-year triple-schedule utilities (threshold 500);
- 819 >=4-year comparable IEEE-with-MED + geography-complete utilities (threshold 300);
- 4,857 qualified utility-years (threshold 2,000);
- 37,156 qualified utility-year×county mappings (threshold 8,000);
- Reliability basis route, AMI header route and NOAA county-key route pass for all six years.

Diagnostic Run `34553361343` is not scientific HOLD evidence: it selected documentation/auxiliary worksheets and yielded 2024 identity counts inconsistent with the already validated F01 source. `BASIS_HEADER_RESOLUTION.md` fixed only source-schema selection before any magnitude was opened. / 초기 0-count는 parser 오류였으며 연구 HOLD로 사용하지 않는다.

## Promotion boundary / 승격 경계

**PANEL_DESIGN_READY ≠ RELATIONSHIP_TESTED.**

Do not automatically open a US-UTIL E01. Return to Stage 0 portfolio control. / E01 자동 개시 금지, Stage 0 복귀.

A future relationship experiment may proceed only after fresh portfolio selection and preregistration of:
- one Reliability outcome and reporting basis;
- exact AMI penetration numerator/denominator;
- storm exposure aggregation and time window;
- major-event-day treatment;
- utility×county many-to-many/dependence handling;
- confounding/baseline specification;
- falsification and minimum materiality;
- novelty and decision-utility assessment plan.

Generic AMI outage-management/resilience mechanisms already have prior official/research precedent, so a favorable coefficient alone cannot establish novelty. / 유리한 계수만으로 신규성 승격 금지.

Incremental monetary cost remains **0 USD**.
'''
    (REG / "DEC-133.md").write_text(decision, encoding="utf-8")

    readme = README.read_text(encoding="utf-8")
    readme = readme.replace("state: ACTIVE_SOURCE_COMPARABILITY_PREFLIGHT", "state: COMPLETED_PASS_PANEL_DESIGN_READY")
    if "final_gate:" not in readme:
        readme = readme.replace("contract_decision: DEC-132", "contract_decision: DEC-132\nfinal_decision: DEC-133\nclaim_basis: CLM-140\nfinal_gate: PASS_US_UTIL_F02_PANEL_DESIGN_READY")
    if "## Final disposition / 최종 처분" not in readme:
        readme += f'''\n\n## Final disposition / 최종 처분\n\nRun `{RUN}` resolves F02 as **`{GATE}`** under DEC-133 / CLM-140.\n\nVerified repeated support: **883** triple-schedule utilities, **819** comparable >=4-year utilities, **4,857** utility-years and **37,156** utility-year×county mappings. All six years have identifiable Reliability basis, AMI field routes and NOAA county-key routes.\n\nNo Reliability/AMI magnitude or relationship was opened. A later E01 is not automatically authorized. / 효과실험 자동승격 금지.\n'''
    README.write_text(readme, encoding="utf-8")

    ledger = CLAIM_LEDGER.read_text(encoding="utf-8")
    row = f'''| `CLM-140` | Under the frozen 2019–2024 outcome-blind contract, US-UTIL-F02 retains 883 >=4/6-year triple-schedule utilities, 819 >=4-year comparable utilities, 4,857 qualified utility-years and 37,156 utility-year×county mappings; all six years have identifiable Reliability-basis, AMI-header and NOAA county routes, yielding `{GATE}` without reading outcome/exposure magnitudes. / 결과 비사용 다년 panel 구조 PASS. | `OBSERVED/DERIVED/VALIDATED` | `V3_PREREGISTERED_LONGITUDINAL_SOURCE_AND_CARDINALITY_REPRODUCED` | Run `{RUN}`; `research/US-UTIL-F02/RESULT.md`; `registry/CLM-140.md`; Issue #96 | 2026-09-11 | active-panel-design-ready |\n\n'''
    if "`CLM-140`" not in ledger:
        ledger = ledger.replace("## Rule / 규칙", row + "## Rule / 규칙")
    CLAIM_LEDGER.write_text(ledger, encoding="utf-8")

    dlog = DECISION_LOG.read_text(encoding="utf-8")
    additions = []
    if "[DEC-131]" not in dlog:
        additions.append("- [DEC-131](DEC-131.md): R12 selects US-UTIL-F02 longitudinal comparability preflight before any relationship / 효과검증 전 다년 비교가능성 gate 선정.")
    if "[DEC-132]" not in dlog:
        additions.append("- [DEC-132](DEC-132.md): freeze 2019–2024 outcome-blind F02 panel-feasibility contract / 2019–2024 결과 비사용 panel 계약 고정.")
    if "[DEC-133]" not in dlog:
        additions.append("- [DEC-133](DEC-133.md): accept US-UTIL-F02 PANEL_DESIGN_READY PASS and return to Stage 0 / F02 PASS 수용·Stage 0 복귀.")
    if additions:
        dlog = dlog.rstrip() + "\n" + "\n".join(additions) + "\n"
    DECISION_LOG.write_text(dlog, encoding="utf-8")

    checkpoint_id = "CHK-20260911-US-UTIL-F02-PASS-PORTFOLIO-RETURN"
    STATUS.write_text(f'''---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: 96
last_completed_research: US-UTIL-F02
last_decision: DEC-133
updated: 2026-09-11
---

# Project Status / 프로젝트 상태

**State / 상태:** `US_UTIL_F02_PANEL_DESIGN_READY_PASS__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

## Latest completed research / 최신 완료 연구

Issue #96 `US-UTIL-F02` resolves to:

**`{GATE}`**

Verified outcome-blind 2019–2024 support:
- 883 utilities with Reliability+AMI+Service Territory in >=4/6 years;
- 819 utilities with >=4 comparable IEEE-with-MED + geography-complete years;
- 4,857 qualified utility-years;
- 37,156 utility-year×county mappings;
- Reliability/AMI/NOAA routes valid in all six years.

No Reliability/AMI magnitude or relationship was opened. / 효과값 비사용.

## Exact next action / 정확한 다음 행동

Return to **Stage 0 portfolio control**. Do not automatically open a US-UTIL relationship experiment. Recompare a rigorously preregistered US-UTIL descendant against independent opportunities, including C-US-006 inland-waterway hydrology × lock-delay feasibility. / 다음은 portfolio opportunity-cost 재선정이다.

Incremental monetary cost remains **0 USD**.
''', encoding="utf-8")

    HANDOFF.write_text(f'''---
checkpoint_id: {checkpoint_id}
active_issue: none
active_research: NONE
last_completed_issue: 96
last_completed_research: US-UTIL-F02
last_decision: DEC-133
updated: 2026-09-11
---

# Session Handoff / 세션 인수인계

## Canonical restart point / 정확한 재개점

US-UTIL-F02 is complete under DEC-133 with:

**`{GATE}`**

Do not rerun F01/F02 by default and do not open SAIDI/SAIFI or AMI magnitudes automatically. / F01/F02 기본 재실행·효과값 자동개방 금지.

Canonical support:
- 883 >=4/6-year triple-schedule utilities;
- 819 >=4-year comparable utilities;
- 4,857 qualified utility-years;
- 37,156 utility-year×county mappings;
- 6/6 Reliability basis, AMI field-route and NOAA county-route support.

Canonical evidence: `research/US-UTIL-F02/RESULT.md`, `BASIS_ADJUDICATION.md`, `BASIS_HEADER_RESOLUTION.md`, `registry/CLM-140.md`, `registry/DEC-133.md`.

## Exact next action / 정확한 다음 행동

Return to **Stage 0** with no active research issue. Compare a potential US-UTIL preregistered relationship design against independent portfolio opportunities before opening magnitudes. / 효과실험 자동 승격 금지.

If US-UTIL is selected later, first freeze one Reliability outcome/basis, AMI penetration definition, storm exposure aggregation/window, MED treatment, dependence, baseline/confounding, falsification/materiality, and novelty/utility plan.

Cost remains **0 USD**.
''', encoding="utf-8")

    CHECKPOINT.write_text(json.dumps({
        "checkpoint_id": checkpoint_id,
        "active_issue": "none",
        "active_research": "NONE",
        "last_completed_issue": 96,
        "last_completed_research": "US-UTIL-F02",
        "last_decision": "DEC-133",
        "updated": "2026-09-11",
    }, indent=2) + "\n", encoding="utf-8")

    print(f"FINALIZE_US_UTIL_F02_PASS;gate={GATE};run={RUN}")


if __name__ == "__main__":
    main()
