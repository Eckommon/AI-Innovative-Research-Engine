"""Synthetic, no-network E01 frozen runner transport-binding regression checks."""
import hashlib
import json
import unittest
from pathlib import Path

from tools.run_us_cms_npi_e01_transport_locked import (
    DownloadSequenceGuard, enforce_result_source, release_weekly_url
)
from tools.verify_us_cms_npi_e01_source_release import PASS

FULL = "https://download.cms.gov/nppes/NPPES_Data_Dissemination_October_2026_V2.zip"
DEACT = "https://download.cms.gov/nppes/NPPES_Deactivated_NPI_Report_101226_V2.zip"
FIRST = "https://download.cms.gov/nppes/NPPES_Data_Dissemination_101226_101826_Weekly_V2.zip"
LATER = "https://download.cms.gov/nppes/NPPES_Data_Dissemination_101926_102526_Weekly_V2.zip"


def fixtures():
    candidate = {
        "earliest_observed_qualifying": {
            "token": "101226_101826", "start": "2026-10-12",
            "end": "2026-10-18", "href": FIRST,
        }
    }
    raw = (json.dumps(candidate, sort_keys=True) + "\n").encode()
    release = {
        "decision": PASS,
        "candidate_sha256": hashlib.sha256(raw).hexdigest(),
        "first_publication_adjudication": "PASS",
        "prior_week_exclusion_reviewed": True,
        "zip_body_opened": False,
        "future_membership_opened": False,
        "approved_source": dict(candidate["earliest_observed_qualifying"]),
    }
    return raw, release


class TransportLockTests(unittest.TestCase):
    def fake(self):
        events = []
        def transport(url, path, timeout=1200):
            events.append((url, Path(path).name, timeout))
            return {"url": url}
        return transport, events

    def test_three_locked_downloads_in_order(self):
        transport, events = self.fake()
        guard = DownloadSequenceGuard(FULL, DEACT, FIRST)
        func = guard.guarded(transport)
        for u, name in ((FULL, "full.zip"), (DEACT, "deact.zip"), (FIRST, "weekly.zip")):
            func(u, Path("/tmp") / name)
        self.assertEqual(len(events), 3)
        self.assertEqual(guard.count, 3)

    def test_baseline_wrong_order_is_denied_before_transport(self):
        transport, events = self.fake()
        with self.assertRaises(RuntimeError):
            DownloadSequenceGuard(FULL, DEACT, FIRST).guarded(transport)(DEACT, "deact.zip")
        self.assertEqual(events, [])

    def test_later_week_zip_is_denied_before_transport(self):
        transport, events = self.fake()
        guard = DownloadSequenceGuard(FULL, DEACT, FIRST)
        download = guard.guarded(transport)
        download(FULL, "full.zip")
        download(DEACT, "deact.zip")
        with self.assertRaises(RuntimeError):
            download(LATER, "weekly.zip")
        self.assertEqual(len(events), 2)

    def test_unexpected_destination_is_denied(self):
        transport, events = self.fake()
        with self.assertRaises(RuntimeError):
            DownloadSequenceGuard(FULL, DEACT, FIRST).guarded(transport)(FULL, "weekly.zip")
        self.assertEqual(events, [])

    def test_fourth_zip_is_denied(self):
        transport, events = self.fake()
        guard = DownloadSequenceGuard(FULL, DEACT, FIRST)
        dl = guard.guarded(transport)
        dl(FULL, "full.zip"); dl(DEACT, "deact.zip"); dl(FIRST, "weekly.zip")
        with self.assertRaises(RuntimeError): dl(FIRST, "weekly.zip")
        self.assertEqual(len(events), 3)

    def test_authorized_release_binds_to_candidate_raw_bytes(self):
        raw, release = fixtures()
        self.assertEqual(release_weekly_url(raw, release), FIRST)

    def test_candidate_hash_change_is_rejected(self):
        raw, release = fixtures()
        with self.assertRaises(RuntimeError):
            release_weekly_url(raw+b" ", release)

    def test_unreviewed_source_is_rejected(self):
        raw, release = fixtures()
        release["first_publication_adjudication"] = "UNKNOWN"
        with self.assertRaises(RuntimeError):
            release_weekly_url(raw, release)

    def test_changed_release_weekly_is_rejected(self):
        raw, release = fixtures()
        release["approved_source"]["href"] = LATER
        with self.assertRaises((RuntimeError, ValueError)):
            release_weekly_url(raw, release)

    def test_empirical_result_cannot_promote_if_source_mismatch(self):
        record = {"attempt_valid": True, "disposition": "INCONCLUSIVE_US_CMS_NPI_E01",
                  "chosen_future_source": {"href": LATER}}
        with self.assertRaises(RuntimeError):
            enforce_result_source(record, FIRST, 3)

    def test_empirical_result_cannot_promote_if_transport_missing(self):
        record = {"attempt_valid": True, "disposition": "INCONCLUSIVE_US_CMS_NPI_E01",
                  "chosen_future_source": {"href": FIRST}}
        with self.assertRaises(RuntimeError):
            enforce_result_source(record, FIRST, 2)

    def test_valid_result_with_exact_downloads_passes(self):
        record = {"attempt_valid": True, "disposition": "INCONCLUSIVE_US_CMS_NPI_E01",
                  "chosen_future_source": {"href": FIRST}}
        self.assertEqual(enforce_result_source(record, FIRST, 3), "INCONCLUSIVE_US_CMS_NPI_E01")

    def test_blocked_experiment_does_not_promote(self):
        record = {"attempt_valid": False, "disposition": "IMPLEMENTATION_BLOCKED_US_CMS_NPI_E01_ATTEMPT_01"}
        with self.assertRaises(RuntimeError):
            enforce_result_source(record, FIRST, 3)


if __name__ == "__main__":
    unittest.main()
