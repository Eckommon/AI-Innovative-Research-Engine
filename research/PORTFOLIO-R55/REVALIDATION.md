---
id: PORTFOLIO-R55-REVALIDATION
type: bounded-direct-body-revalidation
created: 2026-10-08
issue: 197
contract: ecbbe4cb6689f71095065e2d857d8e4d538deefe
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R55 — bounded direct-body revalidation

## US-EPA-RCRA-001

EPA ECHO currently exposes a direct RCRAInfo ZIP and a published data dictionary. Facility, enforcement, evaluation, violation, NAICS and VIO/SNC-history tables share documented source-native handler keys. The history table carries explicit monthly `YRMONTH`; evaluation rows carry date/type and `FOUND_VIOLATION`.

This is the strongest current route to row-level F01 adjudication because no archive SPA or undocumented service call is required.

The scientific limitation is inspection selection. Any descendant must define the future event at a future evaluation opportunity and may not use prior compliance/enforcement fields as exposure.

## US-CMS-NPI-001

CMS currently publishes a >1 GB monthly NPPES full replacement ZIP, a separate monthly deactivation update and weekly incremental files. CMS explicitly states the full replacement file contains deactivated NPIs and deactivation dates.

Identity and transport are excellent. Event semantics are weaker: deactivation is heterogeneous and can be followed by reactivation. A future design must keep reason/re-activation handling separate.

## US-FAA-AIR-001

FAA directly publishes a daily ~60 MB complete aircraft registry bundle containing Master and Deregistered Aircraft files plus official yearly archives for 2012–2021.

Transport and event bodies are strong. Temporal identity remains harder because N-numbers can be reassigned, so serial/manufacturer identity must be proved and reason strata remain heterogeneous.

## US-FDIC-BANK-001

FDIC BankFind/Bulk Data provides long quarterly/weekly history, exact CERT identity and Failures & Assistance. Transport and longitudinal quality are excellent.

The main penalty is mission marginal value: failures are rare and bank-failure prediction is a highly mature research domain, reducing event support and novelty.

## Canonical overlap

No exact RCRA F01 has been activated. CMS NPI was a held candidate in R49 but not selected. FAA deregistration was a held candidate in R50 but not activated. FDIC bank failure was a held R52 candidate; distinct prior FDIC branch work focused branch network/closure rather than insured-bank failure.

## Conclusion

RCRA has the highest combined probability of:
- direct row-body access;
- exact deterministic identity;
- dense historical event support;
- longitudinal history;
- enough future evaluation opportunities to support a later N01.

Future candidate membership remains unopened. Cost remains 0 USD.
