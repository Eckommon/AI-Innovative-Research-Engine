---
id: PORTFOLIO-R40-REVALIDATION
type: source-literature-revalidation
created: 2026-09-18
issue: 165
contract_commit: 22ff4cc6045bb895e5e4fe45dccca42bfc25867f
candidate_future_event_membership_used_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R40 bounded revalidation / 제한 재검증

This revalidation follows the pre-Issue candidate/rubric freeze at `22ff4cc6045bb895e5e4fe45dccca42bfc25867f` and Issue #165 binding. No historical exposure→future-event relationship, candidate-level risk, effect, prediction or ranking was computed. No specific candidate future-event membership was queried by historical unit or counted for scoring. Generic source-search results that exposed public example event records were not used as association evidence, cardinality evidence, or tie-break information.

## `US-SEC-ISSUER-001`

### Official source / identity / event structure

- SEC `data.sec.gov` exposes submissions history by filer and XBRL data without authentication or API keys. The submissions endpoint is keyed by zero-padded 10-digit CIK, and bulk submissions/XBRL ZIPs are republished on a recurring basis.
- Form 25-NSE is a direct EDGAR filing family for removal from listing/registration. Public EDGAR filing detail distinguishes the exchange filing entity from the **subject** issuer and shows a subject CIK.
- Exact subject CIK is therefore a strong identity prospect, but F01 must prove that subject-CIK extraction is deterministic in machine-readable Form-25 filings and that a historical issuer cohort can be built without ticker/name reconciliation.
- Event semantics are heterogeneous: Form-25 filings include exchange delistings as well as removals associated with matured, redeemed or retired securities and other listing transitions. A raw “any Form 25” outcome is therefore not automatically a distress/failure event.

### Overlap / novelty boundary

- Financial distress, deregistration, going-dark behavior and delisting are long-established finance/accounting research topics.
- R40 therefore gives no novelty credit for generic financial weakness → delisting. Any descendant would need a narrower data-structure or transition question and a prospective reason/adjudication rule.

**Disposition:** technically strong identity/access; retain with material outcome-heterogeneity and mature-literature penalties.

## `US-FMCSA-CARRIER-001`

### Official source / identity / event structure

- FMCSA’s Open Data Program states that the Company Census File contains active, pending and inactive entities and assigns each entity a unique `USDOT Number`.
- FMCSA also documents the USDOT Number as the key linking carrier census and safety records. Official Licensing & Insurance pages expose Out-of-Service orders with USDOT number, reason, date and status.
- The direct OOS event is high-quality, but the New Entrant program itself explicitly links failed/refused safety audits and inadequate safety management controls to registration revocation and OOS orders.
- Therefore descendant exposure must stay strictly outside prior audit/violation/OOS/safety-trigger fields. Historical non-outcome census/fleet/driver snapshots must also be proven reproducible; current FMCSA products are frequently refreshed and parts of the public ecosystem are under IT modernization.

### Overlap / novelty boundary

- FMCSA already monitors every new entrant during an 18-month program, uses roadside/audit/crash information for interventions, and has agency-sponsored research on new-entrant safety culture, audit failures and business survival.
- This is substantial framework overlap. The candidate remains useful only if F01 can establish an independent historical operating-structure layer that is not a proxy for the statutory/program trigger.

**Disposition:** strong direct event and exact identity; retain but penalize framework overlap, anti-tautology difficulty and historical-snapshot risk.

## `US-FCC-ULS-001`

### Official source / identity / event structure

- FCC’s ULS public-access-file guide states that anyone can download zipped license/application data.
- It defines complete database files plus daily transaction files containing licenses/applications that were new or modified on the prior day.
- FCC assigns each license/application a unique **9-digit system identifier**. The documentation explicitly says this identifier distinguishes an active call sign from a prior license that expired, was cancelled or terminated when call signs are reassigned.
- The unique system identifier can substitute for call sign/ULS file number in joins. This directly addresses identity drift that would otherwise make call-sign-only continuity unsafe.
- F01 still must prove which radio-service families expose comparable status/action/date fields, whether complete/daily files preserve enough historical transition lineage, and whether cancellation vs termination vs ordinary expiration can be prospectively adjudicated without service-specific leakage.

### Overlap / novelty boundary

- ULS is a mature licensing system, so the fact of public license status is not novel.
- In the bounded search, however, no agency-standard predictive “license structure → later cancellation/termination” framework comparable to FMCSA New Entrant or the mature SEC/NCES failure literatures was identified. This is **not** a novelty claim; it supports only moderate low-overlap credit pending a later dedicated novelty stage.
- Exposure and outcome remain within one FCC licensing ecosystem, so cross-system information-gain credit is deliberately limited.

**Disposition:** strongest next-gate information gain: exact identity, direct status transitions, public machine-readable complete/daily files, and a cheap F01 capable of failing quickly before any future-event cohort is opened.

## `US-NCES-SCHOOL-001`

### Official source / identity / event structure

- NCES CCD is the Department of Education’s comprehensive annual national database of public elementary/secondary schools and districts.
- Annual directory files expose NCES identification numbers and operational status. NCES documentation explicitly distinguishes operational, closed, new, temporarily closed, agency-change and reopened states.
- The NCES School ID is a stable 12-digit source-native key prospect. Historical enrollment, teacher FTE and school attributes are available in school-universe files.
- F01 must prove exact ID continuity across annual files and prospectively handle temporary closures, reopened schools, school-agency reassignment and non-reporting without interpreting absence as closure.

### Overlap / novelty boundary

- Public-school closure is a mature education-policy research topic. Recent work uses CCD’s status indicator directly, and enrollment decline is already documented as associated with permanent closure.
- R36 also already considered higher-education institutional closure, although under a different UNITID/IPEDS family. R40 therefore treats conceptual closure overlap conservatively.

**Disposition:** excellent identity and direct annual outcome semantics, but same-system information gain and novelty are weak.

## Internal-history check / 내부 이력 확인

- No earlier canonical branch executed exact candidate IDs `US-SEC-ISSUER-001`, `US-FMCSA-CARRIER-001`, `US-FCC-ULS-001` or `US-NCES-SCHOOL-001`.
- `US-FCC-ULS-001` is not a rescue of R38 `US-FCC-BDC-001`: BDC was broadband-location/provider withdrawal, whereas R40 uses ULS license-native 9-digit identity and license action/status.
- `US-NCES-SCHOOL-001` is not R36 `US-EDU-FIN-001`: the latter was higher-education IPEDS/College Scorecard with UNITID; R40 is K-12 CCD with 12-digit School ID. Conceptual institution-closure overlap is nevertheless penalized.
- No IRS-EO, DOL-5500, FEMA-BPS, BLS-CBP or FDIC branch is re-entered.

## Revalidation conclusion / 재검증 결론

All four candidates remain scoreable under the frozen R40 rubric.

- `US-FCC-ULS-001` has the cleanest combination of exact source-native identity, directly encoded later license state and low-cost next-gate falsifiability.
- `US-FMCSA-CARRIER-001` has excellent identity and outcome quality but stronger agency-framework/anti-tautology and historical-snapshot risks.
- `US-SEC-ISSUER-001` has excellent machine-readable infrastructure and exact CIK, but undifferentiated Form-25 outcome semantics are heterogeneous and the research area is mature.
- `US-NCES-SCHOOL-001` is technically clean but has low cross-system information gain and substantial closure/enrollment literature overlap.

No candidate-specific future-event membership was used to calculate a score, no exposure-outcome relationship was computed, and no candidate was ranked outside the single frozen scorecard that follows. Cost: **0 USD**.
