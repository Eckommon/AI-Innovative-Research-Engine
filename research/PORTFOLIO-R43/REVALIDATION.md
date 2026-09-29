---
id: PORTFOLIO-R43-REVALIDATION
type: bounded-source-overlap-revalidation
created: 2026-09-29
issue: 172
contract: a52045f7526c0f601d40cba0387d92141f90e75d
candidate_outcomes_opened: false
incremental_monetary_cost_usd: 0
---

# PORTFOLIO-R43 — bounded source / overlap revalidation

## Outcome firewall / outcome 방화벽

No candidate-specific future event row, membership, effect, prediction, ranking or causal result was opened. Revalidation used official source/documentation pages, public schema descriptions and canonical repository history only.

## 1. CA-CORP-001

Corporations Canada currently provides open federal-corporation data, a JSON API and monthly transaction publications. The API identifies corporations by source-native corporation ID/Corporation Number and returns current legal status plus corporate structure. Monthly transactions separately publish dissolution events, including CBCA section-212 non-compliance dissolution.

Official search guidance distinguishes active, dissolved, inactive-amalgamated and inactive-discontinued legal states. Current corporation pages can explicitly state `Dissolved for non-compliance (s. 212)`.

The decisive F01 requirement is anti-tautology: historical overdue-filing indicators, intent-to-dissolve notices and dissolution-pending status must remain excluded from exposure variables because they mechanically precede the legal event.

Current source architecture is anonymous, zero-cost and highly deterministic. Corporate dissolution/failure is a mature topic, so novelty credit remains conservative.

## 2. UK-CHARITY-001

The Charity Commission currently provides a daily full-register extract in JSON and tab-delimited formats, including charity, annual-return history and event-history files. Current public data definitions include exact charity identity, `date_of_removal`, `reporting_status` and `removal_reason`; removal reasons can include cessation, no-longer-charitable status or transfer/merger.

Identity and source operability are strong. However this branch is conceptually adjacent to the project's prior IRS exempt-organization/revocation work, and charity removal is not equivalent to organizational failure. A future F01 would need to separate removal reason classes and prohibit submission-default or removal-proximate fields as exposure.

## 3. UK-EA-PERMIT-001

Environment Agency Public Registers provide searchable/downloadable permit data and an API without registration. The permit ontology includes status, effective date, surrender date, revocation date and cancellation date. Separate public compliance-assessment datasets provide historical permit-compliance structure.

Exact permit reference is a strong identity prospect and event semantics are direct. However dataset reuse can be governed by the Environment Agency Conditional Licence, requiring licence-compatibility verification, and the project has substantial prior EPA/RCRA compliance work. Overlap and reuse constraints therefore materially reduce portfolio value.

## 4. US-USDA-PACA-001

USDA AMS operates official PACA licensing, licence-status search and disciplinary/enforcement processes. The public ePACA licence search can expose licence and complaint information.

The unresolved structural risk is larger than for the other candidates: this revalidation did not establish an anonymous bulk historical snapshot, stable machine-readable licence identifier across historical exposure/event sources, or a bulk disciplinary-event table suitable for a prospective national design. Complaint information also creates substantial anti-tautology leakage risk.

## Canonical internal-history check / 내부 이력

No prior exact candidate IDs `CA-CORP-001`, `UK-CHARITY-001`, `UK-EA-PERMIT-001` or `US-USDA-PACA-001` existed before R43.

- Canada federal corporation unit/event family is new to the canonical project.
- UK charity receives strong conceptual overlap penalty for IRS-EO.
- UK EA permit receives strong environmental-compliance overlap penalty for EPA/RCRA/US-WW.
- PACA is a fresh regulator/source family but carries the largest unresolved source-operability risk.

## Revalidation conclusion / 결론

All four frozen candidates remain eligible for the one-time scorecard.

- Canada corporations: strongest exact identity, legal-event semantics, anonymous operability and next-gate falsifiability.
- UK charity: strong data and identity, but high nonprofit/removal overlap.
- UK EA: strong permit/event architecture, but environmental overlap and conditional-licence considerations.
- PACA: direct disciplinary event, but weak established bulk historical source lineage.

Incremental monetary cost: **0 USD**.
