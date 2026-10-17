# NOAA×QCEW F01 Attempt 01 / 최초 실증 결과

- Disposition: \`HOLD_US_NOAA_QCEW_F01_FROZEN_STRUCTURAL_GATES_NOT_ALL_READY\`
- Scientific gates evaluated: 18 / 18
- Source lineage: \`49ddd7987737bac51442db91c7082666c79e56b2\`
- **NO** 2025+ QCEW employment outcomes, association, causal estimate, ranking or PII disclosed.
- Cost: **0 USD**.

- Gate 01: PASS — NOAA first-party provenance/license documentation and 0 USD; 1 / 1 (exact first-party, no billing)
- Gate 02: PASS — Pinned NOAA source gzip + SHA and >1MB; 12888092 / None (>1000000 bytes)
- Gate 03: PASS — Three frozen BLS sector CSV bodies fingerprinted; 3 / 3 (3/3)
- Gate 04: PASS — NOAA schema exact fields; 6 / 6 (6/6)
- Gate 05: PASS — BLS required schema each sector; 3 / 3 (3/3)
- Gate 06: PASS — County-only C vs zonal/marine exclusion; 42515 / 75593 (CZ_TYPE=C only, excluded Z/M)
- Gate 07: PASS — NOAA exact county syntax >=95%; 42515 / 42515 (>=95%)
- Gate 08: PASS — NOAA unique event ID >=99.9%; 42311 / 42311 (>=99.9%)
- Gate 09: PASS — NOAA 2023 true event time >=99%; 42515 / 42515 (>=99%)
- Gate 10: PASS — NOAA distinct valid non-CT counties >=1200; 3035 / None (>=1200)
- Gate 11: PASS — Five frozen event types >=4000, >=900 counties; {'events': 40790, 'counties': 2994} / None (events>=4000 counties>=900)
- Gate 12: HOLD — BLS filtered sector syntax/disclosure >=99%; 9929 / 11116 (>=99%)
- Gate 13: PASS — BLS exact county-sector key uniqueness >=99.9%; 7458 / 7458 (>=99.9%)
- Gate 14: PASS — Three BLS private sector supports >=1500 counties; {'23': 2916, '62': 2091, '72': 2451} / None (each >=1500)
- Gate 15: PASS — NOAA exact county match >=900 per industry; {'23': 2650, '62': 1880, '72': 2237} / None (each >=900)
- Gate 16: PASS — Binary recorded-storm metadata assigned >=95%; 7458 / 7458 (>=95%; absence=NO_RECORDED_EVENT)
- Gate 17: PASS — Future QCEW outcome/PII firewall; 1 / 1 (2025+ employment/wage columns never inspected)
- Gate 18: PASS — Complete 18-gate SHA/time evidence and zero-cost; 18 / 18 (18 entries + SHA/fetch UTC)
