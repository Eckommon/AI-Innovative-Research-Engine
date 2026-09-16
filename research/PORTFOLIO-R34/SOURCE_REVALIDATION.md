---
id: PORTFOLIO-R34-SOURCE-REVALIDATION
type: source-internal-history-literature-revalidation
created: 2026-09-17
issue: 149
contract_commit: db56429107fc1a7054b9be0b5a78d91424f72971
activation: DEC-210
candidate_outcomes_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R34 Source / Internal-History / Literature Revalidation

## Scope / 범위

This document revalidates the **exact four-candidate pool frozen before Issue #149**. It does not alter candidate membership and does not persist a portfolio score or selection.

Evidence categories are deliberately separated:

1. current official public-source access / semantics;
2. deterministic identity prospects;
3. internal repository overlap from completed earlier branches;
4. bounded external direct-overlap literature / agency-practice evidence;
5. exact information a separately authorized outcome-blind F01 would resolve.

No candidate-specific outcome magnitude, exposure-stratified outcome count, coefficient, predictive statistic, relationship direction, future-event membership or causal quantity was opened in R34 revalidation. Search absence is **not** treated as novelty proof.

## 1. US-EPA-XMEDIA-001 — RCRA compliance structure → later NPDES effluent exceedance

### Current official-source status

**Source-operable with strong official cross-program identity.**

Current EPA ECHO downloads expose the required source families through public zero-cost products:

- `RCRAInfo` and `RCRA Pipeline` national data;
- `FRS Facilities and Program Linkages`;
- `ICIS-NPDES` facility / permit / inspection / enforcement files;
- national and jurisdiction-level NPDES effluent-violation downloads;
- ECHO public web services for RCRA and NPDES facility queries / DFR and effluent-related retrieval.

EPA's current ECHO download documentation states that the FRS identifier is used to join ECHO dataset files and provides a separate Facilities and Program Linkages product. The public products are periodically refreshed and do not require a paid data vendor.

Official references:

- https://echo.epa.gov/tools/data-downloads
- https://echo.epa.gov/resources/echo-data/about-the-data/rcra-data-download
- https://echo.epa.gov/resources/echo-data/about-the-data/npdes-download-summary
- https://echo.epa.gov/tools/web-services
- https://www.epa.gov/frs

### Native identity prospect

**Very strong.** The authorized future route is exact official linkage only:

- RCRA `SOURCE_ID` identifies the RCRA facility;
- RCRA / ECHO `REGISTRY_ID` is the Federal Registry / FRS identity;
- ICIS-NPDES facility data expose the FRS-assigned facility identifier (`FACILITY_UIN` / Registry ID semantics) together with source-native `NPDES_ID`;
- FRS Program Linkages provides the official cross-program bridge.

A future F01 must use the exact official FRS link and reject name, address, corporate-parent, latitude/longitude or manual entity repair.

### Direct outcome quality

The downstream NPDES product has a direct regulatory outcome family rather than a proxy: effluent-limit violations are represented as ICIS-NPDES violation records linked to source-native NPDES permits and monitoring periods. A future descendant could therefore preregister a later **effluent-exceedance occurrence** endpoint without substituting a general enforcement score or facility ranking.

R34 does **not** open those violation rows or conditioned occurrence values.

### Internal portfolio overlap

Material but not near-identical.

Earlier `US-RCRA-F01 → N01 → E01` used the RCRA ecosystem for a different relationship:

> FEMA-declared physical hazard / disaster → same-facility RCRA CEI `FOUND_VIOLATION` monitoring outcome.

That branch reached a terminal preregistered E01 with 297 paired facilities and did not support its positive hypothesis. The new R34 candidate **must not rescue or reinterpret that result**. Its exposure/outcome relation is independently framed as historical RCRA compliance-monitoring / violation structure → later NPDES effluent exceedance at the same officially linked physical facility.

Internal references:

- `research/US-RCRA-F01/RESULT.md`
- `research/US-RCRA-N01/RESULT.md`
- `research/US-RCRA-E01/RESULT.md`

### External direct-overlap / novelty risk

**Moderate.** EPA already operates cross-statute / multi-media compliance screening and has a long history of multi-media enforcement concepts. Therefore the high-level idea that one facility's compliance state across environmental programs can be jointly screened is not novel.

Bounded revalidation did **not** identify a materially near-identical prospective public-data design that freezes RCRA inspection/violation history and tests a later ICIS-NPDES effluent-exceedance endpoint through exact FRS identity. This absence must not be interpreted as proof of novelty.

Adjacent official references:

- EPA ECHO Corporate Compliance Screener and cross-program facility search;
- EPA multi-media enforcement / compliance initiative materials;
- ECHO facility-search capability to filter facilities with multiple program IDs.

### Prospective next-gate information

A cheap, outcome-blind F01 could resolve the most decision-relevant unknowns before any NPDES outcome is opened:

1. exact current RCRA↔FRS↔NPDES facility-link coverage;
2. facility and permit cardinality;
3. longitudinal RCRA evaluation / violation date support;
4. NPDES permit / monitoring-period structural time support;
5. whether enough exact cross-program facilities remain after fail-closed identity and date rules;
6. whether current official endpoints / jurisdictional files permit reproducible zero-cost descendant execution without loading the national multi-gigabyte effluent file.

**Revalidation status:** `STRONG_F01_CANDIDATE__EXACT_FRS_JOIN__NOVELTY_CONSERVATIVE`.

---

## 2. US-BTS-PORT-001 — vessel berthing stress → later port trade throughput

### Current official-source status

**Operational metrics exist, but the exact machine-readable cross-source port identity remains unresolved.**

BTS Port Performance currently publishes / presents:

- weekly vessel-berthing statistics by port (2025 onward), including average / median berthing time and calls;
- monthly TEU data by port;
- broader port-performance measures derived in part from USCG AIS.

U.S. Census foreign-trade products separately use Schedule-D port codes and provide port-level trade records / shipping weight.

Official references:

- https://www.bts.gov/ports
- https://www.bts.gov/port-performance-freight-statistics
- https://www.census.gov/foreign-trade/schedules/d/distcode.html

### Native identity prospect

**Weak pending proof.** BTS itself warns that port boundaries / definitions can differ across its Port Performance source products and Census trade sources. The frozen candidate contract prohibits port-name normalization, geospatial nearest-neighbor mapping or manual crosswalk repair.

A future F01 can PASS only if an official deterministic BTS→Census port identity or exact crosswalk is established prospectively. A shared human-readable port label is insufficient.

### Internal portfolio overlap

**High and directly informative.** Earlier `US-PORT-F01` examined BTS berthing/dwell data and terminated at:

`HOLD_US_PORT_PUBLIC_JOIN_ROUTE`

because the inspected public machine-readable dwell assets did not expose a reproducible `port × time` identity field, despite source-ready NOAA / USACE geography. That prior branch specifically forbids dashboard scraping or ad-hoc manual port mapping as a rescue.

The current R34 candidate changes the downstream outcome from weather-linked dwell to trade throughput, but **the same upstream machine-readable port-identity bottleneck remains highly relevant**.

Internal reference:

- `research/US-PORT-F01/RESULT.md`

### External direct-overlap / novelty risk

**High overlap.** Port dwell, congestion, vessel-call efficiency, AIS-derived port-stay measures and throughput estimation are mature research / operational topics. Current literature continues to model port stays / turnaround and infer throughput / performance from AIS and port activity.

The candidate can still have operational value, but R34 must not infer innovation novelty from combining an AIS-derived dwell measure with port throughput.

### Prospective next-gate information

The first future gate would largely re-test a known structural bottleneck:

1. whether the current post-2025 BTS weekly product exposes a stable machine-readable per-port identity;
2. whether that identity has an official exact Schedule-D mapping;
3. whether enough ports remain for heterogeneous independent-unit support.

Because the candidate's top-port universe is inherently small relative to facility / vessel / mine alternatives, the FTA N01 lesson also lowers its independent-unit prospect.

**Revalidation status:** `HOLD_LEANING__PORT_IDENTITY_UNRESOLVED__PRIOR_INTERNAL_BLOCKER__HIGH_OVERLAP`.

---

## 3. US-USCG-VESSEL-001 — inspection deficiencies / operational control → later marine casualty

### Current official-source status

**Technically very strong.** USCG CGMIX currently exposes public, zero-cost products for both sides:

- Port State Information Exchange (PSIX): vessel summary, vessel cases / inspection activity, deficiencies and operational controls;
- Investigation Information Reports (IIR): closed reportable marine casualties / investigations and involved-vessel records;
- downloadable XML / spreadsheet products and web-service documentation.

Official references:

- https://cgmix.uscg.mil/
- https://cgmix.uscg.mil/PSIX/PSIXData.aspx
- https://cgmix.uscg.mil/IIR/IIRData.aspx

### Native identity prospect

**Very strong, subject to an outcome-blind equality/coverage proof.** Both products are MISLE-derived. PSIX exposes Coast Guard vessel identifiers; IIR involved-vessel records expose `MISLEVesselId` and primary vessel identification. A future F01 could prospectively verify exact identifier equality and overlap without vessel-name repair.

No IMO/name/callsign fuzzy identity is authorized as a substitute if native MISLE linkage fails.

### Direct outcome quality

Marine casualty is a direct event endpoint, not a general inspection score. A later descendant could freeze future reportable casualty occurrence by vessel after an inspection / deficiency window, subject to outcome-blind time / observation eligibility rules.

R34 does not open deficiency-conditioned casualty membership or rates.

### Internal portfolio overlap

No prior repository branch materially matching **USCG inspection deficiency → later marine casualty** was found in the bounded repository-history review.

### External direct-overlap / novelty risk

**Very high / near-identical.** Published maritime-safety research already studies the predictive power of port-state-control inspection outcomes / deficiencies for future shipping accidents. In particular, Heij & Knapp (2018), *Predictive power of inspection outcomes for future shipping accidents*, is conceptually near-identical to the candidate's core relationship.

Therefore source readiness is excellent but low-overlap / novelty credit must be near zero. Selecting the candidate would mostly reproduce / transfer an established relationship into a U.S. Coast Guard public-data implementation rather than explore a genuinely under-tested cross-domain relation.

### Prospective next-gate information

An F01 would efficiently quantify current native MISLE-ID coverage and longitudinal support, but those technical unknowns are less strategically informative because the scientific relationship family already has strong direct precedent.

**Revalidation status:** `TECHNICALLY_STRONG__DIRECT_LITERATURE_OVERLAP_HIGH`.

---

## 4. US-MSHA-001 — mine inspection / violation structure → later accident / injury incidence

### Current official-source status

**Extremely strong technically.** MSHA publishes zero-cost machine-readable national files with native identity:

- Mine data with source-native `MINE_ID`;
- inspection records with `MINE_ID` and source-native `EVENT_NO` / Event Number;
- violation records directly linked to inspections by Event Number;
- accident / injury data linked by Mine ID;
- longitudinal employment / hours products.

Official references:

- https://www.msha.gov/data-reports/data-sources-calculators
- https://www.msha.gov/data-and-reports

### Native identity prospect

**Excellent.** Mine ID and Event Number provide exact deterministic source-native joins; no entity repair is necessary.

### Internal portfolio overlap

**High.** Earlier `US-MINE-F01` already established structural source readiness on 2019–2025 MSHA products and `US-MINE-N01` separately tested an all-sector operator-hours ramp-up design outcome-blind.

The earlier F01 reported 92,007 mine IDs and very high accident/employment key overlap. N01 formed 2,084 deterministic pairs but failed two preregistered design-support / identity requirements and correctly stopped before injury outcomes.

The current R34 candidate changes the exposure family from hours ramp-up to inspection / violation structure, so it is not an impermissible direct rescue of that N01. Nevertheless the same data ecosystem, units and downstream injury domain have already yielded substantial internal information.

Internal references:

- `research/US-MINE-F01/RESULT.md`
- `research/US-MINE-N01/RESULT.md`

### External direct-overlap / novelty risk

**Near-identical direct overlap.** Prior published work using MSHA data already uses inspection violations / enforcement histories to forecast later injuries / lost workdays, including research evaluating violations as predictors of nonfatal / disabling injuries over a subsequent time window. Additional longitudinal mine-level research links regulatory adherence measures and injury rates.

Accordingly the candidate remains an excellent technical benchmark but has essentially no low-overlap / novelty advantage for this innovation-discovery mission.

### Prospective next-gate information

The source/join question is already largely resolved by prior internal F01 and public MSHA semantics. A new inspection-violation F01 could still freeze a distinct exposure, but its marginal information gain is lower than a genuinely new cross-media join.

**Revalidation status:** `TECHNICALLY_EXCELLENT__INTERNAL_AND_EXTERNAL_DIRECT_OVERLAP_HIGH`.

---

## Cross-candidate revalidation summary / 후보간 재검증 요약

| Candidate | Current source operability | Native/exact join | Independent-unit prospect | Internal overlap | External direct-overlap risk | Next-gate implication |
|---|---|---|---|---|---|---|
| `US-EPA-XMEDIA-001` | Strong | **Very strong — official FRS cross-program identity** | Strong, actual exact overlap still unknown | Medium / adjacent RCRA branch | Medium | High-value F01: quantify exact cross-program support before outcomes |
| `US-BTS-PORT-001` | Medium | **Weak/unresolved** | Low–medium; small top-port universe | **High — prior US-PORT identity blocker** | High | Mostly re-tests known identity blocker |
| `US-USCG-VESSEL-001` | **Very strong** | **Very strong — MISLE-derived vessel identity** | Very strong | Low | **Very high / near-identical** | Technically easy, scientifically lower information gain |
| `US-MSHA-001` | **Very strong** | **Excellent — Mine ID / Event Number** | Very strong | **High — prior mine F01/N01** | **Very high / near-identical** | Low marginal discovery gain despite technical ease |

## Revalidation conclusion / 재검증 결론

All four frozen candidates remain in the pool exactly as prospectively registered. This document **does not select a candidate**.

The evidence materially differentiates them before one-time scoring:

- EPA cross-media has the strongest combination of official exact cross-program identity, direct regulatory outcome and new cross-domain information gain, but novelty remains only **conservatively plausible**, not proven.
- BTS port remains constrained by the same type of exact port-identity problem already observed internally and by small independent-unit support.
- USCG vessel is technically excellent but has near-identical published predictive precedent.
- MSHA is technically excellent but has both near-identical published precedent and substantial internal portfolio history.

The next allowed action is to create **one immutable `SCORECARD.md` exactly once** under the frozen /45 rubric. No candidate outcomes may be opened before that scorecard and terminal portfolio decision.

Incremental monetary cost remains **0 USD**.
