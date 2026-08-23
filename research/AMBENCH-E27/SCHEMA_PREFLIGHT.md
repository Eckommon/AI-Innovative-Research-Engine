---
id: AMBENCH-E27-SCHEMA-PREFLIGHT
type: schema-preflight-incident-state
created: 2026-08-23
updated: 2026-08-23
source_of_truth: github
raw_artifacts_committed: false
---

# AMBENCH-E27 Schema Preflight — Incident/Redaction State / E27 schema 사전검증 — 사고·redaction 상태

## Current state / 현재 상태

**`PRELIMINARY_HOLD_PENDING_CORRECT_ENCODING_SCHEMA`**

The current branch tip intentionally contains **no numerical outcome cells** from the malformed parse. / 현재 branch tip에는 잘못된 parse에서 노출된 numerical outcome cell을 의도적으로 보존하지 않는다.

## Verified source facts before parser failure / parser 실패 전 검증된 source 사실
- source: NIST `mds2-4103` v1.0.0;
- frozen primary component: `Cross_Sections/Tracks_Results/overlap_depths_avg.csv`;
- NERDm size: `30012` bytes;
- NERDm SHA-256: `e56c702fba658efd87e99e305ac61d7679d40a855cb331941679d8cdfb66373f`;
- local size match: `YES`;
- local SHA-256 match: `YES`.

## Incident / 사고
1. First preflight attempted UTF-8 decoding and stopped with `UnicodeDecodeError` before numerical analysis.
2. Amendment 01 permitted deterministic encoding repair.
3. The second parser incorrectly accepted BOM-less bytes as UTF-16 merely because decoding did not raise an exception. This converted ordinary byte sequences into a malformed one-line pseudo-header.
4. That malformed pseudo-header unintentionally included numerical cells and was committed by the Actions workflow.
5. No six-plate P1 mapping, group comparison, effect statistic, permutation test, ranking, endpoint switching, or model was performed from those values.

## Exposure state / 사전노출 상태

**`NEW_E27_NUMERICAL_OUTCOME_BLIND = VIOLATED_SCHEMA_PREFLIGHT_GIBBERISH_EMISSION`**

This state is permanent for E27 and descendants. The E27 scientific design, endpoint, direction, statistic and frozen gates were committed before the incident and must not be modified in response to the emitted values.

## History boundary / Git history 경계
The erroneous bot commit remains in Git history. Rewriting public Git history would be destructive and is **not authorized**. The current tip is redacted instead, and the incident is preserved transparently in `AMENDMENT-02.md`.

## Next / 다음
Run a corrected schema-only preflight that:
- uses UTF-16 only when a UTF-16 BOM is actually present (or an explicitly frozen strong byte-pattern rule, if ever separately justified);
- otherwise uses ASCII-compatible decoding (`utf-8-sig` then `cp1252`/`latin-1`);
- emits only bounded header names and identifier counts, never malformed full lines or outcome cells;
- applies the frozen E27 source/schema gate without endpoint/source substitution.

Incremental monetary cost: `0 USD`.