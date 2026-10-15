"""Pure offline regression fixtures; no CMS request, no outcome rows."""
import unittest
from datetime import datetime, timezone
from email.message import Message
from tools import probe_us_cms_npi_e01_weekly_head as probe


class DummyResponse:
    status = 200
    def __init__(self):
        self.headers = Message()
        self.headers["Content-Length"] = "123"
    def geturl(self):
        return probe.URL
    def __enter__(self):
        return self
    def __exit__(self, *args):
        return None


class DummyOpener:
    def open(self, request, timeout):
        self.method = request.get_method()
        return DummyResponse()


class CMSHeadAdvisoryTests(unittest.TestCase):
    def test_denies_before_week_end(self):
        with self.assertRaises(ValueError):
            probe.allowed(datetime(2026, 10, 18, 23, 59, tzinfo=timezone.utc), probe.URL)

    def test_end_inclusive_start_only(self):
        probe.allowed(datetime(2026, 10, 19, tzinfo=timezone.utc), probe.URL)

    def test_denies_nonexact_url(self):
        with self.assertRaises(ValueError):
            probe.allowed(datetime(2026, 10, 20, tzinfo=timezone.utc), "https://other.example/any.zip")

    def test_no_get_possible_with_injected_opener(self):
        stub = DummyOpener()
        record = probe.probe(datetime(2026, 10, 20, tzinfo=timezone.utc), stub)
        self.assertEqual(stub.method, "HEAD")
        self.assertEqual(record["signal"], "POSSIBLE_PUBLIC_OBJECT_METADATA_ONLY")

    def test_200_is_never_release_authorization(self):
        record = probe.classify(200, Message())
        for key in ("official_listing_confirmed", "first_publication_adjudicated",
                    "candidate_commit_authorized", "e01_experiment_authorized",
                    "zip_body_opened", "provider_outcomes_opened"):
            self.assertFalse(record[key], key)

    def test_non200_has_no_absence_conclusion(self):
        for code in (301, 403, 404, 405, 500):
            self.assertEqual(probe.classify(code, Message())["signal"], "NOT_ESTABLISHED")

    def test_redirect_denied(self):
        self.assertIsNone(probe.NoRedirect().redirect_request(None, None, 302, "", {}, "https://example.com/"))

    def test_naive_clock_rejected(self):
        with self.assertRaises(ValueError):
            probe.allowed(datetime(2026, 10, 20), probe.URL)


if __name__ == "__main__":
    unittest.main()
