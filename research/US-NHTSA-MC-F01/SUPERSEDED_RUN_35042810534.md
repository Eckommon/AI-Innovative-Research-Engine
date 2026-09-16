---
id: US-NHTSA-MC-F01-SUPERSEDED-35042810534
type: implementation-nonconformity
created: 2026-09-16
issue: 143
run: 35042810534
classification: EXECUTION_INVALID_FOR_GATE
scientific_disposition: NONE
superseded: true
incremental_monetary_cost_usd: 0
---

# Superseded Run 35042810534 — execution invalid for scientific gate

Run `35042810534` downloaded and durably audited the frozen official NHTSA sources, but it is **not** a PASS/HOLD scientific disposition.

## What happened

- `MFR_COMMS_RECEIVED_2020-2024.zip`: HTTP 200, 11,695,292 bytes.
- `MFR_COMMS_RECEIVED_2025-2026.zip`: HTTP 200, 5,240,968 bytes.
- `FLAT_RCL_POST_2010.zip`: HTTP 200, 14,842,725 bytes.
- Manufacturer Communications dictionary: HTTP 200.
- Recall dictionary: HTTP 200.
- Frozen dictionary semantic checks all passed.
- NHTSA catalog HTML returned HTTP 403 to the GitHub-hosted runner.

The runner incorrectly coupled **all source responses**, including the catalog HTML, into one `all_sources_ok` condition. Because the catalog returned 403, it skipped parsing otherwise successfully downloaded ZIP files. The resulting zero counts and `IMPLEMENTATION_OR_SOURCE_PARSE_NOT_VALID_FOR_GATE` therefore do not evaluate the frozen F01 cardinality/date/identity requirements.

## Allowed correction

Preserve the frozen source URLs, product normalization, thresholds and outcome boundary. Correct only execution control flow so ZIP/dictionary parsing proceeds whenever the actual frozen data sources and dictionaries are readable, while the catalog reachability remains an independent frozen requirement. A normal public browser User-Agent may be used for the unauthenticated catalog request; no authentication bypass, mirror or alternate dataset is authorized.

No recall incidence, conditional future-recall membership or relationship was opened in this invalid run.

Incremental monetary cost: **0 USD**.
