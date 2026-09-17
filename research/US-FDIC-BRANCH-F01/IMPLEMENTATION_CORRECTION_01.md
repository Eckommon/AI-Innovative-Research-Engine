---
id: US-FDIC-BRANCH-F01-IMPLEMENTATION-CORRECTION-01
type: implementation-correction
created: 2026-09-18
issue: 160
research: US-FDIC-BRANCH-F01
contract_commit: 6568d9bd0d897abb0bcabf8eaf04f2e54f50177f
changes_scientific_contract: false
opens_future_rows: false
incremental_monetary_cost_usd: 0
---

# US-FDIC-BRANCH-F01 Implementation Correction 01

## Why a second attempt is permitted

The first immutable staging attempt produced `17/18` gates with all empirical historical support gates passing. Its only failing requirement was frozen requirement #8: 2025 SOD source/schema readiness without opening any 2025 row.

The first implementation tested #8 by requiring the literal string `UNINUMBR` to occur in either the raw top-level OpenAPI YAML or the raw client-side SOD Custom Download HTML shell. That is an implementation assumption, not part of the frozen scientific contract. The FDIC OpenAPI uses referenced property definitions, while the BankFind web application can render variable metadata client-side. A missing literal in those two raw transport payloads therefore does not establish that the 2025 SOD schema lacks `UNINUMBR`.

## Correction

The frozen requirement and every numerical threshold remain unchanged.

Attempt 02 will verify #8 without reading a 2025 data row by combining:

1. an HTTP `HEAD` request to the official `/sod` endpoint with `YEAR:2025` and requested fields `YEAR,CERT,BRNUM,UNINUMBR`, so no response body/data row is consumed;
2. the already-persisted pre-count official FDIC source preflight establishing that current SOD mandatory variables include `YEAR`, `CERT`, `BRNUM`, and `UNINUMBR`;
3. the fingerprinted official FDIC API/OpenAPI and SOD Custom Download metadata sources.

The first staging result remains immutable and is not deleted or rewritten. Attempt 02 writes to a separate staging directory.

## Boundaries unchanged

- no 2025 SOD data row or branch membership;
- no future BankFind Location row;
- no future History/Structure Change event membership;
- no closure/non-continuation outcome;
- no fuzzy/name/address/ZIP/geospatial/manual identity repair;
- no relationship, prediction, causal, ranking, or novelty claim;
- no change to any of the 18 frozen requirements or thresholds;
- incremental monetary cost remains **0 USD**.
