---
id: US-USDA-ORG-F01
type: outcome-blind-structural-feasibility
created: 2026-09-29
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R46
parent_decision: DEC-269
selected_candidate: US-USDA-ORG-001
future_suspended_revoked_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-USDA-ORG-F01 — exact Organic-INTEGRITY Operation-ID gate before future suspension/revocation

## Mission / 목적

Determine, **before opening any post-baseline Suspended/Revoked membership**, whether official USDA Organic INTEGRITY and AMS enforcement sources can support a deterministic operation-level prospective design using exact source-native NOP Operation ID.

F01 is structural only. It does not test whether certifier, geography, scope, business type, anniversary timing, acreage, product mix or any other historical characteristic predicts suspension or revocation.

## Frozen population / 고정 모집단

The focal population is USDA-NOP organic operations in Organic INTEGRITY.

Trade-partner-only records, certifier entities and accreditation records may be inspected only for schema separation and may not be pooled into focal support counts unless the official export itself marks them as USDA-NOP operations.

## Frozen source anchors / 공식 소스

- USDA Organic enforcement: `https://www.ams.usda.gov/services/enforcement/organic`
- AMS final decisions: `https://www.ams.usda.gov/services/enforcement/organic/ams-decisions`
- USDA Organic INTEGRITY public search/export surfaces under `organic.ams.usda.gov`
- current USDA INTEGRITY data dictionary / official documentation under `ams.usda.gov`

After Issue binding, the runner may resolve the current zero-cost public export from the official Organic INTEGRITY search/report surface and must fingerprint the exact export body.

Historical AMS decision/enforcement pages dated on or before **2026-09-29** may be opened for status/event semantics only.

## Frozen Operation ID / 식별자

Primary identity is USDA NOP **Operation ID / NOP ID**.

The official data dictionary describes Operation ID as a **10-digit unique ID**.

Allowed normalization:
1. convert source value to text without numeric rounding;
2. trim leading/trailing ASCII whitespace;
3. accept only exact `^[0-9]{10}$`.

Prohibited:
- zero-padding;
- deleting punctuation;
- certifier/client-ID substitution;
- certificate-number substitution;
- operation-name/certifier/address matching;
- fuzzy/manual/geospatial repair.

## Frozen baseline / 기준시점

Baseline is the official public Organic INTEGRITY export resolved and downloaded **after Issue binding on 2026-09-29**.

F01 may inspect baseline rows only for:
- exact Operation ID;
- program;
- certification status;
- status effective date;
- certifier;
- geography;
- scope/business-type/non-outcome structural fields;
- support/cardinality.

F01 does not define a predictive exposure.

## Frozen future event window / 미래 event 창

A later descendant may identify future adverse status only when the source-native status effective date is:

- **start:** 2026-09-30
- **end:** 2027-03-31 inclusive.

In F01:
- no operation may be classified as future Suspended/Revoked;
- no post-2026-09-29 adverse-status membership may be opened, searched or cached;
- metadata-only future page checks are allowed only if no entity membership/body is consumed.

## Frozen event hierarchy / event 계층

Keep separate:
1. **Suspended**
2. **Revoked**
3. **Surrendered**
4. Certified
5. Transitional/Denied/Withdrew or other source-native non-adverse categories.

Primary adverse event prospect is later first transition into **Suspended or Revoked**. Surrendered is not adverse and may never be pooled with Suspended/Revoked.

AMS final notices/decisions may support semantics but may not be linked to an operation by name if an exact Operation ID is absent.

## Anti-tautology firewall / 순환성 방화벽

The following may not be used as historical exposure in descendants:
- proposed suspension/revocation notice;
- pending appeal/adverse-action flag;
- known unresolved noncompliance disposition;
- explicit reinstatement-pending state;
- any direct precursor mechanically encoding future suspension/revocation.

## Immutable 18-gate contract

Exactly **18/18 PASS** is required.

| # | Requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R46 selection `US-USDA-ORG-001`, checkpoint `CHK-20260929-PORTFOLIO-R46-TERMINAL`, last decision `DEC-269` |
| 2 | Issue binding | empirical runner executes only after a new Issue is bound to this exact pre-Issue contract commit |
| 3 | Official documentation access | enforcement, AMS-decisions and current INTEGRITY documentation/search surfaces are reachable or officially redirected |
| 4 | Public export access | an anonymous zero-cost official Organic INTEGRITY operation export can be resolved and downloaded from USDA-owned/public USDA-operated surfaces |
| 5 | Export schema | export exposes Operation ID/NOP ID, Program, Operation Certification Status and Status Effective Date concepts |
| 6 | Exact ID syntax | ≥ **99.90%** of nonblank focal USDA-NOP operation IDs satisfy exact 10-digit rule |
| 7 | Independent operation support | ≥ **40,000** distinct qualified USDA-NOP Operation IDs exist |
| 8 | Certified support | ≥ **30,000** distinct qualified IDs have exact source-native Certified status |
| 9 | Status semantic coverage | ≥ **99.90%** of nonblank focal statuses belong to documented source-native status labels without inference |
| 10 | Status-date support | ≥ **99.00%** of focal rows have parseable nonblank status effective date |
| 11 | Historical adverse support | ≥ **1,000** distinct qualified Operation IDs have source-native Suspended or Revoked status with effective date ≤ 2026-09-29 |
| 12 | Surrender separation | ≥ **100** distinct qualified Operation IDs have source-native Surrendered status and Surrendered is separately encoded from Suspended/Revoked |
| 13 | AMS legal-semantic support | official AMS enforcement/decision sources separately describe suspension and revocation as adverse certification actions and distinguish operations pending appeal/final decision status |
| 14 | Current-profile concordance | deterministic lexicographic sample of up to **100** qualified export Operation IDs yields ≥ **95.00%** exact NOP-ID/status concordance on official Organic INTEGRITY operation profile pages where profiles are directly available by ID; no name search |
| 15 | Historical lineage adequacy | official current dataset/documentation supports retained formerly certified Suspended/Revoked operations and effective-date semantics sufficient to construct pre-cutoff historical adverse-status support without external name matching |
| 16 | Future source seal | post-2026-09-29 Suspended/Revoked membership opened = **false** and future entity rows consumed for membership = **0** |
| 17 | Outcome/identity firewall | relationship/prediction/ranking/causal metric computed = **false**; certificate/name/certifier/address/fuzzy/manual/geo identity repair = **false**; prohibited precursor exposure computed = **false** |
| 18 | Reproducibility/cost | immutable JSON/Markdown records URLs/metadata, export SHA-256, schema/counts/statuses/dates, sample rule/results, contract SHA, runner SHA-256, firewall values and `incremental_monetary_cost_usd = 0` |

## Frozen API/profile sample rule

Sort all qualified focal Operation IDs lexicographically and take the first 100. Use only direct official profile access keyed by exact NOP ID if available. If the public profile architecture requires name search or another identifier substitution, Gate 14 fails rather than using a repaired identity.

## Terminal rule

PASS only if all 18 gates pass:

`PASS_US_USDA_ORG_F01_EXACT_OPERATION_FUTURE_SUSPENSION_REVOCATION_DESIGN_READY`

Any valid empirical failure:

`HOLD_US_USDA_ORG_F01_EXACT_OPERATION_FUTURE_SUSPENSION_REVOCATION_DESIGN_NOT_READY`

A valid HOLD is terminal for this exact design. Do not lower support thresholds, broaden status classes, use name/certifier/address matching, substitute certificate/client ID, or redefine Surrendered as adverse after observation.

Transport/parser/official-host migration defects may be corrected only if no scientific criterion changes and prior attempts remain immutable.

## PASS consequence

PASS authorizes only a separate outcome-blind `US-USDA-ORG-N01` design. E01 is not authorized by F01 PASS alone.

## Non-claims

F01 makes no claim that any organic-operation characteristic predicts or causes suspension/revocation; no business-risk score, enforcement recommendation, certification recommendation, ranking, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.
