# PORTFOLIO-R35 — Immutable Mission-ROI Scorecard / 불변 평가표

**Date:** 2026-09-17  
**Issue:** #153  
**Frozen contract:** `4febd519dfae899897bed8d2c8ab45edb85fb33c`  
**Source revalidation:** `127170adafcddefb66e3a9bfd33943b8fd5d53be`  
**Candidate outcomes opened:** false  
**Scoring occurrence:** exactly once

The nine dimensions and tie-break were frozen before Issue binding. This file applies them once and must not be rescored from future F01/N01/outcome observations.

| Candidate | Mission bottleneck | Cross-source value | Direct outcome | Independent-unit prospect | Practical value | Zero-cost operability | Join defensibility | Next-gate info gain | Low overlap / novelty risk | **Total /45** | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **US-FAA-AIP-001** | 5 | 5 | 5 | 4 | 5 | 5 | 3 | 5 | 3 | **40** | **SELECT_F01** |
| US-EPA-DWSRF-001 | 4 | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 1 | **39** | HOLD_DIRECT_PRECEDENT |
| US-PHMSA-LI-001 | 3 | 4 | 5 | 5 | 5 | 5 | 5 | 5 | 1 | **38** | HOLD_AGENCY_INTENT_AND_OVERLAP |
| US-NRC-ROP-001 | 3 | 3 | 5 | 2 | 5 | 5 | 5 | 3 | 1 | **32** | HOLD_INTEGRATED_FRAMEWORK_AND_SMALL_N |

## Score rationale / 점수 근거

### US-FAA-AIP-001 — 40/45

- **Mission bottleneck 5:** tests whether public capital-investment records can be connected prospectively to a later operational-performance dataset, a high-value pattern for the innovation engine.
- **Cross-source 5:** FAA AIP grants and BTS airline operations are genuinely distinct administrative/operational systems.
- **Direct outcome 5:** airport departure/on-time delay performance is an operational outcome rather than an indirect proxy.
- **Independent units 4:** the commercial-airport reporting universe should provide many airport-years, but exact AIP↔BTS support is not yet proven.
- **Practical 5:** directly relevant to infrastructure allocation, airport resilience and project prioritization questions, with causal claims explicitly excluded.
- **Zero-cost 5:** FAA grant histories and BTS downloads are public/free.
- **Join 3:** the key weakness. `Loc ID` ↔ BTS airport identity is not yet proven as an official deterministic bridge and cannot be assumed from matching strings.
- **Next-gate info 5:** an outcome-blind F01 can decisively answer source/schema/identity/cardinality feasibility at low cost.
- **Novelty 3:** AIP/PFC funding and airport efficiency have published precedent, but revalidation did not identify a near-identical AIP-project→future BTS-delay design. This is not a novelty claim.

### US-EPA-DWSRF-001 — 39/45

Technically this is the cleanest join: SRF/WIITS and SDWIS expose exact `PWSID`; project dates/attributes and downstream compliance support are highly practical and zero-cost. It loses primarily on **mission novelty/overlap**: EPA OIG already examined DWSRF projects followed by post-project violations in a compliance-targeted category, and CWSRF assistance→post-funding compliance has direct empirical literature. Detailed project-level portal coverage also begins only in 2021, reducing longitudinal design freedom.

### US-PHMSA-LI-001 — 38/45

Exact `OpID`, public leading-indicator downloads and incident data make this technically excellent. It is not selected because PHMSA itself defines SRCR/Integrity Assurance notifications as leading indicators monitored before failures, while published operator-level enforcement→safety-performance research already combines regulatory activity with incident consequences. The engine would gain less new relationship-discovery information than from FAA AIP.

### US-NRC-ROP-001 — 32/45

NRC provides unusually clean inspection-finding and PI data with plant/site/docket semantics, but the operating-reactor universe is small and the proposed relation is close to the explicit ROP design: NRC already integrates inspection findings and performance indicators in quarterly plant assessment. This is valuable benchmark material but weak as the next innovation-discovery branch.

## Selection / 선정

**`SELECT_US_FAA_AIP_001_AIRFIELD_INFRASTRUCTURE_TO_BTS_DELAY_F01`**

`US-FAA-AIP-001` is the unique highest score at **40/45**. No tie-break is required.

The selection authorizes only a separate **outcome-blind F01** whose first job is to prove or reject the exact FAA AIP `Loc ID` ↔ BTS airport identity route, current machine-readable access, time support and aggregate cardinality **without opening grant-conditioned future delay values**.

If the exact identity route cannot be established prospectively, F01 must HOLD. It may not use airport-name matching, manual repair, geographic nearest-neighbor matching, or an assumption that identical-looking three-character codes have identical semantics.

No candidate relationship, causal effect, infrastructure effectiveness claim or novelty claim is established by this scorecard. Incremental monetary cost remains **0 USD**.
