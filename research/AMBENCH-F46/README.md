---
id: AMBENCH-F46
type: source-ingress-resume-qualification-gate
created: 2026-09-03
status: PREREGISTERED
predecessor: AMBENCH-F45
source_dataset: mds2-2507
incremental_monetary_cost_usd: 0
capability_status: SHARED-INTERNAL-CANDIDATE
---

# AMBENCH-F46 — Persistent Partial-File Resume Ingress Qualification
# AMBENCH-F46 — Persistent Partial-File Resume Ingress 자격검증

## Purpose / 목적

F44 whole-object fetching sometimes received multi-megabyte prefixes before failure, while F45's frozen explicit 1 MiB Range request never completed. F46 tests a distinct source-only transfer strategy: retain the bytes successfully written by a failed whole-object transfer and explicitly resume the same output file on the next bounded attempt.

No simulator is built or run. No P01 numerical contents, MP_Stats, representation equivalence, path-order performance or physical measurement outcome is analyzed.

## Frozen source identity / 고정 source identity

Official NIST NERDm must reproduce:
- dataset `mds2-2507`;
- version `1.0.1`;
- exactly one component `RHF_Command.zip`;
- size `18,079,576` bytes;
- SHA-256 `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
- exact NERDm `downloadURL` only.

Successful final reconstruction must open as ZIP and contain exactly one member matching `(?:^|/)RHF_P01_layer0001.csv`. Numerical CSV rows are not emitted or interpreted.

## Frozen transfer protocol / 고정 transfer protocol

Use the standard public GitHub Ubuntu runner and its installed curl, recording `curl --version` in the result.

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

The outer loop is chosen prospectively because curl documentation specifies that `--continue-at -` determines the resume offset from the output file. Curl built-in retry is deliberately excluded because curl documentation warns that failed output data may be reset before a retry; F46 explicitly tests persistence across separate invocations.

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

The exact final size/SHA is authoritative regardless of the last curl return code: if the complete expected byte count and checksum were written before a connection-close error, the final object is considered source-complete only after ZIP/P01 validation also passes.

## Frozen gates / 고정 gate

### `PASS_F46_PERSISTENT_RESUME_INGRESS`
Exact size/SHA and ZIP/P01 identity pass after <=5 frozen persistent-file attempts.

### `REJECT_F46_RESUME_PROTOCOL_OR_INTEGRITY`
Deterministic incompatibility/integrity failure occurs: non-monotonic/truncated partial state, file size above expected, exact-size SHA mismatch, invalid ZIP/P01 identity, or curl range error (`33`) on an actual non-zero resume attempt.

### `HOLD_F46_SOURCE_OR_NETWORK`
NERDm identity cannot be verified, the 12-minute workflow cap is reached, or five frozen attempts end with an incomplete file without deterministic resume-protocol evidence.

## Claim boundary / 주장 경계

A PASS qualifies only this source-ingress method for the exact NIST component on the observed standard runner. It does not establish F44 representation equivalence or any path-order/performance/physical claim.

A PASS may support a separately authorized minimal P01 fixture or newly numbered representation-equivalence experiment. F44/F45 remain closed historical HOLDs.

## Cost / 비용

Incremental monetary cost remains `0 USD`. Billable transfer/storage/compute requires explicit prior user approval.
