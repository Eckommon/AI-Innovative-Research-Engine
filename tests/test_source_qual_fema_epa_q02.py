"""Synthetic offline boundaries for prospective FEMA-EPA Q02 monitor product only."""
import io
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase, mock
import zipfile

from tools import qualify_source_fema_epa_q02 as q

COLUMNS = ["State Code", "County Code", "Site Num", "Parameter Code",
           "Year", "Pollutant Standard", "Event Type"]


def synthetic_zip(columns=COLUMNS, filename=q.EPA_MEMBER, payload=None):
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
        row = ",".join(columns) + "\r\n"
        archive.writestr(filename, row.encode() if payload is None else payload)
    return out.getvalue()


class MockResponse:
    status = 200

    def __init__(self, payload):
        self.payload = payload
        self.headers = {"Content-Type": "application/zip"}

    def __enter__(self):
        return self

    def __exit__(self, *_):
        return False

    def geturl(self):
        return q.EPA_URL

    def read(self, n):
        return self.payload[:n]


class MockOpener:
    def __init__(self, payload):
        self.payload = payload
        self.methods = []

    def open(self, request, timeout):
        self.methods.append((request.get_method(), request.full_url, timeout))
        return MockResponse(self.payload)


class Q02BoundaryTests(TestCase):
    def test_existing_q01_terminal_hold_and_fema_receipt_are_not_reinterpreted(self):
        data = q.verify_existing_q01()
        self.assertEqual(data["fema_original_sha256"], q.FEMA_SHA)
        self.assertTrue(data["fema_original_q01_holding_preserved"])

    def test_exact_url_and_bound_locked_before_request(self):
        for altered_url, altered_size in (
            ("https://aqs.epa.gov/aqsweb/airdata/annual_aqi_by_county_2024.zip", q.MAX_BYTES),
            (q.EPA_URL + "?v=1", q.MAX_BYTES), (q.EPA_URL, q.MAX_BYTES + 1),
        ):
            with self.assertRaises(ValueError):
                q.download(url=altered_url, max_bytes=altered_size, opener=MockOpener(b""))

    def test_single_get_and_complete_fingerprint_no_rows(self):
        raw = synthetic_zip()
        opener = MockOpener(raw)
        blob, meta = q.download(opener=opener)
        self.assertEqual(blob, raw)
        self.assertEqual(opener.methods, [("GET", q.EPA_URL, 55)])
        self.assertEqual(meta["zip_byte_count"], len(raw))
        self.assertFalse(meta["case_rows_parsed"])
        self.assertFalse(meta["first_publication_verified"])

    def test_header_only_positive_exact_product(self):
        h = q.inspect_header_only(synthetic_zip())
        self.assertTrue(h["required_exact_fields_confirmed"])
        self.assertEqual(h["actual_case_rows_parsed"], 0)
        self.assertEqual(q.classify(h), "DUAL_D2_SOURCE_HEADERS_ONLY_Q02")

    def test_missing_field_is_hold_not_alias_rescue(self):
        h = q.inspect_header_only(synthetic_zip(columns=[c for c in COLUMNS if c != "County Code"] + ["County Name"]))
        self.assertFalse(h["required_exact_fields_confirmed"])
        self.assertIn("County Code", h["missing_required_field_names"])
        self.assertEqual(q.classify(h), "HOLD_SOURCE_ACCESS_OR_SCHEMA_Q02")

    def test_wrong_product_and_extra_member_rejected(self):
        with self.assertRaises(ValueError):
            q.inspect_header_only(synthetic_zip(filename="annual_aqi_by_county_2024.csv"))
        out = io.BytesIO()
        with zipfile.ZipFile(out, "w") as archive:
            archive.writestr(q.EPA_MEMBER, ",".join(COLUMNS) + "\n")
            archive.writestr("extra.csv", "State Code,County Code\n")
        with self.assertRaises(ValueError):
            q.inspect_header_only(out.getvalue())

    def test_unbounded_or_nonzip_header_rejected(self):
        with self.assertRaises(ValueError):
            q.inspect_header_only(b"not a ZIP")
        with self.assertRaises(ValueError):
            q.inspect_header_only(synthetic_zip(payload=(b"a" * 17000 + b"\n")))

    def test_synthetic_run_persists_only_schema_receipt(self):
        with TemporaryDirectory() as td:
            result_path = Path(td) / "evidence" / "source-qualification-01.json"
            fake = (synthetic_zip(), {"http_status": 200, "method": "GET",
                   "zip_byte_count": 150, "zip_sha256": "a" * 64,
                   "case_rows_parsed": False})
            with (mock.patch.object(q, "OUT", result_path),
                  mock.patch.object(q, "download", return_value=fake) as net):
                q.run()
                self.assertEqual(net.call_count, 1)
            receipt = json.loads(result_path.read_text())
            self.assertEqual(receipt["disposition"], "DUAL_D2_SOURCE_HEADERS_ONLY_Q02")
            self.assertFalse(receipt["exact_join_cardinality_verified"])
            self.assertFalse(receipt["science_f01_authorized"])
            self.assertEqual(receipt["q01_original_disposition_preserved"], "HOLD_SOURCE_ACCESS_OR_SCHEMA")
            self.assertFalse(receipt["source_outcome_rows_opened"])
            with mock.patch.object(q, "OUT", result_path):
                with self.assertRaises(RuntimeError):
                    q.run()


if __name__ == "__main__":
    import unittest
    unittest.main()
