---
id: PORTFOLIO-R05-RESULT
type: mission-roi-portfolio-selection
created: 2026-09-04
issue: 78
state: COMPLETED_SELECT
mission_anchor: MEM-054
selected_candidate: C-JP-001
selected_gate: JP-PORT-F01
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R05 Result — Post-US-Grid Structural HOLD Mission-ROI Reselection
# PORTFOLIO-R05 결과 — 미국 전력망 구조적 HOLD 이후 목적-ROI 재선정

## Final selection / 최종 선정

**`SELECT_C_JP_001_PORT_WEATHER_THROUGHPUT_STRESS`**

Selected branch:

**`C-JP-001 — Japan Port Weather–Throughput Stress`**  
**`C-JP-001 — 일본 항만 기상–물동량 스트레스`**

Exact next bounded gate:

**`JP-PORT-F01 — MLIT Port-Month × JMA Weather-Station Deterministic Join Feasibility`**.

## Why U.S.-grid does not continue automatically / 미국 전력망 즉시 연장 금지

`US-GRID-F01` remains a real PASS and reusable asset.

However, outcome-blind E01 structural preflight showed that a reasonable anti-pseudoreplication BA-year design collapses to only:
- ERCO 2021;
- ERCO 2022;
- ERCO 2023.

That is three cells from one BA. `DEC-109` therefore stops the immediate numerical descendant before any queue-duration magnitude or EIA operating relationship is opened.

## Current source refresh / 현행 소스 갱신

### Japan MLIT Port Survey
Official MLIT Port Survey states that it is Japan's fundamental port statistic and publishes:
- vessel arrivals;
- maritime inbound/outbound cargo;
- container counts;
- monthly preliminary, port-level aggregate and final results.

Current MLIT page:
`https://www.mlit.go.jp/k-toukei/kouwan.html`

As of the current source refresh, MLIT lists 2026 monthly releases and future publication dates.

### Japan Meteorological Agency
JMA's official historical-weather download supports selection of:
- station;
- weather element;
- date period;
- CSV output;
- quality/homogeneity flags.

Current JMA route:
`https://www.data.jma.go.jp/risk/obsdl/`

The site explicitly documents missing/quality and observation-environment homogeneity indicators. This is important for a later reproducible port-month weather aggregation.

### ENTSO-E / ERA5
`C-EU-001` remains scientifically excellent, but current automated source access has two independent credential dependencies:
- ENTSO-E Transparency Platform export/Web API uses account/security-token management;
- ERA5 CDS API requires an account and personal access token, and dataset terms must be accepted before download.

These are zero-price routes but materially reduce immediate minimum operability in the current execution context.

### Singapore MPA / NEA
MPA continues to publish monthly vessel arrivals and tonnage through 2026, with keyless public sample API/CSV access.
NEA also exposes high-frequency rainfall via data.gov.sg.

The Singapore branch remains highly operable, but the primary maritime outcome is one national-port-system monthly series, providing less cross-port independent-unit diversity than Japan.

## Candidate comparison / 후보 비교

Scores are 0–5 portfolio decision aids, not empirical findings.

| Candidate | Mission value | Cross-source value | Independent-unit / falsifiability | Practical utility | Source access | Low mapping/rescue friction | Next-gate info gain | Low diminishing-return risk | Total /40 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **`C-JP-001 Port Weather–Throughput Stress`** | 4 | 4 | 4 | 4 | 5 | 3 | 4 | 5 | **33** | **SELECT** |
| `C-EU-001 Cross-National Grid Stress` | 5 | 5 | 5 | 5 | 2 | 2 | 4 | 5 | **33** | `HOLD_READY_HIGH_VALUE` |
| `C-EU-004 Industrial Site Climate Risk` | 4 | 5 | 3 | 4 | 5 | 5 | 2 | 4 | **32** | `PRESERVE_JOIN_ASSET` |
| `C-SG-001 Maritime Activity × Weather Regime` | 3 | 4 | 3 | 4 | 5 | 5 | 3 | 5 | **32** | `HOLD_READY` |
| `C-US-003R Critical Mineral continuation` | 5 | 5 | 4 | 5 | 5 | 4 | 2 | 1 | **31** | `VALIDATED_RESULT__NO_AUTO_CONTINUATION` |
| `C-US-001 U.S. Grid continuation` | 5 | 5 | 2 | 5 | 5 | 4 | 1 | 1 | **28** | `PRESERVE_F01__E01_STRUCTURAL_HOLD` |

## Tie-break / 동률 판정

Japan and EU score equally on the transparent portfolio matrix.

Tie-break uses the project continuity principle:
**prefer the route whose next gate can reduce a scientific/source-semantic uncertainty with minimum-operable current capabilities, rather than first requiring external credential provisioning.**

Japan therefore wins the immediate slot.

This does **not** reject the EU candidate. If ENTSO-E/CDS credentials become available or a zero-credential official route is qualified, C-EU-001 remains a top-tier candidate.

## Exact next gate / 정확한 다음 게이트

Open only:

### `JP-PORT-F01 — MLIT Port-Month × JMA Weather-Station Deterministic Join Feasibility`

F01 must remain outcome-blind and source-semantic.

It may verify:
1. exact MLIT/e-Stat port-month source identity, file/version/snapshot and port identifiers;
2. exact monthly vessel/cargo/container fields and units;
3. official or deterministic port coordinate source;
4. JMA station identifier, coordinates, daily variables, quality and homogeneity semantics;
5. a prospective port→weather-station mapping rule with a maximum-distance/identity rule frozen before throughput-weather results;
6. common month/time coverage and revision/missingness rules;
7. whether a future multi-port × month experiment can use a full or prospectively qualified subset without choosing ports after viewing relationships.

F01 shall **not** calculate:
- port weather sensitivity;
- rainfall/wind vs cargo correlations;
- port rankings;
- disruption thresholds;
- causal effects;
- investment/policy rankings.

## Branch-stop / 중단

HOLD/REJECT and return to Stage 0 if:
- port identity/coordinates cannot be reconciled to JMA stations without arbitrary manual assignment;
- official monthly port data cannot be retrieved reproducibly under a zero-cost route;
- JMA quality/homogeneity semantics make the planned weather exposure non-comparable;
- only a tiny post-hoc port subset can be made to work.

## Cost / 비용

Incremental monetary cost remained **0 USD**. Any potentially billable work requires explicit prior user approval.
