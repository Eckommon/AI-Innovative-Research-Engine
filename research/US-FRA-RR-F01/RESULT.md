---
id: US-FRA-RR-F01-RESULT
type: feasibility-execution-result
created: 2026-10-08
issue: 196
research: US-FRA-RR-F01
operational_disposition: BLOCKED_IMPLEMENTATION
scientific_disposition: NOT_EXECUTED
contract_commit: 492e2a29261e786fe115fa9eaf2f89a8862fa5a6
attempt_01_commit: 107e433bbd1ab3b3aecf68e99a8de9afa5178dad
attempt_02_commit: 1cbcde5014639646dc4eb3653322d780d35e9786
incremental_monetary_cost_usd: 0
---

# US-FRA-RR-F01 Result / 결과

## Terminal operational disposition

**`BLOCKED_IMPLEMENTATION_FRA_HISTORICAL_DATA_OPERATION__SCIENTIFIC_GATE_NOT_EXECUTED`**

The frozen 18-gate scientific F01 was not validly executed.

Attempt 01 proved the FRA ASMX landing and WSDL were reachable and exposed all required operations, but a parser defect incorrectly rejected no-argument WSDL operations.

Attempt 02 corrected only that parser defect. It validly established:
- ASMX landing: HTTP 200;
- WSDL: HTTP 200;
- `GetRailroadData`, `GetF54Schema`, `GetF55Schema`, `GetAccident54DataByRailroad`, `GetAccident55DataByRailroad`: present;
- source-native historical data signatures: `year` only;
- railroad reference body: HTTP 200, **2,981** row candidates, fields `Name` + `Railroad`;
- Form54 schema: HTTP 200 / 19,652 bytes;
- Form55 schema: HTTP 200 / 3,924 bytes.

The first authorized historical Form54/Form55 data operation then returned HTTP 500 from the official ASMX service before row-level historical evidence was obtained.

This is not a scientific HOLD.

## Preserved firewall

- 2026+ Form54 accident membership opened: false;
- future rows consumed: 0;
- relationship/prediction/ranking/causal metric: false;
- prior-accident predictor computed: false;
- identity repair: false;
- cost: 0 USD.

## Branch-stop

Two consecutive implementation descendants have now occurred:
1. WSDL no-argument parser representation defect;
2. official historical data operation HTTP 500.

The route is not uniquely mission-critical, and R54 retained a strong independent alternative, EPA RCRA. A third FRA workaround would primarily reduce transport/service uncertainty rather than scientific uncertainty.

Apply:

**`HOLD_BRANCH / ARCHIVE_ROUTE → RETURN_TO_PORTFOLIO`**

A future FRA re-entry requires a separately frozen contract around a reproducibly working official row-bearing download/API route.

## Consequence

- `US-FRA-RR-N01` not authorized.
- `US-FRA-RR-E01` not authorized.
- preserve Attempts 01/02 as implementation evidence.
- return to independent Stage-0 portfolio reselection.

Incremental monetary cost: **0 USD**.
