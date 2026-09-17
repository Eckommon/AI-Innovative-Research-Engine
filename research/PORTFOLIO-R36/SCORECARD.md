# PORTFOLIO-R36 Immutable Scorecard

Date: 2026-09-17
Contract: `6550f4cfbde9df2702c793b902d7676f05700d61`
Revalidation: `c1a36a8fb522a2aa51a724ac4b78c05421a73d73`
Candidate outcomes opened: **false**

This is the **one and only R36 scorecard** under the frozen nine-dimension `/45` rubric.

| Candidate | Bottleneck | Cross-data | Direct outcome | Independent units | Practical | Zero-cost | Source-native join | Next-gate info | Low-overlap | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `US-EIA-GEN-001` | 5 | 3 | 5 | 5 | 5 | 5 | 5 | 4 | 2 | **39** | **SELECT_F01** |
| `US-CMS-HOSP-001` | 3 | 4 | 5 | 5 | 4 | 5 | 5 | 4 | 1 | **36** | HOLD_AGENCY_FRAMEWORK_OVERLAP |
| `US-FDIC-BANK-001` | 3 | 4 | 5 | 4 | 5 | 5 | 5 | 4 | 0 | **35** | HOLD_MATURE_FAILURE_PREDICTION_OVERLAP |
| `US-EDU-FIN-001` | 4 | 4 | 5 | 5 | 4 | 5 | 3 | 4 | 0 | **34** | HOLD_NEAR_IDENTICAL_CLOSURE_PREDICTION_OVERLAP |

No tie-break was required.

## `US-EIA-GEN-001` — 39/45

- **Mission bottleneck 5:** generator commissioning slippage is an infrastructure-delivery bottleneck rather than only a descriptive performance metric.
- **Cross-data 3:** annual/monthly snapshot integration adds temporal structure, but both source families are EIA and therefore less heterogeneous than a true cross-agency join.
- **Direct outcome 5:** later operating status / actual operation timing is directly observable and naturally prospective.
- **Independent units 5:** national generator inventories provide a large prospective unit pool.
- **Practical 5:** commissioning bottlenecks affect capacity build-out, planning and project execution.
- **Zero-cost 5:** official EIA annual/monthly files are public and standard compute is sufficient.
- **Source-native join 5:** plant code + generator ID is an agency-native generator key; F01 can fail closed on any longitudinal ambiguity without external crosswalk repair.
- **Next-gate info 4:** F01 can cheaply test identifier stability, snapshot/version lineage, schedule fields and cardinality before any later slippage outcome is opened.
- **Low-overlap 2:** EIA itself has published solar/generator delay analyses, so generic 'projects are delayed' novelty is unavailable. The remaining hypothesis space must be narrower and preregistered at generator-trajectory/bottleneck level.

## `US-CMS-HOSP-001` — 36/45

Exact CCN, large provider N, direct outcomes and excellent public access are strong. Scores are reduced because CMS already integrates readmission/unplanned-visit measures into formal quality reporting, risk adjustment and value-based programs; a generic process→readmission relation risks re-deriving an agency-defined quality framework.

## `US-FDIC-BANK-001` — 35/45

Exact FDIC `Cert` and direct failure events make this technically excellent. It receives the minimum low-overlap score because financial-ratio/CAMEL bank-failure prediction is mature in both research and supervisory practice. This makes it a useful calibration branch but not the preferred innovation-discovery branch.

## `US-EDU-FIN-001` — 34/45

IPEDS offers strong institutional panels, but the proposed finance/enrollment→closure relation is nearly identical to recent NBER work. Join defensibility is also conservatively reduced because Scorecard's broader Title-IV institution construction can involve OPEID/UNITID crosswalk and manual matching even though the candidate would accept exact UNITID rows only.

## Selection

**`SELECT_US_EIA_GEN_001_GENERATOR_COMMISSIONING_SLIPPAGE_F01`**

R36 authorizes exactly one separate **outcome-blind `US-EIA-GEN-F01`** to test source/snapshot/identity/time/cardinality feasibility. It does **not** authorize opening generator slippage outcomes, comparing technologies, estimating delay probabilities, ranking projects/developers, or claiming causal/novel relationships.

Incremental monetary cost: **0 USD**.
