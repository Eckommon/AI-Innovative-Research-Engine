---
id: US-FDIC-BRANCH-F01
type: outcome-blind-structural-feasibility
created: 2026-09-18
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R38
parent_decision: DEC-231
candidate_future_closure_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-FDIC-BRANCH-F01 — exact physical-branch longitudinal identity feasibility

## Mission / 목적

Determine, before opening any future branch-closure/non-continuation membership, whether official FDIC Summary of Deposits (SOD) and BankFind structure metadata support a deterministic, longitudinal, source-native physical-branch design suitable for a later separately preregistered branch-continuity study.

F01 is structural only. It does **not** test whether low deposits, market position, ownership change or any other exposure predicts branch closure.

## Frozen time structure

### Historical structural/exposure support allowed in F01
- SOD reporting years: **2022, 2023, 2024** only (June 30 snapshots).
- Branch-level rows and structural ownership transitions within these three snapshots may be opened.

### Candidate future outcome window — sealed in F01
- **2024-07-01 through 2025-06-30**.
- 2025 SOD and corresponding BankFind structure-event data may be inspected only for source/schema/field availability and fingerprints where technically possible **without reading row-level branch membership or event membership**.
- No branch may be classified as closed, continued, sold, leased, acquired, merged, relocated, opened or otherwise dispositioned in F01 using future-window rows.

## Frozen identity rule

Primary physical-location identity is exact FDIC **`UNINUMBR`** only.

Official FDIC documentation/Q&A establishes that `UNINUMBR` is associated with a specific physical branch location regardless of ownership and changes only in rare circumstances. `CERT` and `BRNUM` are retained as ownership/institutional context, not substitutes for the physical-location identity.

Allowed normalization:
1. parse official numeric/string representation losslessly;
2. trim surrounding whitespace;
3. preserve the exact integer/string identity after canonical numeric formatting if the official definition declares it numeric.

Prohibited:
- bank/branch name matching;
- address matching;
- ZIP/city/state proximity matching;
- latitude/longitude/geospatial repair;
- fuzzy/manual reconciliation;
- constructing synthetic identity from `CERT + BRNUM` when `UNINUMBR` is missing;
- altering identity rules after observed support counts.

## Frozen structural question

Can 2022–2024 SOD establish a large, clean physical-branch panel in which exact `UNINUMBR` continuity is stable even when institutional ownership context (`CERT`) changes, while official BankFind source/schema metadata provide a future mechanism to distinguish true closure/non-continuation from merger/acquisition/sale/lease/relocation/identifier transitions without using name/address repair?

## Frozen 18-requirement gate

All 18 must PASS for F01 PASS.

1. Official FDIC SOD is publicly machine-readable at zero incremental cost.
2. Official SOD variable/definition metadata are accessible and fingerprintable before structural counts are interpreted.
3. National SOD 2022, 2023 and 2024 sources are each reproducibly accessible and fingerprinted.
4. Required branch identity/time fields `YEAR`, `CERT`, `BRNUM`, `UNINUMBR` are present in all three historical snapshots, and at least one official branch-deposit measure is documented in the SOD schema.
5. Official FDIC documentation supporting `UNINUMBR` as physical-location identity regardless of ownership is persisted in the evidence record before counts are interpreted.
6. Official BankFind Locations source/schema is publicly machine-readable/fingerprintable and exposes branch/institution identity structure sufficient for later exact-link validation.
7. Official BankFind History Events/Bank Structure Changes metadata are accessible and expose event semantics sufficient to prospectively distinguish ownership/merger/relocation-type changes from a genuine branch-discontinuation definition before future event membership is opened.
8. 2025 SOD future source is accessible/fingerprintable and its header/schema confirms `UNINUMBR` identity availability **without reading any 2025 data row**.
9. Candidate 2024-07-01–2025-06-30 future branch membership/event rows remain unopened; no future disposition is computed.
10. No bank/branch name, address, ZIP, geography, coordinates, fuzzy logic or manual identity repair is used.
11. `>=150,000` structurally usable branch-year rows exist across 2022–2024.
12. `>=60,000` distinct valid `UNINUMBR` physical identities exist across 2022–2024.
13. `>=50,000` distinct `UNINUMBR` identities appear in at least two of the three historical SOD years.
14. `>=40,000` distinct `UNINUMBR` identities appear in all three historical SOD years.
15. `>=99%` of otherwise branch-level historical rows carry valid non-null `UNINUMBR`, `CERT`, `BRNUM` and `YEAR` values under the frozen parser.
16. `>=100` exact `UNINUMBR` identities show a `CERT` ownership-context change across 2022–2024 while retaining the same physical identity, demonstrating measurable cross-owner continuity without name/address repair.
17. Deterministic source fingerprints, parser/schema decisions, exclusions and an exposure-only `UNINUMBR × YEAR × CERT × BRNUM` manifest are persisted; no future closure/non-continuation relationship, prediction, ranking, causal metric or novelty claim is computed.
18. Incremental monetary cost is exactly **0 USD**.

## Frozen terminal strings

If all 18 requirements pass:

`PASS_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_READY`

If a valid scientific structural run executes but any requirement fails:

`HOLD_US_FDIC_BRANCH_F01_EXACT_PHYSICAL_BRANCH_LONGITUDINAL_DESIGN_NOT_READY`

Implementation/network/parser defects before a valid structural run are **not** scientific HOLD and must be recorded separately, following the distinction established in `US-FSIS-SAMPLE-F01`.

## PASS consequence

PASS authorizes only a separate outcome-blind `US-FDIC-BRANCH-N01` design. N01 must prospectively define how future 2025 SOD absence and BankFind structure-event semantics distinguish true closure/non-continuation from acquisition, sale/lease, merger, relocation or rare `UNINUMBR` change **before any future branch membership is opened**.

PASS does not authorize an E01.

## Non-claims

F01 makes no claim that deposit level, deposit share, market concentration, ownership transition or any other feature predicts or causes branch closure. FDIC has already published descriptive branch closure analyses; generic low-deposit→closure association is not a novelty claim.

Incremental monetary cost must remain **0 USD**.
