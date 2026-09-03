---
id: US-GRID-F01
type: source-semantic-join-feasibility
created: 2026-09-04
issue: 77
state: PREREGISTERED_ACTIVE
mission_anchor: MEM-054
portfolio_decision: DEC-107
relationship_outcome_computed: false
incremental_monetary_cost_usd: 0
---

# US-GRID-F01 — LBNL Queued Up Operator/Region × EIA-930 Balancing-Authority Identity & Bottleneck-Outcome Feasibility
# US-GRID-F01 — LBNL Queued Up 운영자/지역 × EIA-930 Balancing Authority 식별 및 병목 outcome 실행가능성

## 1. Objective / 목적

Test only whether official U.S. public sources support a deterministic semantic bridge:

`interconnection project → queue operator/region → EIA balancing-authority identity → bounded time/cohort`

while freezing one direct LBNL project-level queue bottleneck outcome before any cross-source relationship statistic is calculated.

F01 is **not** the queue-vs-grid experiment.

## 2. Frozen LBNL source / 고정 LBNL 소스

Primary official source:
- `Queued Up: 2026 Edition, Characteristics of Power Plants Seeking Transmission Interconnection As of the End of 2025`;
- official project page: `https://emp.lbl.gov/queues`;
- publication/data page: `https://emp.lbl.gov/publications/queued-2026-edition-characteristics`;
- exact current XLSX candidate exposed by the official attachment: `https://eta-publications.lbl.gov/sites/default/files/2026-05/lbnl_ix_queue_data_file_thru2025.xlsx`.

The official publication states that the workbook contains:
- the full project-level queue dataset through end-2025;
- a codebook/data dictionary;
- additional summary tabs.

F01 shall hash the actual workbook bytes before relying on its schema.

## 3. Frozen EIA source family / 고정 EIA 소스 계열

Primary source family:
- Form EIA-930 `Hourly and Daily Balancing Authority Operations Report`;
- official Open Data route: `https://www.eia.gov/opendata/browser/electricity/rto`;
- official bulk catalog: `https://www.eia.gov/opendata/bulk-downloads.php`;
- target bulk family: `U.S. Electric System Operating Data (2019-present)`.

The official EIA route defines hourly/daily electric-power operations by balancing authority and exposes demand, forecast demand, net generation and interchange products.

F01 shall use the public bulk route or another official keyless static route. It shall not provision an API key merely for convenience.

## 4. Exposure boundary / 노출 경계

Allowed during F01:
- XLSX sheet names and workbook/hash metadata;
- project-dataset column names and codebook definitions;
- queue operator/region identity vocabulary;
- project status vocabulary and date-field semantics;
- non-outcome cardinality needed for mapping feasibility;
- EIA balancing-authority codes/names and route/schema identity;
- mapping cardinality and bounded cohort counts.

Prohibited during F01:
- computing queue-duration differences by operator/BA;
- computing EIA operating-stress metrics for matched operators;
- correlation/regression between queue outcomes and EIA system state;
- operator/BA rankings;
- causal effects;
- investment/policy rankings.

## 5. Outcome-free direct bottleneck-outcome selection rule / 결과 비사용 직접 병목 outcome 규칙

F01 may inspect LBNL codebook semantics and must freeze exactly one future primary project-level bottleneck outcome before any EIA operating values are related to it.

Prospective priority order, based on source semantics rather than observed outcome magnitude:
1. elapsed time from interconnection request (`IR`) to commercial operation (`COD`) for completed projects, if exact fields and censoring semantics are reproducible;
2. if IR→COD cannot be defined for a defensible prospective cohort, an explicitly source-defined queue progression/duration outcome using available milestone dates;
3. if no direct duration/progression outcome is reproducible, HOLD/REJECT rather than substituting a generic project status score.

Withdrawal/completion status may be preserved as a separate possible future binary outcome only if it is source-defined and preregistered in a later experiment; it may not be selected inside F01 after examining EIA relationships.

## 6. Identity qualification / 식별성 검증

F01 must determine:

1. the exact LBNL field(s) identifying queue/grid operator and any region/area taxonomy;
2. the exact EIA balancing-authority code/name taxonomy available from current official source metadata;
3. whether identities match directly, through explicit official synonyms, or through a one-to-one prospective alias table supported by source documentation;
4. whether any LBNL operator maps to multiple EIA balancing authorities or vice versa in a way that destroys the intended unit;
5. whether ISO/RTO coverage and non-ISO utility coverage require different treatment;
6. whether a prospectively support-qualified subset can be defined before any queue-vs-EIA outcome is computed.

No state-overlap, county-overlap, fuzzy-name similarity or manually invented service-territory mapping may silently convert a many-to-many relationship into a one-to-one identity.

## 7. Time/cohort qualification / 기간·cohort 검증

EIA-930 current bulk coverage begins in 2019 for the selected current family, while the LBNL project dataset includes requests through end-2025 and older historical projects.

F01 shall define a later common analytical cohort only from source semantics. Candidate principles:
- EIA system-state exposure window must be temporally available for the selected project/operator unit;
- project outcome dates must be defined before system-state aggregation;
- no operator or project may be retained because its later relationship result is stronger;
- right-censoring and projects without completed outcome dates must be handled prospectively rather than converted to arbitrary durations.

The exact cohort is not frozen until the F01 source/schema inspection establishes which date fields exist and what they mean.

## 8. Data integrity and snapshot plan / 데이터 무결성·스냅샷 계획

F01 must define before PASS:
- LBNL XLSX URL/access timestamp/HTTP metadata/SHA-256;
- workbook sheet names and relevant schema/codebook snapshot;
- EIA bulk-manifest URL/hash/update timestamp and target bulk asset identity;
- target EIA asset hash if bounded download is practical under standard GitHub-hosted execution;
- duplicate project-ID rule;
- operator/BA null/unknown rule;
- date parsing and right-censoring semantics;
- source revision/version policy;
- exact prospective alias/mapping table with provenance.

Any duplicate or null rule that would require choosing records based on later relationship performance is prohibited.

## 9. Gate / 게이트

### PASS

**`PASS_US_GRID_QUEUE_BA_JOIN_READY`** if all are true:
- Queued Up 2026 exact workbook and codebook are reproducibly frozen;
- one direct project-level queue bottleneck outcome is source-defined and prospectively frozen;
- EIA-930 public keyless source route and BA identity taxonomy are reproducibly frozen;
- a deterministic full or prospectively qualified operator/BA identity universe exists;
- bounded cohort and integrity/snapshot rules can be frozen without viewing relationship outcomes.

### PARTIAL

`PARTIAL_US_GRID_JOIN_SEMANTICS` if the research unit remains identifiable but one bounded non-outcome component remains unresolved.

### HOLD

`HOLD_US_GRID_PUBLIC_JOIN_ROUTE` if required source access/versioning or deterministic identity cannot be established under the zero-cost route.

### REJECT

`REJECT_US_GRID_OPERATOR_BA_UNIT_NOT_IDENTIFIABLE` if official source semantics show the queue-operator/region × EIA-BA unit is invalid as framed.

## 10. Branch-stop / 중단 규칙

Do not rescue F01 through:
- paid commercial grid/queue databases;
- dashboard scraping;
- arbitrary state/county overlap mapping;
- fuzzy matching without source-backed one-to-one provenance;
- replacing EIA-930 with another stress proxy merely because it maps more easily;
- selecting only operators that later produce interesting queue-vs-grid results.

If those are needed, apply HOLD/REJECT and return to Stage 0.

## 11. Cost / 비용

Incremental monetary cost must remain **0 USD**. Any potentially billable work requires explicit prior user approval.
