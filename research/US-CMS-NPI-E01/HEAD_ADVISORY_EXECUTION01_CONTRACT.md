---
id: US-CMS-NPI-E01-HEAD-ADVISORY-ATTEMPT01
type: prospective-one-time-operational-contract
date: 2026-10-19
parent_issue: 203
base_commit: d9651b8f5aa8f9d42cc900ba525d27ac27269ad9
science_decision: DEC-318
status: FROZEN_BEFORE_ONE_TIME_PROBE
incremental_monetary_cost_usd: 0
---

# CMS hypothetical V2 first-week HEAD — one-time independent advisory / 1회 HEAD 운영 계약

**Track A authority / 승인:** Issue #203 stays open; 346,859 pairs, frozen 18 scientific gates, first-publication lineage gate and canonical CMS HTML listing watcher remain unchanged. Existing `HEAD_ADVISORY.md` and `tools/probe_us_cms_npi_e01_weekly_head.py` are the approved advisory semantics. The manual-only advisory workflow remains unmodified; this is a distinct **one-shot push-triggered operational receipt**, not automatic E01 execution.

## Fixed boundary / 사전고정 제한
1. Only after **2026-10-19T00:00:00Z**, issue **one** HTTP HEAD to exactly `https://download.cms.gov/nppes/NPPES_Data_Dissemination_101226_101826_Weekly_V2.zip`. Hypothetical filename is **not** official publication proof.
2. Use existing `tools.probe_us_cms_npi_e01_weekly_head` unchanged, no follow redirects, no GET, Range GET, ZIP read, provider IDs, historical archive substitution or query to a second URL. Eight existing offline safety tests must PASS before the network step.
3. Classify HTTP 200 only as `POSSIBLE_PUBLIC_OBJECT_METADATA_ONLY`, never first-publication; 403/404/405/3xx as `NOT_ESTABLISHED`, not absence. Transport errors become `HOLD_HEAD_TRANSPORT_UNVERIFIED`.
4. Before running require existing candidate/attempt absence, unchanged `DEC-318`, canonical active Issue #203 and secondary #244. This one-shot workflow is triggered only by its own newly merged YAML path on `main`; if immutable receipt exists it does **not** request the URL again.
5. Preserve one immutable JSON and bilingual MD under `research/US-CMS-NPI-E01/evidence/head-advisory-attempt-01.*`, including observed UTC, workflow run ID, status or transport error category, no scientific authorization, unmodified watcher, no ZIP/outcome rows. Never print a source outcome.
6. No Issue body edits, candidate, first-release authorization, E01 marker or attempt, no modification of existing scientific runner. Zero additional monetary cost; never use paid runner or service.
7. Distinguish transport publication headers from true CMS official listing and human source-lineage review. Even HTTP 200 is advisory and cannot override official 6-hour listing.

**Decision:** `ADVISORY_ONLY_NOT_E01_RELEASE` if valid HEAD response; otherwise `HOLD_HEAD_TRANSPORT_UNVERIFIED`. No E01 experiment.
