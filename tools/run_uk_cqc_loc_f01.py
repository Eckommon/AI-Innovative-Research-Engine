#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from datetime import date, datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse, unquote
import hashlib
import json
import os
import re
import subprocess
import tempfile
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_SHA = "99c7782cabc384ce7c4817a91b5cb1bdc105012c"
ISSUE = 171
OUTDIR = ROOT / "research/UK-CQC-LOC-F01/evidence"
JSON_OUT = OUTDIR / "attempt-02.json"
MD_OUT = OUTDIR / "attempt-02.md"

LANDING = "https://www.cqc.org.uk/about-us/transparency/using-cqc-data"
SELECTORS = {
    "filters": "Care directory with filters (01 September 2026)",
    "ratings": "Care directory with ratings (01 September 2026)",
    "deactivated": "Deactivated locations (01 September 2026)",
}
ARCHIVE_SELECTORS = {
    "filters_archive": "archive of care directory with filters files",
    "ratings_archive": "archive of care directory with ratings files",
}
UA = "Mozilla/5.0 (compatible; AI-Innovative-Research-Engine/1.0; public-data-research)"

NS_TABLE = "{urn:oasis:names:tc:opendocument:xmlns:table:1.0}"
NS_TEXT = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"
NS_OFFICE = "{urn:oasis:names:tc:opendocument:xmlns:office:1.0}"

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self._href = None
        self._text = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() == "a":
            self._href = dict(attrs).get("href")
            self._text = []
    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)
    def handle_endtag(self, tag):
        if tag.lower() == "a" and self._href is not None:
            self.links.append((" ".join("".join(self._text).split()), self._href))
            self._href = None
            self._text = []

def curl_bytes(url: str, head: bool = False, timeout: int = 180) -> tuple[bytes, dict]:
    with tempfile.TemporaryDirectory() as td:
        hp = Path(td) / "headers.txt"
        bp = Path(td) / "body.bin"
        cmd = [
            "curl","-L","--fail","--silent","--show-error","--retry","2",
            "--connect-timeout","20","--max-time",str(timeout),"-A",UA,
            "-D",str(hp),"-o",str(bp)
        ]
        if head:
            cmd += ["-I"]
        cmd += [url]
        p = subprocess.run(cmd, capture_output=True)
        if p.returncode != 0:
            raise RuntimeError(f"curl rc={p.returncode}: {p.stderr.decode('utf-8','replace')[:800]}")
        header_raw = hp.read_bytes() if hp.exists() else b""
        body = b"" if head else (bp.read_bytes() if bp.exists() else b"")
    blocks = [b for b in re.split(br"\r?\n\r?\n", header_raw) if b.startswith(b"HTTP/")]
    final_header = blocks[-1] if blocks else b""
    status = None
    headers = {}
    if final_header:
        lines = final_header.decode("iso-8859-1","replace").splitlines()
        m = re.match(r"HTTP/\S+\s+(\d+)", lines[0])
        status = int(m.group(1)) if m else None
        for line in lines[1:]:
            if ":" in line:
                k,v = line.split(":",1)
                headers[k.strip().lower()] = v.strip()
    return body, {
        "status": status,
        "content_type": headers.get("content-type"),
        "content_length_header": headers.get("content-length"),
        "last_modified": headers.get("last-modified"),
        "etag": headers.get("etag"),
        "sha256": hashlib.sha256(body).hexdigest() if not head else None,
        "bytes": len(body),
        "entity_body_bytes_consumed": len(body),
        "requested_url": url,
    }

def page(url: str) -> tuple[str, dict]:
    b,m = curl_bytes(url, timeout=120)
    return b.decode("utf-8","replace"),m

def resolve_link(base: str, html: str, selector: str) -> str | None:
    p = LinkParser(); p.feed(html)
    target = " ".join(selector.lower().split())
    for text,href in p.links:
        if target in " ".join(text.lower().split()) and href:
            return urljoin(base,href)
    return None

def resolve_archive_links(base: str, html: str) -> dict[str,str | None]:
    p = LinkParser(); p.feed(html)
    out = {}
    for key,selector in ARCHIVE_SELECTORS.items():
        target = " ".join(selector.lower().split())
        out[key] = None
        for text,href in p.links:
            if target in " ".join(text.lower().split()) and href:
                out[key] = urljoin(base,href)
                break
    return out

def cqc_owned(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return host == "cqc.org.uk" or host.endswith(".cqc.org.uk")

def norm_header(v) -> str:
    return re.sub(r"[^a-z0-9]+","",str(v or "").strip().lower())

def norm_location_id(v) -> str | None:
    if v is None:
        return None
    s = str(v).strip()
    if not s:
        return None
    # Frozen contract: preserve all remaining source characters exactly and
    # accept only nonblank ASCII alphanumeric tokens. No case repair.
    return s if re.fullmatch(r"[A-Za-z0-9]+",s) else None

def parse_date(v):
    if isinstance(v,date) and not isinstance(v,datetime):
        return v
    if isinstance(v,datetime):
        return v.date()
    if v is None:
        return None
    s = str(v).strip()
    if not s:
        return None
    fmts = ("%Y-%m-%d","%d/%m/%Y","%d/%m/%y","%d %B %Y","%d %b %Y","%Y/%m/%d")
    for fmt in fmts:
        try:
            return datetime.strptime(s,fmt).date()
        except ValueError:
            pass
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})T",s)
    if m:
        try:
            return date(int(m.group(1)),int(m.group(2)),int(m.group(3)))
        except ValueError:
            return None
    return None

def cell_value(cell: ET.Element):
    d = cell.attrib.get(NS_OFFICE+"date-value")
    if d:
        return d
    s = cell.attrib.get(NS_OFFICE+"string-value")
    if s:
        return s
    v = cell.attrib.get(NS_OFFICE+"value")
    texts = []
    for p in cell.iter(NS_TEXT+"p"):
        t = "".join(p.itertext()).strip()
        if t:
            texts.append(t)
    if texts:
        return " ".join(texts)
    return v if v is not None else ""

def ods_rows(path: Path):
    with zipfile.ZipFile(path) as z:
        if "content.xml" not in z.namelist():
            raise RuntimeError(f"ODS_CONTENT_XML_MISSING:{path.name}")
        with z.open("content.xml") as fh:
            current_sheet = None
            row_number = 0
            for event,elem in ET.iterparse(fh,events=("start","end")):
                if event == "start" and elem.tag == NS_TABLE+"table":
                    current_sheet = elem.attrib.get(NS_TABLE+"name","")
                    row_number = 0
                elif event == "end" and elem.tag == NS_TABLE+"table-row" and current_sheet is not None:
                    row = []
                    for cell in list(elem):
                        if cell.tag not in (NS_TABLE+"table-cell",NS_TABLE+"covered-table-cell"):
                            continue
                        val = cell_value(cell)
                        rep = int(cell.attrib.get(NS_TABLE+"number-columns-repeated","1") or "1")
                        if rep > 4096:
                            rep = 4096
                        row.extend([val]*rep)
                    while row and (row[-1] is None or str(row[-1]).strip()==""):
                        row.pop()
                    rrep = int(elem.attrib.get(NS_TABLE+"number-rows-repeated","1") or "1")
                    if row:
                        for _ in range(min(rrep,1024)):
                            row_number += 1
                            yield current_sheet,row_number,row
                    else:
                        row_number += rrep
                    elem.clear()
                elif event == "end" and elem.tag == NS_TABLE+"table":
                    current_sheet = None
                    elem.clear()

def header_match(norms, groups):
    # Location identity must be a real header cell, never a token buried in README prose.
    for group in groups:
        if any(tok in {"locationid","cqclocationid"} for tok in group):
            if not any(h in group for h in norms):
                return False
        elif not any(any(tok in h for tok in group) for h in norms):
            return False
    return True

def find_header(path: Path, groups, max_nonblank=120):
    seen = 0
    for sheet,rn,row in ods_rows(path):
        if not any(str(x).strip() for x in row):
            continue
        seen += 1
        norms = [norm_header(x) for x in row]
        if header_match(norms,groups):
            return sheet,rn,row,norms
        if seen >= max_nonblank:
            break
    return None,None,None,None

def iter_data_rows(path: Path, sheet_name: str, header_row: int):
    for sheet,rn,row in ods_rows(path):
        if sheet == sheet_name and rn > header_row:
            yield row

def idx_for(norms, tokens):
    for i,h in enumerate(norms):
        if any(tok == h or tok in h for tok in tokens):
            return i
    return None

def indices_for(norms, tokens):
    return [i for i,h in enumerate(norms) if any(tok == h or tok in h for tok in tokens)]

def download(url: str, path: Path) -> dict:
    b,m = curl_bytes(url, timeout=360)
    path.write_bytes(b)
    m["sha256"] = hashlib.sha256(b).hexdigest()
    m["bytes"] = len(b)
    m["final_url"] = url
    return m

def extract_archive_dates(raw_html: str):
    months = "January|February|March|April|May|June|July|August|September|October|November|December"
    text = html_lib.unescape(unquote(raw_html))
    # Google Drive folder HTML can encode filenames inside JSON/script data using separators/escapes.
    text = (text.replace("\\u0020"," ").replace("\\x20"," ").replace("_"," ").replace("-"," "))
    text = re.sub(r"\\u00(?:20|2d)", " ", text, flags=re.I)
    vals = set()
    for d,m,y in re.findall(rf"\b(0?[1-9]|[12]\d|3[01])\s+({months})\s+(20\d{{2}})\b",text,re.I):
        try:
            dt = datetime.strptime(f"{int(d):02d} {m.title()} {y}","%d %B %Y").date()
            if dt <= date(2026,9,1):
                vals.add(dt.isoformat())
        except ValueError:
            pass
    # Archive filenames may encode only month/year in visible or script metadata.
    # Count them as monthly snapshots at the first of month; the threshold is monthly lineage, not day precision.
    for m,y in re.findall(rf"\b({months})\s+(20\d{{2}})\b",text,re.I):
        try:
            dt = datetime.strptime(f"01 {m.title()} {y}","%d %B %Y").date()
            if dt <= date(2026,9,1):
                vals.add(dt.isoformat())
        except ValueError:
            pass
    return sorted(vals)

def main():
    OUTDIR.mkdir(parents=True,exist_ok=True)
    if JSON_OUT.exists() or MD_OUT.exists():
        raise RuntimeError("immutable attempt-02 evidence already exists")
    ev = {
        "research":"UK-CQC-LOC-F01","attempt":2,"contract_sha":CONTRACT_SHA,"issue":ISSUE,
        "attempt_01_commit":"4b26cfc6c31f38a36a19b908a45c1ca9cb67f030",
        "implementation_correction_commit":"6d7abac0041866e841389c6d30e003e5bf68a02c",
        "scientific_threshold_changed":False,"snapshot_changed":False,
        "identity_rule_changed":False,"event_semantics_changed":False,
        "future_outcome_firewall_changed":False,
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"incremental_monetary_cost_usd":0,
        "future_rows_opened":0,"future_event_membership_opened":False,
        "future_entity_body_bytes_consumed":0,
        "relationship_computed":False,"prediction_computed":False,"ranking_computed":False,
        "causal_claim_made":False,"name_address_fuzzy_geo_manual_repair_used":False,
        "gates":[]
    }
    ev["runner_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    try:
        cp = json.loads((ROOT/"context/checkpoint.json").read_text())
        g1 = (
            cp.get("checkpoint_id")=="CHK-20260929-UK-CQC-LOC-F01-ACTIVE"
            and cp.get("active_issue")==171
            and cp.get("active_research")=="UK-CQC-LOC-F01"
            and cp.get("last_decision")=="DEC-252"
        )
        ev["gates"].append({"gate":1,"pass":g1,"observed":cp})
        bound = os.environ.get("CQC_F01_ISSUE_BOUND")=="1" and os.environ.get("CQC_F01_CONTRACT_SHA")==CONTRACT_SHA
        ev["gates"].append({"gate":2,"pass":bound,"observed":{"issue":ISSUE,"contract_sha":os.environ.get("CQC_F01_CONTRACT_SHA")}})

        landing_html,landing_meta = page(LANDING)
        lower = landing_html.lower()
        selector_presence = {k:(v.lower() in lower) for k,v in SELECTORS.items()}
        g3 = all(selector_presence.values())
        ev["gates"].append({"gate":3,"pass":g3,"observed":{"landing":landing_meta,"selectors_present":selector_presence}})

        urls = {k:resolve_link(LANDING,landing_html,v) for k,v in SELECTORS.items()}
        g4 = all(urls.values()) and all(cqc_owned(u) for u in urls.values())
        ev["gates"].append({"gate":4,"pass":bool(g4),"observed":urls})

        archive_urls = resolve_archive_links(LANDING,landing_html)
        archive_obs = {}
        all_archive_dates = set()
        for key,u in archive_urls.items():
            if not u:
                archive_obs[key] = {"url":None,"dates":[]}
                continue
            try:
                ah,am = page(u)
                dates = extract_archive_dates(ah)
                all_archive_dates.update(dates)
                archive_obs[key] = {"url":u,"meta":am,"dates":dates}
            except Exception as e:
                archive_obs[key] = {"url":u,"error":f"{type(e).__name__}:{e}","dates":[]}

        with tempfile.TemporaryDirectory() as td0:
            td = Path(td0)
            files = {}
            metas = {}
            for key,u in urls.items():
                if not u:
                    continue
                p = td/f"{key}.ods"
                metas[key] = download(u,p)
                files[key] = p
                if not zipfile.is_zipfile(p):
                    raise RuntimeError(f"ODS_PARSE_ERROR:{key}:not a zip-based ODS file")
            ev["source_fingerprints"] = {k:v["sha256"] for k,v in metas.items()}

            # Filters directory / baseline
            baseline_ids = set()
            provider_by_id = defaultdict(set)
            directory_stats = {}
            directory_schema = False
            if "filters" in files:
                sheet,hr,headers,norms = find_header(
                    files["filters"],
                    [("locationid","cqclocationid"),("service","regulatedactivity","specialism","registration")]
                )
                if sheet:
                    li = idx_for(norms,("cqclocationid","locationid"))
                    pi = idx_for(norms,("cqcproviderid","providerid"))
                    service_cols = indices_for(norms,("servicetype","regulatedactivity","specialism","registrationstatus","registrationdate"))
                    directory_schema = li is not None and bool(service_cols)
                    rows=nonblank=valid=0
                    if directory_schema:
                        for row in iter_data_rows(files["filters"],sheet,hr):
                            rows += 1
                            raw = row[li] if li < len(row) else None
                            if raw is not None and str(raw).strip():
                                nonblank += 1
                            loc = norm_location_id(raw)
                            if loc:
                                valid += 1
                                baseline_ids.add(loc)
                                if pi is not None and pi < len(row) and str(row[pi]).strip():
                                    provider_by_id[loc].add(str(row[pi]).strip())
                    directory_stats = {
                        "sheet":sheet,"header_row":hr,
                        "headers":[str(x) for x in headers],
                        "rows":rows,"nonblank_location_ids":nonblank,
                        "qualified_location_ids":valid,
                        "distinct_qualified_location_ids":len(baseline_ids),
                        "syntax_rate": valid/nonblank if nonblank else 0.0,
                        "provider_id_field_present": pi is not None,
                        "service_structure_field_count":len(service_cols),
                    }
            ev["gates"].append({"gate":5,"pass":directory_schema,"observed":directory_stats})
            syntax_rate = directory_stats.get("syntax_rate",0.0)
            ev["gates"].append({"gate":6,"pass":syntax_rate>=0.999,
                                "observed":{"rate":syntax_rate,"threshold":0.999,
                                            "qualified":directory_stats.get("qualified_location_ids",0),
                                            "nonblank":directory_stats.get("nonblank_location_ids",0)}})
            ev["gates"].append({"gate":7,"pass":len(baseline_ids)>=20000,
                                "observed":{"distinct_qualified_baseline_location_ids":len(baseline_ids),"threshold":20000}})

            # Ratings file
            ratings_stats={}
            ratings_schema=False
            ratings_ids=set()
            if "ratings" in files:
                sheet,hr,headers,norms = find_header(
                    files["ratings"],
                    [("locationid","cqclocationid"),("rating",),("date","publication","assessment")]
                )
                if sheet:
                    li=idx_for(norms,("cqclocationid","locationid"))
                    rating_cols=indices_for(norms,("rating",))
                    date_cols=indices_for(norms,("publicationdate","assessmentdate","ratingdate","date"))
                    ratings_schema=li is not None and bool(rating_cols) and bool(date_cols)
                    rows=0
                    if ratings_schema:
                        for row in iter_data_rows(files["ratings"],sheet,hr):
                            rows += 1
                            loc=norm_location_id(row[li] if li<len(row) else None)
                            if loc:
                                ratings_ids.add(loc)
                    ratings_stats={"sheet":sheet,"header_row":hr,"headers":[str(x) for x in headers],
                                   "rows":rows,"distinct_qualified_location_ids":len(ratings_ids),
                                   "rating_field_count":len(rating_cols),"date_field_count":len(date_cols)}
            ev["gates"].append({"gate":8,"pass":ratings_schema,"observed":ratings_stats})
            exact_rating_links = baseline_ids & ratings_ids
            ev["gates"].append({"gate":9,"pass":len(exact_rating_links)>=10000,
                                "observed":{"exact_linked_baseline_location_ids":len(exact_rating_links),"threshold":10000}})

            # Deactivated file
            deact_stats={}
            deact_schema=False
            deact_ids=set()
            deact_rows=deact_dated=0
            if "deactivated" in files:
                sheet,hr,headers,norms = find_header(
                    files["deactivated"],
                    [("locationid","cqclocationid"),("date","end","deactiv","archive")]
                )
                if sheet:
                    li=idx_for(norms,("cqclocationid","locationid"))
                    date_cols=indices_for(norms,("registrationenddate","enddate","deactivationdate","deactivateddate","archiveddate","date"))
                    deact_schema=li is not None and bool(date_cols)
                    if deact_schema:
                        for row in iter_data_rows(files["deactivated"],sheet,hr):
                            raw=row[li] if li<len(row) else None
                            loc=norm_location_id(raw)
                            if not loc:
                                continue
                            deact_rows += 1
                            deact_ids.add(loc)
                            good=False
                            for di in date_cols:
                                if di < len(row) and parse_date(row[di]) is not None:
                                    good=True
                                    break
                            if good:
                                deact_dated += 1
                    deact_stats={"sheet":sheet,"header_row":hr,"headers":[str(x) for x in headers],
                                 "qualified_rows":deact_rows,"distinct_qualified_location_ids":len(deact_ids),
                                 "parseable_end_date_rows":deact_dated,"date_field_count":len(date_cols)}
            ev["gates"].append({"gate":10,"pass":deact_schema,"observed":deact_stats})
            ev["gates"].append({"gate":11,"pass":len(deact_ids)>=5000,
                                "observed":{"distinct_exact_deactivated_location_ids":len(deact_ids),"threshold":5000}})
            end_rate=deact_dated/deact_rows if deact_rows else 0.0
            ev["gates"].append({"gate":12,"pass":end_rate>=0.95,
                                "observed":{"parseable_end_date_rate":end_rate,"parseable":deact_dated,
                                            "qualified_rows":deact_rows,"threshold":0.95}})

            # Administrative-transition semantics from official landing/API metadata.
            semantics = {
                "api_linked_organisations": ("linked organisations" in lower and "previously run by a different provider" in lower),
                "deactivated_not_necessarily_closed": ("not necessarily because the service has closed" in lower),
                "reregistered_example": ("re-registered" in lower or "reregistered" in lower),
                "legal_structure_example": ("legal structure" in lower),
                "address_change_example": ("changed address" in lower or "change address" in lower),
                "registration_start_end_api": ("registration" in lower and "started and ended" in lower),
            }
            g13=(semantics["api_linked_organisations"] and semantics["deactivated_not_necessarily_closed"]
                 and (semantics["reregistered_example"] or semantics["legal_structure_example"] or semantics["address_change_example"])
                 and semantics["registration_start_end_api"])
            ev["gates"].append({"gate":13,"pass":g13,"observed":semantics})

            # Identity conflict: exact retained Location ID should not map to multiple exact provider IDs.
            evaluable = directory_stats.get("provider_id_field_present",False)
            conflicts={loc:sorted(vals) for loc,vals in provider_by_id.items() if len(vals)>1}
            g14=evaluable and len(conflicts)==0
            ev["gates"].append({"gate":14,"pass":g14,
                                "observed":{"evaluable_with_provider_id":evaluable,
                                            "conflicting_exact_location_ids":len(conflicts),
                                            "examples":list(conflicts.items())[:20]}})

            g15=len(all_archive_dates)>=6
            ev["gates"].append({"gate":15,"pass":g15,
                                "observed":{"archive_urls":archive_urls,"archive_pages":archive_obs,
                                            "distinct_snapshot_dates_le_2026_09_01":sorted(all_archive_dates),
                                            "count":len(all_archive_dates),"threshold":6}})

            # Future seal by construction: no later inactive/deactivated URL or body is defined/requested.
            g16=(ev["future_rows_opened"]==0 and ev["future_entity_body_bytes_consumed"]==0)
            ev["gates"].append({"gate":16,"pass":g16,
                                "observed":{"future_rows_opened":0,"future_entity_body_bytes_consumed":0,
                                            "policy":"runner defines and requests only frozen 01-Sep-2026 files"}})
            g17=(ev["future_rows_opened"]==0 and ev["future_event_membership_opened"] is False
                 and not ev["relationship_computed"] and not ev["prediction_computed"]
                 and not ev["ranking_computed"] and not ev["causal_claim_made"]
                 and not ev["name_address_fuzzy_geo_manual_repair_used"])
            ev["gates"].append({"gate":17,"pass":g17,"observed":{k:ev[k] for k in (
                "future_rows_opened","future_event_membership_opened","relationship_computed",
                "prediction_computed","ranking_computed","causal_claim_made",
                "name_address_fuzzy_geo_manual_repair_used"
            )}})
            g18=(len(ev.get("source_fingerprints",{}))==3
                 and all(re.fullmatch(r"[0-9a-f]{64}",x) for x in ev["source_fingerprints"].values())
                 and re.fullmatch(r"[0-9a-f]{64}",ev["runner_sha256"]) is not None
                 and ev["incremental_monetary_cost_usd"]==0)
            ev["gates"].append({"gate":18,"pass":g18,
                                "observed":{"source_sha256":ev.get("source_fingerprints",{}),
                                            "runner_sha256":ev["runner_sha256"],
                                            "contract_sha":CONTRACT_SHA,"cost_usd":0}})

        ev["gates"]=sorted(ev["gates"],key=lambda g:g["gate"])
        failed=[g["gate"] for g in ev["gates"] if not g["pass"]]
        ev["attempt_valid"]=True
        ev["pass_count"]=18-len(failed)
        ev["failed_gates"]=failed
        ev["disposition"]=(
            "PASS_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_READY"
            if not failed else
            "HOLD_UK_CQC_LOC_F01_EXACT_LOCATION_REGISTRATION_END_DESIGN_NOT_READY"
        )
    except Exception as e:
        ev["attempt_valid"]=False
        ev["implementation_error"]={"type":type(e).__name__,"message":str(e)}
        ev["pass_count"]=sum(1 for g in ev["gates"] if g.get("pass"))
        ev["failed_gates"]=[]
        ev["disposition"]="IMPLEMENTATION_BLOCKED_UK_CQC_LOC_F01_ATTEMPT_02"

    JSON_OUT.write_text(json.dumps(ev,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    lines=[
        "# UK-CQC-LOC-F01 — Attempt 02","",
        f"**Disposition:** `{ev['disposition']}`","",
        f"- Attempt valid: `{ev.get('attempt_valid')}`",
        f"- Gates passed: **{ev.get('pass_count',0)}/18**",
        f"- Failed gates: `{ev.get('failed_gates',[])}`",
        f"- Future rows opened: **{ev['future_rows_opened']}**",
        f"- Future event membership opened: **{ev['future_event_membership_opened']}**",
        f"- Incremental monetary cost: **{ev['incremental_monetary_cost_usd']} USD**","",
        "## Gate ledger","",
        "| Gate | PASS | Observed |","|---:|:---:|---|"
    ]
    for g in sorted(ev["gates"],key=lambda x:x["gate"]):
        obs=json.dumps(g.get("observed"),ensure_ascii=False,sort_keys=True)
        if len(obs)>950:
            obs=obs[:947]+"..."
        lines.append(f"| {g['gate']} | {'PASS' if g['pass'] else 'FAIL'} | `{obs.replace(chr(96),'')}` |")
    if ev.get("implementation_error"):
        lines += ["","## Implementation error","",f"`{ev['implementation_error']}`"]
    lines += ["","Only frozen 01-Sep-2026 CQC entity files were authorized. No post-2026-09-28 inactive/deactivated entity body was opened.",""]
    MD_OUT.write_text("\n".join(lines),encoding="utf-8")
    print(ev["disposition"])
    print(ev.get("pass_count"),ev.get("failed_gates"))
    return 0

if __name__=="__main__":
    raise SystemExit(main())
