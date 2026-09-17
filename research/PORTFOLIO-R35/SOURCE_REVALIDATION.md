# PORTFOLIO-R35 — Source & Literature Revalidation / 소스·문헌 재검증

**Date:** 2026-09-17  
**Issue:** #153  
**Frozen contract:** `4febd519dfae899897bed8d2c8ab45edb85fb33c`  
**Candidate outcomes opened:** false  
**Incremental monetary cost:** 0 USD

This document revalidates only current official source access, identifier semantics, support risk and prior-work overlap. It does **not** inspect grant-conditioned delays, funded-system future violations, leading-indicator-conditioned incidents, finding-conditioned reactor PIs, or any relationship direction.

## 1. US-FAA-AIP-001

### Current official source support

- FAA AIP Grant Histories currently provides annual grant histories for NPIAS airports and downloadable annual grant summaries, including Excel for recent years.
- Current FAA AIP grant listings expose `Loc ID`, airport, project description, entitlement/discretionary amounts and total grant amount.
- BTS TranStats Master Coordinate defines a DOT `AirportID` for longitudinal airport analysis and a separate three-character alpha-numeric `Airport` code issued by U.S. DOT.
- BTS on-time tables expose `OriginAirportID` / `DestAirportID` and airport codes, creating a technically accessible operational-performance side.

Official anchors:
- https://www.faa.gov/airports/aip/grant_histories
- https://www.faa.gov/airports/aip/2026_aip_grants
- https://www.transtats.bts.gov/Fields.asp?gnoyr_VQ=FLL
- https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGK

### Identity assessment

**Unresolved but sharply testable.** FAA `Loc ID` and BTS `Airport` frequently have equal-looking three-character codes for commercial airports, but R35 found no authoritative statement establishing universal semantic equivalence. String equality alone is not accepted as an official crosswalk.

A selected F01 can remain outcome-blind while testing:
1. current FAA annual grant-file schema and exact `Loc ID` support;
2. current BTS airport-code / `AirportID` semantics;
3. whether FAA/NASR contains a deterministic official bridge adequate to bind the two systems;
4. exact-match subset cardinality and calendar support;
5. exclusion of state-block/program rows such as `*GAB`, `*PAB`, etc.

This makes F01 highly informative: a clean exact route produces a large airport-year design candidate; failure terminates cheaply before delay outcomes are opened.

### Literature overlap

A published 2015 airport-efficiency study explicitly examined AIP/PFC funding and U.S. airport productive efficiency, so AIP funding effects are not a blank research area. The revalidation did **not** identify a near-identical preregistered FAA-AIP-airfield-project → subsequent BTS airport-delay design. Search absence is not novelty proof.

Reference:
- `US airport financial reform and its implications for airport efficiency: An exploratory investigation`, Journal of Air Transport Management 47 (2015), DOI family indexed at ScienceDirect.

### R35 source disposition

**`STRONG_INFORMATION_GAIN__IDENTITY_PREFLIGHT_REQUIRED__OVERLAP_MODERATE`**

---

## 2. US-EPA-DWSRF-001

### Current official source support

EPA's current SRF Public Portal provides detailed project-specific DWSRF data for projects signed or modified since 2021 and allows customizable report downloads. The Drinking Water Assistance Agreement data dictionary explicitly exposes:

- `PWSID` — unique number assigned to the PWS as identified in SDWIS;
- PWS name/type;
- initial agreement date;
- project start;
- project completion;
- project category / description;
- compliance category;
- agreement amounts and other financing attributes.

EPA's SDWIS Federal Reporting Services data dictionary independently defines PWS ID as the unique public-water-system identifier. Thus the prospective WIITS/SRF ↔ SDWIS identity is source-native exact `PWSID`, not name/address repair.

Official anchors:
- https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/owsrf_public/home
- https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/owsrf_public/reports
- https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/owsrf_public/drinking-water-data-dictionary-page
- https://www.epa.gov/DWdata/sdwis-federal-reporting-services-data-dictionary

### Support assessment

Technically very strong, but detailed project-level portal coverage begins in 2021. A later N01 would have to handle funding selection/endogeneity, project completion timing and explicit compliance-targeting categories prospectively. The branch cannot simply interpret post-funding change causally.

### Literature / agency overlap

Direct-overlap risk is high:

- EPA OIG Report 15-P-0032 sampled DWSRF projects in the `Assist Non-Compliant Systems to Achieve Compliance` category and examined reported violations after project completion; it reported 347/370 sampled systems with no reported post-completion violation, while warning that missing compliance dates limited conclusions.
- A 2023 Land Economics study examined CWSRF financial assistance and post-funding NPDES compliance, including violation changes after funding.
- DWSRF investment allocation / state discretion has also been studied empirically.

This means an exact PWSID national dataset may enable a more reproducible modern design, but the broad funding→later-compliance proposition itself has substantial precedent.

### Anti-rescue check

This candidate is independent from completed RCRA→NPDES E01: unit=`PWSID`; exposure=DWSRF/WIITS assistance; outcome family=SDWA drinking-water compliance. No RCRA/NPDES endpoint or pair is reused.

### R35 source disposition

**`TECHNICALLY_EXCELLENT__DIRECT_DWSRF_COMPLIANCE_PRECEDENT_HIGH`**

---

## 3. US-PHMSA-LI-001

### Current official source support

PHMSA Source Data provides free operator-submitted incident/accident downloads and a dedicated `Leading Indicators - SRCR and Integrity Assurance Notifications` family. PHMSA states that these notifications are tracked to monitor integrity programs and safety-management systems **before accidents, damages or failures happen**, while also cautioning that SRCR exemptions limit the indicator's usefulness.

PHMSA separately publishes `Pipeline Operators - OpIDs`; `OpID` is described as the unique operator identifier used for PHMSA reporting. Current operator file effective date observed during revalidation: 2026-09-01.

Official anchors:
- https://www.phmsa.dot.gov/data-and-statistics/pipeline/source-data
- https://www.phmsa.dot.gov/data-and-statistics/pipeline/pipeline-operators-opids
- https://primis-uat.phmsa.dot.gov/enforcement-data/

### Support assessment

Source access, exact operator identity and longitudinal support prospects are excellent. A future F01 could likely establish a deterministic OpID/time panel cheaply and without outcome access.

### Literature / operational overlap

Novelty risk is high for two independent reasons:

1. PHMSA itself labels SRCR / Integrity Assurance notifications as leading indicators monitored before failures.
2. Stafford (2014), `Will additional federal enforcement improve the performance of pipelines in the U.S.?`, combined federal inspections/enforcement/penalties with injuries, fatalities, property damage and lost product across the 344 largest U.S. pipeline operators.

The proposed exact SRCR exposure differs from enforcement-history exposure, but operator-safety precursor → later incident/performance is already a mature operational question.

### R35 source disposition

**`TECHNICALLY_EXCELLENT__AGENCY_LEADING_INDICATOR_INTENT__DIRECT_OPERATOR_SAFETY_OVERLAP_HIGH`**

---

## 4. US-NRC-ROP-001

### Current official source support

NRC's current Reactor Oversight Process provides public:

- inspection findings / violations supporting data and data dictionary;
- quarterly operating-reactor Performance Indicator raw values;
- plant/site/docket identity;
- indicators including IE01 Unplanned Scrams, IE03 Unplanned Power Changes and IE04 Unplanned Scrams with Complications.

NRC Data states inspection findings/violations are available by site and docket, while PI raw data contain plant, indicator code, year/month and value.

Official anchors:
- https://www.nrc.gov/reactors/operating/oversight
- https://www.nrc.gov/reactors/operating/oversight/findings-search
- https://www.nrc.gov/documents-reports/nrc-data
- https://www.nrc.gov/facilities-safety/operating-reactors/reactor-oversight-process-rop/rop-framework

### Support assessment

Identity and data quality are excellent. Independent-unit support is structurally limited by the comparatively small U.S. operating-reactor universe, and findings/PI strata may become sparse under prospective separation requirements.

### Overlap assessment

The proposed relation is extremely close to the agency's existing oversight architecture. NRC explicitly states that ROP analyzes two distinct inputs — inspection findings and performance indicators — and integrates them in quarterly plant performance assessment / Action Matrix response. Therefore using inspection findings to predict subsequent ROP PI deterioration has low novelty even if a lagged predictive design is technically possible.

### R35 source disposition

**`CLEAN_DATA__SMALL_UNIT_UNIVERSE__ROP_ARCHITECTURE_OVERLAP_VERY_HIGH`**

---

# Revalidation conclusion / 재검증 결론

No candidate outcome was opened. The frozen pool remains unchanged.

- `US-FAA-AIP-001`: strongest **next-gate information gain** and comparatively lower direct-overlap risk, but exact FAA↔BTS airport identity remains the decisive F01 uncertainty.
- `US-EPA-DWSRF-001`: strongest exact join and highly practical, but direct DWSRF post-project compliance precedent substantially reduces novelty.
- `US-PHMSA-LI-001`: excellent exact OpID infrastructure, but agency leading-indicator intent plus operator-safety literature creates high overlap.
- `US-NRC-ROP-001`: very clean data, but small unit support and explicit ROP integration create the strongest structural overlap.

Next action is to apply the **already frozen** nine-dimension rubric exactly once in `SCORECARD.md`. This document does not itself select a winner.
