---
id: PORTFOLIO-R48-REVALIDATION
type: bounded-source-lineage-overlap-revalidation
created: 2026-09-30
issue: 183
contract: 5a7d40c57ef1b8401e9761e821306b36fc857691
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R48 — source, longitudinal lineage and overlap revalidation

## Outcome firewall / outcome 방화벽

No candidate-specific future event membership, effect, prediction, ranking or causal result was opened. Revalidation used official source/documentation pages, canonical project history and bounded public literature/framework context only.

## 1. US-EIA-GEN-001

Official EIA evidence establishes genuine longitudinal files rather than a replace-in-place snapshot.

- Form EIA-860M is published as identifiable monthly files; the current page lists individual months for 2026 and earlier years.
- EIA documents monthly generator inventory data beginning in 2015.
- From March 2017 onward, each 860M file contains a comprehensive retired-generator list for generators retired since 2002.
- EIA-860 annual detailed generator files are published by year with history back to 1990.
- EIA-923 publishes monthly and annual generation/fuel data and supports generator/plant performance context.
- EIA Electric Power Monthly retirement tables expose official Plant ID + Generator ID and retirement month/year.

Longitudinal qualification: **strong**.

Identity prospect: source-native exact **Plant ID + Generator ID**. EIA states Plant ID is an official unique identification number, while Generator ID is assigned by plant owners/operators and is interpreted within plant.

Event prospect: source-native generator retirement.

Critical anti-tautology:
- planned retirement date/month/year;
- planned retirement status;
- explicit announced-retirement fields

must remain prohibited exposures.

Overlap:
Generator retirement and power-sector transition are established research areas, so novelty credit is conservative. The candidate's value is high-quality prospective unit/event lineage and the ability to combine EIA-860/860M structure with EIA-923 operating performance without using planned-retirement signals.

## 2. US-SEC-IA-001

SEC/IAPD publishes historical Form ADV Part 1 filing data for SEC-registered advisers from January 2001 through the most recent quarter. Historical Form ADV-W data are separately provided, and SEC monthly/quarterly adviser information reports are available over long periods.

Longitudinal qualification: **strong**.

Identity prospect: Organization CRD number, subject to exact ADV↔ADV-W confirmation in F01.

Event semantics:
Form ADV-W distinguishes **full withdrawal** from **partial withdrawal**. SEC guidance also makes clear that withdrawal can reflect switching between SEC and state registration; therefore a withdrawal cannot be labeled business failure without independent evidence.

Critical anti-tautology:
- filed ADV-W;
- direct registration-withdrawal/ineligibility fields;
- cessation date;
- stated withdrawal intention

must remain prohibited exposures.

Overlap:
Investment-adviser business structure and registration transitions are meaningful but the event is administratively heterogeneous. This reduces direct-outcome value compared with a physical retirement event.

## 3. US-EPA-RCRA-001

EPA ECHO's RCRAInfo national download contains separate facility, enforcement, evaluation, violation, NAICS and violation/SNC-history CSV files.

Official documentation states:
- `ID_NUMBER` is a unique RCRA site identification number assigned by a state or EPA region;
- `ID_NUMBER + ACTIVITY_LOCATION` are cross-table key fields;
- enforcement actions have source-native identifiers, type and `ENFORCEMENT_ACTION_DATE`;
- evaluations have dates and finding fields;
- violation records have determination/compliance dates;
- VIO/SNC history contains monthly `YRMONTH` values.

Longitudinal qualification: **strong through dated event history**, even though the downloadable package itself is refreshed weekly.

Event prospect: a new formal source-native enforcement action in a future refresh.

Critical anti-tautology:
prior violation/SNC, inspections/evaluations, enforcement, penalty and unresolved-compliance indicators may not be descendant predictive exposures. Inspection-selection bias is a mandatory design concern.

Overlap:
Environmental enforcement/compliance is an established research domain, and this candidate follows immediately after an EPA SDWIS branch. Institutional-family overlap therefore receives a conservative penalty despite strong source structure.

## 4. US-FMCSA-CAR-001

FMCSA's Open Data Program states that SMS input files are monthly snapshots of motor-carrier census, inspection, violation and crash data, and that the SMS process runs monthly. Carrier history pages expose multiple prior monthly runs.

Identity prospect: exact USDOT Number.

Event prospect: new reportable crash.

Longitudinal qualification: **moderate / not yet fully established for reproducible bulk history**. The reviewed official material proves monthly snapshots and per-carrier history, but does not yet establish an easily reproducible national bulk archive with the same strength as EIA's explicit historical monthly-file matrix.

Critical anti-tautology:
prior crash counts, BASIC/Crash Indicator, inspection/violation history, safety intervention and enforcement fields are prohibited predictive exposures.

Overlap:
FMCSA explicitly publishes crash-prediction research and carrier crash-risk methodology. The research space is therefore highly mature; novelty/marginal information value is heavily discounted.

## Canonical internal-history check / 내부 이력 확인

Repository search found no prior branch using the exact candidate IDs:
- `US-EIA-GEN-001`
- `US-SEC-IA-001`
- `US-EPA-RCRA-001`
- `US-FMCSA-CAR-001`

Recent source-family history is nevertheless relevant:
- EPA receives an institutional-overlap penalty because SDWIS immediately preceded R48.
- Prior U.S. aviation, bridge, FDIC, IRS, MSHA and other branches do not constitute the same exact unit/event family.
- SDWIS negative evidence is applied methodologically: update cadence alone earns no lineage credit.

## Revalidation conclusion / 재검증 결론

All four candidates remain eligible for the single frozen scorecard.

**EIA has the strongest mission-adjusted next-gate structure**:
- explicit monthly historical files;
- exact plant/generator identity prospect;
- direct retirement event;
- annual cross-check lineage;
- EIA-923 independent operating-performance context;
- no need to reconstruct history from a replace-in-place latest snapshot.

SEC is the strongest alternative for long-term filing lineage but its withdrawal event is administratively heterogeneous. RCRA has excellent dated event structure but immediate EPA-family overlap and enforcement-selection bias. FMCSA has strong exact identity and practical value but the bulk historical-snapshot archive is less prospectively demonstrated and crash prediction is mature.

Incremental monetary cost: **0 USD**.
