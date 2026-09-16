---
id: US-NHTSA-MC-F01-SUPERSEDED-35042957163
type: implementation-nonconformity
created: 2026-09-16
issue: 143
run: 35042957163
classification: EXECUTION_INVALID_FOR_GATE
scientific_disposition: NONE
superseded: true
incremental_monetary_cost_usd: 0
---

# Superseded Run 35042957163 — parser validity classification correction required

Run `35042957163` successfully separated the NHTSA catalog response from the frozen data-file downloads and parsed the recall source correctly, but it still cannot be used as a scientific PASS/HOLD disposition.

## Valid evidence obtained

Recall source parsing is valid:
- `FLAT_RCL_POST_2010.txt` read as TAB-delimited;
- 245,597 rows observed;
- 221,007 valid product rows;
- 40,700 distinct exact normalized product keys;
- 1,007 distinct normalized makes;
- 17 recall-date years (2010–2026);
- recall date parse rate = 100%;
- 13,610 distinct recall campaign IDs.

Manufacturer Communications ZIPs are also readable and their CSV headers are now directly observed:

`TSB/Document ID, Make, Model, Model Year, Concise Summary`

The CSV files **do not expose** `NHTSA ID Number`, `Mfr Communication Date`, or `Date Added to File` even though the richer Manufacturer Communications dictionary documents those fields for the broader/flat-file schema. This matches the dictionary statement that the CSV is a smaller field subset.

## Remaining implementation defect

The parser treated absence of the date/NHTSA-ID fields as making the entire communication archive unreadable and therefore did not calculate product-key cardinality. That is too strict for gate evaluation.

The correct frozen-contract evaluation is:
- treat `TSB/Document ID + Make + Model + Model Year` as a structurally readable CSV product/document schema;
- calculate communication product cardinality/multiplicity/fingerprints outcome-blind;
- separately mark the frozen requirement for a communication/addition date field as failed if the frozen CSV bytes lack such a field;
- do not substitute a different TSV/flat source after observing this result.

If execution becomes valid under this classification and the date-field requirement remains failed, the scientific/source disposition is HOLD under the existing frozen contract. No threshold or source may be changed.

No recall incidence, communication-conditioned future-recall membership, relationship or predictive statistic was opened.

Incremental monetary cost: **0 USD**.
