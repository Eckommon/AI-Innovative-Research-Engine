#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATE = "2026-09-12"

status_path = ROOT / "STATUS.md"
handoff_path = ROOT / "context" / "SESSION_HANDOFF.md"
checkpoint_path = ROOT / "context" / "checkpoint.json"
claim_ledger_path = ROOT / "registry" / "CLAIM_LEDGER.md"
decision_log_path = ROOT / "registry" / "DECISION_LOG.md"
claim_path = ROOT / "registry" / "CLM-155.md"
dec157_path = ROOT / "registry" / "DEC-157.md"
dec158_path = ROOT / "registry" / "DEC-158.md"
discovery_dir = ROOT / "research" / "DISCOVERY-R01"
f01_dir = ROOT / "research" / "US-WW-F01"
f01_dir.mkdir(parents=True, exist_ok=True)

status = status_path.read_text(encoding="utf-8")
assert "active_issue: 113" in status
assert "active_research: DISCOVERY-R01" in status
assert "last_decision: DEC-156" in status
for p in (claim_path, dec157_path, dec158_path, discovery_dir / "RESULT.md", f01_dir / "README.md"):
    assert not p.exists(), f"already exists: {p}"

(discovery_dir / "RESULT.md").write_text("""---
id: DISCOVERY-R01-RESULT
type: fresh-opportunity-discovery
created: 2026-09-12
issue: 113
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: US-WW-001
selected_gate: US-WW-F01
next_issue: 114
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# DISCOVERY-R01 Result — Fresh Cross-Source Bottleneck Scan
# DISCOVERY-R01 결과 — 신규 cross-source bottleneck 탐색

## Final selection / 최종 선정

**`SELECT_US_WW_001_CWNS_INFRASTRUCTURE_NEED_TO_NPDES_COMPLIANCE`**

Advance only to Issue #114 `US-WW-F01`, an outcome-blind CWNS-2022 × ICIS-NPDES source/identity/join gate. No infrastructure-cost magnitude, violation count, effluent value, compliance rate or relationship is authorized.

## Selected candidate / 선정 후보

### US-WW-001 — Wastewater Infrastructure Need Profile × Subsequent Compliance Persistence

Baseline source: EPA **2022 Clean Watersheds Needs Survey (CWNS)** facility/project and need-category identities.

Future outcome source family: EPA **ICIS-NPDES / ECHO** permit/compliance identities.

Why this is structurally attractive before values:
- EPA publishes the nationwide 2022 CWNS dataset as CSV/Access files and a data dictionary;
- CWNS covers wastewater facilities and infrastructure needs over the next 20 years;
- EPA ECHO exposes CWNS IDs for wastewater facilities and uses NPDES IDs as deterministic program-system identifiers;
- EPA documentation states 2022 CWNS wastewater technical records were prepopulated from ICIS-NPDES, including NPDES permit number and facility geography;
- wet-weather/conveyance-relevant need-category semantics include infiltration/inflow correction, sewer rehabilitation/replacement and combined-sewer-overflow correction;
- the baseline survey precedes a future post-2022 compliance window, supporting prospective temporal ordering in a later separately preregistered non-causal study.

Current literature search found adjacent wastewater-compliance studies using rainfall, electronic reporting and ICIS-NPDES/CWNS treatment characteristics, but no near-identical facility-level design directly testing whether 2022 CWNS capital-need category identities prospectively stratify later NPDES compliance persistence. This is an overlap screen, not a proof of novelty.

## Fresh candidate comparison / 신규 후보 비교

0–5 each; /45. Scores are discovery/portfolio judgments, not empirical findings.

| Candidate | Mission bottleneck | Cross-source | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low diminishing-return / novelty risk | Total | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-WW-001 CWNS need profile → later NPDES compliance** | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | **43** | **SELECT** |
| US-WW-002 precipitation → NPDES compliance | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **39** | HOLD_CURRENT_OVERLAP |
| US-RCRA-001 natural-hazard exposure → hazardous-waste compliance | 5 | 5 | 5 | 5 | 5 | 5 | 4 | 3 | 2 | **39** | HOLD_POLICY_OVERLAP |
| US-MINE-001 production pressure / operational stress → mine injuries | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 3 | 2 | **38** | HOLD_PRIOR_CONCEPTUAL_OVERLAP |
| US-PIPE-001 hydrologic stress → pipeline incidents | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **37** | HOLD_DIRECT_CAUSE_OVERLAP |
| US-FRA-001 heat → rail accident/track failure | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 2 | 0 | **36** | HOLD_DIRECT_2025_2026_OVERLAP |
| US-FAA-WL-001 weather regime → wildlife strikes | 3 | 5 | 4 | 5 | 4 | 5 | 5 | 2 | 0 | **33** | HOLD_EXISTING_RESEARCH_OPERATIONAL_OVERLAP |
| US-DW-001 climate hazards → drinking-water compliance | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 1 | 0 | **36** | HOLD_NEAR_EXACT_2026_OVERLAP |

## Why the selected candidate is distinct enough for F01 / F01 가치

The discovery value is **not** the general proposition that weather can affect wastewater performance. That pathway already has substantial prior evidence. The bounded new question is whether a nationally reported **pre-existing infrastructure-need structure** can serve as a reproducible public-data signal for later compliance vulnerability/prioritization. A later experiment, if ever authorized, must explicitly handle the risk that CWNS needs may themselves reflect pre-existing compliance problems and therefore must not be interpreted causally without a much stronger design.

## Official source basis / 공식 source 근거

- EPA 2022 CWNS nationwide data download: https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/cwns_pub/data-download
- EPA 2022 CWNS report/data: https://www.epa.gov/cwns/clean-watersheds-needs-survey-cwns-2022-report-and-data
- EPA CWNS needs categories: https://www.epa.gov/cwns/about-clean-watersheds-needs-survey-cwns
- ECHO custom-search help (CWNS ID / facility linkage): https://echo.epa.gov/help/loading-tool/custom-search/custom-search-help
- ECHO wastewater/NPDES search help: https://echo.epa.gov/help/facility-search/search-criteria-help

## Exact next action / 정확한 다음 행동

Execute Issue #114 outcome-blind. Establish the national CWNS data route, deterministic CWNS ID → NPDES ID linkage, ECHO/ICIS permit identity coverage, need-category identity route, and post-2022 compliance-record schema support. Persist no dollar needs, effluent/limit values, violation rates/counts by exposure group or relationship statistics.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

claim_path.write_text("""---
id: CLM-155
type: claim
created: 2026-09-12
issue: 113
status: active
---

# CLM-155 — CWNS 2022 and ICIS-NPDES expose a prospective public-data infrastructure-need → compliance identity bridge

EPA publishes the nationwide 2022 CWNS dataset and data dictionary, ECHO exposes CWNS IDs for wastewater facilities, and NPDES IDs are deterministic wastewater program-system identifiers. EPA's CWNS documentation also describes ICIS-NPDES prepopulation for wastewater facility technical records.

These source semantics support a prospectively testable **CWNS facility → NPDES permit → later compliance-record identity** route without opening infrastructure-cost or compliance magnitudes. This is a source-route/discovery claim only; it does not establish feasibility, predictive value, causality or novelty. Cost: **0 USD**.
""", encoding="utf-8")

dec157_path.write_text("""---
id: DEC-157
type: decision
created: 2026-09-12
issue: 113
status: accepted
---

# DEC-157 — DISCOVERY-R01 selects US-WW-001 at 43/45

Select `US-WW-001 — 2022 CWNS infrastructure-need profile × subsequent NPDES compliance persistence` for the first bounded feasibility gate at **43/45**.

Selection is based on official-source identity structure, direct public-service bottleneck relevance, deterministic EPA-internal identifiers, national independent-unit prospect and lower current near-identical overlap than the other screened fresh candidates. Do not interpret the selection as evidence that infrastructure needs predict violations.
""", encoding="utf-8")

dec158_path.write_text("""---
id: DEC-158
type: decision
created: 2026-09-12
issue: 114
status: accepted
---

# DEC-158 — Authorize US-WW-F01 outcome-blind CWNS × ICIS-NPDES join gate

Authorize Issue #114 exactly as written. Inspect only source access, archive/table/header identities, CWNS IDs, NPDES IDs, facility/permit/state/county identities, need-category labels, compliance-record date/type schema identities, row/distinct counts and deterministic mapping cardinalities.

Do not open/persist need-dollar amounts, facility flow/capacity/performance magnitudes, effluent measurements/limits, exceedance magnitudes, exposure-group violation counts/rates, or any relationship. PASS/PARTIAL cannot authorize an effect test. Cost remains **0 USD**.
""", encoding="utf-8")

(f01_dir / "README.md").write_text("""---
id: US-WW-F01
issue: 114
state: ACTIVE_SOURCE_JOIN_FEASIBILITY
mission_anchor: MEM-054
discovery_decision: DEC-157
authorization_decision: DEC-158
relationship_computed: false
magnitudes_opened: false
incremental_monetary_cost_usd: 0
---

# US-WW-F01 — CWNS-2022 × ICIS-NPDES Facility/Permit Join Feasibility

Canonical contract is Issue #114.

The gate is strictly source/schema/identity/cardinality only. Establish whether the 2022 nationwide CWNS public dataset can deterministically bridge facility CWNS IDs to NPDES permit identities and then to public ECHO/ICIS compliance-record identities, while preserving need-category labels without reading project-dollar amounts or compliance outcomes.

No fuzzy facility-name/address matching is allowed. No effect is authorized. Cost: **0 USD**.
""", encoding="utf-8")

status_path.write_text("""---
checkpoint_id: CHK-20260912-US-WW-F01-ACTIVE
active_issue: 114
active_research: US-WW-F01
last_completed_issue: 113
last_completed_research: DISCOVERY-R01
last_decision: DEC-158
updated: 2026-09-12
---

# Project Status / 프로젝트 상태

**State / 상태:** `DISCOVERY_R01_SELECTED_US_WW_001__US_WW_F01_ACTIVE`

DISCOVERY-R01 selected **US-WW-001 — 2022 CWNS infrastructure-need profile × subsequent NPDES compliance persistence** at **43/45**. Selection opens no needs/compliance magnitude. The only active gate is Issue #114 source/schema/identity/cardinality feasibility.

## Exact next action / 정확한 다음 행동

Execute Issue #114 outcome-blind. Verify nationwide CWNS download operability, deterministic CWNS ID/NPDES ID linkage, ECHO/ICIS permit coverage, prospectively identifiable need-category labels and post-2022 compliance-record schema support. Persist no candidate outcome magnitudes and compute no relationship.

Incremental monetary cost remains **0 USD**.
""", encoding="utf-8")

handoff_path.write_text("""---
checkpoint_id: CHK-20260912-US-WW-F01-ACTIVE
active_issue: 114
active_research: US-WW-F01
last_completed_issue: 113
last_completed_research: DISCOVERY-R01
last_decision: DEC-158
updated: 2026-09-12
---

# Session Handoff / 세션 인수인계

DISCOVERY-R01 / Issue #113 selected **US-WW-001** at 43/45 and authorized Issue #114 `US-WW-F01`.

Exact restart: perform source/schema/identity/cardinality qualification only for EPA 2022 CWNS nationwide data and ECHO/ICIS-NPDES. Prove deterministic `CWNS ID → NPDES ID → permit/compliance-record identity` support and need-category-label support. Do not read/persist needs dollars, effluent values, violation rates/counts by need group, or any relationship.

PASS/PARTIAL returns to Stage 0 and does not authorize an effect. Cost: **0 USD**.
""", encoding="utf-8")

checkpoint_path.write_text(json.dumps({
    "checkpoint_id": "CHK-20260912-US-WW-F01-ACTIVE",
    "active_issue": 114,
    "active_research": "US-WW-F01",
    "last_completed_issue": 113,
    "last_completed_research": "DISCOVERY-R01",
    "last_decision": "DEC-158",
    "updated": DATE,
}, indent=2) + "\n", encoding="utf-8")

cl = claim_ledger_path.read_text(encoding="utf-8")
assert "`CLM-155`" not in cl
claim_ledger_path.write_text(cl.rstrip() + """

| `CLM-155` | EPA 2022 CWNS and ICIS-NPDES/ECHO expose a prospective CWNS facility → NPDES permit → later compliance-record identity bridge without opening needs/compliance magnitudes. / CWNS 인프라 필요 구조와 이후 NPDES compliance를 연결할 공식 식별 route가 존재한다. | `OBSERVED/DERIVED` | `V2_PRIMARY_OFFICIAL_SOURCE_ROUTE` | EPA CWNS 2022 data/download & methods; ECHO CWNS-ID/NPDES-ID help; DISCOVERY-R01 | 2026-09-12 | active |
""", encoding="utf-8")

dl = decision_log_path.read_text(encoding="utf-8")
assert "`DEC-157`" not in dl and "`DEC-158`" not in dl
decision_log_path.write_text(dl.rstrip() + """

| `DEC-157` | 2026-09-12 | DISCOVERY-R01 selects US-WW-001 at 43/45. / CWNS infrastructure need → later NPDES compliance 후보 선정. | Strong national direct-outcome/public-service value, official deterministic EPA identifiers and lower current near-identical overlap than screened alternatives. | Issue #113; `CLM-155`; `research/DISCOVERY-R01/RESULT.md` | active |
| `DEC-158` | 2026-09-12 | Authorize Issue #114 outcome-blind CWNS×ICIS-NPDES source/join feasibility only. / US-WW-F01 값 비사용 join gate 승인. | Must prove national deterministic identifiers before any predictive/effect question. | Issue #114; `research/US-WW-F01/README.md` | active |
""", encoding="utf-8")

print(json.dumps({"selection":"US-WW-001","score":43,"issue":114,"cost_usd":0}))
