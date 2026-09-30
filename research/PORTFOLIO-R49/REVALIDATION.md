---
id: PORTFOLIO-R49-REVALIDATION
type: bounded-source-overlap-support-revalidation
created: 2026-09-30
issue: 186
contract: 02c6730b43ff9e73a7933587b9a4d862b2637c9f
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R49 — bounded source / lineage / common-support revalidation

## Outcome firewall / 결과 방화벽

No candidate-specific future event membership, effect, prediction, ranking or causal result was opened. Revalidation used official source/documentation pages, canonical project history and bounded framework/literature context only.

## 1. US-SEC-IA-001

SEC currently provides historical Form ADV Part 1 data and historical Form ADV-W data in structured downloadable files. SEC's Investment Adviser Information Reports provide adviser snapshots from July 2006 onward, and SEC states that historical ADV filing data extend from January 2001 through the most recent quarter.

Official Form ADV and Form ADV-W both expose firm-level CRD identifiers when assigned. Form ADV-W explicitly distinguishes:
- **full withdrawal** — withdrawal from all jurisdictions in which the adviser is registered or pending;
- **partial withdrawal** — withdrawal from some but not all jurisdictions.

Official SEC guidance also confirms that withdrawal from SEC registration can represent a regulatory transition, including SEC→state or SEC-registered→exempt-reporting-adviser transitions. Therefore a future descendant may classify **full registration withdrawal**, but may not relabel it business failure or firm cessation without separate evidence.

Strengths:
- long structured filing lineage;
- source-native firm identity prospect through CRD;
- direct full/partial event semantics;
- broad active-adviser universe;
- rich non-outcome baseline business/client/organization structure;
- future filing events can be sealed prospectively.

Prospective common-support risk:
- comparatively low because business-structure variables occur across the broad registered-adviser population and event ascertainment is not conditional on inspection selection.
- N01 must nevertheless choose one exposure with large support and verify overlap before opening future ADV-W membership.

Critical F01 questions:
- exact CRD coverage and ADV↔ADV-W join rate;
- full/partial withdrawal field semantics in historical files;
- current active SEC-registration population;
- filing-date/event-date support;
- transition/re-registration edge cases;
- post-cutoff future-file seal.

## 2. US-CMS-NPI-001

CMS currently publishes:
- a monthly full replacement NPPES file;
- a monthly NPI deactivation file;
- weekly incremental files.

NPPES exposes exact 10-digit NPI, deactivation reason/date and reactivation date. Official code values distinguish death, disbandment, fraud and other reasons. CMS also states that deactivated NPIs may later be reactivated and that NPI issuance does not establish licensure or credentialing.

Strengths:
- exact NPI;
- very large independent-unit universe;
- direct deactivation/reactivation dates and reason codes;
- rich taxonomy/entity/practice-location structure;
- zero-cost bulk files.

Critical limitations:
- deactivation is heterogeneous and reactivation is allowed;
- current monthly full file replaces the prior file, so replace-in-place downloads do not alone prove archive lineage;
- NPI deactivation is not equivalent to provider closure or loss of license;
- extremely broad provider heterogeneity may require careful N01 restriction to obtain interpretable common support.

## 3. US-EPA-RCRA-001

EPA ECHO documents RCRAInfo as a national hazardous-waste-handler system with six downloadable CSV families. `ID_NUMBER + ACTIVITY_LOCATION` key fields are present across files and are explicitly documented as join keys. Enforcement files expose source-native enforcement identifiers, type and action date; violation/evaluation files expose corresponding dates; VIO/SNC history is monthly.

Strengths:
- excellent deterministic identity/join semantics;
- dated historical enforcement/evaluation/violation records;
- large structured facility universe;
- rich stable facility roles and NAICS structure;
- zero-cost bulk access.

Critical limitations:
- formal enforcement is conditional on inspection/evaluation and regulatory attention;
- enforcement/evaluation/violation history is prohibited as predictive exposure;
- a structure-only exposure may create substantial confounding and inspection-selection differences;
- N01 must explicitly demonstrate common support in inspection opportunity or remain non-causal/descriptive.

The candidate remains structurally strong, but its next-gate support/selection uncertainty is higher than SEC.

## 4. US-FDA-DEV-001

FDA provides weekly registration/listing downloadable files and openFDA registration-listing data. openFDA device-recall records cover records since 2002 and are updated regularly. openFDA harmonizes several device identifiers where available, including FEI/registration-related fields.

Strengths:
- direct, high-value safety event;
- long recall-event history;
- large establishment/listing universe;
- registration/listing and recall datasets are both public and machine-readable.

Critical limitations:
- recall is fundamentally product/device-level while the proposed baseline unit is establishment-level;
- FEI/registration harmonization is not assumed complete;
- one recall may involve multiple products/establishments and one establishment may own many listings;
- common-support and attribution may collapse once exact establishment linkage is required;
- recall research is mature.

F01 must prove exact establishment attribution before any prospective design.

## Canonical history / 내부 이력

Repository search found no earlier canonical branches using the exact IDs:
- `US-SEC-IA-001`
- `US-CMS-NPI-001`
- `US-EPA-RCRA-001`
- `US-FDA-DEV-001`

R48 had previously screened SEC and RCRA conceptually but did not open either F01. R49 is a new separately frozen portfolio round after the EIA N01 common-support failure.

## Revalidation conclusion / 재검증 결론

All four candidates remain eligible for the single R49 scorecard.

The strongest pair is SEC and RCRA:
- RCRA has the stronger environmental/enforcement bottleneck mission fit and equally strong exact join semantics;
- SEC has cleaner prospective event ascertainment and a more credible path to broad common support because withdrawal is filing-based rather than inspection-conditioned.

CMS has exceptional scale/identity but lower event specificity. FDA has a direct safety event but weaker establishment-level attribution.

No candidate future-event membership was opened. Cost remains **0 USD**.
