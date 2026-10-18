---
id: PORTFOLIO-R59
created: 2026-10-18
type: fresh-independent-parallel-outcome-blind-stage0
status: FROZEN_PRE_ISSUE
last_terminal_f01: US-NOAA-QCEW-F01
last_terminal_disposition: HOLD_US_NOAA_QCEW_F01_FROZEN_STRUCTURAL_GATES_NOT_ALL_READY
primary_still_active: US-CMS-NPI-E01
candidate_outcome_rows_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R59 — Source-native entity-ID research selection / 원천 식별자 기반 독립 신후보 선별

## Purpose / 목적

The user's 2-Track authority permits a **second, explicitly separate** research selection while canonical `US-CMS-NPI-E01 / Issue #203` waits for the first eligible future CMS NPPES V2 weekly. Track B's completed NOAA×BLS F01 in Issue #233 was a valid scientific **17/18 HOLD** at original Gate 12 (9,929/11,116, 89.321698% vs frozen 99%), NOT an operational ZIP failure. This contract **cannot** salvage that route by changing county eligibility or denominator.

**Mission ROI change / 연구 최적화:** After many exact-geo/identity failures, R59 prospectively prioritizes *original agency-assigned persistent entity keys* and **verified** public longitudinal releases rather than inferred joins, hand-built geospatial bridges, or exposure proxies built from the same target. This is a new candidate universe, fixed before scoring and before the new Stage-0 Issue; no outcome observations have been opened.

## Three frozen and independent candidates / 독립 사전 고정 3종

### A — `US-ED-IPEDS-SCORECARD-001`: Higher-education institutional resources × later student outcomes / 대학 운영구조 × 후속 교육성과

- First-party [NCES IPEDS annual survey downloads](https://nces.ed.gov/ipeds/use-the-data), published complete CSVs and final/provisional version schedules, versus [US Department of Education College Scorecard](https://collegescorecard.ed.gov/data/) institution-level annual ZIPs and [institutional technical documentation](https://collegescorecard.ed.gov/files/InstitutionDataDocumentation.pdf).
- Source-native hypothetical unit: **IPEDS `UNITID`** at institution × reference academic year, not free-form name. NCES [official grouping guidance](https://nces.ed.gov/ipeds/use-the-data/institutional-groupings-in-ipeds) warns **UNITID and OPEID/OPEID6 are not one-to-one**; household earnings or debt sometimes aggregate at the main-campus OPEID6 level. This potential **non-identifiability** is a hard veto, not a posthoc name repair.
- Exposure prospect: older independently reported IPEDS institutional structure/resource mix **excluding any IPEDS value mirrored in Scorecard**, prior to genuinely later student outcomes. Later Scorecard institution-level repayment/earnings release must have a *distinct, verifiable time and unit*, not current “latest” reused as a future outcome.
- Failure risks: branch replication, multi-UNITID OPEID6 aggregation, publication lag/revisions, privacy suppression, different source years, scorecard composites drawing IPEDS variables, very large all-history archive. Not yet row-access proven.

### B — `US-SEC-CIK-XBRL-001`: Filing structure × prospective amendment/filing cadence / 기업 공시구조 × 후속 정정공시

- Official [SEC EDGAR public REST APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces): `https://data.sec.gov/submissions/CIK##########.json` and `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`; 10-digit padded source-native **CIK** common key, date/accession metadata. Separate official bulk submissions/companyfacts ZIPs are updated nightly, and SEC data.sec.gov APIs are **no-auth** but subject to [SEC fair-access rules](https://www.sec.gov/about/webmaster-frequently-asked-questions).
- Unit prospect: exact SEC filer CIK + locked historical submission year; prospective event **new 10-K/A amendment filing**, NOT proof of accounting fraud/restatement/financial distress. Freeze a pre-future-file observation opportunity, event date semantics, and taxonomic XBRL concept before any future amendments are inspected.
- Structural exposure candidate: past non-outcome XBRL disclosure completeness across explicitly qualified taxonomies only; avoid using already future filing type or amendment status as exposure.
- Failure risks: SEC XBRL and submissions ultimately derive from the same EDGAR filings; independently measured cross-source information gain may be low, SEC HTTP anti-bot, 10-K/A amendment is not a correction of financial results, and CIK company merges/filing-type lineage. Do not bulk scrape large corpora or fetch numeric future results at Stage 0.

### C — `US-USPTO-PATENT-FEE-001`: Official patent grant identity × maintenance fee lifecycle / 특허 등록 구조 × 후속 유지료 사건

- First-party [USPTO Patent Maintenance Fee Events bulk catalog](https://data.uspto.gov/bulkdata/datasets/ptmnfee2) and [US Government catalog record](https://catalog.data.gov/dataset/patent-maintenance-fee-events-1981-present); records are published as **weekly cumulative** files. Grant identity must come from an **independently documented official USPTO patents grants/downloads family**, with source-native **patent number**, not an assignee/company-name link.
- Unit prospect: patent number + issue date/type + maintenance-fee eligibility window, requiring correct distinction among utility, design and plant patents, changes to fee rules and reinstatement.
- Prospective endpoint: later recorded maintenance fee nonpayment/expiration or payment event as officially defined. **Do NOT** treat fee lapse as commercialization failure, low technical quality, patent abandonment in all cases, or innovation non-value. Patent age creates deterministic payment windows; prevent target leakage.
- Failure risks: first-party archived grant bulk body/access is unverified, fee file is cumulative and possibly corrected, nonpayment may be missing from fee-event extract rather than represented by a standalone event, and patent-type denominator may be ambiguous. No scraping of a fee-paying private portal.

## Frozen /45 selection criteria / 결과 미개봉 고정 평가

Each candidate scored 0–5 on precisely nine same-weight dimensions **after separate official source documentation/transport revalidation and before outcome opening**:

1. Public exact first-party row-bearing data availability on the canonical **zero-cost** runner (landing HTML/HEAD alone never a PASS).
2. Original persistent agency-assigned identifier validity, one-to-one qualified unit and longitudinal survival **without names/addresses**.
3. Prospective future event/endpoint independently dateable and reproducible, no retrospective outcome selection.
4. Exposure is non-tautological and measured before the endpoint, without mirrored fields or source leakage.
5. Event observation opportunity/denominator, disclosure support, and population common support.
6. Genuine cross-dataset information gain rather than mere two file views of the same original input.
7. Industrial/institutional innovation discovery and decision utility with calibrated noncausal claims.
8. Stable first-party historical archive, refresh lineage, no paid service, deterministic replay.
9. Scientific novelty vs canonical terminal routes, especially **no old NOAA/BLS, SEC-adviser F01, FDA device or patent mineral route rescue**.

Tie-breaks: proven canonical source access; exact one-to-one unit; future release lineage; independent exposure; mission ROI. Strong score cannot override a fatal exact-source or ID veto; select **at most one conditional F01** or `HOLD_NO_ELIGIBLE_CANDIDATE`. Never promote the second-highest based on later results.

## Hard prohibitions / 금지

- Do not reopen NOAA 17/18 scientific HOLD by narrowing BLS denominator or dropping noncounty aggregates **after observing 89.32%**; do not use R58 runners-up.
- Do not treat Scorecard's OPEID6-level outcomes as unique UNITID-level, EDGAR amendment as fraud, or patent fee expiration as failed innovation.
- No institutional outcome rows, amendments, patent-expiration membership, associations, p-values, confidence intervals, causal effects, prediction/ranking or winner selection before blind scorecard.
- No data provider fees, GitHub paid services, hidden key/authorization circumvention, bulk SEC scraping, owner/personnel records, or alternate private mirrors.
- Do not mutate the frozen CMS E01 first weekly source, paired cohort, source release, original scientific `DEC-318`, active Issue #203 or its checkpoint.

## Ordered continuation / 정확한 다음 단계

1. Commit this candidate universe on `main` **before** its distinct secondary Stage-0 Issue.
2. Preserve NOAA F01 terminal immutable evidence and close Issue #233. Create R59 Issue and authorize exactly one **new** secondary Issue in a narrow sidecar decision with State Integrity; canonical E01 #203 remains OPEN.
3. Independently verify genuine official source links, full source licensing, exact identity definitions, effective release dates, and *only non-outcome schema/prefix* in canonical 0 USD runner. Register fail-closed transport/codepoint/ID risks before scores.
4. Freeze one outcome-blind /45 scorecard, choose one F01 candidate or scientific Stage-0 HOLD, and do not alter the pool after seeing results.
5. Only upon eligible selection: freeze separate 18-gate F01 source/identity/temporal contract on main before its Issue; no future-outcome rows until separate N01/E01 preregistration.

**No candidate has a recorded row-body access PASS yet. No scientific PASS claimed. Cost: 0 USD.**
