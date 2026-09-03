---
id: AMBENCH-F45
type: source-ingress-qualification-gate
created: 2026-09-03
status: PREREGISTERED
predecessor: AMBENCH-F44
source_dataset: mds2-2507
incremental_monetary_cost_usd: 0
capability_status: SHARED-INTERNAL-CANDIDATE
---

# AMBENCH-F45 — Checksum-Preserving Resumable Source-Ingress Qualification
# AMBENCH-F45 — Checksum 보존 Resumable Source-Ingress 자격검증

## Purpose / 목적

F44 ended `HOLD_F44_RUNTIME_OR_INTEGRITY` before simulator execution because three bounded whole-object transfers of NIST `RHF_Command.zip` did not produce a complete archive. F45 isolates that infrastructure question from all scientific/performance questions.

F45 tests only whether the exact same checksum-frozen NIST component can be reconstructed on a standard public GitHub runner using a fixed HTTP byte-range protocol.

No simulator is built or run. No P01 measurement/performance outcome is read. No representation or path-order claim is tested.

## Frozen source identity / 고정 source identity

Authoritative NERDm metadata must reproduce:

- dataset: `mds2-2507`;
- version: `1.0.1`;
- component filepath: `RHF_Command.zip`;
- expected size: `18,079,576` bytes;
- expected SHA-256: `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`.

After reconstruction the ZIP central directory must open successfully and contain exactly one member matching `(?:^|/)RHF_P01_layer0001.csv`. F45 does not parse or emit CSV numerical contents.

## Frozen transfer protocol / 고정 전송 protocol

### Chunk geometry

- fixed chunk size: `1,048,576` bytes (`1 MiB`);
- sequential, non-overlapping ranges from byte `0` through byte `18,079,575` inclusive;
- expected range count: `18`;
- no concurrent range requests;
- no adaptive chunk-size change.

The 1 MiB boundary is frozen prospectively as a standard binary chunk size and is substantially smaller than both previously observed incomplete whole-object transfer prefixes. It is not selected using scientific outcomes.

### Per-range contract

For each range `[start,end]`:

- send HTTP header `Range: bytes=start-end` to the exact NERDm `downloadURL`;
- require HTTP status `206 Partial Content`;
- require exact `Content-Range: bytes start-end/18079576`;
- require response body length `end-start+1` exactly;
- maximum `3` attempts for that exact unchanged range;
- fixed read timeout `90 s` per attempt;
- fixed `3 s` delay between failed attempts;
- after a successful chunk, proceed to the next range;
- never restart previously verified chunks within the same run.

Maximum theoretical range requests: `18 x 3 = 54`.

No fallback to whole-object transfer, different chunk size, alternate mirror, GitHub artifact source, VPN/proxy, paid storage, or alternate dataset endpoint is allowed inside F45.

## Frozen reconstruction / 고정 재구성

Successful chunks are concatenated strictly by ascending byte offset.

PASS requires:

1. all 18 exact ranges acquired;
2. reconstructed byte count exactly `18,079,576`;
3. reconstructed SHA-256 exactly `c57a56cc9c906e4db134d7bfb8618b6678e80dd0318324de0b7baf1ce092a3f4`;
4. ZIP central directory opens without error;
5. exactly one P01 member matches the frozen member regex;
6. no unverified/missing/overlapping byte range.

Persist only transfer diagnostics, chunk ranges/body sizes/attempt counts, final size/SHA and ZIP-member identity. The reconstructed raw archive remains transient and is not committed or uploaded as an artifact.

## Frozen gates / 고정 gate

### `PASS_F45_CHECKSUM_PRESERVING_RANGE_INGRESS`
All HTTP range semantics and exact final size/SHA/ZIP identity checks pass.

### `REJECT_F45_RANGE_PROTOCOL_NOT_SUPPORTED`
A deterministic protocol-semantic failure is observed, such as server response `200` instead of `206`, malformed/mismatched `Content-Range`, or body length inconsistent with the requested range. No fallback is allowed.

### `HOLD_F45_SOURCE_OR_NETWORK`
NERDm source identity drifts, metadata cannot be verified, or one or more unchanged ranges exhaust the three bounded attempts because of transport/network errors before protocol semantics can be validated.

## Claim boundary / 주장 경계

A PASS establishes only that this exact NIST component can be checksum-preservingly reconstructed with the frozen range protocol on the observed standard public runner. It does not establish F44 representation equivalence, full-P01 runtime feasibility, path-order added value, physical NIST reproduction, scanner feasibility, production readiness, or novelty.

A PASS may support a separate decision to use the qualified ingress protocol in a newly numbered representation-equivalence experiment. It does not reopen or rewrite F44.

## Cost / 비용

Incremental monetary cost remains `0 USD`. Any billable transfer/storage/compute requires explicit prior user approval.
