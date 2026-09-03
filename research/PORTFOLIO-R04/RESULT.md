---
id: PORTFOLIO-R04-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-04
issue: 76
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-US-001
selected_gate: US-GRID-F01
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R04 Result — Post-US-Mineral PASS Mission-ROI Reselection
# PORTFOLIO-R04 결과 — 미국 핵심광물 PASS 이후 목적-ROI 재선정

## Final selection / 최종 선정

**`SELECT_C_US_001_US_GRID_BOTTLENECK_INTELLIGENCE`**

Selected branch:

**`C-US-001 — U.S. Grid Bottleneck Intelligence`**  
**`C-US-001 — 미국 전력망 병목 지능화`**

Exact next bounded gate:

**`US-GRID-F01 — LBNL Queued Up Operator/Region × EIA-930 Balancing-Authority Identity & Bottleneck-Outcome Feasibility`**.

The critical-mineral branch is preserved as a validated result branch but is **not** continued automatically after E01 PASS.

## Why portfolio priority changed / 왜 우선순위가 바뀌었는가

`US-MINERAL-E01` added a real validated result: under the prospectively frozen eight-mineral 2023 trade-value construct, `5/8` minerals crossed the preregistered dual country-origin × district-of-unlading concentration threshold. This materially reduces the scientific uncertainty that originally justified continuing the critical-mineral branch.

The immediate remaining variants in that branch — HS6 port detail, alternate years, thresholds or geography variants — now have substantially lower marginal information value and are explicitly barred as automatic descendants by `DEC-106`.

By contrast, `C-US-001` still carries a high-value unresolved scientific question: whether a project-level interconnection-queue bottleneck outcome can be related to an independently defined U.S. grid operating identity without unsupported region/operator mapping.

## Current official-source refresh / 현행 공식 소스 갱신

### Lawrence Berkeley National Laboratory — Queued Up 2026

Current official project page:
`https://emp.lbl.gov/queues`

As of the 2026 edition:
- the downloadable Excel file was last updated in May 2026;
- the dataset covers interconnection data through the end of 2025;
- it includes all seven U.S. ISOs/RTOs plus 50 non-ISO utilities;
- those operators collectively represent about 98% of currently installed U.S. generating capacity;
- approximately 8,200 projects were actively seeking interconnection at end-2025, representing 1,312 GW generation plus about 749 GW storage;
- the data file is licensed CC BY 4.0.

This is a direct project-level bottleneck/outcome surface rather than a generic grid proxy.

### U.S. Energy Information Administration — EIA-930

Current official EIA Open Data dashboard:
`https://www.eia.gov/opendata/browser/electricity`

The current public bulk-file catalog includes:
- `U.S. Electric System Operating Data (2019-present)`;
- hourly and daily electric-power operations by balancing authority from Form EIA-930.

EIA-930 provides balancing-authority operating identities and system-state variables at hourly/daily grain. The public bulk route allows the next source-semantic gate to avoid provisioning an API key merely for convenience.

### ENTSO-E / Europe

`C-EU-001` remains high-value, but current ENTSO-E Transparency Platform REST access still requires registration and a Web API security-token request. This is not a rejection, but it preserves a material access/automation friction relative to the U.S. candidate.

### Japan ports

Current MLIT Port Survey remains an official Fundamental Statistics source publishing vessel calls, maritime cargo and container counts. Current port-level outputs remain monthly, preserving the temporal-grain limitation already identified in prior portfolio reviews.

### Singapore maritime

Current MPA open data provides monthly vessel arrivals and gross tonnage, including vessel-type breakdown, through 2026 and supports keyless sample OpenAPI access. The main bottleneck for the present mission remains monthly outcome grain rather than source access.

## Candidate comparison / 후보 비교

Scores are transparent 0–5 **portfolio decision aids**, not empirical findings. Higher `diminishing-return` score means lower diminishing-return risk.

| Candidate | Mission bottleneck value | Cross-source value | Falsifiability / independent-unit quality | Practical utility | Current source access | Low mapping/rescue friction | Next-gate information gain | Diminishing-return profile | Total /40 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **`C-US-001 U.S. Grid Bottleneck Intelligence`** | 5 | 5 | 5 | 5 | 5 | 3 | 5 | 5 | **38** | **SELECT** |
| `C-EU-001 Cross-National Grid Stress` | 5 | 5 | 5 | 5 | 3 | 2 | 4 | 5 | **34** | `HOLD_READY_SECONDARY` |
| `C-EU-004 Industrial Site Climate Risk` | 4 | 5 | 3 | 4 | 5 | 5 | 2 | 4 | **32** | `PRESERVE_JOIN_ASSET` |
| `C-JP-001 Port Weather–Throughput Stress` | 4 | 4 | 3 | 4 | 5 | 4 | 3 | 5 | **32** | `HOLD_READY` |
| `C-US-003R Critical Mineral continuation` | 5 | 5 | 4 | 5 | 5 | 4 | 2 | 1 | **31** | `VALIDATED_RESULT__NO_AUTO_CONTINUATION` |
| `C-SG-001 Maritime Activity × Weather Regime` | 3 | 4 | 3 | 4 | 5 | 5 | 2 | 5 | **31** | `HOLD_READY` |

## Selected scientific uncertainty / 선정된 과학적 불확실성

The next uncertainty is **not** whether EIA or LBNL files can merely be downloaded.

It is whether the two official source systems support a defensible common research identity and a direct bottleneck outcome:

`interconnection project / queue operator / region`
`× balancing-authority operating identity`
`× time`
`→ queue delay / progression / withdrawal / completion bottleneck outcome`

without silently assuming that ISO/RTO, utility, queue region and EIA balancing authority are interchangeable geographies.

That identity/construct question has high mission-level information value because a PASS could support a later controlled cross-dataset experiment, while a FAIL/HOLD would prevent a misleading grid-stress claim before numerical tuning.

## Exact next gate / 정확한 다음 게이트

Open only:

### `US-GRID-F01 — LBNL Queued Up Operator/Region × EIA-930 Balancing-Authority Identity & Bottleneck-Outcome Feasibility`

F01 is source-semantic / join-feasibility only. Before any relationship statistic, it must:

1. freeze the exact Queued Up 2026 data file/version/hash and inspect its official project, operator/region, status and date/outcome fields;
2. freeze the exact EIA-930 public bulk product/version/hash route and balancing-authority identity fields;
3. determine whether queue operator/region identities can be reconciled to EIA balancing authorities by explicit official identifiers or a prospective one-to-one/qualified-subset rule;
4. reject unsupported many-to-many geographic substitution;
5. identify a direct project-level queue bottleneck outcome that can be frozen before EIA system-state values are examined;
6. define a bounded common cohort/time period, duplicate/null/revision rules and source-snapshot plan;
7. determine whether a later experiment can use the full qualified universe or a prospectively support-qualified subset without operator/region selection after seeing outcomes.

F01 shall **not** calculate:
- queue-delay differences by balancing authority;
- demand/generation/interchange stress rankings;
- queue-outcome correlations/regressions;
- system/operator rankings;
- causal grid-bottleneck effects;
- investment or policy rankings.

## Branch-stop rule / 중단 규칙

HOLD/REJECT and return to Stage 0 if:
- LBNL operator/region identities cannot be linked to EIA balancing-authority identities without arbitrary manual many-to-many mapping;
- no direct, reproducible queue bottleneck outcome can be frozen from the official LBNL data;
- the usable common cohort is created only by post-outcome operator selection;
- a paid database, opaque visualization scraping or credential-heavy rescue is required.

Do not replace EIA-930 with a more convenient stress proxy after seeing queue outcomes inside F01.

## Cost / 비용

Incremental monetary cost remained **0 USD**. Any potentially billable work requires explicit prior user approval.
