#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-12"
RUN = "34689346777"
AUDIT_RUN = "34690867196"
REVALIDATION_RUN = "34690978853"

status_path = ROOT / "STATUS.md"
handoff_path = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_path = ROOT / "context" / "checkpoint.json"
claim_ledger_path = ROOT / "registry" / "CLAIM_LEDGER.md"
decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
readme_path = ROOT / "research" / "CA-GRAIN-E02" / "README.md"
result_path = ROOT / "research" / "CA-GRAIN-E02" / "RESULT.md"
primary_path = ROOT / "research" / "CA-GRAIN-E02" / "STAGE_B_PRIMARY_RESULT.json"
target_audit_path = ROOT / "research" / "CA-GRAIN-E02" / "TARGET_DUPLICATE_PROVENANCE.json"
reval_path = ROOT / "research" / "CA-GRAIN-F01" / "DATE_SEMANTICS_REVALIDATION.json"
claim_path = ROOT / "registry" / "CLM-153.md"
decision_path = ROOT / "registry" / "DEC-154.md"
f01_erratum_path = ROOT / "research" / "CA-GRAIN-F01" / "TECHNICAL_ERRATUM_GSW_DATE_SEMANTICS.md"
e01_erratum_path = ROOT / "research" / "CA-GRAIN-E01" / "TECHNICAL_ERRATUM_GSW_DATE_SEMANTICS.md"
e02_adj_path = ROOT / "research" / "CA-GRAIN-E02" / "TECHNICAL_ADJUDICATION.md"

status = status_path.read_text(encoding="utf-8")
result = result_path.read_text(encoding="utf-8")
primary = json.loads(primary_path.read_text(encoding="utf-8"))
audit = json.loads(target_audit_path.read_text(encoding="utf-8"))
reval = json.loads(reval_path.read_text(encoding="utf-8"))
assert "active_issue: 110" in status
assert "last_decision: DEC-153" in status
assert "gate: HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL" in result
assert primary["gate"] == "HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL"
assert primary["primary"] is None
assert audit["classification"] == "MONDAY_COLLISION_DISTINCT_SOURCE_DATES"
assert audit["values_read"] is False and audit["relationship_computed"] is False
assert audit["crop_files"] == ["2024-25"]
assert set(audit["raw_week_ending_dates"]) == {"07/06/2025", "08/06/2025"}
ids = {(x["grain_week"], x["raw_week_ending_date"]) for x in audit["source_identities"]}
assert ids == {("44", "08/06/2025"), ("48", "07/06/2025")}
assert reval["common_official_week_keys_both_carriers"] >= 80
assert reval["family_official_week_counts"]["Primary/Deliveries/Current Week"] >= 80
assert reval["family_official_week_counts"]["Process/Producer Deliveries/Current Week"] >= 80
assert not claim_path.exists() and not decision_path.exists()

status_path.write_text("""---
checkpoint_id: CHK-20260912-CA-GRAIN-E02-HOLD-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 110
last_completed_research: CA-GRAIN-E02
last_decision: DEC-154
updated: 2026-09-12
---

# Project Status / 프로젝트 상태

**State / 상태:** `CA_GRAIN_E02_STRUCTURAL_HOLD__PORTFOLIO_RETURN__NO_ACTIVE_RESEARCH_ISSUE`

CA-GRAIN-E02 completed at **`HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL`** before model fitting. The initial technical run was invalidated for slash-date parser semantics; corrected Run `34689346777` still encountered a duplicate component week under the preregistered explicit-source-date → ISO-Monday rule. Targeted value-blind audit showed this is a collision between two distinct source identities in the same 2024-25 file: Grain Week 44 / raw `08/06/2025` and Grain Week 48 / raw `07/06/2025` collapse to the same Monday under a single fixed slash-date interpretation. Official CGC archive semantics identify these as 2025-06-08 and 2025-07-06 respectively.

Issue #110 froze explicit source dates as the temporal identity. Replacing that rule post-value with `grain_week`, dropping a week, or choosing a date interpretation by fit would be a prohibited repair. No relationship model was fitted.

A separate value-blind technical revalidation using official `grain_week` schedule identities establishes 103 common GSW×TC weeks and preserves the earlier F01 feasibility PASS and E01 semantic-ambiguity HOLD; prior raw-date-derived counts must not be cited.

## Exact next action / 정확한 다음 행동

Return to Stage 0 portfolio control. Do not rerun or repair E02. Any future Canadian grain descendant that uses official `grain_week` rather than raw slash dates must be separately selected and preregistered against independent alternatives before values are opened.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260912-CA-GRAIN-E02-HOLD-PORTFOLIO-RETURN
active_issue: none
active_research: NONE
last_completed_issue: 110
last_completed_research: CA-GRAIN-E02
last_decision: DEC-154
updated: 2026-09-12
---

# Session Handoff / 세션 인수인계

CA-GRAIN-E02 / Issue #110 is terminal at **`HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL`**.

Corrected Run `34689346777` did not fit the preregistered relationship model. Targeted value-blind audit Run `34690867196` proved the remaining structural collision is between distinct source week identities in the 2024-25 GSW file: Week 44 raw `08/06/2025` and Week 48 raw `07/06/2025`. The official CGC archive maps those week identities to 2025-06-08 and 2025-07-06. Issue #110 had frozen explicit source-date normalization, so switching post hoc to `grain_week` is not permitted.

Technical revalidation Run `34690978853`, using official crop-year week identities without values, yields **103** common GSW×TC weeks and 103 weeks for each E01 upstream semantic family. Therefore F01 PASS and E01 ambiguity HOLD remain valid, while their earlier raw-date-derived counts are superseded by errata.

Canonical restart: **Stage 0 portfolio control**. E02 may not be repaired or rerun. A grain-week-keyed descendant, if ever considered, must be a new separately selected/preregistered branch. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260912-CA-GRAIN-E02-HOLD-PORTFOLIO-RETURN",
    "active_issue": "none",
    "active_research": "NONE",
    "last_completed_issue": 110,
    "last_completed_research": "CA-GRAIN-E02",
    "last_decision": "DEC-154",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

claim_path.write_text(f"""---
id: CLM-153
type: claim
created: {DATE}
issue: 110
status: active
---

# CLM-153 — CA-GRAIN-E02 terminates at structural temporal-identity HOLD before model fitting

Corrected Run `{RUN}` terminates at **`HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL`** before fitting. Targeted value-blind audit Run `{AUDIT_RUN}` shows the remaining duplicate component week is not an exact source-row duplicate: within the 2024-25 GSW file, Grain Week 44 / raw `08/06/2025` and Grain Week 48 / raw `07/06/2025` are distinct source identities that collide under a single fixed slash-date-to-Monday interpretation. Official CGC archive semantics distinguish their week endings as 2025-06-08 and 2025-07-06.

Because Issue #110 prospectively froze **explicit source date → ISO Monday** temporal identity, substituting `grain_week`, deleting a week, or choosing a parsing convention after values were authorized would change the preregistered design. E02 therefore remains structural HOLD and no relationship estimate exists.

Value-blind revalidation Run `{REVALIDATION_RUN}` separately confirms 103 official week-identity common keys across GSW and both TC carriers, so the earlier F01 feasibility PASS and E01 semantic-ambiguity HOLD remain intact; their prior raw-date-derived week-count details are superseded. Cost: **0 USD**.
""", encoding="utf-8")

decision_path.write_text(f"""---
id: DEC-154
type: decision
created: {DATE}
issue: 110
status: accepted
---

# DEC-154 — Finalize CA-GRAIN-E02 as structural HOLD and return to Stage 0

Finalize Issue #110 at **`HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL`**. Do not fit the primary relationship, deduplicate the collided week, reinterpret slash dates selectively, or replace the frozen explicit-date temporal identity with `grain_week` inside E02.

Record technical errata for F01 and E01: their terminal gates remain valid after independent value-blind week-identity revalidation, but earlier raw-date-derived temporal counts must not be cited. Return to Stage 0 portfolio control. Any future Canadian grain descendant using `grain_week` must be a new selection and preregistration rather than an E02 repair.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

claim_ledger = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-153`" not in claim_ledger
claim_ledger_path.write_text(claim_ledger.rstrip() + f"""

| `CLM-153` | CA-GRAIN-E02 terminates at structural temporal-identity HOLD before model fitting; distinct GSW Week 44/48 source identities collide under frozen explicit-date normalization, and post-value grain_week substitution is prohibited. / E02는 시간 식별 구조 HOLD로 모형 적합 전 종료. | `OBSERVED/DERIVED/VALIDATED` | `V3_PREREGISTERED_RELATIONSHIP_GATE` | Run `{RUN}`; audit `{AUDIT_RUN}`; revalidation `{REVALIDATION_RUN}`; `research/CA-GRAIN-E02/RESULT.md`; `TARGET_DUPLICATE_PROVENANCE.json` | {DATE} | active |
""", encoding="utf-8")

decision_log = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-154`" not in decision_log
decision_log_path.write_text(decision_log.rstrip() + f"""

| `DEC-154` | {DATE} | Finalize CA-GRAIN-E02 as `HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL`; prohibit post-value temporal repair; preserve F01/E01 gates with technical date-semantics errata; return Stage 0. / E02 구조 HOLD 확정·사후 시간키 구제 금지·Stage 0 복귀. | Frozen explicit-date identity collides for distinct source weeks; official grain_week revalidation preserves prior non-effect gates but cannot repair E02. | Issue #110; `CLM-153`; Runs `{RUN}`, `{AUDIT_RUN}`, `{REVALIDATION_RUN}` | active |
""", encoding="utf-8")

readme = readme_path.read_text(encoding="utf-8")
assert "state: ACTIVE_PREREGISTERED_RELATIONSHIP_TEST" in readme
readme = readme.replace("state: ACTIVE_PREREGISTERED_RELATIONSHIP_TEST", "state: COMPLETED_HOLD_TEMPORAL_IDENTITY", 1)
readme = readme.replace("magnitudes_opened: false", "magnitudes_opened: authorized_but_no_model_fitted", 1)
readme_path.write_text(readme.rstrip() + f"""

## Final disposition / 최종 판정

- gate: **`HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL`**
- corrected execution: `{RUN}`
- targeted provenance audit: `{AUDIT_RUN}`
- technical week-identity revalidation: `{REVALIDATION_RUN}`
- primary relationship model: **not fitted**
- cause: frozen explicit-date normalization cannot uniquely preserve distinct GSW Week 44 and Week 48 temporal identities
- decision: `DEC-154`
- restart: **Stage 0 portfolio control**

E02 is terminal under its frozen temporal contract. Do not repair it by switching to `grain_week` after value authorization.
""", encoding="utf-8")

f01_erratum_path.write_text(f"""# Technical Erratum — GSW date semantics / 기술 정정

Applies to **CA-GRAIN-F01**. Terminal gate remains **`PASS_CA_GRAIN_F01_WEEKLY_PANEL_FEASIBLE`**.

The original F01 corrected probe still used a fixed slash-date parser for GSW `week_ending_date`; later E02 targeted provenance showed that raw slash strings cannot safely be treated with one locale convention across the frozen files. Therefore the earlier F01 raw-date-derived figure of **81 common weekly keys is superseded and must not be cited**.

Value-blind technical revalidation Run `{REVALIDATION_RUN}` uses the official CGC `grain_week` schedule identity and finds **103 common official week keys** with both frozen TC carriers, above the preregistered F01 threshold of 80. Source access, two-carrier identity, and no-value boundary remain unchanged. F01 PASS therefore remains valid.

This erratum does not authorize any relationship test or alter E02. Cost: **0 USD**.
""", encoding="utf-8")

e01_erratum_path.write_text(f"""# Technical Erratum — GSW date semantics / 기술 정정

Applies to **CA-GRAIN-E01 Stage A**. Terminal gate remains **`HOLD_CA_GRAIN_E01_EXPOSURE_IDENTITY_AMBIGUOUS`**.

The E01 Stage A probe used the same fixed slash-date interpretation for some temporal-support counts. Those raw-date-derived counts, including the previously recorded one-week-lag support of zero, are **superseded and must not be cited**.

Value-blind revalidation Run `{REVALIDATION_RUN}` establishes **103 official week identities** for each surviving GSW family (`Primary / Deliveries / Current Week` and `Process / Producer Deliveries / Current Week`) and 103 common official week keys with both TC carriers. E01's HOLD did not depend on the bad temporal count; it depended on two same-level semantic exposure families surviving the frozen identity screen. The ambiguity HOLD therefore remains valid.

This erratum does not narrow E01 post hoc and does not authorize Stage B. Cost: **0 USD**.
""", encoding="utf-8")

e02_adj_path.write_text(f"""# Technical Adjudication — CA-GRAIN-E02 temporal identity

## Valid execution

Corrected Run `{RUN}` supersedes the earlier invalid parser run and remains the valid E02 execution. It terminated before model fitting at **`HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL`**.

## Targeted provenance

Audit Run `{AUDIT_RUN}` inspected no `Ktonnes` or dwell values. It found 120 matching structural rows at the collided normalized week: 60 components for each of two distinct 2024-25 source identities:

- Grain Week **44**, raw `08/06/2025`; official CGC week ending **2025-06-08**
- Grain Week **48**, raw `07/06/2025`; official CGC week ending **2025-07-06**

Thus the collision is a temporal-identity problem, not duplicated magnitude rows.

## Adjudication

Issue #110 froze explicit source-date normalization. After magnitude access was authorized, switching E02 to `grain_week`, dropping either identity, or selecting a slash-date interpretation would change the frozen design. No such repair is allowed. E02 is terminal HOLD.

Separate value-blind revalidation Run `{REVALIDATION_RUN}` may correct historical F01/E01 structural counts because those gates did not depend on an effect estimate; it cannot rescue E02.

Incremental monetary cost: **0 USD**.
""", encoding="utf-8")

print(json.dumps({
    "gate": "HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL",
    "claim": "CLM-153",
    "decision": "DEC-154",
    "relationship_computed": False,
    "cost_usd": 0,
}))
