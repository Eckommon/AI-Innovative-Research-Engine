"""No-network Q09 original Census directory metadata gates."""
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest import mock
from tools import qualify_source_census_usda_q09 as q

def listing(year,extra=""):
    target=q.SOURCES[year][1]
    return ('<html><body><a href="../">parent</a><a href="'+target+'">'+target+'</a>'+extra+'</body></html>').encode()

class FakeResponse:
    status=200
    headers={}
    def __init__(self,raw,url):self.raw=raw;self.url=url
    def __enter__(self):return self
    def __exit__(self,*_):return False
    def read(self,n):return self.raw[:n]
    def geturl(self):return self.url
class FakeOpener:
    def __init__(self,resp):self.resp=resp;self.calls=0
    def open(self,req,timeout=40):self.calls+=1;return self.resp

class Q09Tests(unittest.TestCase):
    def test01_2023_exact_href(self):
        r=q.check_listing("2023",listing("2023"))
        self.assertEqual(r["exact_relative_href_count"],1)
        self.assertFalse(r["archive_body_downloaded"])
    def test02_2024_exact_href(self):
        self.assertEqual(q.check_listing("2024",listing("2024"))["required_archive_basename"],
                         "tl_2024_us_county.zip")
    def test03_wrong_case_never_accepted(self):
        with self.assertRaises(ValueError):q.check_listing("2023",b'<a href="TL_2023_us_county.zip">x</a>')
    def test04_duplicate_anchor_holds(self):
        a=q.SOURCES["2023"][1]
        with self.assertRaises(ValueError):q.check_listing("2023",listing("2023",'<a href="'+a+'">duplicate</a>'))
    def test05_redirect_href_not_accepted(self):
        with self.assertRaises(ValueError):q.check_listing("2024",b'<a href="https://example.org/tl_2024_us_county.zip">x</a>')
    def test06_unapproved_year_denied(self):
        with self.assertRaises(ValueError):q.check_listing("2025",b"")
    def test07_retrieval_exact_url_and_SHA_before_parse(self):
        raw=listing("2023")
        client=FakeOpener(FakeResponse(raw,q.SOURCES["2023"][0]))
        got,meta=q.source_fetch("2023",opener=client)
        self.assertEqual(client.calls,1)
        self.assertEqual(got,raw)
        self.assertEqual(meta["listing_sha256"],hashlib.sha256(raw).hexdigest())
    def test08_redirect_is_hard_hold(self):
        client=FakeOpener(FakeResponse(listing("2024"),"https://example.org/"))
        with self.assertRaises(ValueError):q.source_fetch("2024",opener=client)
    def test09_oversize_directory_rejected(self):
        client=FakeOpener(FakeResponse(b"x"*(q.LIMIT+1),q.SOURCES["2023"][0]))
        with self.assertRaises(ValueError):q.source_fetch("2023",opener=client)
    def test10_no_archive_body_is_ever_opened(self):
        self.assertTrue(all(url.endswith("/COUNTY/") for url,_ in q.SOURCES.values()))
        self.assertFalse(any(url.endswith(".zip") for url,_ in q.SOURCES.values()))
    def test11_success_receipt_zero_geometry(self):
        with TemporaryDirectory() as d:
            out=Path(d)/"evidence/attempt-01.json"
            def fake(year):
                raw=listing(year)
                return raw,{"listing_sha256":hashlib.sha256(raw).hexdigest(),"listing_bytes":len(raw)}
            with mock.patch.object(q,"verify_context"):
                result=q.run(fetch=fake,out=out)
                with self.assertRaises(RuntimeError):q.run(fetch=fake,out=out)
            self.assertEqual(result["disposition"],q.PASS)
            self.assertFalse(result["archive_bodies_opened"])
            self.assertFalse(result["geographic_boundary_equivalence_verified"])
            self.assertNotIn("SECRET_COUNTY",out.read_text())
    def test12_failure_receipt_excludes_arbitrary_error_details(self):
        with TemporaryDirectory() as d:
            out=Path(d)/"evidence/attempt-01.json"
            with mock.patch.object(q,"verify_context"):
                def bad(year):raise RuntimeError("SECRET_COUNTY_01001")
                result=q.run(fetch=bad,out=out)
            self.assertEqual(result["disposition"],"HOLD_Q09_OFFICIAL_CATALOG_OR_SOURCE_ACCESS")
            self.assertNotIn("SECRET_COUNTY_01001",out.read_text())
            self.assertIs(result["science_f01_authorized"],False)

if __name__=="__main__":unittest.main()
