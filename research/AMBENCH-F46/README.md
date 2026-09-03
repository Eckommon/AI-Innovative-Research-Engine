---
id: AMBENCH-F46
type: source-ingress-resume-qualification-gate
created: 2026-09-03
status: DORMANT__NOT_ACTIVE__REQUIRES_REAUTHORIZATION
predecessor: AMBENCH-F45
source_dataset: mds2-2507
incremental_monetary_cost_usd: 0
capability_status: SHARED-INTERNAL-CANDIDATE
superseded_execution_authority_by: DEC-093
---

# AMBENCH-F46 — Persistent Partial-File Resume Ingress Qualification
# AMBENCH-F46 — Persistent Partial-File Resume Ingress 자격검증

> **Current disposition / 현재 상태:** `DORMANT__NOT_ACTIVE__REQUIRES_REAUTHORIZATION`
>
> `DEC-093` supersedes the automatic execution authorization previously inherited from `DEC-092`. This document is preserved as a technical preregistration draft only. Do **not** create an Issue, workflow, download, or descendant from F46 unless a future `MISSION-ROI` review establishes mission-level necessity or the user explicitly prioritizes this branch.

## Purpose / 목적

F44 whole-object fetching sometimes received multi-megabyte prefixes before failure, while F45's frozen explicit 1 MiB Range request never completed. F46 was designed to test a distinct source-only transfer strategy: retain the bytes successfully written by a failed whole-object transfer and explicitly resume the same output file on the next bounded attempt.

Following the 2026-09-03 root research-process audit, this transport problem is classified as a **route dependency rather than a mission dependency**. Therefore the protocol below is retained for reproducibility but is not active research.

No simulator is built or run. No P01 numerical contents, MP_Stats, representation equivalence, path-order performance or physical measurement outcome is analyzed.

## Frozen source identity / 고정 source identity

If reauthorized in the future, official NIST NERDm must reproduce:
- dataset `mds2-2507`;
- version `1.0.1`;
- exactly one component `RHF_Command.zip`;
- size `18,079,576` bytes;
- SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
- exact NERDm `downloadURL` only.

Successful final reconstruction must open as ZIP and contain exactly one member matching `(?:^|/)RHF_P01_layer0001.csv`. Numerical CSV rows are not emitted or interpreted.

## Frozen transfer protocol / 고정 transfer protocol

If and only if separately reauthorized, use the standard public GitHub Ubuntu runner and its installed curl, recording `curl --version` in the result.

One persistent local file is used for all attempts.

For attempts `1..5`:

```text
timeout 120 curl \
  --fail \
  --location \
  --connect-timeout 30 \
  --continue-at - \
  --output <same persistent file> \
  <exact NERDm downloadURL>
```

Rules:
- maximum attempts: `5`;
- external hard cap per curl attempt: `120 s`;
- connect timeout: `30 s`;
- fixed `3 s` delay after an unsuccessful attempt if another attempt is allowed;
- no curl built-in `--retry`;
- no deletion/truncation of a non-empty partial file between attempts;
- `--continue-at -` must derive the next resume offset from the persistent output file;
- no adaptive timeout, attempt count, alternate curl flags, parallelism, pre-split ranges, alternate endpoint/mirror/proxy/VPN, or paid transfer/storage;
- workflow hard cap: `12 min`.

## Frozen per-attempt diagnostics / 고정 attempt 진단

Before and after each invocation persist only:
- attempt number;
- file size before;
- curl/timeout return code;
- file size after;
- byte increase;
- whether size was monotonic.

No raw archive bytes are persisted in GitHub.

## Frozen completion logic / 고정 완료 logic

After each invocation:

1. if file size decreases, deterministic resume-integrity failure;
2. if file size exceeds `18,079,576`, deterministic resume-integrity failure;
3. if file size equals `18,079,576`, immediately calculate SHA-256:
   - exact frozen SHA => validate ZIP/P01 identity and PASS;
   - mismatched SHA => deterministic integrity REJECT;
4. curl return code `33` (`CURLE_RANGE_ERROR`) when a non-zero partial file existed at invocation start => deterministic resume-protocol REJECT;
5. other non-zero codes with incomplete file are transport failures and may proceed to the next frozen attempt;
6. after attempt 5, incomplete file => HOLD.

## Frozen gates / 고정 gate

### `PASS_F46_PERSISTENT_RESUME_INGRESS`
Exact size/SHA and ZIP/P01 identity pass after <=5 frozen persistent-file attempts.

### `REJECT_F46_RESUME_PROTOCOL_OR_INTEGRITY`
Deterministic incompatibility/integrity failure occurs: non-monotonic/truncated partial state, file size above expected, exact-size SHA mismatch, invalid ZIP/P01 identity, or curl range error (`33`) on an actual non-zero resume attempt.

### `HOLD_F46_SOURCE_OR_NETWORK`
NERDm identity cannot be verified, the 12-minute workflow cap is reached, or five frozen attempts end with an incomplete file without deterministic resume-protocol evidence.

## Reauthorization gate / 재승인 게이트

Before any execution, a new decision must answer the `MEM-054 / DEC-093` Mission-ROI questions and explicitly explain why this route is more valuable than returning to a higher-value portfolio candidate.

## Cost / 비용

Incremental monetary cost remains `0 USD`. Billable transfer/storage/compute requires explicit prior user approval.
