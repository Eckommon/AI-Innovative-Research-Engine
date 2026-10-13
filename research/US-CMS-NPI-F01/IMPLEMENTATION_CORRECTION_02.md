---
id: US-CMS-NPI-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-10-13
issue: 201
attempt_01_run: 38354790453
attempt_01_disposition: IMPLEMENTATION_BLOCKED_US_CMS_NPI_F01_ATTEMPT_01
scientific_threshold_changed: false
population_changed: false
identity_rule_changed: false
event_semantics_changed: false
future_update_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# US-CMS-NPI-F01 — Attempt 02 implementation-only correction

Attempt 01 is immutable and preserved.

It validly established Gates 1–12 against the exact October 12, 2026 Version-2 monthly full replacement baseline:

- full ZIP SHA-256: `45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e`;
- 9,852,180 exact unique NPIs;
- 1,979,717 active Type-2 organization NPIs;
- 1,569,636 single-taxonomy and 410,081 multi-taxonomy active Type-2 NPIs;
- Practice Location reference: 1,274,332 rows, 817,918 distinct NPIs, 100% exact syntax and 100% main-file join.

The run stopped only when the official monthly deactivation ZIP was found to contain:

`NPPES Deactivated NPI Report 20261012.xlsx`

rather than a CSV.

## Demonstrated implementation defect

The frozen scientific contract requires a **monthly deactivation body** with NPI and deactivation-date concepts. It does not require CSV format.

Attempt 01's runner incorrectly encoded CSV as the only accepted internal serialization for that ZIP. The official source is an XLSX workbook, so `DEACTIVATION_CSV_NOT_FOUND` is a representation/parser defect.

## Allowed Attempt 02 correction

Attempt 02 may only:

1. preserve and verify Attempt 01's exact full-file baseline fingerprint and Gates 1–12;
2. re-resolve the same named October 2026 V2 full/deactivation/weekly source family;
3. use HEAD/metadata to verify the full ZIP URL, size and ETag still match Attempt 01 without re-consuming the 1.16 GB body;
4. download the same monthly deactivation ZIP and parse its XLSX workbook with a deterministic read-only parser;
5. detect the header row containing NPI and deactivation-date concepts;
6. evaluate frozen Gates 13–18 unchanged;
7. preserve the weekly incremental body seal and all outcome/identity firewalls.

## Frozen boundaries retained

Unchanged:
- pre-Issue contract `18646fff22a499fedb058df397269281e62793b8`;
- Issue #201;
- exact 10-digit NPI identity;
- active Type-2 population;
- all numeric thresholds;
- single-taxonomy / multi-taxonomy support rule;
- deactivation administrative-event semantics;
- reactivation separation;
- weekly/later update body seal;
- no relationship/prediction/ranking/causal computation;
- cost 0 USD.

If Attempt 02 produces any valid frozen-gate failure, that result is terminal scientific HOLD unless a separate demonstrable implementation defect exists without changing the scientific contract.
