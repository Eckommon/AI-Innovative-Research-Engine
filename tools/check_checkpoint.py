"""Validate or synchronize checkpoint mirrors; scientific gates remain separate."""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
data = json.loads((root / "context/checkpoint.json").read_text())
keys = ("checkpoint_id", "active_issue", "active_research", "last_completed_issue",
        "last_completed_research", "last_decision", "updated")
assert set(data) == set(keys), "checkpoint fields differ"
for path in ("STATUS.md", "context/SESSION_HANDOFF.md"):
    p = root / path
    content = p.read_text()
    head, body = content.split("---", 2)[1:]
    parsed = dict(line.split(":", 1) for line in head.splitlines() if ":" in line)
    if "--sync" in sys.argv:
        for key in keys:
            parsed[key] = str(data[key])
        p.write_text("---\n" + "\n".join(k + ": " + str(v).strip() for k, v in parsed.items()) + "\n---" + body)
    else:
        assert all(parsed.get(k, "").strip() == str(data[k]) for k in keys), path
decision = data["last_decision"]
assert (root / "registry" / (decision + ".md")).exists(), "missing decision"
assert decision in (root / "registry/DECISION_LOG.md").read_text(), "decision not indexed"
if str(data["active_issue"]).lower() in {"none", "null", "n/a"}:
    assert data["active_research"] == "NONE", "inactive checkpoint must use active_research=NONE"
else:
    active_number = int(data["active_issue"])
    assert active_number > 0, "active_issue must be positive or none"
    assert data["active_research"] != "NONE", "active issue requires active research"
    assert (root / "research" / data["active_research"] / "README.md").exists(), "missing active research"
print("CHECKPOINT_LOCAL_PASS; live issue check still required")
