---
id: US-MSHA-MINE-F01
type: outcome-blind-structural-feasibility
created: 2026-09-29
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R45
parent_decision: DEC-263
selected_candidate: US-MSHA-MINE-001
future_serious_fatal_event_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-MSHA-MINE-F01 — exact Mine-ID structural gate before future serious/fatal accident events

## Mission / 목적

Determine, **before opening any post-2026-09-29 serious/fatal accident membership**, whether official MSHA public mine, quarterly employment/production and accident/injury datasets support a deterministic Mine-ID-level prospective design.

F01 is structural only. It does not test whether employment, mine type, production, inspections, ownership, commodity, 103(i) status or any other historical characteristic predicts an accident.

## Frozen focal population / 고정 모집단

The focal unit is one MSHA mine with exact source-native `MINE_ID`.

For active-support gates, the focal operating population is mines whose source-native `CURRENT_MINE_STATUS` is exactly one of:

- `Active`
- `Intermittent`
- `NonProducing`
- `Temporarily Idled`

`New Mine`, `Abandoned`, and `Abandoned and Sealed` are not included in active-support counts.

No post-observation status regrouping is allowed.

## Frozen official source anchors / 공식 소스

- `https://arlweb.msha.gov/OpenGovernmentData/OGIMSHA.asp`
- Mines Data Set and definition file
- Employment/Production Data Set (Quarterly) and definition file
- Accident Injuries Data Set and definition file
- `https://www.msha.gov/mine-data-retrieval-system`

The Open Government portal states that files are updated every Friday unless otherwise noted. The exact official dataset URLs resolved from the numbered dataset links after Issue binding become the frozen source selectors and must be fingerprinted.

## Frozen Mine-ID identity / 고정 식별자

Primary identity is exact MSHA `MINE_ID`.

Official MSHA definition files specify `MINE_ID` as `VARCHAR2(7)` and the unique key for the Mines dataset, with Mine ID used to join Mines to Accidents and Quarterly Employment/Production.

Allowed normalization:
1. convert source value to text without numeric rounding;
2. trim leading/trailing ASCII whitespace;
3. accept only exact `^[0-9]{7}$`.

Prohibited:
- zero-padding;
- hyphen or punctuation deletion;
- integer coercion that discards leading zeros;
- operator/controller/name/address matching;
- fuzzy/geospatial/manual repair.

## Frozen historical baseline / 고정 historical baseline

F01 uses the official source state downloaded after Issue binding on 2026-09-29.

Historical accident rows may be opened only when `ACCIDENT_DT <= 2026-09-29` and only for structural identity/date/severity/cardinality support.

Quarterly employment/production support is frozen to **2026 Q1 and 2026 Q2** rows. Later-quarter employment rows may not be substituted if a frozen support gate fails.

## Frozen future event window / 미래 event 창

A later descendant may identify a future primary event only from official MSHA accident/injury rows with:

- **start:** 2026-09-30
- **end:** 2027-03-31 inclusive.

In F01:
- no accident row with `ACCIDENT_DT >= 2026-09-30` may be used to classify future membership;
- future serious/fatal membership remains false/unopened;
- if the downloaded official current accident file unexpectedly contains a post-cutoff row, the runner must stop before inspecting its severity fields and record a future-firewall block.

## Frozen serious/fatal event semantics / 고정 event 의미

A future **primary serious/fatal event** is prospectively defined as an official accident/injury record satisfying at least one of:

1. `DEGREE_INJURY_CD in {'01','02'}`
   - 01 = Fatality
   - 02 = Permanent total or permanent partial disability
2. `IMMED_NOTIFY_CD in {'01','02'}`
   - 01 = Death
   - 02 = Serious injury

These exact source-native codes are frozen before future membership is opened.

The descendant must keep separate:
- fatality/death;
- permanent disability;
- serious injury immediate notification;
- days-away/restricted-work injuries;
- accident-only/no injury;
- occupational illness;
- natural-cause/non-employee/first-aid or other cases.

No narrative keyword classification is allowed.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical state is terminal R45 selection `US-MSHA-MINE-001`, checkpoint `CHK-20260929-PORTFOLIO-R45-TERMINAL`, last decision `DEC-263` |
| 2 | Issue binding | empirical runner executes only after a new Issue is created and bound to this exact pre-Issue contract commit |
| 3 | Official documentation access | Open Government portal, Mines/Accidents/Qrtly-Employment definition files and MDRS anchor are reachable or officially redirected |
| 4 | Official dataset resolution | portal resolves zero-cost official Mines, Accident Injuries and Quarterly Employment/Production entity bodies from MSHA-owned sources |
| 5 | Mines schema | Mines source exposes `MINE_ID`, `CURRENT_MINE_STATUS`, `CURRENT_STATUS_DT`, mine type and state concepts |
| 6 | Exact Mine-ID syntax | ≥ **99.90%** of nonblank Mines `MINE_ID` values satisfy exact seven-digit syntax under the frozen rule |
| 7 | Independent mine support | ≥ **50,000** distinct qualified Mine IDs exist in the complete Mines dataset |
| 8 | Operating-mine support | ≥ **10,000** distinct qualified Mine IDs fall in the frozen operating-status set |
| 9 | Quarterly employment schema | frozen 2026-Q1/Q2 source exposes Mine ID, calendar year, quarter, subunit and employee-hours/employment concepts |
| 10 | Quarterly employment support | ≥ **8,000** distinct qualified Mine IDs have at least one 2026-Q1 or Q2 operator employment/production row |
| 11 | Employment identity coverage | ≥ **99.00%** of distinct qualified 2026-Q1/Q2 employment Mine IDs exact-match the Mines dataset |
| 12 | Accident schema | Accident source exposes `MINE_ID`, `DOCUMENT_NO`, `ACCIDENT_DT`, `DEGREE_INJURY_CD`, `IMMED_NOTIFY_CD` and calendar-year/quarter concepts |
| 13 | Historical accident identity coverage | ≥ **99.00%** of distinct qualified pre-cutoff accident Mine IDs exact-match the Mines dataset |
| 14 | Historical serious/fatal support | pre-cutoff rows yield ≥ **1,000** distinct accident document numbers satisfying the frozen serious/fatal code rule across ≥ **500** distinct qualified Mine IDs |
| 15 | Event date/severity integrity | ≥ **99.00%** of frozen historical serious/fatal rows have a parseable `ACCIDENT_DT`, valid exact Mine ID and at least one qualifying source-native severity code |
| 16 | Event-class separation | official definition files establish the frozen Degree Injury and Immediate Notification code meanings without narrative inference |
| 17 | Future/outcome/identity firewall | post-cutoff event membership opened = **false**; relationship/prediction/ranking/causal metric computed = **false**; operator/controller/name/address/fuzzy/geo/manual identity repair used = **false** |
| 18 | Reproducibility and cost | immutable JSON/Markdown records resolved URLs/HTTP metadata, source SHA-256 values, schemas, row/cardinality/join/event counts, contract SHA, runner SHA-256, firewall values and `incremental_monetary_cost_usd = 0` |

## Frozen future-firewall implementation rule / 미래 방화벽 구현

The accident file may be streamed row-by-row. The runner may inspect only Mine ID and accident date first. If `ACCIDENT_DT >= 2026-09-30`, it must:
1. increment only a sealed future-row counter;
2. not read or record the severity/event columns for that row;
3. not include the row in any membership or support computation;
4. preserve `future_serious_fatal_event_membership_opened = false`.

F01 PASS therefore does not reveal which baseline mines later experience a future event.

## Frozen terminal rule / 종결 규칙

PASS only if every gate passes:

`PASS_US_MSHA_MINE_F01_EXACT_ID_SERIOUS_FATAL_FUTURE_EVENT_DESIGN_READY`

Any valid empirical failure:

`HOLD_US_MSHA_MINE_F01_EXACT_ID_SERIOUS_FATAL_FUTURE_EVENT_DESIGN_NOT_READY`

A valid scientific HOLD is terminal for this exact F01. Population/status sets, Mine-ID syntax, quarterly baseline, support thresholds, event codes and future firewall may not be loosened after observation.

Transport/parser/official-host-migration defects may be corrected only when no scientific criterion changes and prior attempts remain immutable.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `US-MSHA-MINE-N01` design.

N01 must freeze one non-tautological historical exposure, eligibility/exclusions, comparator/matching or stratification rules, future serious/fatal event adjudication, competing event handling, minimum future-event support and statistical gate **before** future event membership is opened.

E01 is not authorized by F01 PASS alone.

## Non-claims / 비주장

F01 makes no claim that any mine characteristic predicts or causes accidents; no safety score, mine ranking, enforcement target, employment recommendation, causal claim or novelty claim is authorized.

Incremental monetary cost must remain **0 USD**.
