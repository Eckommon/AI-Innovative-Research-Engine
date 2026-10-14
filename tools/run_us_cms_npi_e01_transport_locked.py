#!/usr/bin/env python3
"""E01 operational transport interlock around the unchanged preregistered runner.

The frozen runner reconstructs the cohort, selects the weekly, and computes all
18 gates/statistics unchanged. This wrapper permits its three ZIP downloads
ONLY in the preregistered baseline/baseline-deactivation/released-future order.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Callable

from tools.verify_us_cms_npi_e01_source_release import (
    CANDIDATE, RELEASE, PASS, source_identity
)


class DownloadSequenceGuard:
    """Fail closed *before transport* on an unexpected URL, order or destination."""

    def __init__(self, baseline_full: str, baseline_deact: str, approved_weekly: str):
        self.expected = (
            (baseline_full, "full.zip"),
            (baseline_deact, "deact.zip"),
            (approved_weekly, "weekly.zip"),
        )
        self.count = 0

    def guarded(self, original: Callable):
        def only_approved_download(url, path, timeout=1200):
            position = self.count
            if position >= len(self.expected):
                raise RuntimeError("E01_ZIP_TRANSPORT_DENIED_EXTRA_DOWNLOAD")
            permitted_url, filename = self.expected[position]
            if url != permitted_url or Path(path).name != filename:
                raise RuntimeError(
                    "E01_ZIP_TRANSPORT_DENIED_SOURCE_OR_ORDER:"
                    f"position={position+1} path={Path(path).name}"
                )
            self.count += 1
            return original(url, path, timeout=timeout)
        return only_approved_download


def release_weekly_url(candidate_bytes: bytes, release: dict) -> str:
    """Re-read the release/candidate integrity at the actual execution boundary."""
    candidate = json.loads(candidate_bytes)
    digest = hashlib.sha256(candidate_bytes).hexdigest()
    if (release.get("candidate_sha256") != digest
            or release.get("decision") != PASS
            or release.get("first_publication_adjudication") != "PASS"
            or release.get("prior_week_exclusion_reviewed") is not True
            or release.get("zip_body_opened") is not False
            or release.get("future_membership_opened") is not False):
        raise RuntimeError("E01_TRANSPORT_RELEASE_NOT_AUTHORIZED_OR_HASH_MISMATCH")
    approved = source_identity(release.get("approved_source"))
    observed = source_identity(candidate.get("earliest_observed_qualifying"))
    if approved != observed:
        raise RuntimeError("E01_TRANSPORT_SOURCE_DIFFERS_FROM_FIRST_CANDIDATE")
    return approved[3]


def enforce_result_source(record: dict, authorized_url: str, download_count: int):
    """An empirical E01 artifact cannot be promoted after a wrong/absent transfer."""
    if record.get("disposition") == "IMPLEMENTATION_BLOCKED_US_CMS_NPI_E01_ATTEMPT_01":
        raise RuntimeError("E01_TRANSPORT_OR_RUNNER_IMPLEMENTATION_BLOCKED")
    if record.get("disposition") == "WAIT_SOURCE_US_CMS_NPI_E01":
        raise RuntimeError("E01_NO_QUALIFYING_FUTURE_SOURCE")
    source = record.get("chosen_future_source")
    if (not isinstance(source, dict) or source.get("href") != authorized_url
            or download_count != 3 or record.get("attempt_valid") is not True):
        raise RuntimeError("E01_ATTEMPT_SOURCE_NOT_EQUAL_TO_APPROVED_TRANSFER")
    return record["disposition"]


def main():
    if not CANDIDATE.is_file() or not RELEASE.is_file():
        raise RuntimeError("E01_SOURCE_RELEASE_NOT_YET_AVAILABLE")
    locked_url = release_weekly_url(
        CANDIDATE.read_bytes(),
        json.loads(RELEASE.read_text(encoding="utf-8")),
    )

    # Import of the scientific runner occurs only during the real execution.
    # The frozen module itself is never changed or re-hashed by this guard.
    from tools import run_us_cms_npi_e01 as frozen

    guard = DownloadSequenceGuard(frozen.FULL_URL, frozen.DEACT_URL, locked_url)
    original = frozen.download
    try:
        frozen.download = guard.guarded(original)
        frozen.main()
    finally:
        frozen.download = original

    evidence = frozen.JSON_OUT
    if not evidence.is_file():
        raise RuntimeError("E01_ATTEMPT_EVIDENCE_MISSING")
    record = json.loads(evidence.read_text(encoding="utf-8"))
    result = enforce_result_source(record, locked_url, guard.count)
    print("E01_TRANSPORT_SOURCE_LOCK_PASS", result, guard.count)


if __name__ == "__main__":
    main()
