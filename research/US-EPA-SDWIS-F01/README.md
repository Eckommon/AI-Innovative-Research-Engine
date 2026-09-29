---
id: US-EPA-SDWIS-F01
type: outcome-blind-structural-feasibility
created: 2026-09-30
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R47
parent_decision: DEC-273
selected_candidate: US-EPA-SDWIS-001
future_health_based_violation_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-EPA-SDWIS-F01 — exact PWSID quarterly structural gate before future health-based violation

## Mission / 목적

Determine, **before opening any event membership from a later SDWIS quarterly refresh**, whether EPA ECHO's national Safe Drinking Water Act / SDWIS download supports a deterministic public-water-system prospective design using exact PWSID and source-native health-based violation semantics.

F01 is structural only. It does not test whether system type, source, ownership, population served, seasonality, facility structure or any other baseline characteristic predicts a later violation.

## Frozen official source anchors / 공식 소스

- SDWA national download page: `https://echo.epa.gov/tools/data-downloads`
- SDWA data dictionary: `https://echo.epa.gov/tools/data-downloads/sdwa-download-summary`
- SDWA resources/data caveats: `https://echo.epa.gov/help/sdwa-faqs`
- current official ZIP selector resolved from the download page:
  `https://echo.epa.gov/files/echodownloads/SDWA_latest_downloads.zip`

EPA states that the national SDWA dataset is compiled from the latest SDWIS refresh and is updated quarterly.

## Frozen baseline / 고정 baseline

After Issue binding, Attempt 01 may download the official `SDWA_latest_downloads.zip` exactly once for empirical evaluation.

That exact body becomes the F01 historical baseline and must be recorded by:
- final URL;
- HTTP metadata;
- byte size;
- SHA-256;
- ZIP member inventory;
- maximum `SUBMISSIONYEARQUARTER` observed in the required baseline tables.

All rows contained in that exact fingerprinted ZIP are treated as **historical baseline/support only**, regardless of event date. No relationship, exposure selection or outcome comparison may be computed from them.

The raw ZIP remains transient under RAW-001 and is not committed to GitHub.

## Frozen future refresh / 미래 refresh

A future descendant may classify outcome membership only from a **later official quarterly SDWA ZIP** satisfying all of:

1. body SHA-256 differs from the F01 baseline SHA-256;
2. maximum `SUBMISSIONYEARQUARTER` is strictly later than the baseline maximum;
3. the source is the same official EPA SDWA national download family;
4. the later refresh is first opened only after N01 has frozen its prospective design.

In F01, no later-refresh ZIP body may be opened.

## Frozen PWSID identity / 고정 식별자

Primary identity is exact source-native **PWSID**.

Allowed normalization:
1. convert source value to text;
2. trim leading/trailing ASCII whitespace;
3. uppercase ASCII letters;
4. accept only exact pattern `^[A-Z0-9]{2}[0-9]{7}$`.

The first two characters must also be source-valid under the SDWIS state/region-code semantics or present consistently in the official dataset.

Prohibited:
- zero-padding;
- inserting/deleting characters;
- PWS name matching;
- address/city/county/geospatial repair;
- FRS-ID substitution;
- facility-ID substitution for the system identity;
- fuzzy/manual repair.

## Frozen event semantics / 고정 event 의미

The primary descendant event prospect is a **new source-native health-based violation**.

F01 freezes the health-based event rule to:
- `IS_HEALTH_BASED_IND == 'Y'`;
- the violation must have exact PWSID and VIOLATION_ID;
- event onset is `NON_COMPL_PER_BEGIN_DATE`;
- MCL, MRDL and Treatment Technique categories remain source-native subtypes, not post-hoc redefinitions.

Monitoring/reporting violations with `IS_HEALTH_BASED_IND != 'Y'` are not primary health-based outcomes.

Formal/informal enforcement, unresolved status and enforcement priority are not themselves the primary outcome and may not be used as descendant predictive exposures.

## Competing system states / 경쟁 상태

The following PWS activity states remain distinct:
- `A` Active
- `I` Inactive
- `N` changed from public to non-public
- `M` merged
- `P` potential future regulated system

A later N01 must prospectively define handling of inactivation, merger and deactivation before future violation membership is opened. F01 does not treat absence after merger/deactivation as a violation outcome.

## Anti-tautology firewall / 순환성 방화벽

A descendant predictive exposure may not include:
- prior/current violation count or status;
- `IS_HEALTH_BASED_IND` history;
- enforcement action/category;
- enforcement-priority flags;
- unresolved/Addressed/Unaddressed compliance status;
- direct contaminant exceedance or current violation measure;
- any variable mechanically derived from the future outcome window.

F01 may inspect historical violation rows only for structural support and event semantics, not to select an exposure.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R47 selection `US-EPA-SDWIS-001`, checkpoint `CHK-20260930-PORTFOLIO-R47-TERMINAL`, last decision `DEC-273` |
| 2 | Issue binding | empirical runner executes only after a new Issue is bound to this exact pre-Issue contract commit |
| 3 | Official source access | EPA download page, SDWA dictionary and SDWA FAQ are reachable or officially redirected |
| 4 | Baseline ZIP access | `SDWA_latest_downloads.zip` returns a parseable official ZIP, size ≥ **100 MB**, with SHA-256 recorded |
| 5 | Required table inventory | ZIP contains `SDWA_PUB_WATER_SYSTEMS.csv`, `SDWA_FACILITIES.csv`, `SDWA_VIOLATIONS_ENFORCEMENT.csv` and `SDWA_REF_CODE_VALUES.csv` |
| 6 | Public-system schema | PWS table exposes `SUBMISSIONYEARQUARTER`, `PWSID`, `PWS_ACTIVITY_CODE`, `PWS_TYPE_CODE`, `PRIMARY_SOURCE_CODE`, `OWNER_TYPE_CODE`, `POPULATION_SERVED_COUNT` and `PWS_DEACTIVATION_DATE` concepts |
| 7 | Exact PWSID syntax | ≥ **99.99%** of nonblank PWS-table PWSID values satisfy the frozen exact-ID rule |
| 8 | Quarterly key uniqueness | ≥ **99.99%** of PWS rows are unique on exact `SUBMISSIONYEARQUARTER + PWSID` |
| 9 | Temporal lineage | PWS table contains ≥ **8** distinct valid submission quarters and a deterministically identifiable maximum baseline quarter |
| 10 | Latest-quarter active support | latest baseline quarter contains ≥ **140,000** distinct exact PWSIDs with `PWS_ACTIVITY_CODE == 'A'` |
| 11 | Structural-field support | among latest-quarter active systems, ≥ **90.00%** have nonblank PWS type, primary source and population served; ownership may be separately reported but is not required to rescue the gate |
| 12 | Violation schema | violation/enforcement table exposes exact `SUBMISSIONYEARQUARTER`, `PWSID`, `VIOLATION_ID`, `NON_COMPL_PER_BEGIN_DATE`, `VIOLATION_CATEGORY_CODE`, `IS_HEALTH_BASED_IND`, `VIOLATION_STATUS`, `RULE_CODE`, `ENFORCEMENT_ID`, `ENFORCEMENT_DATE` and `ENF_ACTION_CATEGORY` concepts |
| 13 | Violation identity/join support | ≥ **99.90%** of nonblank violation PWSIDs satisfy the exact PWSID rule, and ≥ **99.00%** of distinct violation PWSIDs exact-match at least one PWS-table PWSID without name/geography repair |
| 14 | Health-event semantic coverage | ≥ **99.00%** of violation rows with nonblank health indicator use only documented `Y/N` values, and ≥ **10,000** distinct historical health-based `PWSID + VIOLATION_ID` events exist |
| 15 | Event-date support | ≥ **99.00%** of historical health-based events have a parseable nonblank `NON_COMPL_PER_BEGIN_DATE` |
| 16 | Future-refresh seal | no SDWA ZIP with a different body SHA or a later max submission quarter is opened; future event membership opened = **false** |
| 17 | Outcome/identity firewall | relationship/prediction/ranking/causal metric computed = **false**; prohibited compliance/enforcement exposure computed = **false**; name/address/geographic/fuzzy/manual identity repair = **false** |
| 18 | Reproducibility/cost | immutable JSON/Markdown records URLs/HTTP metadata, baseline ZIP SHA-256/member inventory, schemas, row/cardinality/quarter/event counts, contract SHA, runner SHA-256, firewall values and `incremental_monetary_cost_usd = 0` |

## Frozen reporting-lag rule / 보고 지연 규칙

EPA documents that violation/enforcement information is reported quarterly with an additional verification lag. Therefore a later N01 may not define an event solely by wall-clock discovery date.

N01 must use source-native `SUBMISSIONYEARQUARTER` plus `NON_COMPL_PER_BEGIN_DATE` and must freeze a minimum observation lag before opening a future refresh.

## Frozen terminal rule / 종결 규칙

PASS only if every gate passes:

`PASS_US_EPA_SDWIS_F01_EXACT_PWSID_FUTURE_HEALTH_VIOLATION_DESIGN_READY`

Any valid empirical gate failure:

`HOLD_US_EPA_SDWIS_F01_EXACT_PWSID_FUTURE_HEALTH_VIOLATION_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01. Do not lower cardinality/completeness thresholds, reinterpret non-health violations as health-based, substitute another identity, introduce geographic/name repair or open a later quarterly refresh after observation.

Transport/parser defects may be corrected only if every scientific criterion remains unchanged and prior attempts remain immutable.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `US-EPA-SDWIS-N01` design.

N01 must freeze one non-tautological baseline exposure, eligible active-system cohort, comparator/matching or stratification design, competing inactivation/merger handling, reporting-lag rule, future quarterly-refresh window, minimum event support and statistical/balance gates **before** a later refresh is opened.

E01 is not authorized by F01 PASS alone.

## Non-claims / 비주장

F01 makes no claim that source type, ownership, population, system type, facility structure or any other characteristic predicts or causes a future health-based violation. No utility ranking, enforcement recommendation, public-health risk score, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.
