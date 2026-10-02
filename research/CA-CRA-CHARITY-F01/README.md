---
id: CA-CRA-CHARITY-F01
type: outcome-blind-structural-feasibility
created: 2026-10-02
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R52
parent_decision: DEC-295
selected_candidate: CA-CRA-CHARITY-001
future_revocation_membership_opened: false
incremental_monetary_cost_usd: 0
---

# CA-CRA-CHARITY-F01 — exact registration-number longitudinal gate before future revocation

## Mission / 목적

Determine, before opening any revocation membership from a later CRA public-status refresh, whether Canada's official charity data support a deterministic charity-level prospective design linking non-tautological T3010 organisational/financial structure to later registration revocation.

F01 is structural only. It does not test whether any charity characteristic predicts revocation.

## Frozen official source family

Allowed official sources only:
- Government of Canada Open Data annual **List of Charities** datasets and their CSV/data-dictionary resources;
- CRA List of charities / public charity-status surfaces;
- CRA published revocation guidance/list surfaces;
- CRA official registration-number documentation.

No commercial registry, third-party mirror or paid API is authorized.

## Frozen annual baseline

Exactly **2018 through 2024 inclusive**.

For each year, F01 may open only that year's official Government of Canada annual charity release and its row-bearing CSV resources.

Record:
- official dataset/resource URL;
- final URL and HTTP metadata;
- byte size/SHA-256;
- headers/schema fingerprint;
- row counts;
- distinct exact charity registration numbers;
- structural-field support.

## Frozen exact identity

Primary identity is the complete registered-charity program account number:

**`^[0-9]{9}RR[0-9]{4}$`**

CRA defines it as:
- 9-digit Business Number;
- program identifier `RR`;
- 4-digit reference number.

Allowed normalization:
- text conversion;
- trim ASCII whitespace;
- remove ASCII spaces internal to the displayed registration number only;
- uppercase letters.

Prohibited:
- changing the nine-digit BN;
- replacing RR;
- zero-padding missing BN/reference digits;
- collapsing different RR reference numbers to the same BN;
- charity-name/address/geographic/fuzzy/manual repair.

## Frozen historical event support

F01 may inspect only the current official CRA published-revocation/public-status source first resolved after Issue binding, and only to establish historical event semantics/support.

Primary event prospect:
- source-native **revoked charity registration**;
- exact full charity registration number;
- source-native effective/publication date where available;
- reason/status retained source-natively.

Annulment is not revocation.
Reinstatement/re-registration is not uninterrupted survival and must remain separately identifiable.

## Future event firewall

A future descendant may classify revocation membership only from a later official CRA public-status/revocation source refresh first opened **after N01 prospective lock**, with a different source fingerprint or newly published status/event row.

F01 may not open a later refresh after its runner-start cutoff.

## Anti-tautology firewall

Descendant predictive exposures may not include:
- failure-to-file/delinquency status;
- direct compliance/default status;
- notice/intention-to-revoke fields;
- sanction/enforcement fields;
- current revocation/annulment status;
- variables mechanically derived from a future status window.

F01 may inspect status/revocation rows only for event support/semantics and identity continuity.

## Immutable 18-gate contract

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R52 selection, checkpoint `CHK-20261002-PORTFOLIO-R52-TERMINAL`, last decision `DEC-295` |
| 2 | Issue binding | empirical runner executes only after new Issue binding to this exact pre-Issue contract |
| 3 | Official source access | annual Open Data, CRA registration-number and revocation/status anchors are reachable or officially redirected |
| 4 | Annual-body lineage | every year 2018–2024 resolves to at least one row-bearing official charity CSV with independent fingerprint |
| 5 | Annual identity schema | every frozen year exposes BN/registration identity sufficient to reconstruct the full source-native charity registration number without inference |
| 6 | Exact registration syntax | ≥ **99.90%** of nonblank annual charity identities satisfy the frozen full registration-number rule after allowed whitespace normalization |
| 7 | Annual support | every frozen year contains ≥ **50,000** distinct exact charity registration numbers |
| 8 | Longitudinal continuity | ≥ **70.00%** of 2024 qualified registrations appear in at least **5 of 7** frozen annual years |
| 9 | Structural support | 2024 body exposes category/designation plus at least three non-tautological financial/organisational concepts with ≥ **90.00%** usable support |
| 10 | Revocation/status source access | official current CRA revocation/public-status source resolves and is fingerprintable |
| 11 | Event semantics | source/documentation distinguishes registered, revoked and annulled states and documents revocation effective/publication semantics |
| 12 | Event identity support | ≥ **99.00%** of historical revoked-charity identities with nonblank identifiers satisfy the exact registration-number rule |
| 13 | Historical event join | ≥ **95.00%** of distinct exact historical revoked identities match at least one 2018–2024 annual charity identity |
| 14 | Historical event support | ≥ **1,000** distinct historical revoked charity registrations are observed in the allowed historical support source |
| 15 | Event-date support | ≥ **95.00%** of historical revoked events have a parseable source-native effective/publication date |
| 16 | Reinstatement separation | official source/documentation supports separating reinstated/re-registered records from uninterrupted registration, without identity repair |
| 17 | Future/outcome firewall | later refresh opened = false; future revocation membership opened = false; relationship/prediction/ranking/causal metric = false; prohibited compliance exposure = false; identity repair = false |
| 18 | Reproducibility/cost | immutable evidence records source URLs/metadata/fingerprints, annual schemas/counts/continuity, event support, contract SHA, runner SHA, cutoff/firewalls and cost = 0 USD |

## Frozen terminal rule

PASS only if all gates pass:

`PASS_CA_CRA_CHARITY_F01_EXACT_REGISTRATION_FUTURE_REVOCATION_DESIGN_READY`

Any valid empirical gate failure:

`HOLD_CA_CRA_CHARITY_F01_EXACT_REGISTRATION_FUTURE_REVOCATION_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01.

Do not rescue by changing annual years, collapsing RR reference numbers, using name/address matching, lowering support thresholds, reclassifying annulment as revocation, using filing delinquency as exposure, or opening a later status refresh.

Transport/parser defects may be corrected only if scientific criteria remain unchanged and prior attempts remain immutable.

## PASS consequence

PASS authorizes only a separate outcome-blind `CA-CRA-CHARITY-N01`.

N01 must freeze one non-tautological baseline exposure, exact eligible cohort, comparator/matching design, common-support/balance gates, reinstatement handling, one future status-refresh window and minimum event support before later revocation membership is opened.

E01 is not authorized by F01 PASS alone.

## Non-claims

No charity quality/risk ranking, funding recommendation, revocation prediction, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.
