---
id: CA-GRAIN-E02-DATE-SEMANTICS-AUDIT
type: technical-source-semantics-audit
issue: 110
initial_effect_run: 34689155367
initial_gate: HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL
disposition: INVALIDATE_INITIAL_GATE_PENDING_DATE_CORRECTED_RERUN
relationship_computed_in_initial_run: false
frozen_contract_changed: false
incremental_monetary_cost_usd: 0
---

# CA-GRAIN-E02 GSW Date-Semantics Audit / GSW 날짜 의미 감사

The first authorized E02 execution Run `34689155367` stopped before model fitting at `HOLD_CA_GRAIN_E02_INSUFFICIENT_PANEL` because nine normalized weeks appeared to contain duplicate copies of all 60 frozen grain × region components.

That HOLD is **not accepted as the scientific E02 gate**. A value-blind technical audit found that the runner's generic slash-date parser tried `%m/%d/%Y` before `%d/%m/%Y`, while the Canadian Grain Commission GSW CSV uses day/month/year slash strings.

## Official-source disambiguation

The Canadian Grain Commission historical GSW archive publishes the authoritative week-ending calendar in ISO form. Examples from the frozen 2024-25 crop year include:

- Week 43 → `2025-06-01`, corresponding to CSV raw date `01/06/2025`;
- Week 22 → `2025-01-05`, corresponding to CSV raw date `05/01/2025`;
- Week 01 → `2024-08-11`.

Official archive: `https://www.grainscanada.gc.ca/en/grain-research/statistics/grain-statistics-weekly/archived.html`

Therefore GSW slash dates must be parsed as **`DD/MM/YYYY`**, not `MM/DD/YYYY`. The apparent all-component duplicate weeks were parser-created normalized-key collisions, not evidence of duplicate source components.

## Governance disposition

This is a technical source-date correction discovered before Issue #110 closure. It does **not** change any frozen E02 scientific choice: source files, 15 grains, four regions, `Primary / Deliveries / Current Week`, CN/CPKC outcome, one-week lag, first differences, minimum N, model, HAC lag, materiality threshold and gate all remain unchanged.

A corrected runner may therefore repeat E02 using source-specific GSW `DD/MM/YYYY` parsing. The first Run `34689155367` and its emitted HOLD are invalid technical-run artifacts and must not be used as scientific evidence.

The same parser defect also explains why earlier CA-GRAIN-F01 / E01 structural week counts were understated. Their substantive gates must be checked for stability and corrected by durable erratum if necessary; historical files are not silently rewritten.

No additional monetary cost. **0 USD**.
