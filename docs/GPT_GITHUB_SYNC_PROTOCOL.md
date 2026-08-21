# GPT ↔ GitHub Sync Protocol

## Purpose

This protocol defines how GPT-assisted work stays synchronized with `Eckommon/AI-Innovative-Research-Engine`.

GitHub is the persistent project record. GPT sessions are analytical workspaces that must read from and write back to that record when material project work occurs and repository access is available.

## A. Session Start — READ BEFORE REASONING

For project-related work, GPT should first inspect the repository rather than rely only on chat memory.

Minimum read set:

1. `README.md`
2. `STATUS.md`
3. relevant files under `docs/`
4. relevant source/dataset/project entries under `registry/` or future research directories
5. recent commits/issues when they may affect the requested task

If current chat instructions conflict with repository state, the conflict must be surfaced and resolved through an explicit change rather than silently assumed.

## B. During Work — CLASSIFY CLAIMS

Material claims should be tagged conceptually as:

- `OBSERVED`
- `DERIVED`
- `HYPOTHESIZED`
- `VALIDATED`
- `REJECTED`
- `INCONCLUSIVE`

GPT must not present a hypothesis as a validated project result.

## C. Before Repository Write

Before changing a file:

1. fetch the current file/version;
2. preserve existing valid content unless replacement is intentional;
3. incorporate new evidence and decisions;
4. use a descriptive commit message;
5. avoid duplicate or contradictory registries.

For new files, choose paths consistent with the repository taxonomy.

## D. Session End — WRITE MATERIAL STATE

A session should write back when it materially changes one or more of:

- research direction;
- methodology;
- source inventory;
- dataset candidate assessment;
- scoring;
- hypothesis;
- feasibility findings;
- experiment results;
- project status;
- next action.

At minimum, significant research progress should update `STATUS.md` and the relevant research artifact.

## E. Recommended Repository Taxonomy

```text
README.md
STATUS.md

docs/
  GOVERNANCE.md
  METHODOLOGY.md
  GPT_GITHUB_SYNC_PROTOCOL.md

registry/
  GLOBAL_PUBLIC_DATA_SOURCE_REGISTRY.md
  INNOVATION_POTENTIAL_SCORE.md

research/
  <research-id>/
    README.md
    SOURCES.md
    DATASET_PROFILE.md
    HYPOTHESES.md
    EXPERIMENT.md
    RESULTS.md

src/                  # future automation/analysis code
tests/                # future reproducibility tests
data/README.md         # rules for external/large data; avoid blindly committing large raw data
```

## F. Synchronization Semantics

`GitHub → GPT`

- Repository files define durable context.
- GPT should refresh them at the start of a materially related task.

`GPT → GitHub`

- Decisions, findings, and validated changes are persisted through commits/issues.
- Chat-only conclusions are treated as provisional until recorded.

This means synchronization is **workflow synchronization**, not a claim that every ChatGPT conversation is automatically mirrored to GitHub.

## G. Status Discipline

`STATUS.md` should contain:

- baseline/version;
- active research wave;
- completed work;
- active work;
- blocked/hold items;
- next actions;
- latest relevant commit(s), when useful.

## H. Safety Against Drift

When repository and chat appear inconsistent:

1. inspect the latest repository state;
2. identify the divergence;
3. prefer explicit recorded decisions over unstored assumptions;
4. update the repository if the user intentionally changes direction.

## I. Commit Message Convention

Suggested patterns:

- `docs: refine innovation discovery methodology`
- `registry: add Korea public data sources`
- `research: add NIST AM Bench dataset profile`
- `experiment: record feasibility test results`
- `status: advance Wave 1 source discovery`

## J. Human/GPT Roles

GPT may autonomously analyze, compare, score, generate hypotheses, critique results, and prepare repository updates within user authorization. The repository should preserve enough evidence that another GPT session—or a human reviewer—can reconstruct why a research decision was made.
