"""Q11 source-native GEOID / PRJ proof — synthetic no-network tests before source access."""
import hashlib
import io
import json
from pathlib import Path
import struct
from tempfile import TemporaryDirectory
import unittest
from unittest import mock
import zipfile

from tools import qualify_source_census_usda_q10 as q10
from tools import qualify_source_census_usda_q11 as q


def pool():
    return {f"{state:02d}{county:03d}".encode()
            for state in range(1,53) for county in range(1,61)}


def make_dbf(keys, *, version=3, field="GEOID", geoid_width=5,
             deleted=False, duplicate=False):
    keys = list(keys)
    if duplicate and len(keys)>1:
        keys[1] = keys[0]
    fields = [("NAME","C",10),(field,"C",geoid_width)]
    header_length = 32+32*len(fields)+1
    record_length = 1+sum(z for _,_,z in fields)
    header = bytearray(32)
    header[0] = version
    struct.pack_into("<IHH",header,4,len(keys),header_length,record_length)
    descs = bytearray()
    for name,kind,width in fields:
        entry = bytearray(32)
        entry[:len(name)] = name.encode()
        entry[11] = ord(kind)
        entry[16] = width
        descs.extend(entry)
    rows = bytearray()
    for index, key in enumerate(keys):
        rows.extend((b"*" if deleted and index==0 else b" ") +
                    b"SECRET_AAA" + key[:geoid_width].ljust(geoid_width,b" "))
    return bytes(header)+bytes(descs)+b"\x0d"+bytes(rows)+b"\x1a"


WKT = b'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983"],UNIT["Degree",0.0174]]'


def archive(year, ids=None):
    ids = list(ids or pool())
    buf = io.BytesIO()
    with zipfile.ZipFile(buf,"w",compression=zipfile.ZIP_DEFLATED) as zf:
        for suffix,raw in [
            (".shp",b"NO_GEOMETRY_WILL_BE_READ"),
            (".shx",b"NO_GEOMETRY_WILL_BE_READ"),
            (".dbf",make_dbf(ids)),
            (".prj",WKT),
            (".cpg",b"UTF-8"),
            (".shp.iso.xml",b"metadata"),
            (".shp.ea.iso.xml",b"metadata"),
        ]:
            zf.writestr(f"tl_{year}_us_county{suffix}",raw)
    return buf.getvalue()


class FakeResp:
    status = 200
    def __init__(self,data,url,headers=None):
        self.reader = io.BytesIO(data)
        self.url = url
        self.headers = headers or {}
    def __enter__(self):
        return self
    def __exit__(self,*args):
        return False
    def geturl(self):
        return self.url
    def read(self,n):
        return self.reader.read(n)


class FakeClient:
    def __init__(self,resp):
        self.resp=resp
        self.calls=0
    def open(self,req,timeout=None):
        self.calls+=1
        return self.resp


class Q11Tests(unittest.TestCase):
    def test01_exact_q10_historical_SHA_locks(self):
        self.assertEqual(q.ORIGINALS["2023"]["bytes"],83451409)
        self.assertEqual(q.ORIGINALS["2024"]["bytes"],83913260)
        self.assertEqual(len(q.ORIGINALS["2023"]["sha256"]),64)

    def test02_dbf_geoid_only_valid_and_no_secret_output(self):
        raw=make_dbf(pool())
        keys,info=q.parse_dbf_geoid_only(raw)
        self.assertEqual(len(keys),3120)
        self.assertFalse(info["other_dbf_value_columns_interpreted"])
        self.assertNotIn("SECRET_AAA",str(info))

    def test03_dbf_invalid_version_rejected(self):
        with self.assertRaises(ValueError):
            q.parse_dbf_geoid_only(make_dbf(pool(),version=255))

    def test04_dbf_missing_geoid_fails(self):
        with self.assertRaises(ValueError):
            q.parse_dbf_geoid_only(make_dbf(pool(),field="WRONG"))

    def test05_dbf_wrong_geoid_width_fails(self):
        with self.assertRaises(ValueError):
            q.parse_dbf_geoid_only(make_dbf(pool(),geoid_width=4))

    def test06_dbf_duplicate_id_fails(self):
        with self.assertRaises(ValueError):
            q.parse_dbf_geoid_only(make_dbf(pool(),duplicate=True))

    def test07_dbf_nondigit_identifier_fails(self):
        codes=list(pool())
        codes[0]=b"abcde"
        with self.assertRaises(ValueError):
            q.parse_dbf_geoid_only(make_dbf(codes))

    def test08_dbf_deleted_row_is_hard_hold(self):
        with self.assertRaises(ValueError):
            q.parse_dbf_geoid_only(make_dbf(pool(),deleted=True))

    def test09_dbf_truncated_record_body_fails(self):
        with self.assertRaises(ValueError):
            q.parse_dbf_geoid_only(make_dbf(pool())[:-40])

    def test10_support_3120_exact_codes_and_52_prefixes(self):
        s=pool()
        res=q.support_receipt(s,s.copy())
        self.assertEqual(res["distinct_geoid_overlap"],3120)
        self.assertEqual(res["shared_jurisdiction_prefix_count"],52)
        self.assertFalse(res["raw_individual_geoid_emitted"])

    def test11_low_overlap_fails(self):
        first=pool()
        second=set(list(first)[:500])
        with self.assertRaises(ValueError):
            q.support_receipt(first,second)

    def test12_low_prefix_support_fails(self):
        a={f"01{i:03d}".encode() for i in range(1,1000)}
        with self.assertRaises(ValueError):
            q.support_receipt(a,a)

    def test13_prj_syntax_proof_and_no_WKT_output(self):
        v=q.prj_receipt(WKT)
        self.assertEqual(v["prj_sha256"],hashlib.sha256(WKT).hexdigest())
        self.assertFalse(v["prj_wkt_text_emitted"])

    def test14_prj_malformed_or_oversize_rejected(self):
        for raw in [b"NOT_A_WKT", WKT+b"x"*(q.MAX_PRJ+1),b""]:
            with self.assertRaises(ValueError):
                q.prj_receipt(raw)

    def test15_exact_mock_full_sha_before_only_DBFPJR_read(self):
        raw=archive("2023")
        with zipfile.ZipFile(io.BytesIO(raw)) as zf:
            prior=q10.check_manifest("2023",zf.infolist())
        fake=FakeClient(FakeResp(raw,q.SOURCES["2023"],headers={"Content-Length":str(len(raw))}))
        read_names=[]
        orig_read=zipfile.ZipFile.read
        def guarded_read(zf,name,*args,**kwargs):
            read_names.append(name)
            if not name.endswith((".dbf",".prj")):
                raise AssertionError("FORBIDDEN_SHP_OR_SHX")
            return orig_read(zf,name,*args,**kwargs)
        with mock.patch.dict(q.ORIGINALS,{"2023":{"bytes":len(raw),
                    "sha256":hashlib.sha256(raw).hexdigest()}}):
            with mock.patch.object(zipfile.ZipFile,"read",new=guarded_read):
                receipt,keys,sha=q.fetch_source("2023",prior,opener=fake)
        self.assertEqual(fake.calls,1)
        self.assertEqual(len(read_names),2)
        self.assertEqual(len(keys),3120)
        self.assertTrue(receipt["q10_original_source_sha_and_manifest_matched"])
        self.assertFalse(receipt["shp_shx_or_polygon_payload_read"])

    def test16_redirect_fails_before_member_read(self):
        raw=archive("2024")
        fake=FakeClient(FakeResp(raw,"https://example.org/redirect"))
        with self.assertRaises(ValueError):
            q.fetch_source("2024",{"member_inventory_sha256":"bad"},opener=fake)

    def test17_wrong_original_bytes_SHA_hard_hold_before_members(self):
        raw=archive("2024")
        fake=FakeClient(FakeResp(raw,q.SOURCES["2024"]))
        with self.assertRaises(ValueError):
            q.fetch_source("2024",{"member_inventory_sha256":"bad"},opener=fake)

    def test18_prespecified_transport_size_drift_rejected(self):
        raw=archive("2023")
        fake=FakeClient(FakeResp(raw,q.SOURCES["2023"],
                    headers={"Content-Length":"104857601"}))
        with self.assertRaises(ValueError):
            q.fetch_source("2023",{"member_inventory_sha256":"bad"},opener=fake)

    def test19_full_mock_Q11_run_pass_no_raw_ids(self):
        with TemporaryDirectory() as d:
            out=Path(d)/"evidence/attempt-01.json"
            mock_prior={"source_receipts":{"2023":{},"2024":{}}}
            def getter(year,previous):
                return ({"official_original_url":q.SOURCES[year],
                         "dbf_non_geoid_columns_parsed":False,
                         "shp_shx_or_polygon_payload_read":False},
                        pool(),hashlib.sha256(WKT).hexdigest())
            r=q.run(fetch=getter,out=out,context=lambda:mock_prior)
            self.assertEqual(r["disposition"],q.PASS)
            self.assertFalse(r["geographic_boundary_equivalence_verified"])
            self.assertNotIn("SECRET",out.read_text())
            self.assertEqual(r["aggregate_geoid_support"]["distinct_geoid_overlap"],3120)
            with self.assertRaises(RuntimeError):
                q.run(fetch=getter,out=out,context=lambda:mock_prior)

    def test20_failure_class_only_no_secret_records_persist(self):
        with TemporaryDirectory() as d:
            out=Path(d)/"evidence/attempt-01.json"
            mock_prior={"source_receipts":{"2023":{},"2024":{}}}
            def bad(year,previous):
                raise RuntimeError("SECRET_COUNTY_01001_NAME")
            r=q.run(fetch=bad,out=out,context=lambda:mock_prior)
            self.assertEqual(r["disposition"],q.HOLD)
            self.assertEqual(r["failure_type"],"RuntimeError")
            self.assertNotIn("SECRET_COUNTY",out.read_text())
            self.assertNotIn("SECRET_COUNTY",out.with_suffix(".md").read_text())
            self.assertFalse(r["science_f01_authorized"])

    def test21_prj_mismatch_hold_even_if_key_support_passes(self):
        with TemporaryDirectory() as d:
            out=Path(d)/"evidence/attempt-01.json"
            mock_prior={"source_receipts":{"2023":{},"2024":{}}}
            def mismatch(year,previous):
                return ({},pool(),"a"*64 if year=="2023" else "b"*64)
            r=q.run(fetch=mismatch,out=out,context=lambda:mock_prior)
            self.assertEqual(r["disposition"],q.HOLD)
            self.assertFalse(r["crs_exact_wkt_sha_equal"])


if __name__ == "__main__":
    unittest.main()
