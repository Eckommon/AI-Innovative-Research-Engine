---
id: US-IRS-EO-N01
type: outcome-blind-matched-design-identifiability
created: 2026-09-18
status: CONTRACT_FROZEN_PRE_ISSUE
parent: US-IRS-EO-F01
parent_gate: PASS_US_IRS_EO_F01_EXACT_EIN_JOIN_READY
future_outcome_membership_opened: false
relationship_computed: false
incremental_monetary_cost_usd: 0
---

# US-IRS-EO-N01 — outcome-blind matched governance-independence design

## Purpose / 목적

Determine, **before any Automatic Revocation List row is opened**, whether one historical pre-COVID Form 990 baseline can support a deterministic matched design comparing lower versus higher governing-body independence among otherwise comparable U.S. 501(c)(3) organizations.

Automatic revocation is mechanically caused by failure to file a required annual return or notice for three consecutive years. Therefore N01 deliberately does **not** use filing gaps, missed-filing counts, years-since-filing, 990-N/nonfiling indicators, final-return flags, or future revocation information as an exposure. The candidate exposure is a substantive governance characteristic reported on an actually filed Form 990.

N01 is a design-identifiability gate only. It may construct and persist a historical exposure/matching manifest. It may not open, count, infer, or condition on any Automatic Revocation membership.

## Why the 2019 posting-year baseline is frozen / 2019 baseline 고정 이유

The official IRS Form 990 download page still exposes a 2019 index and 2019 XML bundles. N01 freezes **posting year 2019 only** before any outcome access because:

1. it is the oldest posting year still directly listed on the current official Form 990 download page;
2. it provides a pre-COVID historical baseline rather than constructing exposure from the 2020 filing-extension period;
3. a later frozen revocation-effective-date window beginning in 2023 leaves at least a multi-year temporal gap after the historical filed-return baseline;
4. no later historical year may be substituted if support is weak.

This choice is outcome-blind and may not be changed after N01 counts are observed.

## Authorized official historical sources / 허가된 공식 과거 소스

N01 may read only zero-cost official IRS material needed for the historical design:

- 2019 Form 990 index CSV:
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/index_2019.csv`
- 2019 XML ZIP bundles currently listed by the official IRS Form 990 downloads page:
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/2019_TEOS_XML_CT1.zip`
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/download990xml_2019_1.zip`
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/download990xml_2019_2.zip`
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/download990xml_2019_3.zip`
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/download990xml_2019_4.zip`
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/download990xml_2019_5.zip`
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/download990xml_2019_6.zip`
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/download990xml_2019_7.zip`
  - `https://apps.irs.gov/pub/epostcard/990/xml/2019/download990xml_2019_8.zip`
- official Form 990 download page:
  - `https://www.irs.gov/charities-non-profits/form-990-series-downloads`
- official 2019 Form 990 and instructions:
  - `https://www.irs.gov/pub/irs-prior/f990--2019.pdf`
  - `https://www.irs.gov/pub/irs-prior/i990--2019.pdf`
- official IRS MeF schema/documentation pages as needed to establish exact 2019 XML concept mappings.

N01 may download the frozen 2019 XML ZIP payloads. It may not download the Automatic Revocation ZIP body.

## Frozen substantive concepts / 고정 substantive concepts

The primary exposure is derived only from Form 990 Part I Summary, lines 3 and 4:

- number of voting members of the governing body;
- number of independent voting members of the governing body.

Historical matching/balance may additionally use these Form 990 concepts from the same selected return:

- current-year total revenue;
- current-year total expenses;
- end-of-year total assets;
- end-of-year net assets or fund balances;
- U.S. state from the return header;
- tax-period end year;
- 501(c)(3) status.

A concept is usable only when the official 2019 IRS form/schema lineage establishes one deterministic XML mapping. Ambiguous semantic aliases, free-text inference, names, addresses beyond exact state code, geocoding, fuzzy matching, manual repair, or third-party normalized copies are prohibited.

## Hard outcome/tautology firewall / outcome·순환성 방화벽

N01 must not open or query any Automatic Revocation data row. The frozen bulk endpoint may receive only body-free metadata access if required for continuity checking:

`https://apps.irs.gov/pub/epostcard/data-download-revocation.zip`

Required persisted values:

- `future_outcome_rows_opened: 0`
- `automatic_revocation_entity_body_bytes_consumed: 0`
- `future_outcome_membership_opened: false`
- `missed_filing_or_nonfiling_exposure_constructed: false`
- `final_return_or_termination_indicator_used_as_exposure: false`
- `name_address_fuzzy_geo_manual_identity_repair_used: false`
- `relationship_computed: false`
- `predictive_metric_computed: false`
- `causal_claim_made: false`
- `organization_ranking_made: false`
- `novelty_claim_made: false`

## Exact historical identity and baseline-return selection / 정확한 과거 식별·baseline 선택

The unit is one exact 9-digit EIN.

A candidate filing is historically eligible only if:

1. the 2019 index EIN normalizes by trim + optional display-hyphen removal to exactly nine digits;
2. the return is exact **Form 990**, excluding Form 990-EZ, 990-PF and 990-N;
3. tax period is source-parseable and ends in calendar year **2018 or 2019**;
4. the XML is exact-linked to the index through the documented filing/object locator without name/address repair;
5. the selected return identifies the filer as **501(c)(3)**;
6. a domestic U.S. state code is present directly in the return header;
7. `InitialReturnInd`, `FinalReturnInd`/termination, `AmendedReturnInd`, and `ApplicationPendingInd` are not true on the selected baseline return;
8. group-return-for-affiliates status is not true;
9. voting governing-body members is an integer **>= 3**;
10. independent voting members is an integer in **[0, voting_members]**;
11. total revenue is numeric and **>= 0**;
12. total expenses is numeric and **> 0**;
13. end-of-year total assets is numeric and **>= 0**;
14. end-of-year net assets/fund balances is numeric;
15. no filing-gap, missed-filing, 990-N, future-event, name/address repair, or manual classification variable contributes to eligibility.

For each EIN, among eligible non-amended candidate filings choose the filing with the numerically latest tax period. If more than one distinct Object ID remains for that same maximum tax period, the EIN is excluded fail-closed. No return is selected using any outcome information.

## Frozen exposure / 고정 exposure

For each historically eligible EIN:

`governance_independence_ratio = independent_voting_members / voting_members`

Sort all eligible organizations ascending by:

`(governance_independence_ratio, EIN)`

Let `k = floor(n / 4)`.

- `LOW_INDEPENDENCE` = first `k` organizations;
- `HIGH_INDEPENDENCE` = last `k` organizations;
- middle 50% is excluded.

Exposure separation requires:

`max(ratio in LOW_INDEPENDENCE) < min(ratio in HIGH_INDEPENDENCE)`

If the quartile boundary is tied such that this strict inequality fails, the design fails prospectively rather than changing cut points.

This exposure is governance structure, not a filing-compliance proxy.

## Frozen deterministic matching / 고정 결정론적 매칭

### Exact matching strata

Each selected baseline return is assigned to:

- exact U.S. state;
- exact tax-period end year: 2018 or 2019;
- board-size bin:
  - `B1 = 3–5`
  - `B2 = 6–9`
  - `B3 = 10–19`
  - `B4 = 20+`
- deterministic total-revenue decile computed on the full eligible cohort by sorting `(total_revenue, EIN)` and assigning ranks 1–10 as evenly as possible.

Match only within the identical four-part stratum.

### Pair construction

Match `LOW_INDEPENDENCE` to `HIGH_INDEPENDENCE` without replacement.

Process LOW organizations in ascending `(governance_independence_ratio, EIN)` order. For each LOW organization choose the unused HIGH organization in the same exact stratum by, in order:

1. minimum absolute difference in `log1p(total_assets_eoy)`;
2. minimum absolute difference in `log1p(total_expenses)`;
3. minimum absolute difference in `net_assets_eoy / max(total_assets_eoy, 1)`;
4. lexical EIN.

Each EIN may appear in at most one pair.

No outcome variable may be present in the N01 pair manifest.

## N01 PASS requirements / N01 PASS 요건

All requirements are frozen before Issue creation and before 2019 index/XML row access under N01:

1. parent canonical state is terminal `US_IRS_EO_F01_PASS__N01_DESIGN_AUTHORIZED` under `DEC-238`;
2. N01 executes only after its Issue is created and bound to this exact pre-Issue contract commit;
3. the frozen 2019 index and all nine frozen XML ZIP endpoints resolve from official IRS domains at zero incremental cost;
4. exact index-to-XML filing linkage is reproducible without name/address repair;
5. all frozen substantive concepts have deterministic official-IRS semantic mappings; no ambiguous concept is silently repaired;
6. at least **50,000** EINs satisfy the full historical baseline-return eligibility rules;
7. at least **10,000** organizations exist in each of LOW_INDEPENDENCE and HIGH_INDEPENDENCE before matching;
8. strict quartile exposure separation holds;
9. at least **3,000** deterministic matched pairs remain;
10. matched pairs span at least **30** U.S. states;
11. every pair is exact-matched on state, tax-period end year, board-size bin and revenue decile;
12. no EIN occurs in more than one pair;
13. absolute standardized mean difference is **<= 0.10** for `log1p(total_revenue)`;
14. absolute standardized mean difference is **<= 0.10** for `log1p(total_expenses)`;
15. absolute standardized mean difference is **<= 0.10** for `log1p(total_assets_eoy)`;
16. absolute standardized mean difference is **<= 0.10** for end-of-year net-assets/total-assets ratio;
17. canonical historical cohort and pair-manifest SHA-256 values are persisted with exact source ZIP/index fingerprints;
18. all outcome/tautology/firewall fields remain at their required zero/false values and incremental monetary cost is exactly **0 USD**.

### N01 PASS

`PASS_US_IRS_EO_N01_MATCHED_GOVERNANCE_INDEPENDENCE_DESIGN_IDENTIFIABLE`

### N01 HOLD

`HOLD_US_IRS_EO_N01_MATCHED_GOVERNANCE_INDEPENDENCE_DESIGN_NOT_IDENTIFIABLE`

A valid scientific HOLD is terminal for this exact design. The 2019 source year, Form-990-only cohort, 501(c)(3) restriction, baseline-return selection, governance exposure, quartile rule, exact strata, pair ordering, balance thresholds, minimum pair/state counts, and future event window may not be relaxed after observed N01 counts.

Network/download/parser/schema-implementation defects before a valid empirical N01 result may be corrected transparently only if no scientific criterion changes and all prior attempts remain immutable.

## Prospectively frozen future E01 adjudication / 향후 E01 사전고정

This section does **not** authorize Automatic Revocation row access. It freezes the event rule and primary analysis that a later E01 must use **only if N01 passes and a separate E01 contract/Issue is created**.

### Outcome snapshot and event window

- official source: IRS Automatic Revocation List bulk data;
- identity: exact normalized `TIN/EIN == baseline EIN` only;
- primary revocation-effective-date window: **2023-01-01 through 2025-12-31 inclusive**;
- 2026-effective events are excluded from the primary endpoint as an incomplete current calendar year;
- any baseline EIN with an automatic-revocation effective date **before 2023-01-01** is excluded from the primary E01 cohort as pre-existing event history;
- if multiple events occur in the primary window, use the earliest effective revocation date as the primary event;
- posting date is audit metadata and never substitutes for effective revocation date.

### Reinstatement rule

Automatic revocation remains a historical event even when exemption is later reinstated. Therefore a qualifying effective revocation in the frozen window remains `Y = 1`; a reinstatement date is recorded only as a secondary post-event descriptor and does not recode the event to zero.

### Primary paired endpoint

For frozen N01 pairs that survive the pre-existing-event exclusion:

- `Y_LOW = 1` iff LOW_INDEPENDENCE EIN has a qualifying automatic revocation effective date in 2023–2025, else 0;
- `Y_HIGH = 1` iff HIGH_INDEPENDENCE EIN has a qualifying event, else 0;
- `risk_LOW = mean(Y_LOW)`;
- `risk_HIGH = mean(Y_HIGH)`;
- `RD = risk_LOW - risk_HIGH`;
- `b = count(LOW=1, HIGH=0)`;
- `c = count(LOW=0, HIGH=1)`;
- exact two-sided McNemar/binomial test on `b+c` with `p=0.5`.

### Frozen E01 ascertainment gate

The primary paired analysis may proceed only if, after the pre-existing-event exclusion:

- at least **2,500** frozen N01 pairs remain;
- at least **50** total qualifying automatic-revocation events occur across retained pair members.

If either fails, E01 terminates as insufficient outcome support without changing the event window, exposure definition, or matching.

### Frozen E01 relationship gates

- `PASS_POSITIVE_MATERIAL_US_IRS_EO_E01_RELATIONSHIP` iff `RD >= +0.02`, exact two-sided `p < 0.05`, and `b > c`;
- `POSITIVE_BELOW_MATERIALITY_US_IRS_EO_E01_RELATIONSHIP` iff `0 < RD < +0.02`, exact two-sided `p < 0.05`, and `b > c`;
- `NO_PREREGISTERED_POSITIVE_US_IRS_EO_E01_RELATIONSHIP` otherwise.

The later analysis is observational and noncausal. A negative estimate must not be reframed as a protective-governance causal claim. No result may be used as an organization risk score, compliance recommendation, donor targeting tool, eligibility decision, or novelty claim without a separate evidence stage.

## Non-claims / 비주장

N01 does not claim that board independence prevents filing failure, that lower independence causes automatic revocation, that governance ratios predict current exempt status, or that this relationship is novel. R39 already prohibits presenting generic nonprofit financial vulnerability -> failure as novel; this descendant remains bounded to an exact-EIN, direct-event, anti-tautology public-data design.

## Cost boundary / 비용 경계

Incremental monetary cost must remain **0 USD**. Any paid source/API/runner requirement needs explicit user approval before execution.
