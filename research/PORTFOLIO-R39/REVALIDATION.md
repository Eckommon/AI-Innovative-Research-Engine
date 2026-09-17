---
id: PORTFOLIO-R39-REVALIDATION
type: source-literature-revalidation
created: 2026-09-18
issue: 162
contract_commit: 9d6a16975bc02638aae938f20b6591ffe02d1fa9
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R39 bounded revalidation / 제한 재검증

This revalidation was performed only after the candidate pool, rubric, tie-break, exclusions and exposure/outcome boundaries were frozen at `9d6a16975bc02638aae938f20b6591ffe02d1fa9` and bound to Issue #162. No candidate future outcome row or membership was opened or counted.

## `US-IRS-EO-001`

### Official source/schema/current-access

- IRS currently exposes a comprehensive public-disclosure download family covering Form 990-series returns, the Automatic Revocation List, Form 990-N and related tax-exempt-organization products.
- Form 990-series filings are downloadable as official XML bundles with year/month indexes; current 2026 XML bundles are listed publicly.
- The Automatic Revocation List is separately downloadable as a pipe-delimited text product and is updated monthly. IRS documentation states that the list contains organization name, EIN, exemption type, revocation effective date, posting date and reinstatement information.
- IRS states that automatic revocation occurs after three consecutive missed required annual filings. Therefore prior nonfiling streaks remain prohibited as exposure under the frozen anti-tautology boundary.
- EO Business Master File extracts are downloadable CSV and sorted by EIN. The 2026-09-08 posting reports 1,964,958 records, establishing very large organization-level structural support before any future revocation membership is opened.
- Exact EIN is therefore a strong source-native identity prospect across the authorized IRS families. F01 still must prove which historical Form-990 XML/index releases expose EIN consistently enough for longitudinal filed-organization construction and must prospectively handle reinstatement/pre-existing-revocation semantics.

### Overlap/novelty boundary

- Nonprofit financial vulnerability and organizational failure from Form 990 data are established research topics. A 2020 dissertation, for example, studies Form-990 financial/governance measures preceding nonprofit closure and reports revenue concentration among the useful signals.
- R39 therefore does not treat generic “Form-990 financial weakness predicts nonprofit failure” as novel.
- The remaining candidate information gain is narrower: a fully public, source-native EIN design that separates *actually filed* historical operational/financial structure from a later direct IRS legal-status event while explicitly excluding prior nonfiling as exposure.

**Revalidation disposition:** technically strong; retain with conservative overlap penalty.

## `US-BLS-CBP-001`

### Official source/schema/current-access

- BLS QCEW provides anonymous public CSV data slices and historical downloadable files. Current documentation exposes `area_fips`, `industry_code`, ownership, disclosure code, establishment counts, employment and wages.
- QCEW covers more than 95% of U.S. jobs and currently publishes through 2025 annual/quarterly products with 2026 partial data.
- Census County Business Patterns provides annual county × industry establishment/employment/payroll statistics in downloadable CSV products. Current public CBP reference year is 2023; Census has stated that 2024 timing is not yet planned while it evaluates methodological changes.
- BLS itself documents conceptual differences between QCEW and CBP coverage/methodology. Therefore apparent FIPS+NAICS equality is not by itself sufficient: F01 must freeze a compatible private-sector universe, NAICS version/level, disclosure/suppression rule and common calendar support before any later contraction outcome is opened.
- Because CBP lags QCEW, this candidate has a feasible historical prospective split but weak near-real-time outcome freshness.

### Overlap/novelty boundary

- QCEW and CBP are mature inputs to regional-economics and establishment-growth research and are often combined or compared by county and industry.
- Suppression and universe differences are known methodological issues rather than new discoveries.
- Candidate value therefore comes from a tightly preregistered structural-to-subsequent-contraction design, not from the fact that the two datasets can be merged.

**Revalidation disposition:** retain, but penalize outcome freshness, aggregate-unit semantics and literature overlap.

## `US-FEMA-BPS-001`

### Official source/schema/current-access

- OpenFEMA Disaster Declarations Summaries provides API/CSV/JSON access to federally declared disasters back to 1953, including declaration and incident dates, assistance-program flags and declared geographic areas.
- FEMA documents `placeCode` as `99` plus the three-digit county FIPS for recognized counties; current FEMA GIS products separately expose `state_fips`, `cnty_fips` and five-digit `fips` fields.
- Census Building Permits Survey publishes county-level comma-delimited files. Current county-file documentation exposes survey date, FIPS state code and FIPS county code, while the BPS definitions page states that state/county FIPS uniquely identify the relevant geographic entities.
- BPS publishes monthly, year-to-date and annual county statistics, with final 2025 annual data released in May 2026.
- F01 must still prove a prospectively fixed county-universe rule because FEMA includes non-county declared areas and BPS permit coverage/imputation varies across geography/time.

### Overlap/novelty boundary

- Disaster recovery, housing construction and permitting response are mature research areas. Building permits are an indirect recovery measure rather than a direct welfare or reconstruction-completion event.
- Consequently this candidate receives strong feasibility credit but conservative direct-outcome and novelty credit.

**Revalidation disposition:** retain as a technically clean geographic comparator, not as a presumed novel disaster-recovery design.

## `US-DOL-5500-001`

### Official source/schema/current-access

- DOL EBSA publishes structured Form 5500/5500-SF datasets for approximately 800,000 retirement and welfare benefit plans. 2009+ datasets are typically refreshed monthly and are provided as zipped CSV files with annual data dictionaries.
- DOL explicitly states that the nine-digit sponsor EIN plus three-digit Plan Number (PN) forms a unique 12-digit plan/DFE identifier and instructs filers to keep that combination consistent across future filings and not reuse a PN for another plan even after termination.
- Within a filing, `ACK_ID` is the unique filing identifier used to connect schedules/tables; it is not the longitudinal plan identity.
- DOL instructions directly define final-return/termination reporting semantics, including the requirement that plans with remaining assets or participants continue filing and should not simply mark a final return.
- F01 must therefore distinguish persistent plan identity (`EIN+PN`) from filing identity (`ACK_ID`), use the documented `Latest` dataset logic for amended/duplicate filings and freeze merger/transfer/termination adjudication before future membership is opened.

### Overlap/novelty boundary

- Form 5500 is a mature regulatory/reporting system with extensive EBSA/IRS research use. DOL research files themselves define terminating/nonterminating plans from final-return and related termination fields, and IRS has conducted compliance projects on Form-5500-identified terminated plans.
- The candidate is structurally excellent but has lower cross-system information gain and substantial agency-framework overlap.

**Revalidation disposition:** retain as the strongest technical comparator, with a material overlap/cross-system penalty.

## Internal-history check

- No canonical repo branch before R39 executed the exact candidate IDs `US-IRS-EO-001`, `US-BLS-CBP-001`, `US-FEMA-BPS-001`, or `US-DOL-5500-001`.
- R39 does not re-enter R34–R38 terminal branches or near-misses. In particular it does not rescue FDIC branch matching, FAA-AIP, EIA generator schedules, FSIS transport-blocked sampling, FRA crossing prediction, FCC BDC withdrawal, CMS provider candidates, USAspending continuity, EPA SDWIS/XMEDIA, PHMSA, NRC, BTS-Port, USCG-Vessel or MSHA.
- The IRS candidate is not treated as a generic organization-closure clone: its direct endpoint is the separate IRS automatic-revocation legal-status list, and the frozen anti-tautology rule prohibits using the statutory nonfiling trigger as exposure.

## Revalidation conclusion

All four candidates remain scoreable under the frozen R39 contract. `US-IRS-EO-001` and `US-DOL-5500-001` have the strongest source-native identity. `US-IRS-EO-001` preserves greater cross-dataset information gain and a cleaner externally published legal-status event; `US-DOL-5500-001` has stronger framework overlap. `US-FEMA-BPS-001` has a clean geographic key but a proxy recovery outcome; `US-BLS-CBP-001` has mature data but aggregate-cell identity, suppression/universe differences and CBP release lag.

No future automatic-revocation membership, establishment-contraction value, post-disaster permit outcome or plan-termination membership was opened or counted. No relationship, prediction, ranking, causal effect or novelty claim was computed. Cost: 0 USD.
