# Governance

## 1. Purpose

AI-Innovative-Research-Engine exists to discover potentially valuable innovations from public/research data by combining datasets, generating falsifiable hypotheses, testing them, and preserving the resulting evidence trail.

## 2. Repository Authority

GitHub is the persistent system of record for:

- project scope and architecture;
- research methodology;
- source registries;
- dataset evaluations;
- hypothesis and experiment records;
- decisions and status;
- reproducible code and outputs where practical.

Chat sessions are working environments, not the final source of truth.

## 3. Core Principles

1. **Evidence before narrative** — attractive explanations do not outrank data.
2. **Hypothesis is not conclusion** — every untested claim remains explicitly provisional.
3. **Reproducibility** — transformations, joins, assumptions, and evaluation criteria should be recorded.
4. **Negative results are assets** — rejected and inconclusive hypotheses remain in the research ledger.
5. **Source provenance** — official or primary sources are preferred and source URLs/metadata must be retained.
6. **Join discipline** — dataset combinations require documented join keys, temporal alignment, spatial alignment, and semantic compatibility.
7. **No forced innovation** — if evidence does not support novelty or usefulness, the correct result is HOLD, REJECTED, or INCONCLUSIVE.
8. **Progressive scaling** — prove the method on high-quality cases before broad harvesting.

## 4. Research Object States

Research objects may use the following lifecycle states:

- `DISCOVERED`
- `SCREENING`
- `CANDIDATE`
- `FEASIBILITY_TEST`
- `EXPERIMENT`
- `VALIDATED`
- `REJECTED`
- `INCONCLUSIVE`
- `HOLD`
- `ARCHIVED`

## 5. Evidence Classes

- `OBSERVED` — directly supported by source data or official documentation.
- `DERIVED` — computed from observed evidence with a documented method.
- `HYPOTHESIZED` — a proposed relationship or innovation claim awaiting validation.
- `VALIDATED` — passed defined experiment criteria.
- `REJECTED` — failed defined criteria.
- `INCONCLUSIVE` — evidence is insufficient or ambiguous.

## 6. Decision Rule

No hypothesis is promoted to a project claim unless:

- source provenance is recorded;
- data access is confirmed;
- key variables are identifiable;
- feasibility of joining or modeling is demonstrated;
- validation criteria are defined before final evaluation;
- observed/derived/hypothesized statements are clearly separated.

## 7. Initial Scope

The initial benchmark is NIST AM Bench. Expansion follows the staged geographic program documented in the README and source registry.

## 8. Change Control

Material changes to mission, methodology, scoring, evidence classes, or research lifecycle should be committed with a descriptive message and reflected in `STATUS.md` when they alter active work.
