---
id: US-MINE-F01-SUPERSEDED-RUN-35003705306
type: implementation-nonconformity
created: 2026-09-16
issue: 134
run: 35003705306
status: superseded
scientific_contract_changed: false
---

# Superseded Run 35003705306 — boolean polarity implementation nonconformity

Run `35003705306` successfully downloaded and structurally inspected the frozen MSHA sources under the US-MINE-F01 outcome-blind contract. All preregistered substantive PASS requirements in `STAGING_RESULT.json` evaluated true, prohibited injury outcome fields were not selected, injury outcome values remained unopened, no relationship was computed, and cost remained 0 USD.

The runner nevertheless emitted `PARTIAL_US_MINE_F01_IDENTITY_READY__JOIN_OR_HOURS_SUPPORT_PENDING` because the gate implementation applied Python `all()` to two negatively named diagnostic booleans — `prohibited_outcome_fields_accessed=false` and `relationship_computed=false`. Their correct outcome-blind state (`false`) was therefore incorrectly treated as a failed PASS condition.

This is an implementation-polarity defect, not a data failure and not a threshold/source/window issue. The run is retained as superseded evidence. The correction may only convert these two requirements to positive compliance predicates (`no_prohibited_outcome_fields_accessed=true`, `no_relationship_computed=true`) and rerun the **same frozen F01 contract**. No threshold, source, support window, identity rule, sector rule or scientific disposition is changed.
