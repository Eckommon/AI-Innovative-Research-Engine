---
id: PORTFOLIO-R37-SOURCE-LITERATURE-REVALIDATION
type: outcome-blind-source-literature-evidence
created: 2026-09-17
issue: 157
contract_commit: 7ad2e9bf392d3e8fdf41982d7e1a800eca377f5a
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R37 source/literature revalidation / 소스·문헌 재검증

This document records the bounded, outcome-blind revalidation required by the frozen R37 contract. No candidate future outcome row, membership, effect direction, or relationship statistic was opened or computed.

## Internal-history check / 내부 이력 점검

Repository code/content searches for `FSIS Salmonella recall establishment`, `USAspending UEI vendor`, `SDWIS PWSID drinking water`, and `CMS nursing home CCN staffing deficiency` returned no prior dedicated branch implementing these candidate relationships. This establishes **no detected repo-branch duplicate**, not external novelty.

## 1. `US-FSIS-SAMPLE-001`

### Official-source support

- FSIS publicly exposes establishment-specific laboratory sampling datasets and states that the current datasets are updated quarterly with archives updated annually. Raw poultry is explicitly establishment-specific.
  - `https://www.fsis.usda.gov/science-data/data-sets-visualizations/laboratory-sampling-data`
  - `https://catalog.data.gov/dataset/fsis-laboratory-sampling-data-raw-poultry-sampling`
- An April 3, 2026 FSIS constituent update confirms quarterly updates to raw poultry, egg, raw beef, RTE and other establishment-specific laboratory datasets and annual refresh of earlier years.
  - `https://content.govdelivery.com/accounts/USFSIS/bulletins/4116aca`
- FSIS publishes a Meat, Poultry and Egg Product Inspection Directory keyed by establishment number and establishment demographic files.
  - `https://www.fsis.usda.gov/inspection/establishments/meat-poultry-and-egg-product-inspection-directory`
- FSIS recall guidance states that USDA establishment numbers are assigned to producing establishments and are included in recall releases when available. Recall pages visibly expose establishment-number strings for impacted product.
  - `https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/understanding-fsis-food-recalls`
  - `https://www.fsis.usda.gov/recalls`

### Direct-overlap / novelty risk

FSIS already uses Salmonella moving-window categories operationally. Directive 10,250.2 states that Category 3 establishments can trigger follow-up sampling, Public Health Risk Evaluations and Food Safety Assessments. Therefore sampling→regulatory-attention is **not novel**. The R37 candidate remains narrower: whether separately published establishment-specific sampling history can support a reproducible, exact-establishment, prospective linkage to later recall/public-health-alert records. No claim is made that this relationship is novel.

Key overlap source:
- `https://www.fsis.usda.gov/policy/fsis-directives/10250.2`

### Hardest F01 uncertainty

Whether historical sampling identifiers and recall establishment-number representations can be normalized **without fuzzy/name/address repair**, with enough recall records carrying exact establishment numbers and enough independent establishments for a future design.

## 2. `US-USASPEND-VENDOR-001`

### Official-source support

- USAspending exposes public APIs without authorization and supports award/transaction downloads, recipient endpoints, spending-by-recipient and recipient autocomplete/search.
  - `https://api.usaspending.gov/docs/endpoints`
- Recipient endpoint documentation exposes `uei` as the Unique Entity Identifier alongside recipient metadata.
  - `https://github.com/fedspendingtransparency/usaspending-api/blob/master/usaspending_api/api_contracts/contracts/v2/recipient.md`

### Direct-overlap / novelty risk

The platform itself supports recipient, agency, NAICS/PSC and award-time analyses, so basic concentration is not novel. More importantly, a future **absence of awards is not a direct adverse event**: it can reflect vendor exit, procurement-cycle timing, changing agency demand, contract completion, merger/reorganization or ordinary market movement. This weakens direct-outcome quality even though UEI identity and cardinality are strong.

### Hardest F01 uncertainty

Whether a future outcome can be preregistered as a sufficiently interpretable discontinuity without converting ordinary procurement absence into a failure label.

## 3. `US-EPA-SDWIS-001`

### Official-source support

- ECHO SDWA downloads provide national SDWIS tables for public water systems, site visits, violations and enforcement.
- `PWSID` is the official unique public-water-system identifier, and `SUBMISSIONYEARQUARTER + PWSID` identifies quarterly public-water-system rows and joins related tables.
- Violation data distinguish categories and can expose health-based indicators through official reporting services.
  - `https://echo.epa.gov/tools/data-downloads/sdwa-download-summary`
  - `https://sdwis.epa.gov/ords/sfdw_pub/sfdw/r/sdwis_fed_reports_public/9`

### Direct-overlap / novelty risk

The candidate is highly source-native and high-cardinality, but the same regulatory system already integrates monitoring/reporting, treatment-technique and health-based violations. Published drinking-water research also analyzes health-based versus monitoring/reporting violation structure. This produces substantial agency-framework/direct-literature overlap.

### Hardest F01 uncertainty

Not identity; rather whether a prospective exposure definition can add information beyond the existing regulatory violation framework without simply repackaging SDWIS's own compliance logic.

## 4. `US-CMS-NH-001`

### Official-source support

- CMS PBJ provides auditable direct-care staffing information and CMS explicitly uses staffing in Nursing Home Care Compare/Five-Star quality assessment.
  - `https://www.cms.gov/medicare/quality/nursing-home-improvement/staffing-data-submission`
- Provider Data Catalog nursing-home files use exact CMS Certification Number (`CCN`), provide staffing/turnover fields, health deficiencies, penalties and archives.
  - `https://data.cms.gov/provider-data/topics/nursing-homes`
  - `https://data.cms.gov/provider-data/archived-data/nursing-homes`

### Direct-overlap / novelty risk

This candidate has the strongest external overlap. CMS itself treats staff turnover and staffing as quality measures, and multiple published studies directly link nursing-home turnover/staffing to citations, deficiencies and other quality outcomes. Therefore the candidate is technically strong but weak on low-overlap/novelty information gain.

Examples:
- Zheng et al., 2022, *Journal of the American Geriatrics Society* — staff turnover and nursing-home quality.
- 2023 JAMA Internal Medicine study — within-facility turnover associated with inspection citations and quality measures.
- CMS quality-measure materials explicitly state staffing/turnover associations with quality outcomes.

## Outcome-blind conclusion / 결과 비개방 결론

All four candidates remain technically plausible at source level. Their differentiator is not raw accessibility alone:

- FSIS: strongest distinct cross-dataset structure with exact establishment identity prospect; meaningful but incomplete regulatory overlap.
- USAspending: strongest UEI identity/cardinality but ambiguous future `award interruption` semantics and lower cross-system gain.
- SDWIS: excellent exact PWSID structure but high same-regulatory-framework overlap.
- CMS nursing homes: excellent CCN/archives/cardinality but very high direct literature and agency-quality-framework overlap.

Candidate future outcome rows remain unopened. Incremental monetary cost: **0 USD**.
