---
id: PORTFOLIO-R52-REVALIDATION
type: bounded-source-overlap-revalidation
created: 2026-10-02
issue: 191
contract: b9ce6d57e138e295438ebfb76c7d3c446d30b836
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R52 — bounded source / overlap revalidation

## Outcome firewall

No candidate-specific future event membership, effect, prediction, ranking or causal result was opened. Revalidation used official source/documentation pages, canonical project history and bounded literature/framework context only.

## CA-CRA-CHARITY-001

Government of Canada Open Data publishes annual **List of Charities** datasets with CSV resources and data dictionaries across decades, including historical years back to at least the mid-1990s and current releases through 2024. Identification resources expose Business Number / registration identity and annual charity structure.

CRA separately publishes:
- publicly available charity status data;
- lists of published revocations;
- revocation semantics tied to publication/effective status;
- categories such as revoked, annulled and registered status in public charity listings.

Strengths:
- long annual longitudinal lineage;
- exact source-native registration/business identity;
- rich structural/financial/program data;
- direct official revocation semantics;
- zero-cost machine-readable annual bodies.

Critical boundaries:
- reinstatement/re-registration must remain distinct from uninterrupted registration;
- failure-to-file and direct revocation-warning variables are outcome-proximal and prohibited as predictive exposures;
- annual-return filing years and legal status dates must be temporally aligned prospectively.

## UK-CC-CHARITY-001

The Charity Commission provides:
- full-register bulk downloads/API;
- source-native charity number;
- financial history;
- explicit data-definition fields such as `date_of_removal`, `removal_reason` and reporting status.

The Commission also reports thousands of removals annually.

Strengths:
- strong exact identity and direct removal semantics;
- large independent-unit population;
- rich financial history and current bulk/API access.

Critical boundary:
- current/live register data are strong, but durable versioned historical snapshots across a frozen multi-year baseline are less directly established than CRA annual releases;
- reporting-default/overdue status cannot be used as a descendant exposure where it mechanically precedes removal.

## AU-ACNC-CHARITY-001

ACNC publishes the current Charity Register dataset and annual Annual Information Statement datasets, with weekly updates to current annual resources.

Strengths:
- zero-cost bulk charity data;
- annual AIS structure;
- source-native charity/ABN identity prospect.

Critical boundary:
- current-register disappearance is not an admissible revocation event without explicit source-native historical status semantics;
- historical registration-end/revocation lineage is weaker than CRA/UK evidence reviewed here.

## US-FDIC-BANK-001

FDIC provides:
- institution/history/financial bulk data;
- quarterly financial history back to 1992;
- Call Report access;
- failure and assistance data;
- exact FDIC certificate number identity.

Strengths:
- exceptionally strong deterministic join and longitudinal history;
- direct failure event semantics;
- zero-cost bulk/API architecture.

Critical boundary:
- bank-failure prediction is a highly mature empirical field, creating substantial overlap/novelty penalty;
- failures are rare and direct supervisory/enforcement variables cannot be used as predictive exposure.

## Canonical overlap

- No exact prior canonical candidate was found for CA-CRA charity revocation, UK Charity Commission removal, AU-ACNC charity registration end or FDIC bank-level failure.
- Existing FDIC work is branch-level/branch-change oriented, not bank-failure outcome, but same institution family still creates some portfolio overlap.
- R51 NCUA runner-up is not promoted or reused.

## Revalidation conclusion

All four candidates remain eligible for one immutable scorecard.

CRA has the best balance of exact identity, true longitudinal annual bodies, direct legal-status event semantics, practical value and lower saturation than bank-failure prediction.

Incremental monetary cost: **0 USD**.
