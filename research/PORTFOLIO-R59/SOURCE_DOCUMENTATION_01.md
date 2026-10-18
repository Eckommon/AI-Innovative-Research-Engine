---
id: PORTFOLIO-R59-SOURCE-DOC-01
created: 2026-10-18
issue: 237
frozen_contract: 22f68ed247c7e6468c60b477fadd17e30d199076
scope: first-party-official-documentation-only
candidate_future_outcomes_opened: false
cost_usd: 0
---

# R59 — Official agency source documentation and transport boundary / R59 공식 출처·접근 제약

**Source class:** agency *documentation and government catalog metadata*, **NOT** actual rows, institutional outcomes, future 10-K/A filings or patent maintenance events. The connected GitHub 0-cost runner will separately measure only ZIP 4-byte signatures or HEAD metadata, never future membership.

| Candidate | Official source description and frozen transport anchor | Known pre-execution blocker |
|---|---|---|
| US-ED-IPEDS-SCORECARD-001 | [NCES IPEDS annual datasets](https://nces.ed.gov/ipeds/use-the-data/download-access-database), exact listed 2023–24 Final `https://nces.ed.gov/ipeds/tablefiles/zipfiles/IPEDS_2023-24_Final.zip`; [ED College Scorecard Data.gov catalog](https://catalog.data.gov/dataset/college-scorecard) lists 2025 official distribution `https://ed-public-download.scorecard.network/downloads/Most-Recent-Cohorts-Institution_05192025.zip` | NCES ZIP ~92MB is not assumed row-ready. Scorecard publisher is federal but the catalog-designated ZIP host is **nongov**, not by itself agency-host-native. Scorecard dataset catalog timestamps may lag the current live portal. UNITID vs OPEID6 branch mapping, IPEDS reused predictor fields and institution-vintage identity require separate resolution. |
| US-SEC-CIK-XBRL-001 | [SEC original EDGAR API specification](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) explicitly documents CIK and official ZIPs `https://www.sec.gov/Archives/edgar/daily-index/bulkdata/submissions.zip`, `https://www.sec.gov/Archives/edgar/daily-index/xbrl/companyfacts.zip` | SEC fair access/robot policy, bulk ZIP size, no-auth API access does not mean automatic unrestricted bulk scraping; first HEAD may be denied. CIK is source-native but 10-K/A is only a filing amendment and XBRL derives from same original filing. DO NOT request or parse any actual company filing. |
| US-USPTO-PATENT-FEE-001 | [Federal data catalog](https://catalog.data.gov/dataset/patent-maintenance-fee-events-1981-present) documents official `https://data.uspto.gov/bulkdata/datasets/ptmnfee2` and weekly cumulative events; [USPTO Open Data Portal API docs](https://data.uspto.gov/apis/bulk-data/search) identify `https://api.uspto.gov/api/v1/datasets/products/search` | **Critical:** USPTO states that **ODP access requires account sign-in as of June 18, 2026**, and the cited API **requires a key**. Treat this as a potentially decisive availability blocker, not permission to bypass registration. No credentials, account sign-in, unverified mirror or private bulk API in 0 USD run. |

**No cohort, sample sizes, product effects, entity scoring or future outcomes are opened**. A `200` status or ZIP prefix merely certifies one HTTP response; HEAD 403 or ODP 401 does NOT prove files absent. Classification is **pre-score**, and no candidate may be selected before a distinct, independent access/identity/vintage review with preserved original evidence.

**Historical terminal equivalence:** prior SEC IA was different adviser CRD/ADV-W with missing ZIP months; an SEC issuer CIK/EDGAR filing hypothesis is not the same exact route but must still prove novelty. Historic NOAA 17/18 HOLD may never be rescued through narrower BLS eligibility. R59 candidates scored under the pre-committed nine /45 rules only after metadata and rule-equivalence review.

**Decision:** `CONTINUE_R59_FROZEN_ACCESS_AND_IDENTITY_PREFLIGHT`, not `SELECT` or `F01_PASS`. No additional monetary cost.
