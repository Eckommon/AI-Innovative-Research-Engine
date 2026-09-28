---
id: UK-CQC-LOC-F01
type: outcome-blind-structural-feasibility
created: 2026-09-28
status: CONTRACT_FROZEN_PRE_ISSUE
parent: PORTFOLIO-R42
parent_decision: DEC-251
selected_candidate: UK-CQC-LOC-001
future_inactive_deactivated_membership_opened: false
incremental_monetary_cost_usd: 0
---

# UK-CQC-LOC-F01 — exact Location-ID structural gate before future registration end/deactivation

## Mission / 목적

Determine, **before opening any post-2026-09-28 inactive/deactivated location membership**, whether official Care Quality Commission public data can support a deterministic location-level prospective design linking historical rating/service structure to a later registration-end/deactivation event while distinguishing true cessation-like exits from administrative re-registration, legal-structure change or address change.

F01 is structural only. It does not test whether ratings, service type, specialism, regulated activity or ownership structure predicts registration ending.

## Frozen official source family / 고정 소스

Official landing page:

- `https://www.cqc.org.uk/about-us/transparency/using-cqc-data`

Frozen snapshot selectors observed before Issue creation:

- **Care directory with filters (01 September 2026)**
- **Care directory with ratings (01 September 2026)**
- **Deactivated locations (01 September 2026)**

The page also documents that the CQC API contains active and inactive providers/locations, registration start/end dates, organization type, linked organisations, regulated activities, service types/specialisms and latest ratings/report publication dates.

After Issue binding, F01 may retrieve only the exact official CQC-owned files resolved from the three frozen 01-September-2026 selectors. If the landing page rolls forward and the exact September-2026 files are not recoverable from CQC's official archive, F01 is operational HOLD; no later snapshot substitution is allowed.

## Frozen identity / 고정 식별자

Primary unit identity is exact **CQC Location ID**.

Allowed normalization:

1. convert source value to text;
2. trim leading/trailing whitespace;
3. preserve all remaining source characters exactly;
4. accept only nonblank ASCII alphanumeric tokens.

Prohibited:
- case-changing to repair mismatches;
- padding/truncation;
- provider ID substitution;
- name/address/postcode matching;
- fuzzy matching;
- geospatial reconciliation;
- manual repair.

If the same exact Location ID maps to conflicting simultaneously active locations in the frozen baseline, the ID is excluded rather than repaired.

## Frozen historical baseline / 고정 baseline

Baseline date is **2026-09-01**.

Historical directory/rating/deactivated rows dated or published on/before the frozen snapshot may be opened only for structural identity/schema/cardinality/semantic support.

No row from a CQC active/inactive/deactivated source whose snapshot/as-of date is after **2026-09-28** may be opened in F01.

## Frozen future window / 미래 window

A later descendant may consider registration-end/deactivation events with source-native registration end date in:

- start: **2026-09-29**
- end: **2027-03-31 inclusive**

Future inactive/deactivated membership remains sealed in F01.

## Frozen event-semantics boundary / event 의미 경계

CQC explicitly states that an archived/deactivated location is **not necessarily a closed service**; a location may be archived because the provider re-registers, changes legal structure or changes address.

Therefore F01 PASS requires current historical public structure to establish more than mere deactivated membership.

Before any future event membership is opened, F01 must prove that official CQC fields/API semantics provide a deterministic mechanism to identify at least one of:

1. registration-end reason/status;
2. explicit linked-organisation/location lineage showing re-registration or provider change;
3. another source-native field that prospectively distinguishes administrative transition from cessation-like registration ending.

If deactivated membership and end date are available but no source-native transition/lineage semantics can separate administrative re-registration/change from cessation-like exit, this exact F01 is HOLD.

No name/address comparison may be used to infer continuity.

## Immutable 18-gate contract / 불변 18개 gate

Exactly **18/18 PASS** is required.

| # | Frozen requirement | PASS criterion |
|---|---|---|
| 1 | Parent authorization | canonical parent is R42 terminal selection `UK-CQC-LOC-001` / `DEC-251` |
| 2 | Issue binding | empirical runner executes only after a new Issue is created against this exact pre-Issue contract commit |
| 3 | Official landing-page access | official CQC page is reachable by runner or official same-content redirect and identifies all three frozen 01-Sep-2026 selectors |
| 4 | Official file resolution | all three selectors resolve to CQC-owned downloadable files at zero incremental cost |
| 5 | Directory schema | filters directory exposes exact CQC Location ID plus active registration/service structure fields |
| 6 | Location-ID syntax | >= **99.90%** of nonblank baseline Location IDs satisfy the frozen exact-token rule |
| 7 | Active location support | >= **20,000** distinct exact baseline Location IDs |
| 8 | Ratings schema | ratings file exposes exact Location ID plus at least one rating/status field and publication/assessment date field |
| 9 | Ratings exact-link support | >= **10,000** distinct baseline Location IDs exact-link to at least one ratings row |
| 10 | Deactivated schema | frozen deactivated file exposes exact Location ID plus registration-end/deactivation date |
| 11 | Historical deactivated support | >= **5,000** distinct exact deactivated Location IDs |
| 12 | End-date parseability | >= **95.00%** of qualified historical deactivated rows have parseable nonblank registration-end/deactivation date |
| 13 | Administrative-transition semantics | official source fields/API metadata provide deterministic source-native registration-end reason or linked-organisation/location lineage sufficient to distinguish at least one administrative re-registration/change class from cessation-like ending |
| 14 | Identity conflict control | retained exact Location IDs have no unresolved simultaneous active identity conflict after source-native duplicate handling |
| 15 | Historical archive lineage | official CQC page/archive exposes at least **6** monthly historical directory/rating snapshots before or including Sep-2026 |
| 16 | Future source seal | no post-2026-09-28 inactive/deactivated entity row or file body is opened |
| 17 | Outcome/identity firewall | future rows opened = 0; future event membership opened = false; relationship/prediction/ranking/causal metric = false; name/address/fuzzy/geo/manual repair = false |
| 18 | Reproducibility/cost | immutable evidence records resolved URLs, source hashes, schema fields, counts, lineage evidence, contract SHA, runner SHA-256 and cost = 0 USD |

## Terminal rule / 종결 규칙

PASS:

`PASS_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_READY`

Any valid empirical failure:

`HOLD_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_NOT_READY`

No post-observation relaxation, later-snapshot substitution, name/address continuity repair, or generic deactivated=closed relabeling is allowed.

Transport/parser defects may be corrected only without changing source snapshot, identity rule, thresholds, semantics or future firewall, with prior attempts preserved immutably.

## PASS consequence / PASS 이후

PASS authorizes only a separate outcome-blind `UK-CQC-LOC-N01` design. N01 must freeze one non-tautological historical exposure, cohort/exclusions, exact lineage rules, comparator/matching design, support/balance gates, future cessation-like event hierarchy, ambiguous administrative-transition handling, minimum future event support and a later primary statistical gate before future membership is opened.

E01 is not authorized by F01 alone.

## Non-claims / 비주장

F01 makes no claim that CQC ratings or service characteristics predict or cause registration ending, and makes no provider/location ranking or recommendation.

Incremental monetary cost must remain **0 USD**.
