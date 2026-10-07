---
id: US-FRA-RR-F01
type: outcome-blind-structural-feasibility
created: 2026-10-08
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R54
parent_decision: DEC-303
selected_candidate: US-FRA-RR-001
future_2026plus_accident_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-FRA-RR-F01 — exact railroad-code operational/accident structural gate

## Mission / 목적

Before opening any 2026-or-later railroad accident membership, determine whether FRA's official Safety Data / DataDownloadService supports a deterministic railroad-level prospective design linking historical operational exposure from Form 55 to later reportable Rail Equipment Accident/Incident events from Form 54.

F01 is structural only. No accident-risk relationship is computed.

## Frozen official source anchors

- FRA Safety Data portal: `https://railroads.dot.gov/safety-data`
- Data downloads landing: `https://data.transportation.gov/stories/s/Data-Downloads-Landing-Page/yh67-9te8/`
- FRA DataDownloadService: `https://safetydata.fra.dot.gov/MASTERWEBSERVICE/DatadownloadService.asmx`
- WSDL: same endpoint with `?WSDL`
- FRA Database Dictionaries
- annual Rail Equipment Accident/Incident reporting-threshold notices/guidance.

## Frozen historical window / 고정 과거기간

Historical bodies allowed in F01:
- calendar years **2020, 2021, 2022, 2023, 2024, 2025** only;
- Form 55 operational data;
- Form 54 reportable rail-equipment accident/incident data;
- railroad reference file and Form 54/55 schemas;
- threshold documentation for those historical years.

Rows/events for **2026 or later are prohibited** in F01.

## Frozen identity / 식별자

Primary entity identity is the source-native FRA reporting railroad code.

Allowed normalization:
- text conversion;
- trim ASCII whitespace;
- uppercase.

Prohibited:
- railroad-name fuzzy matching;
- manual merger repair;
- parent-company substitution;
- geography-based identity repair;
- arbitrary code padding/truncation.

If source-native reference data explicitly map a historical railroad code to a system/consolidated code, F01 may report that mapping but may not silently replace identity. N01 must prospectively choose the unit.

## Frozen event prospect

Primary future event prospect:
- at least one source-native **Form 54 Rail Equipment Accident/Incident** for the same railroad in a future authorized period;
- event must satisfy FRA's own reportability regime for its occurrence year;
- F01 does not reclassify sub-threshold events or invent a severity threshold.

The future membership window is not opened in F01.

## Anti-tautology firewall

Descendant predictive exposure may not include:
- prior accident count/rate;
- prior casualty/injury count;
- accident cause codes;
- reportable damage;
- prior Form 54 presence;
- violation/defect/enforcement fields;
- any variable mechanically derived from the future accident window.

Permitted exposure family is non-outcome Form 55 operational structure only.

## Immutable 18-gate contract

Exactly **18/18 PASS** is required.

| # | Requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is R54 terminal selection, last decision `DEC-303` |
| 2 | Issue binding | runner executes only after new Issue binds this exact pre-Issue commit |
| 3 | Direct service access | ASMX landing and WSDL or equivalent official service description reachable; Form54/Form55/GetRailroadData operations discoverable |
| 4 | Railroad reference access | official railroad reference body is returned and parseable |
| 5 | Schema access | official Form 54 and Form 55 schemas/dictionaries are directly available and parseable |
| 6 | Historical year completeness | row-bearing Form 55 data are retrievable for all six years 2020–2025 |
| 7 | Form 54 lineage | row-bearing Form 54 accident data are retrievable for all six years 2020–2025 |
| 8 | Railroad-code syntax | ≥99.0% of nonblank historical Form55 railroad codes are source-reference-recognized or source-valid without repair |
| 9 | Cross-form identity | ≥98.0% of distinct Form54 reporting railroad codes exact-match a Form55/reference railroad code |
| 10 | Operational support | each historical year contains ≥300 distinct railroads with nonzero source-native operating exposure |
| 11 | Longitudinal support | ≥250 railroad codes appear with nonzero Form55 exposure in at least 4 of 6 years |
| 12 | Operational-field completeness | ≥95.0% of qualified Form55 railroad-year rows have at least one train-mile concept and employee-hours concept parseable/nonnegative |
| 13 | Accident support | ≥1,500 distinct historical Form54 reportable accident records across 2020–2025 |
| 14 | Accident date/year support | ≥99.0% of Form54 rows have a parseable source-native occurrence year/date consistent with 2020–2025 |
| 15 | Threshold semantics | official FRA documentation establishes year-specific reportability threshold semantics for the historical window; no post-hoc event reclassification |
| 16 | Future seal | zero 2026+ Form54 membership rows opened/consumed |
| 17 | Outcome/identity firewall | no relationship/prediction/ranking/causal metric; no prior accident/casualty predictor; no identity repair |
| 18 | Reproducibility/cost | immutable evidence records source URLs, WSDL/service metadata, response hashes or deterministic request manifests, row/cardinality counts, contract/runner SHA and cost=0 |

## Frozen terminal rule

PASS only if all gates pass:

`PASS_US_FRA_RR_F01_EXACT_RAILROAD_OPERATIONAL_ACCIDENT_DESIGN_READY`

Any valid empirical frozen-gate failure:

`HOLD_US_FRA_RR_F01_EXACT_RAILROAD_OPERATIONAL_ACCIDENT_DESIGN_NOT_READY`

Transport/parser defects remain non-scientific only when demonstrably isolated and scientific criteria are unchanged.

## PASS consequence

PASS authorizes only a separate outcome-blind `US-FRA-RR-N01`. N01 must prospectively freeze:
- one non-tautological Form55 exposure;
- railroad eligibility and code/merger policy;
- comparator/matching/stratification;
- size/common-support controls;
- future observation period;
- accident opportunity/support threshold;
- balance/statistical gates;
before any 2026+ accident membership is opened.

Incremental monetary cost must remain **0 USD**.
