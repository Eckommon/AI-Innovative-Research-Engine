#!/usr/bin/env python3
"""Implementation-only transport wrapper for US-FSIS-SAMPLE-F01.

Scientific contract, thresholds, years, identity rules and outcome firewall remain unchanged.
This wrapper replaces urllib transport with the system curl client because FSIS returned
HTTP 403 to urllib from the GitHub-hosted runner before any empirical support count was read.
"""
from __future__ import annotations

import subprocess

import run_us_fsis_sample_f01 as core


def curl_fetch(url: str) -> bytes:
    cmd = [
        "curl", "--location", "--fail", "--silent", "--show-error",
        "--retry", "3", "--retry-all-errors", "--connect-timeout", "30", "--max-time", "120",
        "--user-agent", core.UA,
        "--header", "Accept: text/html,application/xhtml+xml,application/json,text/csv,*/*;q=0.8",
        "--header", "Accept-Language: en-US,en;q=0.9",
        "--header", "Referer: https://www.fsis.usda.gov/",
        "--header", "Cache-Control: no-cache",
        url,
    ]
    return subprocess.run(cmd, check=True, stdout=subprocess.PIPE).stdout


core.fetch = curl_fetch

if __name__ == "__main__":
    core.main()
