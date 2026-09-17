---
id: US-FDIC-BRANCH-F01-SOURCE-PREFLIGHT
type: source-preflight
created: 2026-09-18
issue: 160
research: US-FDIC-BRANCH-F01
contract_commit: 6568d9bd0d897abb0bcabf8eaf04f2e54f50177f
outcome_blind: true
incremental_monetary_cost_usd: 0
---

# US-FDIC-BRANCH-F01 Source Preflight / 소스 사전점검

This preflight is persisted **before any F01 historical row-count interpretation**. It resolves only official source/schema/identity semantics required by the frozen contract. Candidate future branch/event membership remains unopened.

## Official source findings / 공식 소스 확인

1. **FDIC BankFind Suite API documentation**
   - Official URL: `https://api.fdic.gov/banks/docs`
   - The FDIC documents public API families for `SOD`, `locations`, and `history` and states that public output is available as JSON or CSV.
   - The documentation exposes machine-readable API definition/OpenAPI resources for SOD, Location, and History datasets.

2. **Summary of Deposits custom download**
   - Official URL: `https://banks.data.fdic.gov/bankfind-suite/SOD/customDownload`
   - The national custom-download interface covers annual SOD periods back to 1994.
   - Its mandatory variables include `YEAR`, `CERT`, `BRNUM`, and `UNINUMBR` (along with branch-name/address/state context).

3. **`UNINUMBR` physical-location semantics**
   - Official FDIC 2021 Academic Challenge Q&A source: `https://www.fdic.gov/analysis/academic-challenge/assets/files/2021/second-qa-transcript.pdf`
   - The FDIC explains that `UNINUMBR` is associated with a specific physical bank-branch location regardless of ownership, whereas `BRNUM` is also a branch-level SOD variable but does not carry the same cross-ownership physical-location semantics.
   - This is the frozen scientific reason that F01 treats exact `UNINUMBR` as primary identity and `CERT`/`BRNUM` as ownership/institution context.

4. **Bank structure-event semantics**
   - Official BankFind Bank Structure Changes interface distinguishes categories including branch purchases/assumptions, branch office relocations, openings, and closings.
   - F01 may persist these event-category semantics and schema only; it must not query future event membership for candidate branches.

## Execution boundary / 실행 경계

Authorized after this preflight:
- historical SOD branch rows for 2022, 2023, and 2024 only;
- exact `UNINUMBR` longitudinal continuity and historical `CERT` change counts;
- source/schema fingerprints;
- BankFind SOD/Location/History metadata only where future branch membership would otherwise be exposed.

Still prohibited:
- any 2025 SOD branch data row or membership;
- any 2024-07-01 through 2025-06-30 candidate branch closure/non-continuation membership;
- any future History/Structure-Change event membership;
- any name/address/ZIP/geospatial/fuzzy/manual identity repair;
- relationship, prediction, causal, ranking, or novelty claims.

Incremental monetary cost remains **0 USD**.
