# AI-Innovative-Research-Engine

> Public Data → Data Relationship → Hypothesis → Experiment → Innovation

AI-Innovative-Research-Engine is a research repository for discovering, testing, and recording innovation opportunities from public and research datasets. The project began from the NIST AM Bench case and expands the same reasoning pattern across agencies, countries, and regions.

## Mission

The goal is not to accumulate open-data links. The engine is designed to identify public datasets that can be connected, generate falsifiable hypotheses from those relationships, test feasibility with real data, and preserve both successful and failed experiments as reusable research assets.

Core question:

> Which combinations of public datasets can produce a new, testable, and practically useful insight?

## Research Model

```text
Source Discovery
  ↓
Metadata Harvesting
  ↓
Dataset Triage
  ↓
Relationship Discovery
  ↓
Hypothesis Generation
  ↓
Feasibility Test
  ↓
Controlled Experiment
  ↓
Innovation Registry
```

## Research Levels

| Level | Scope | Example |
|---|---|---|
| L1 | Dataset Innovation | NIST AM Bench → manufacturing quality prediction |
| L2 | Cross-Dataset | NIST manufacturing + robotics + materials |
| L3 | Cross-Agency | NIST + DOE + EPA + NOAA |
| L4 | Cross-National | US + Korea + EU + Japan |
| L5 | Machine-Assisted Innovation Discovery | automated discovery of promising dataset combinations and testable hypotheses |

## Initial Geographic Waves

- **Wave 0** — NIST AM Bench as the methodological proof-of-concept and benchmark.
- **Wave 1** — United States, Korea, European Union.
- **Wave 2** — Japan, United Kingdom, Singapore.
- **Wave 3** — Canada, Australia, OECD, World Bank, and additional regions.

## Core Artifacts

- [`STATUS.md`](STATUS.md) — current project state and next actions.
- [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md) — official research pipeline and evidence rules.
- [`docs/GOVERNANCE.md`](docs/GOVERNANCE.md) — project scope, principles, and decision rules.
- [`docs/GPT_GITHUB_SYNC_PROTOCOL.md`](docs/GPT_GITHUB_SYNC_PROTOCOL.md) — GitHub-as-record-of-truth workflow for GPT-assisted research.
- [`registry/GLOBAL_PUBLIC_DATA_SOURCE_REGISTRY.md`](registry/GLOBAL_PUBLIC_DATA_SOURCE_REGISTRY.md) — initial source registry by country/region.
- [`registry/INNOVATION_POTENTIAL_SCORE.md`](registry/INNOVATION_POTENTIAL_SCORE.md) — dataset/project triage rubric.

## Repository Role

This repository is the **official persistent research record** for the project. ChatGPT/GPT may be used as an analysis, research, synthesis, hypothesis-generation, and review layer, but durable project state should be reflected in GitHub.

A GPT-assisted work session should therefore begin by reading the repository state and should end by recording material changes, decisions, evidence, and next actions back into the repository whenever write access is available.

## Evidence Principle

The engine separates:

- **Observed** — directly supported by a dataset, official documentation, or reproducible computation.
- **Derived** — calculated or transformed from observed evidence.
- **Hypothesized** — a testable claim not yet validated.
- **Validated** — tested against predefined criteria.
- **Rejected / Inconclusive** — failed or insufficiently supported hypotheses retained for learning.

This separation is mandatory because the project is intended to discover innovation without confusing novelty with evidence.

## Initial Focus Domains

Advanced manufacturing, energy and grid systems, data centers, supply chains, critical minerals, logistics, urban systems, disaster risk, finance/industry stress, and labor/technology transition.

## Current Status

**Baseline:** v0.1 — repository and research governance initialization.

See [`STATUS.md`](STATUS.md) for the live project state.
