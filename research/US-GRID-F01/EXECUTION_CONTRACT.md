---
id: US-GRID-F01-EXECUTION-CONTRACT
type: source-semantic-execution-contract
created: 2026-09-04
issue: 77
relationship_outcome_computed: false
eia_operating_values_opened: false
incremental_monetary_cost_usd: 0
---

# US-GRID-F01 Execution Contract / 실행 계약

## Frozen source snapshots

### LBNL Queued Up 2026
- URL: `https://eta-publications.lbl.gov/sites/default/files/2026-05/lbnl_ix_queue_data_file_thru2025.xlsx`
- SHA-256: `794582d3281c6a305e9615fcfec3fae9dc85be2165216d33760b677e976a08b6`
- primary project sheet: `03. Complete Queue Data`
- codebook: `04. Data Codebook`
- project rows: **38,201**

### EIA-930 public bulk
- manifest: `https://www.eia.gov/opendata/bulk/manifest.txt`
- target: `https://www.eia.gov/opendata/bulk/EBA.zip`
- frozen EBA ZIP bytes: **686,684,023**
- EBA ZIP SHA-256: `3b80081e3720e0075ca151bd81308cd548b076a436c9136baf8656b507a50bb1`
- member inventory: one `EBA.txt`, uncompressed bytes **4,323,307,257**
- F01 did not parse EBA numerical operating values.

## Frozen identity unit

Project identity:
**`entity + q_id`**.

LBNL codebook explicitly requires combining `q_id` with `entity` for full-dataset uniqueness.

BA mapping:
- use only the **41 qualified LBNL entities** in `ALIAS_ADJUDICATION.md`;
- use their exact frozen EIA BA codes;
- the **16 excluded entities** may not be restored after relationship outcomes;
- no fuzzy matching, county/state overlap, nearest-BA assignment or parent-company inference.

## Frozen future direct queue outcome

Primary future bottleneck outcome:
**IR→COD elapsed duration**.

Source fields:
- IR = `q_date`, LBNL-defined interconnection request / queue-entry date;
- COD = `on_date`, LBNL-defined date project became operational.

A future numerical experiment may compute the elapsed duration only after its full cross-source predictor/statistic is preregistered.

## Frozen common outcome cohort

A project is eligible for the primary completed-project outcome only if all are true:

1. qualified entity under `ALIAS_ADJUDICATION.md`;
2. `q_date >= 2019-01-01`;
3. `q_date <= 2025-12-31`;
4. source `q_status = operational`;
5. explicit parsable `q_date`;
6. explicit parsable `on_date`;
7. `on_date >= q_date`;
8. `on_date <= 2025-12-31`.

Structural result before duration calculation:
- all 2019–2025 entry rows: **19,794**;
- qualified-entity entry rows: **17,453** (**88.173184%**);
- eligible completed rows: **447**;
- unique completed project keys: **447**;
- represented EIA BA codes: **11**.

No duration distribution, BA-duration comparison or EIA operating relationship was computed in F01.

## Duplicate / conflict rule

Across the full workbook, repeated composite keys exist historically. The future primary cohort applies:

1. if duplicate rows are identical across all experiment-used source fields, collapse to one source record;
2. if any `entity+q_id` has conflicting `q_status/q_date/on_date/wd_date/ia_date`, exclude the whole key prospectively;
3. never choose a preferred conflicting row;
4. if conflicting-key exclusions become material in a future frozen cohort, HOLD rather than repair post-outcome.

For the frozen 2019–2025 completed cohort:
- duplicate composite-key groups: **0**;
- semantic-conflict groups: **0**.

## Null / date / censoring rule

- Blank/invalid entity or q_id: ineligible.
- Blank/invalid q_date or on_date: ineligible for primary completed-project duration.
- `on_date < q_date`: fail numerical integrity for that key; no sign correction.
- active/suspended/withdrawn/unknown projects are not assigned synthetic durations or zero outcomes.
- primary IR→COD experiment is explicitly a **completed-project construct**, not a survival-analysis estimate of all queue entrants.
- right-censored projects may be studied only in a separately preregistered future design.

## Revision / snapshot rule

- LBNL workbook bytes are pinned to the hash above.
- EIA EBA bytes are pinned to the hash above for any immediate descendant that relies on this F01 snapshot.
- A future descendant that intentionally refreshes EIA data requires a new prospective snapshot/hash before numerical exposure; it may not mix revisions opportunistically.
- all source/version changes must be declared before outcome calculation.

## Future experiment boundary

F01 establishes only join/source-semantic readiness.

Before any EIA numerical value is opened for relationship analysis, a descendant must preregister:
- exact EIA-930 predictor field(s);
- temporal aggregation relative to q_date;
- treatment of missing hourly/daily observations;
- independent analytical unit;
- primary statistic;
- materiality/significance gate;
- sensitivity analyses, if any;
- public-result raw-value minimization.

No EIA metric may be selected after observing which one predicts longer queue duration.

Incremental monetary cost remained **0 USD**.
