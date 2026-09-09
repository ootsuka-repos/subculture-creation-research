"""カタログの必須情報、参照、派生形式、ローカルリンクを検証する。"""
import csv
import datetime
import json
import re
from pathlib import Path
from urllib.parse import unquote

from export import render

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
items = data["items"]
ids = {p["id"] for p in items}
categories = {c["id"] for c in data["categories"]}
errors = []


def require(condition, message):
    if not condition:
        errors.append(message)


require(len(ids) == len(items), "重複ID")
require(len({p["repository"].lower() for p in items}) == len(items), "重複repository")
require(data["schema_version"] == "2.0", "未対応のschema_version")
required = ["summary_ja", "inputs_ja", "outputs_ja", "requirements_ja", "dependencies_ja", "limitations_ja", "assessment_ja", "checked_on", "code_revision", "sources", "kind", "ai_role", "maturity", "repository_role"]
for p in items:
    label = p["id"]
    for key in required:
        require(bool(p.get(key)), f"{label}: {key}が空")
    require(p["category"] in categories, f"{label}: 未定義カテゴリ")
    require(p["ai_role"] in {"core", "integration", "optional", "none", "postprocess"}, f"{label}: ai_role")
    require(re.fullmatch(r"[0-9a-f]{40}", p["code_revision"]), f"{label}: commit形式")
    require(p["url"] == "https://github.com/" + p["repository"], f"{label}: URL不一致")
    datetime.date.fromisoformat(p["checked_on"])
    require(p["code_revision"] in p["sources"][0]["url"], f"{label}: READMEが固定されていない")
    require(p["metrics"]["stars"] >= 0, f"{label}: stars")
    require(not p["metrics"]["archived"] or p["maturity"] == "historical", f"{label}: archive区分")
    snapshot = json.loads((ROOT / p["metrics"]["snapshot_path"]).read_text(encoding="utf-8"))
    require(snapshot["repositories"][p["repository"]]["stars"] == p["metrics"]["stars"], f"{label}: snapshot不一致")
    require(p["verification"]["weights_file_inventory_verified"] == any(m["verification"] == "file_listing_checked" for m in p["model_resources"]), f"{label}: 重み確認状態の矛盾")
    for m in p["model_resources"]:
        if m["verification"] == "file_listing_checked":
            require(m["evidence_files"] and m["revision"] and m["http_status"] == 200, f"{label}: 重み根拠不足")
    for relation in p["relations"]:
        require(relation["target_id"] in ids, f"{label}: 関連先が存在しない")

jsonl = [json.loads(line) for line in (ROOT / "catalog.jsonl").read_text(encoding="utf-8").splitlines()]
require(jsonl == items, "JSONLとJSONの不一致")
with (ROOT / "catalog.csv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
require(len(rows) == len(items), "CSV件数の不一致")
for row, p in zip(rows, items):
    for key in ("id", "summary_ja", "url", "checked_on", "code_revision"):
        require(row[key] == p[key], f"{p['id']}: CSV {key}不一致")
    require(json.loads(row["sources_json"]) == p["sources"], f"{p['id']}: CSV根拠不一致")
    require(json.loads(row["model_resources_json"]) == p["model_resources"], f"{p['id']}: CSVモデル不一致")
for name, content in render(data).items():
    require((ROOT / name).read_bytes() == content.encode("utf-8"), f"生成物が古い: {name}")
for path in ROOT.rglob("*.md"):
    for target in re.findall(r"\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
        if target.startswith(("https://", "http://", "#", "mailto:")):
            continue
        local = unquote(target.split("#")[0])
        require((path.parent / local).exists(), f"リンク切れ: {path.name} -> {target}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(items)} entries, {len(categories)} categories, JSON/JSONL/CSV, sources, model evidence, generated files and local links")
