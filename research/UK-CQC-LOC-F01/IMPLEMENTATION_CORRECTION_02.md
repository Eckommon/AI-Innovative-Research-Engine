---
id: UK-CQC-LOC-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-09-29
issue: 171
attempt_01_run: 36525105345
attempt_01_commit: 4b26cfc6c31f38a36a19b908a45c1ca9cb67f030
attempt_01_recorded_disposition: HOLD_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_NOT_READY
attempt_01_adjudication: IMPLEMENTATION_NONCONFORMING_NOT_TERMINAL
scientific_threshold_changed: false
snapshot_changed: false
identity_rule_changed: false
event_semantics_changed: false
future_outcome_firewall_changed: false
incremental_monetary_cost_usd: 0
---

# UK-CQC-LOC-F01 — Attempt 02 implementation-only correction

Attempt 01 is immutable and preserved at commit `4b26cfc6c31f38a36a19b908a45c1ca9cb67f030` / Run `36525105345`.

Although the Attempt-01 runner self-labelled the completed execution as scientific HOLD, canonical adjudication does **not** accept that disposition as terminal because the directory parser demonstrably selected the `README` narrative row as the baseline schema header rather than the actual location-data header. Gates 5, 6, 7, 9 and 14 therefore inherited an artificial empty baseline cohort. This is an implementation nonconformity, not scientific evidence that the baseline cohort is empty.

Attempt 01 nevertheless established several durable facts without opening future membership:

- all three exact 01-Sep-2026 CQC selectors resolved from the official landing page;
- exact official ODS URLs and SHA-256 fingerprints were recorded;
- the ratings data sheet and deactivated data sheet were parseable;
- historical deactivated exact-token support observed under the frozen identity rule was 3,441 distinct IDs in the prematurely executed runner;
- registration-end dates were 100% parseable for those qualified deactivated rows;
- official CQC landing/API metadata exposed linked-organisation semantics and explicitly stated that archived/deactivated does not necessarily mean closed;
- post-2026-09-28 future rows opened remained zero.

## Allowed Attempt-02 corrections

Attempt 02 may change **parser mechanics only**:

1. Header detection must require an exact normalized `Location ID` / `CQC Location ID` header cell rather than accepting the token as a substring inside narrative README text.
2. The same exact-header rule must be used consistently for filters, ratings and deactivated sheets.
3. Google Drive archive-page filename/date extraction may additionally recognize official-linked filenames using underscore, hyphen, URL-encoded or other non-space separators and month-year forms. This changes only archive HTML parsing; the frozen >=6 historical-snapshot threshold is unchanged.
4. Attempt 01 files remain immutable. Attempt 02 must write separate `attempt-02.json` and `attempt-02.md`.

## Boundaries that may not change

Attempt 02 retains exactly:

- pre-Issue contract `99c7782cabc384ce7c4817a91b5cb1bdc105012c`;
- Issue #171;
- 01-Sep-2026 filters / ratings / deactivated source snapshots;
- the frozen Location-ID rule: trim only, preserve remaining characters/case, accept only ASCII alphanumeric tokens;
- all 18 gates and all numeric thresholds, including 99.90% syntax, 20,000 active IDs, 10,000 ratings links, 5,000 historical deactivated IDs, 95% end-date parseability and 6 monthly snapshots;
- the source-native administrative-transition semantic requirement;
- no name/address/postcode/fuzzy/geospatial/manual repair;
- future rows opened = 0 and future event membership opened = false;
- incremental monetary cost = 0 USD.

If Attempt 02 correctly reaches all 18 gates and any frozen gate fails, that result is terminal scientific HOLD. No further correction is authorized merely to improve a scientifically observed support value.
