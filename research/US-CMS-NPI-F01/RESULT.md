---
id: US-CMS-NPI-F01-RESULT
type: structural-feasibility-result
created: 2026-10-13
issue: 201
research: US-CMS-NPI-F01
disposition: PASS
contract_commit: 18646fff22a499fedb058df397269281e62793b8
attempt_01_commit: 2f3325e4d7c0a3f664ef600752f68ad4ebc59df3
attempt_02_commit: 6b17006ecb98a395f169e1f1653ba3ddebee5081
attempt_02_run: 38355457891
incremental_monetary_cost_usd: 0
---

# US-CMS-NPI-F01 Result / 결과

## Terminal disposition / 최종 판정

**`PASS_US_CMS_NPI_F01_EXACT_NPI_TYPE2_FUTURE_DEACTIVATION_DESIGN_READY`**

Attempt 02 validly passed **18/18** frozen structural gates. Attempt 01 remains immutable and records the XLSX-parser implementation defect; Attempt 02 changed only the source-native deactivation-body parser.

## Baseline fingerprints

### Monthly V2 full replacement
- date family: **October 12, 2026**
- bytes: **1,159,720,219**
- SHA-256: `45b17c5fbfb919c4fa4878c0bbbeca979c4fa3bc87a6d733682b61a3e63c662e`

### Monthly V2 deactivation update
- bytes: **2,679,243**
- SHA-256: `fcceb74b2cc99e5e64582edefbb2f891128dc7d1ee7268eb52a961b1b1b998a1`
- source-native body: `NPPES Deactivated NPI Report 20261012.xlsx`

## Structural evidence

- exact unique NPIs: **9,852,180**
- exact syntax rate: **100%**
- duplicate exact NPIs: **0**
- active Type-2 organization NPIs: **1,979,717**
- active Type-2 with taxonomy: **1,979,717 (100%)**
- single-taxonomy active Type-2: **1,569,636**
- multi-taxonomy active Type-2: **410,081**
- Practice Location rows: **1,274,332**
- distinct Practice Location NPIs: **817,918**
- Practice Location exact syntax: **100%**
- Practice Location → main exact join: **100%**
- distinct deactivated NPIs: **357,926**
- deactivation NPI syntax: **100%**
- deactivation-date parseability: **100%**

## Firewall

- weekly incremental body opened: **false**
- later monthly body opened: **false**
- future deactivation membership opened: **false**
- future rows consumed: **0**
- relationship/prediction/ranking/causal metric: **false**
- deactivation/reactivation/history exposure: **false**
- identity repair: **false**
- cost: **0 USD**

## Interpretation

F01 establishes source/identity/support feasibility only. It does **not** establish that taxonomy plurality, location plurality or organizational complexity predicts deactivation.

NPI deactivation remains a source-native administrative registry event and must not be interpreted as provider closure, insolvency, quality failure, death or patient-access loss.

## Consequence

Authorize exactly one separate outcome-blind `US-CMS-NPI-N01` prospective-design gate.

N01 must freeze:
- active Type-2 baseline cohort;
- one non-tautological structural exposure;
- comparator/matching or stratification rules;
- reactivation handling;
- future update window;
- support/balance gates;
before any weekly or later monthly row body is opened.

E01 remains unauthorized.

Incremental monetary cost: **0 USD**.
