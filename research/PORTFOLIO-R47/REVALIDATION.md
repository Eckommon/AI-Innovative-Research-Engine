---
id: PORTFOLIO-R47-REVALIDATION
type: bounded-source-overlap-revalidation
created: 2026-09-30
issue: 181
contract: c3bfe8cd3f85516e7adf4e700103992ab9a29193
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R47 — bounded source / overlap revalidation

## Outcome firewall / outcome 방화벽

No candidate-specific future event membership, effect, prediction, ranking or causal result was opened. Revalidation used official source/documentation pages, canonical project history and bounded literature/framework context only.

## 1. US-EPA-SDWIS-001

EPA ECHO currently publishes a nationwide Safe Drinking Water Act dataset from SDWIS, refreshed quarterly. The official data dictionary states that each public-water-system quarter is keyed by `SUBMISSIONYEARQUARTER + PWSID`, with the same fields used to relate facilities, violations, enforcement, site visits and other tables. `PWSID` is documented as a two-letter state/region code plus seven digits.

The public-water-system table exposes non-outcome structural fields including activity status, source type, ownership, system type, population served and deactivation date; the violation/enforcement table exposes violation ID, noncompliance dates, violation status and enforcement-linked fields.

Strengths:
- exact nine-character source-native PWSID;
- quarterly temporal lineage;
- nationwide machine-readable ZIP/CSV;
- direct source-native violation/enforcement event tables;
- large independent-unit universe and public-health importance.

Critical boundaries:
- reporting lag must be built into any future window;
- mergers/deactivation must be treated separately from adverse water-quality outcomes;
- prior/current violation, unresolved noncompliance, enforcement-priority or direct outcome-proximal fields are prohibited as descendant exposures;
- health-based / severity event definition must be frozen before future membership is opened.

Overlap:
- drinking-water violations and health/compliance analysis are established research areas, so novelty credit is conservative. R47 does not claim a novel domain; it values the exact quarterly prospective design opportunity.

## 2. US-ED-POSTSEC-001

Federal Student Aid currently provides a Weekly Closed School Search File and a cumulative closed-school list. Its search instructions explicitly use OPEID. Department guidance describes closure as a verified institutional/location event with a Department-determined closure date.

College Scorecard provides downloadable institutional data and Department technical documentation describes UNITID and OPEID as distinct institutional identifiers with a historical crosswalk; they are not assumed one-to-one.

Strengths:
- direct verified closure event and date;
- official OPEID event key;
- rich public institutional structure.

Critical boundaries:
- location-level 8-digit OPEID versus UNITID/main-campus aggregation must be resolved exactly;
- mergers, branches, teach-outs and affiliation changes complicate unit identity;
- closure prediction is already a mature contemporary research topic, including recent Federal Reserve/NBER work using institutional, financial, enrollment and staffing characteristics.

Therefore novelty/overlap is heavily discounted despite strong practical value.

## 3. AU-ASIC-COMP-001

ASIC/Data.gov.au publishes a free weekly company-register snapshot. The current dataset includes Company Name, ACN, Type, Class, Sub Class, Status, Date of Registration and Date of Deregistration. The help documentation states that current registered companies plus deregistered companies for the past year are included.

Strengths:
- exact ACN identity;
- weekly machine-readable CSV/ZIP;
- direct registration/deregistration dates;
- clear current public snapshot.

Critical boundaries:
- deregistered-company retention is bounded to roughly the past year;
- deregistration can be voluntary, ASIC-initiated, solvent/insolvent winding-up related or otherwise heterogeneous;
- recent CA-CORP/company-registry work creates strong immediate portfolio overlap;
- corporate closure/deregistration is a mature event family.

## 4. EU-EMAS-ORG-001

The European Commission describes the EMAS register as the comprehensive current list of EMAS-registered organisations and sites and states that register results can be downloaded to Excel. Current official statistics report thousands of organisations and sites.

Strengths:
- official current positive register;
- searchable/downloadable organisation/site records;
- NACE/sector and environmental-statement context.

Critical boundaries:
- current official evidence reviewed here does not establish a reproducible historical deregistration/end-state table;
- disappearance from the current positive register cannot be treated as deregistration without prospective source semantics;
- EMAS withdrawal/non-renewal determinants have already been studied, reducing novelty credit.

## Canonical-history exclusions / 내부이력 제외

- USDA Organic transport route remains terminal; no third transport workaround.
- R46 held PHMSA, TGA and ECHA candidates are not re-entered.
- ASIC receives strong overlap penalty from CA-CORP and other company-registry branches.
- No prior canonical artifact was found for the exact R47 candidate IDs before the R47 contract.
- SDWIS is treated as a new public-water-system unit/event family, not as a rescue of earlier EPA cross-media branches.

## Revalidation conclusion / 재검증 결론

All four frozen candidates remain eligible for one-time scoring.

**SDWIS has the strongest next-gate structure**: exact source-native identity, quarterly national history, direct public-system and violation/enforcement tables, zero-cost bulk access and a sharply enforceable anti-tautology boundary. Postsecondary closure has high practical value but substantially higher mature-literature and crosswalk complexity. ASIC is operationally strong but heavily overlaps recent company-registry work. EMAS has the weakest demonstrated historical event lineage.

Incremental monetary cost: **0 USD**.
