---
id: AMBENCH-F38
type: prior-art-novelty-separation-gate
state: PREREGISTERED_ACTIVE
created: 2026-08-23
source_of_truth: github
incremental_monetary_cost_usd: 0
---

# AMBENCH-F38 — Multi-Actuator History-Control Prior-Art / Novelty Separation Gate
# AMBENCH-F38 — Multi-Actuator History-Control 선행기술 / Novelty Separation Gate

## Purpose / 목적

Test whether `HYP-F37-01` contains any bounded research gap beyond already-known residual-heat/history-aware control, without making a legal patentability determination.

Candidate combination under audit:

`recent scan events → shared history/thermal state → coordinated actuator policy {laser power, turnaround/skywriting timing, local scan order/path} → melt-pool stability objective`

## Frozen decomposition / 고정 분해

Search and classify these elements separately before judging the combination:

A. recent-scan/residual-heat/thermal-history state estimation;
B. history/temperature-informed laser-power modulation;
C. thermal-history-informed scan path/order optimization;
D. turnaround/skywriting/inter-track timing as an adaptive thermal-control variable;
E. joint or coordinated control of two or more of `{power, timing, path/order}` from a shared thermal/history state;
F. explicit three-actuator coordination of `{power + timing + path/order}` from one state estimator.

## Source hierarchy / source 우선순위

Prefer:
1. patent publications / Google Patents / Espacenet-equivalent public patent records;
2. NIST and peer-reviewed primary publications;
3. university/institutional papers with exact technical disclosure;
4. reviews only for recall expansion, not novelty conclusions.

Marketing pages and unsourced summaries cannot establish prior art.

## Frozen search families / 고정 검색군

At minimum search combinations of:
- additive manufacturing / LPBF / powder bed fusion;
- residual heat / thermal history / heat accumulation / preheat state;
- laser power control / feedforward control;
- scan path / scan order / hatch sequence;
- turnaround / skywriting / inter-track delay / dwell time;
- coordinated / joint / multi-variable / multi-parameter control.

## Gates / 판정

### `NOVELTY_REJECTED_F38`
Authoritative pre-existing source explicitly discloses the material F37 combination, including a shared recent-history/thermal state coordinating power, timing and path/order, or an equivalent architecture such that the hypothesis is not meaningfully distinct at research-concept level.

### `NOVELTY_PARTIAL_GAP_F38`
Core components and one/two-actuator combinations are known, but the bounded search does not identify an authoritative pre-existing disclosure of the exact shared-state three-actuator coordination. This means **research gap candidate only**, not legal novelty or patentability.

### `NOVELTY_SEARCH_INCONCLUSIVE_F38`
Search coverage, terminology, inaccessible patent families or semantic ambiguity is too large to distinguish the combination reliably.

### `HOLD_F38_SOURCE_CONFLICT`
Material source identity/date/technical-content conflict prevents classification.

## Mandatory interpretation / 필수 해석

Even `NOVELTY_PARTIAL_GAP_F38` must remain:
`LEGAL_NOVELTY_UNVERIFIED / PATENTABILITY_UNVERIFIED / OBVIOUSNESS_UNVERIFIED`.

No patent filing, freedom-to-operate, commercialization exclusivity or legal advice claim is authorized by F38.

## Cost / capability / 비용

Web/public patent/publication research only; incremental monetary cost `0 USD`. No paid patent database/API, no cloud/GPU, no new Skill/MCP/Plugin promotion.
