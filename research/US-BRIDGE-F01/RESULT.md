---
id: US-BRIDGE-F01-RESULT
type: outcome-blind-feasibility
created: 2026-09-14
issue: 127
gate: PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY
condition_rating_values_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-BRIDGE-F01 Result

**`PASS_US_BRIDGE_F01_HAZARD_CONDITION_PANEL_JOIN_READY`**

The frozen outcome-blind source/identity/time gate is satisfied. This authorizes only a separate N01 design-identifiability gate; it does not authorize opening bridge condition-rating values or computing a disaster-linked condition relationship.

## Frozen support result

- Official NBI annual sources processed: **11** (2015–2025).
- Canonical bridge identities present in >=6/11 archives: **618,357**.
- Repeated-support bridges with >=2 distinct parseable inspection dates: **618,168**.
- County-qualified repeated-support bridges: **598,275** (**96.7524%**).
- Repeated-support state/territory FIPS: **53**.
- Qualified NBI counties: **3,174**.
- FEMA-overlap states/territories: **53**.
- FEMA-overlap counties: **2,764**.
- Duplicate canonical key rows observed: **30**; ambiguous canonical key-years excluded: **30**.
- All annual fixed-width identity/schema checks supported: **True**.

## Implementation-integrity record

Run `34790222911` is preserved as a superseded implementation-nonconformity run. It discarded an entire annual source when any duplicate bridge key existed, despite only 1–4 duplicate keys among roughly 612k–624k rows per year. Before the corrected rerun, Issue #127 and `IMPLEMENTATION_NOTE.md` recorded the correction: duplicate ambiguity fails closed at the canonical key-year level, while unrelated unique keys in the same official annual source remain eligible.

The corrected Run `34791209726` changes no source, time window, threshold, FEMA hazard set, outcome definition, or gate. It is an identity-scope correction only.

## Outcome-blind boundary

Bridge condition-rating values were **not opened**. Legacy condition-item row bytes were **not sliced**. No disaster-linked bridge-condition rate/change/association was computed. No fuzzy repair was used. Raw source bytes remained transient. Therefore this result is a feasibility/identity finding only, not an infrastructure-condition effect finding.

## Next action

Open a separately preregistered US-BRIDGE-N01 design-identifiability gate before any bridge condition-rating value is opened.

Incremental monetary cost: **0 USD**.
