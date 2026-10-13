---
id: PORTFOLIO-R56-REVALIDATION
type: bounded-survivor-source-revalidation
created: 2026-10-13
issue: 200
contract: 0144ed638e671029eeea288eb91402591b2c5a30
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R56 — survivor-first source revalidation

## Outcome firewall

No candidate-specific future membership, event effect, prediction, ranking or causal result was opened. Revalidation used current official source/documentation surfaces and canonical project history only.

## 1. US-CMS-NPI-002

CMS currently publishes Version 2 of:
- a monthly full NPPES replacement file;
- a separate monthly NPI deactivation update;
- weekly incremental NPI files.

The official NPI Files page currently exposes the **October 12, 2026** monthly V2 full file and October 12 monthly deactivation update. CMS separately states that deactivated NPIs and deactivation dates are included in the full replacement monthly file, and that weekly updates include newly assigned, updated and newly deactivated NPIs.

Strengths:
- exact source-native 10-digit NPI;
- large national provider universe;
- direct deactivation event body;
- monthly full replacement + weekly incremental cadence;
- provider taxonomy and practice-location reference files support large structural exposure families;
- likely large exposed/control arms for Type-2 organizational structure.

Critical boundary:
- deactivation is an administrative registry state, not provider closure, insolvency, quality failure or patient-access harm;
- reactivation can occur;
- Type-1 and Type-2 NPIs must remain separate unless prospectively justified;
- structural exposure cannot use deactivation/reactivation/history fields.

Canonical overlap:
- previously held in R55 but never activated;
- no completed NPI F01 exists in canonical history.

## 2. US-FAA-AIR-002

FAA directly publishes the complete releasable aircraft database, refreshed **daily**, including Master, Deregistered Aircraft, Document Index and reference files. Official yearly archives for 2012–2021 remain available.

Strengths:
- direct row bodies and daily future-event opportunity;
- sizeable registry;
- explicit Deregistered Aircraft file.

Critical boundary:
- N-number reuse prevents N-number-alone identity;
- compound serial/manufacturer identity must be established;
- deregistration reason is heterogeneous;
- missing permissible fields cannot be treated as errors.

Canonical overlap:
- held several times but not activated in this exact deregistration design.

## 3. US-PHMSA-PIPE-002

PHMSA publishes operator IDs, annual-report raw data and incident data. Annual-report ZIPs are updated monthly for supplemental submissions. Infrastructure lineage extends decades depending on system family.

Strengths:
- operationally meaningful incident event;
- long historical infrastructure exposure;
- exact operator-ID prospect.

Critical boundary:
- incidents are sparse at operator level;
- a single pipeline family must be fixed;
- supplemental report revisions complicate baseline locking;
- prior incident/enforcement fields cannot be exposures.

Canonical overlap:
- PHMSA has appeared as a held portfolio candidate; no exact current F01 activated.

## 4. US-FCC-ULS-002

FCC ULS provides complete database files updated weekly and daily transaction files for new/modified licenses. Pipe-delimited database downloads and an Open Data/OData surface are available.

Strengths:
- very large license universe;
- dense daily/weekly update opportunities;
- source-native status/application structures.

Critical boundary:
- termination/expiration may be administrative rather than substantive failure;
- service-specific identity/call-sign reuse rules complicate a universal design;
- prior FCC work creates more internal overlap than CMS/FAA.

## Survivor-first conclusion

CMS NPI has the strongest combined probability of surviving both F01 and a later N01 because it pairs:
- exact identity;
- direct event body;
- repeated future updates;
- large eligible universe;
- rich non-outcome structure;
- likely large exposed/control arms.

FAA is the strongest alternate but identity continuity is materially harder. PHMSA has stronger substantive-event semantics but weaker event density. FCC has strong cadence but weaker outcome meaning and higher overlap.

Future memberships remain unopened. Cost remains 0 USD.
