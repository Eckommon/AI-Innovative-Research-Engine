---
id: SOURCE-REGISTRY-S01-PERSIST-R01
type: preregistered-operational-capability
issue: 244
created: 2026-10-20
checkpoint: CHK-20261013-US-CMS-NPI-E01-ACTIVE
status: CONTRACT_BEFORE_LIVE_ADOPTION
money_cost_usd: 0
---

# PERSIST-R01 — evidence durability despite concurrent main updates / 병렬 GitHub 증거 저장 견고화

**Why / 근거:** Source-only Q03 and independently verified CMS E01 live release checks both **completed their allowed evidence computations**, but one-shot runs later failed the final `git push HEAD:main` due concurrent main changes. This is an operational persistence failure, **not** a reason to rerun terminal scientific/source attempts. Q03 terminal `HOLD_Q03_OPERATIONAL_INTEGRITY` remains unchanged and its uncommitted aggregate metrics cannot be fabricated.

## Frozen capability boundary / 운영 정책
1. Persist future new, separately preregistered source-qualification evidence into a **unique immutable per-run branch** `refs/heads/evidence/s01/<qualification>/<run-id>`, never push directly to `refs/heads/main` from a long-running source job.
2. All files must reside under an explicitly whitelisted relative `research/SOURCE-REGISTRY-S01/qualifications/<qualification>/evidence/` path; require exactly one UTF-8 JSON and matching Markdown receipt, no symlinks, `..`, raw archive or alternate casing. Both receipts must be validated as zero-cost, no source case records or outcome values, not automatic F01/E01 promotion.
3. Branch identity is computed solely from prospective qualification ID and GitHub Actions integer run ID, never from measured data, decision or future outcomes. **No force push.** If ref exists, refuse to overwrite or create another receipt; if the main branch advances, the evidence ref remains independent.
4. An operator can subsequently review the saved branch, independently verify evidence SHA/contract and promote to main via **separate PR expected-head merge**, never amend terminal evidence or auto-edit Issue #203. No automatic new Issue or new science gate.
5. Tests must cover URL/path scope, symlink traversal, JSON safety envelope, branch ref determinism, existing remote ref fail-closed, absence of any `main` push, synthetic successful per-run publication and recovery for concurrent main advances. At least 8 offline cases, no original source network access.
6. No changes to existing Q01/Q02/Q03 result, old E01 scientific runner, 346,859 pairs, `DEC-318`, current E01 execution, or existing S01 evidence grades. Future new source experiments must independently opt in after their own contract is frozen.
7. Use only standard free public-repository GitHub runner/CLI, no paid artifacts storage, external database, API key or compute. **Incremental monetary cost 0 USD**.

**Possible outcomes:** `PASS_S01_PERSIST_R01_OPERATIONAL_ONLY` on actual synthetic CI evidence; otherwise `HOLD_S01_PERSIST_R01_IMPLEMENTATION`. Neither is a scientific finding. / 과학적 연구 승인이 아닌 공통 증거보존 능력 검증이다.
