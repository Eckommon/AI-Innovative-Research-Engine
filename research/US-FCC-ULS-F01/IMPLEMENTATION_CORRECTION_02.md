---
id: US-FCC-ULS-F01-IMPLEMENTATION-CORRECTION-02
type: implementation-only-correction
created: 2026-09-21
issue: 166
attempt_01_run: 35555305664
attempt_01_disposition: IMPLEMENTATION_BLOCKED_US_FCC_ULS_F01_ATTEMPT_01
scientific_threshold_changed: false
service_family_changed: false
identity_rule_changed: false
future_window_changed: false
future_outcome_membership_opened: false
incremental_monetary_cost_usd: 0
---

# US-FCC-ULS-F01 — Attempt 02 transport-only correction

Attempt 01 is immutable and preserved. It reached Gates 1–4, then terminated as an implementation/transport block before a valid empirical F01 result.

Observed Attempt-01 boundary:

- canonical authorization and Issue binding passed;
- three frozen official FCC PDF documentation anchors returned HTTP 200 and were fingerprinted;
- the FCC HTML download page returned HTTP 403 from the GitHub-hosted urllib client;
- the baseline archive request then returned HTTP 403 before any baseline ZIP body was accepted or parsed;
- no future Microwave daily transaction body was opened;
- no future cancellation/termination membership was opened;
- no scientific threshold, service family, identity rule, source filename, or future window was changed.

Official FCC Public Notice DA 99-2205 identifies Microwave/Microwave Broadcast Auxiliary complete license file `l_micro.zip`, daily license family `l_mw_xxx.zip`, and states that ULS data files are also available from the FCC FTP publication tree `ftp://ftp.fcc.gov/pub/Bureaus/Wireless/Databases/uls`.

## Allowed Attempt-02 correction

Attempt 02 may change **transport resolution only**:

1. use `curl` with redirects and ordinary browser-compatible request headers instead of Python `urllib` for FCC HTTP retrieval;
2. for the same exact FCC filenames, try only FCC-owned endpoint variants derived from the documented ULS publication tree:
   - current `data.fcc.gov/download/pub/uls/{complete|daily}/...`;
   - legacy/current FCC ULS web path `wireless.fcc.gov/uls/data/{complete|daily}/...`;
   - HTTPS form of the FCC publication host `ftp.fcc.gov/pub/Bureaus/Wireless/Databases/uls/{complete|daily}/...`;
3. record every attempted URL, HTTP status/final URL when available, and the selected official FCC URL;
4. preserve the frozen Gate-3 requirement. A documentation anchor that cannot be retrieved or officially redirected still fails Gate 3 in a **valid** Attempt 02; it is not silently waived;
5. preserve all 18 scientific gates, thresholds, service family, baseline filename `l_micro.zip`, daily filenames `l_mw_xxx.zip`, exact 9-digit system-ID rule, and future window 2026-09-21 through 2027-03-20;
6. future daily ZIP bodies remain prohibited; metadata-only requests consume zero entity-body bytes;
7. third-party mirrors, paid sources, different service families, alternate identifiers, and post-observation threshold changes remain prohibited.

If transport succeeds far enough to execute all 18 gates, Attempt 02 is the first valid empirical result and must be terminalized exactly as PASS or scientific HOLD. If transport still blocks before a valid result, it remains an implementation/operational block rather than a scientific HOLD.

Incremental monetary cost remains **0 USD**.
