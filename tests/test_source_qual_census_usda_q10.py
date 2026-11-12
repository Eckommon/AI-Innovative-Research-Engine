"""Q10 full official ZIP bytes + central-directory only: NO NETWORK synthetic gates."""
import hashlib
import io
import json
from pathlib import Path
import stat
from tempfile import TemporaryDirectory
import unittest
from unittest import mock
import zipfile

from tools import qualify_source_census_usda_q10 as q


def archive(year, extra=None):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for suffix in (".shp", ".shx", ".dbf", ".prj"):
            zf.writestr(f"tl_{year}_us_county{suffix}", b"safe-synthetic-no-record-data")
        for path, data in (extra or []):
            zf.writestr(path, data)
    return buf.getvalue()


def infos(year):
    with zipfile.ZipFile(io.BytesIO(archive(year))) as zf:
        return zf.infolist()


class FakeResp:
    def __init__(self, raw, url, status=200, headers=None):
        self.raw = io.BytesIO(raw)
        self.url = url
        self.status = status
        self.headers = headers or {}
    def __enter__(self):
        return self
    def __exit__(self, *unused):
        return False
    def geturl(self):
        return self.url
    def read(self, size):
        return self.raw.read(size)


class FakeClient:
    def __init__(self, response):
        self.response = response
        self.calls = []
    def open(self, req, timeout=None):
        self.calls.append((req.full_url, req.get_method(), timeout))
        return self.response


class Q10SourceTests(unittest.TestCase):
    def test01_only_preselected_official_year_archive_urls(self):
        self.assertEqual(set(q.SOURCES), {"2023", "2024"})
        self.assertTrue(all(u.startswith("https://www2.census.gov/geo/tiger/TIGER")
                            for u in q.SOURCES.values()))
        self.assertFalse(any("2025" in u or "2026" in u for u in q.SOURCES.values()))

    def test02_raw_SHA_before_zip_metadata_and_exact_one_GET(self):
        raw = archive("2023")
        client = FakeClient(FakeResp(raw, q.SOURCES["2023"],
                        headers={"Content-Length": str(len(raw))}))
        with mock.patch.object(zipfile.ZipFile, "open",
                               side_effect=AssertionError("no member bytes permitted")):
            result = q.fetch_source("2023", opener=client)
        self.assertEqual(result["original_zip_sha256"], hashlib.sha256(raw).hexdigest())
        self.assertEqual(result["original_zip_bytes"], len(raw))
        self.assertEqual(len(client.calls), 1)
        self.assertEqual(client.calls[0], (q.SOURCES["2023"], "GET", 180))
        self.assertFalse(result["member_payloads_decompressed"])
        self.assertFalse(result["member_payloads_read"])

    def test03_redirected_final_url_fail_closed(self):
        client = FakeClient(FakeResp(archive("2023"), "https://example.org/not-census.zip"))
        with self.assertRaises(ValueError):
            q.fetch_source("2023", opener=client)

    def test04_bad_http_status_fail_closed(self):
        client = FakeClient(FakeResp(archive("2023"), q.SOURCES["2023"], status=206))
        with self.assertRaises(ValueError):
            q.fetch_source("2023", opener=client)

    def test05_declared_zip_oversize_rejected_without_read(self):
        client = FakeClient(FakeResp(archive("2024"), q.SOURCES["2024"],
                        headers={"Content-Length": str(q.LIMIT+1)}))
        with self.assertRaises(ValueError):
            q.fetch_source("2024", opener=client)
        self.assertEqual(len(client.calls), 1)

    def test06_http_content_encoding_not_identity_rejected(self):
        client = FakeClient(FakeResp(archive("2023"), q.SOURCES["2023"],
                        headers={"Content-Encoding": "gzip"}))
        with self.assertRaises(ValueError):
            q.fetch_source("2023", opener=client)

    def test07_non_zip_body_fails(self):
        client = FakeClient(FakeResp(b"HTML access denied", q.SOURCES["2024"]))
        with self.assertRaises(ValueError):
            q.fetch_source("2024", opener=client)

    def test08_valid_member_inventory_is_sorted_and_no_payload_opened(self):
        result = q.check_manifest("2023", infos("2023"))
        self.assertEqual(result["member_count"], 4)
        self.assertEqual(len(result["member_inventory_sha256"]), 64)
        self.assertEqual(result["member_inventory"][0]["basename"],
                         "tl_2023_us_county.dbf")
        self.assertFalse(result["member_payloads_decompressed"])

    def test09_path_traversal_and_external_member_forbidden(self):
        items = infos("2023")
        items[0].filename = "../tl_2023_us_county.shp"
        with self.assertRaises(ValueError):
            q.check_manifest("2023", items)

    def test10_duplicate_member_forbidden(self):
        items = infos("2023")
        with self.assertRaises(ValueError):
            q.check_manifest("2023", items+[items[0]])

    def test11_encrypted_member_forbidden(self):
        items = infos("2024")
        items[0].flag_bits |= 1
        with self.assertRaises(ValueError):
            q.check_manifest("2024", items)

    def test12_symlink_member_forbidden(self):
        items = infos("2024")
        items[0].external_attr = ((stat.S_IFLNK | 0o777) << 16)
        with self.assertRaises(ValueError):
            q.check_manifest("2024", items)

    def test13_missing_required_prj_cannot_pass(self):
        items = [x for x in infos("2024") if not x.filename.endswith(".prj")]
        with self.assertRaises(ValueError):
            q.check_manifest("2024", items)

    def test14_wrong_year_file_family_rejected(self):
        with self.assertRaises(ValueError):
            q.check_manifest("2024", infos("2023"))

    def test15_oversized_advertised_member_rejected(self):
        items = infos("2023")
        items[0].file_size = q.MAX_MEMBER_SIZE + 1
        with self.assertRaises(ValueError):
            q.check_manifest("2023", items)

    def test16_unexpected_file_extension_rejected(self):
        raw = archive("2023", [("tl_2023_us_county.exe", b"x")])
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            with self.assertRaises(ValueError):
                q.check_manifest("2023", zf.infolist())

    def test17_two_complete_mock_sources_success_and_immutable_one_shot(self):
        with TemporaryDirectory() as directory:
            out = Path(directory)/"evidence/attempt-01.json"
            def fake(year):
                raw = archive(year)
                return {"official_original_url":q.SOURCES[year],
                        "original_zip_bytes":len(raw),
                        "original_zip_sha256":hashlib.sha256(raw).hexdigest(),
                        **q.check_manifest(year, infos(year))}
            result = q.run(fetch=fake, out=out, context=lambda:None)
            self.assertEqual(result["disposition"], q.PASS)
            self.assertTrue(result["archive_original_bytes_fetched"])
            self.assertFalse(result["archive_members_decompressed"])
            self.assertFalse(result["geographic_boundary_equivalence_verified"])
            self.assertEqual(set(result["source_receipts"]), {"2023", "2024"})
            self.assertTrue(out.with_suffix(".md").exists())
            with self.assertRaises(RuntimeError):
                q.run(fetch=fake, out=out, context=lambda:None)

    def test18_partial_source_error_preserves_redacted_hard_hold(self):
        with TemporaryDirectory() as directory:
            out = Path(directory)/"evidence/attempt-01.json"
            def fake(year):
                if year == "2024":
                    raise RuntimeError("SECRET_COUNTY_01001_2024 leak")
                return {"official_original_url":q.SOURCES[year],
                        "original_zip_sha256":"a"*64,
                        **q.check_manifest(year, infos(year))}
            result = q.run(fetch=fake, out=out, context=lambda:None)
            self.assertEqual(result["disposition"],q.HOLD)
            self.assertEqual(result["failure_type"],"RuntimeError")
            self.assertFalse(result["science_f01_authorized"])
            self.assertNotIn("SECRET_COUNTY",out.read_text())
            self.assertNotIn("SECRET_COUNTY",out.with_suffix(".md").read_text())

    def test19_invalid_year_no_network(self):
        client = FakeClient(FakeResp(b"", "https://example.org/"))
        with self.assertRaises(ValueError):
            q.fetch_source("2025", opener=client)
        self.assertEqual(len(client.calls), 0)

    def test20_zip_member_payload_never_decompressed_from_metadata(self):
        raw = archive("2024")
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            with mock.patch.object(zf, "read",
                                   side_effect=AssertionError("member data read forbidden")):
                result = q.check_manifest("2024", zf.infolist())
        self.assertFalse(result["member_payloads_read"])


if __name__ == "__main__":
    unittest.main()
