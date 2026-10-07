---
id: PORTFOLIO-R55
type: stage0-survivor-first-direct-body-reselection
created: 2026-10-08
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-FRA-RR-F01
parent_disposition: BLOCKED_IMPLEMENTATION_FRA_HISTORICAL_DATA_OPERATION__SCIENTIFIC_GATE_NOT_EXECUTED
candidate_outcomes_opened_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R55 — direct-row-body survivor reselection after FRA branch-stop

## Mission / 목적

Select at most one next **outcome-blind F01** with a high probability of reaching row-level scientific adjudication and a later prospective N01.

R55 prioritizes:
1. direct downloadable row bodies;
2. source-native exact identity;
3. event/date semantics already present in the row body;
4. historical lineage without archive reverse engineering;
5. plausible N01 common support and observation opportunity.

No candidate future-event membership, relationship, prediction, ranking or causal result may be opened during scoring.

## Frozen candidates

### 1. `US-EPA-RCRA-001` — hazardous-waste handler structure → future evaluation-conditioned violation

Unit: one RCRA handler/site identified by exact `ID_NUMBER + ACTIVITY_LOCATION`.

Official architecture:
- ECHO direct RCRAInfo ZIP;
- Facility, Enforcement, Evaluations, Violations, NAICS and VIO/SNC History CSVs;
- all tables carry documented key fields;
- `RCRA_VIOSNC_HISTORY.csv` includes explicit monthly `YRMONTH` lineage;
- evaluations expose source-native date/type and `FOUND_VIOLATION`.

Future event prospect:
- at a prospectively locked future evaluation opportunity, source-native evaluation finding / linked violation.

Exposure family:
- non-outcome handler structure only: generator/TSDF/transporter role, NAICS and stable facility characteristics.

Anti-tautology:
- prior/current violation, SNC, enforcement, penalty, evaluation finding and unresolved compliance variables prohibited.

Critical design issue:
- evaluation/inspection targeting is non-random; N01 must condition on a future evaluation opportunity and establish common support.

### 2. `US-CMS-NPI-001` — provider structure → future NPI deactivation

Unit: exact 10-digit NPI.

Official architecture:
- monthly full NPPES replacement ZIP;
- monthly deactivation update;
- weekly incremental update;
- deactivated NPIs and deactivation dates included in the full replacement file.

Future event:
- new source-native NPI deactivation after a future lock.

Critical limitation:
- deactivation can represent retirement, death, disbandment or other reasons and can be followed by reactivation;
- monthly current file replaces prior body; event-date history, not assumed snapshot lineage, must carry the prospective design.

### 3. `US-FAA-AIR-001` — aircraft registry structure → future deregistration

Unit:
- one aircraft under a prospectively proven identity using source-native N-number plus serial/manufacturer fields.

Official architecture:
- daily complete Aircraft Registration Database;
- current bundle includes Master and Deregistered Aircraft files;
- yearly official archives 2012–2021;
- deregistration reasons include accident, salvage, dismantled, permanently retired, destroyed and owner request.

Critical limitation:
- N-number reassignment means N-number alone cannot be identity;
- deregistration reasons are heterogeneous and reason strata must remain separate.

### 4. `US-FDIC-BANK-001` — insured-bank structure → future bank failure

Unit: exact FDIC CERT.

Official architecture:
- BankFind Suite / APIs and bulk data;
- quarterly financial history back to 1992;
- institution/history data and Failures & Assistance;
- weekly/quarterly update cadence.

Critical limitation:
- bank failures are sparse;
- bank-failure prediction is mature and novelty is low;
- direct supervisory/enforcement/failure-warning variables prohibited.

## Frozen source anchors

### RCRA
- `https://echo.epa.gov/tools/data-downloads`
- `https://echo.epa.gov/tools/data-downloads/rcrainfo-download-summary`

### CMS NPI
- `https://download.cms.gov/nppes/NPI_Files.html`
- `https://www.cms.gov/medicare/regulations-guidance/administrative-simplification/data-dissemination`

### FAA
- `https://www.faa.gov/licenses_certificates/aircraft_certification/aircraft_registry/releasable_aircraft_download`

### FDIC
- `https://banks.data.fdic.gov/bankfind-suite`
- FDIC 2026 Bank Data Guide / Bulk Data and API.

## Frozen /45 rubric

Nine 0–5 dimensions:
1. mission bottleneck fit
2. cross-table information gain
3. direct future-event quality
4. independent-unit prospect
5. practical value
6. zero-cost operability
7. deterministic identity
8. row-lineage + N01 survivor probability
9. low overlap / novelty risk

Tie-break:
1. direct row body / lineage;
2. deterministic identity;
3. observation-opportunity design;
4. likely common support;
5. event support;
6. novelty.

## Frozen exclusions

- no third FRA workaround;
- no automatic promotion of R54 RCRA;
- no prior/current outcome or enforcement field as predictive exposure;
- no identity repair by name/address/geography;
- no paid/private source;
- no future membership during scoring.

Incremental monetary cost must remain **0 USD**.
