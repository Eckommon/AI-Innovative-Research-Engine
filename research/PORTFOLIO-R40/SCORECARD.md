---
id: PORTFOLIO-R40-SCORECARD
type: immutable-stage0-scorecard
created: 2026-09-18
issue: 165
contract_commit: 22ff4cc6045bb895e5e4fe45dccca42bfc25867f
revalidation_commit: 1700a3877e540b68ebec1e85f8624fbe0a02727d
candidate_future_event_membership_used_for_scoring: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R40 immutable scorecard / 불변 평가표

Exactly one scorecard under the frozen nine-dimension `/45` rubric. Scores use only source structure, internal history, bounded agency/literature overlap, and next-gate falsifiability. No candidate-specific future-event membership, exposure→outcome relationship, event count, effect, prediction or ranking signal was used.

| Candidate | Bottleneck | Cross-data | Outcome | Independent units | Practical | $0 operability | Exact join | Next-gate info | Low overlap | Total /45 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `US-FCC-ULS-001` | 4 | 3 | 5 | 5 | 4 | 5 | 5 | 5 | 3 | **39** | **SELECT_F01** |
| `US-FMCSA-CARRIER-001` | 5 | 4 | 5 | 5 | 5 | 5 | 5 | 3 | 1 | **38** | HOLD_TRIGGER_OVERLAP_AND_HISTORY_RISK |
| `US-SEC-ISSUER-001` | 4 | 4 | 3 | 5 | 4 | 5 | 5 | 5 | 1 | **36** | HOLD_HETEROGENEOUS_FORM25_AND_MATURE_LITERATURE |
| `US-NCES-SCHOOL-001` | 4 | 2 | 5 | 5 | 5 | 5 | 5 | 4 | 1 | **36** | HOLD_SAME_SYSTEM_AND_MATURE_CLOSURE_FRAMEWORK |

No tie-break is required for the selected candidate.

## Selection rationale / 선정 근거

`US-FCC-ULS-001` is selected because it combines:

- an FCC-assigned unique **9-digit system identifier** explicitly designed to distinguish current versus expired/cancelled/terminated license records even when a call sign is reassigned;
- public machine-readable complete database files plus daily transaction files;
- direct later license-action/status semantics;
- very large license/application universe potential without name/address reconciliation;
- a cheap outcome-blind F01 that can reject the branch on identity lineage, service-family comparability, action/date semantics, historical transaction support or cardinality **before** any future-event cohort is opened.

The score deliberately limits cross-data credit to **3/5** because exposure and outcome remain primarily inside ULS. Low-overlap credit is only **3/5**, not a novelty finding.

## Why FMCSA is not selected / FMCSA 비선정

`US-FMCSA-CARRIER-001` has excellent USDOT identity and a direct OOS event, but the New Entrant program already makes safety audits, roadside safety information and corrective-action failures central to OOS/revocation. This sharply narrows permissible non-tautological exposure and creates substantial agency-framework overlap. Reproducible historical census/fleet snapshot lineage is also less immediately established than FCC’s documented complete/daily transaction architecture.

## Why SEC is not selected / SEC 비선정

`US-SEC-ISSUER-001` has excellent CIK/API infrastructure, but raw Form 25-NSE is not a single economic-failure state: it covers heterogeneous listing/registration removals including mature/redeemed/retired securities and other transitions. Financial-distress/deregistration/delisting research is mature. A later branch could only proceed with substantial prospective event adjudication and limited novelty expectations.

## Why NCES is not selected / NCES 비선정

`US-NCES-SCHOOL-001` has clean School-ID and closure-status semantics, but historical structure and closure are both within annual CCD, and enrollment/closure relationships are already directly studied. It therefore has lower cross-data information gain and lower low-overlap value.

## Boundary / 경계

This scorecard authorizes only a separate outcome-blind `US-FCC-ULS-F01` structural contract. It does not authorize opening a future cancelled/terminated cohort, computing a termination relationship, choosing exposure from observed event membership, ranking licensees, making regulatory recommendations, or asserting novelty.

Cost: **0 USD**.
