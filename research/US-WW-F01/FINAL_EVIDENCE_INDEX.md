# US-WW-F01 Final Evidence Index

Terminal gate: **`PASS_US_WW_F01_CWNS_NPDES_JOIN_READY`**.

Durable evidence:
- `CWNS_NATIONAL_STRUCTURE.json` — official nationwide CWNS ZIP/member/header structure; raw ZIP transient.
- `CWNS_IDENTITY_MANIFEST.json` — strict `INFRASTRUCTURE_TYPE=Wastewater` + `PERMIT_SOURCE=NPDES` cardinality: 14,578 linked facilities across 56 jurisdictions; 14,067 distinct official NPDES IDs; no need-dollar values read.
- `ECHO_JOIN_MANIFEST.json` — 14,049/14,067 (99.8720%) exact `ICIS_PERMITS` match; post-2022 violation date/type identity support; no fuzzy matching.
- `DICTIONARY_ACCESS_NOTE.md` — no-auth/free data-dictionary access support.
- `RESULT.md` — canonical gate disposition and claim boundary.

Governance: `CLM-156`, `DEC-159`. No relationship/effect test is authorized. Incremental monetary cost: **0 USD**.
