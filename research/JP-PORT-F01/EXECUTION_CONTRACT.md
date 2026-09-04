---
id: JP-PORT-F01-EXECUTION-CONTRACT
type: source-semantic-spatial-temporal-execution-contract
created: 2026-09-04
issue: 79
relationship_outcome_computed: false
weather_values_opened: false
incremental_monetary_cost_usd: 0
---

# JP-PORT-F01 Execution Contract
# JP-PORT-F01 실행 계약

## Analytical identity

Future primary unit candidate:
port × calendar month, nested within a frozen port→JMA-station mapping.

Port support is fixed before numerical weather exposure.

## Qualified port universe

Use exactly the 149 ports listed in:
research/JP-PORT-F01/SUPPORT_ADJUDICATION.md

They satisfy:
- exact 2019–2024 e-Stat port identity;
- consistent prefecture across all six years;
- one-to-one C02 location match after terminal-港 normalization only;
- nearest stable eligible JMA station within 30 km;
- no distance tie within 0.01 km.

The 11 stable ports excluded by C02 ambiguity/unmatched identity cannot be restored after outcomes.

## Common period

2019-01 through 2024-12 only.

This period uses mature annual MLIT port-aggregate workbooks and full-period JMA station-history qualification.

## Primary future throughput outcome

Monthly total maritime cargo:
- MLIT sheet 海上出入貨物;
- port row 種別=計;
- monthly column group 合計;
- preserve source freight-ton semantics.

A descendant may transform the value prospectively, for example log1p, only if the transform is preregistered before opening weather values for relationship analysis.

## JMA station rule

For each port use the frozen nearest eligible station from SUPPORT_ADJUDICATION.md.

No station substitution is allowed after outcomes.

If an E01 raw CSV reveals:
- unsupported element;
- homogeneity break;
- unacceptable quality/missingness;
the affected station/port is excluded under a preregistered rule. It is not remapped.

## Weather observation quality

Historical CSV:
https://www.data.jma.go.jp/risk/obsdl/

Future download options must preserve:
- numeric values;
- separate quality information;
- homogeneity information.

Primary aggregation:
- quality code 8 only;
- non-8 values are missing for the primary construct;
- completeness threshold must be declared in E01 before numerical execution.

## Shared station dependence

149 ports map to 131 unique JMA stations.
16 stations are shared by 34 port mappings.

A future model must account for shared station-month exposure and may not claim 149 independent weather series.

## Duplicate and missingness

MLIT:
- one port total row per source workbook is required;
- duplicate port total rows => HOLD for that source/year;
- blank/non-numeric monthly total is missing, not zero;
- numeric zero remains a valid observed zero.

JMA:
- duplicate station-date-element records => HOLD unless the official source semantics provide a deterministic revision identity;
- missing/invalid quality values are not imputed.

## Revision and hash policy

MLIT raw hashes are frozen in FINAL_SUPPORT_PREFLIGHT.md.

JMA observation values remain unopened in F01.
E01 Stage A must:
1. download only preregistered station/element/date batches;
2. pin raw CSV SHA-256 values;
3. validate station/date/quality/homogeneity identities;
4. stop before Stage B if the frozen support rules fail.

## F01 boundary

This contract establishes source/join readiness only.

It does not establish:
- a weather effect on throughput;
- a port-disruption threshold;
- a causal relationship;
- a sensitive or resilient port ranking;
- policy/investment superiority.

Incremental monetary cost remained 0 USD.
