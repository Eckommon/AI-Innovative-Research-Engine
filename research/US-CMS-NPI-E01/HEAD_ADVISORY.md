# CMS NPI E01 — independent HEAD metadata advisory / 공식 파일 HEAD 메타데이터 단독 점검

**Purpose / 목적:** After 2026-10-18 coverage closes (earliest allowed UTC 2026-10-19 00:00), optionally inspect **only HTTP HEAD response headers** for a *hypothetical* URL derived from the official past file-naming pattern: \`NPPES_Data_Dissemination_101226_101826_Weekly_V2.zip\`. **The guessed URL has not been verified to exist.**

**Workflow:** \`.github/workflows/probe-us-cms-npi-e01-head.yml\`, **manual-only \`workflow_dispatch\`**; **no schedule and no billing-uncertain extra infrastructure**. Eight no-network unit tests are run before any HEAD operation. No redirect is followed. No GET, ZIP data, NPI membership, or statistical output is fetched.

**Scientific firewall / 과학적 방화벽:** A \`200\` response means only \`POSSIBLE_PUBLIC_OBJECT_METADATA_ONLY\`; status 403/404/405/3xx never proves absence. Response Date/Last-Modified/ETag is **not conclusive CMS first-publication chronology**. The frozen canonical six-hour official HTML listing watcher, immutable first observed source candidate, separate independent source lineage adjudication, candidate SHA and exact E01 transport lock remain the **exclusive** approval path. This HEAD workflow **never creates source-candidate-01, updates Issue #203, adds experiment marker or permits an empirical attempt**. No automatic execution before or after the release window.

**Cost rule:** standard public repository Ubuntu runner only if manually dispatched with confirmed zero-cost eligibility; users must approve any possible paid substitution. **Incremental cost 0 USD** for code-only preparation.

**Disposition:** \`ADVISORY_PREPARED_NOT_EXECUTED\`. Not an E01 result and not a substitute for official CMS publication.
