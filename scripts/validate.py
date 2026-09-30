"""カタログの必須情報、参照、派生形式、ローカルリンクを検証する。"""
import csv
import datetime
import json
import re
from pathlib import Path
from urllib.parse import unquote

from export import render
from export_datasets import render as render_datasets
from export_sota import render as render_sota

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
require(data["schema_version"] == "3.0", "未対応のschema_version")
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
    require(p['repository_role'] in {'implementation', 'official_mirror', 'api_documentation', 'model_reference'}, f'{label}: repository_role')
    deep = p['deep_dive']
    for key in ('reviewed_on', 'production_fit_ja', 'next_validation_ja', 'scope_note_ja', 'license_notes_ja', 'entry_points'):
        require(bool(deep.get(key)), f'{label}: deep_dive.{key}が空')
    require(deep['reviewed_on'] == p['checked_on'], f'{label}: 深掘り確認日不一致')
    require([e['path'] for e in deep['entry_points']] == p['evidence_files'], f'{label}: 入口候補の不一致')
    for e in deep['entry_points']:
        require(e['url'] == p['url'] + '/blob/' + p['code_revision'] + '/' + e['path'], f'{label}: 入口URL不一致')
    for a in deep['source_inspections']:
        require(a['commit'] == p['code_revision'] and a['finding_ja'] and re.fullmatch(r'[0-9a-f]{40}', a['blob_sha']), f'{label}: 本文確認根拠不足')
    for m in p["model_resources"]:
        if m["verification"] == "file_listing_checked":
            require(m["evidence_files"] and m["revision"] and m["http_status"] == 200, f"{label}: 重み根拠不足")
    for relation in p["relations"]:
        require(relation["target_id"] in ids, f"{label}: 関連先が存在しない")
        require(relation['basis'] in {'editorial', 'official_documentation'}, f'{label}: 関係の根拠区分')

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
    require(json.loads(row['deep_dive_json']) == p['deep_dive'], f"{p['id']}: CSV深掘り不一致")
models = json.loads((ROOT / 'model-catalog.json').read_text(encoding='utf-8'))
require(models['schema_version'] == '1.0', 'モデルカタログ形式')
require(len({m['id'] for m in models['items']}) == len(models['items']), '重複モデルID')
for m in models['items']:
    dist = m['distribution']
    require(dist['revision'] in m['sources'][0]['url'], f"{m['id']}: モデルカード固定参照")
    require(dist['evidence_files'] and dist['http_status'] == 200 and dist['verification'] == 'file_listing_checked', f"{m['id']}: モデル配布根拠不足")
    require(m['license_notes_ja'] and m['limitations_ja'], f"{m['id']}: モデル条件不足")
require([json.loads(x) for x in (ROOT / 'model-catalog.jsonl').read_text(encoding='utf-8').splitlines()] == models['items'], 'モデルJSONL不一致')
sota = json.loads((ROOT / 'sota-catalog.json').read_text(encoding='utf-8'))
require(sota['schema_version'] == '1.0', 'SOTAカタログ形式')
sota_slices = {s['id'] for s in sota['slices']}
sota_keys = [(t['task_id'], t.get('subtask')) for t in sota['tasks']]
require(len(set(sota_keys)) == len(sota_keys), 'SOTA: タスク/サブタスク重複')
sha40 = re.compile(r'^[0-9a-f]{40}$')
for t in sota['tasks']:
    label = f"SOTA {t['task_id']}/{t.get('subtask')}"
    require(t['slice'] in sota_slices and t['status'] in {'selected', 'general_only', 'none'} and t['confidence'] in {'high', 'medium', 'low'}, f'{label}: 分類不備')
    require(20 <= len(t['decision_short_ja']) <= 140 and len(t['decision_ja']) >= 40, f'{label}: 選定根拠の長さ')
    b = t.get('best')
    require(t['status'] == 'none' or t['task_id'].startswith('repos-') or b is not None, f'{label}: bestなし')
    if b:
        require(sha40.match(b['revision']) and b['revision'] in b['evidence'][0]['url'], f'{label}: モデルカード固定参照')
        require(b['verification']['weights_downloaded'] is False and b['verification']['runtime_tested'] is False and b['verification']['model_card_reviewed'] is True, f'{label}: 未実施の検証を実施済みと記録')
        require(b['license_notes_ja'] and b['limitations_ja'], f'{label}: モデル条件不足')
        datetime.date.fromisoformat(b['last_modified'])
    for g in t.get('repositories', []):
        require(sha40.match(g['commit_sha']) and g['commit_sha'] in g['evidence_url'] and g['url'] == 'https://github.com/' + g['repo'], f"{label}: {g['repo']} 固定参照")
        require((g['catalog_id'] is None) == (g['repo'].lower() not in {p['repository'].lower() for p in items}) and (g['catalog_id'] is None or g['catalog_id'] in ids), f"{label}: {g['repo']} catalog_id不整合")
for r in sota['reviewed_not_included']:
    require(r['slice'] in sota_slices and r['repo'] and r['reason_ja'], f"SOTA検討済み不備: {r.get('repo')}")
require([json.loads(x) for x in (ROOT / 'sota-catalog.jsonl').read_text(encoding='utf-8').splitlines()] == sota['tasks'], 'SOTA JSONL不一致')
papers_data = json.loads((ROOT / 'research/papers.json').read_text(encoding='utf-8'))
comp = json.loads((ROOT / 'companion-catalog.json').read_text(encoding='utf-8'))
paper_cats = {c['id'] for c in papers_data['categories']}
require(len({p['code_repository'].lower() for p in papers_data['papers']}) == len(papers_data['papers']), '論文: 重複repository')
for p in papers_data['papers']:
    label = 'paper:' + p['short_name']
    for key in ('title', 'summary_ja', 'paper_url', 'code_url', 'checked_on', 'models', 'evidence_urls', 'venue', 'year'):
        require(bool(p.get(key)), f'{label}: {key}が空')
    require(re.fullmatch(r'[0-9a-f]{40}', p['code_revision'] or ''), f'{label}: commit形式')
    require(p['code_url'].startswith('https://github.com/' + p['code_repository']), f'{label}: URL不一致')
    require(p['category_id'] in paper_cats, f'{label}: 未定義分野')
    require(p['catalog_id'] is None or p['catalog_id'] in ids, f'{label}: catalog_idが存在しない')
    datetime.date.fromisoformat(p['checked_on'])
for v in papers_data['venues']:
    n = sum(1 for p in papers_data['papers'] if p['venue'] == v['conference'] and p['year'] == v['year'])
    require(n == v['included_count'], f"会議件数不一致: {v['conference']} {v['year']} {n} != {v['included_count']}")
require(sum(v['included_count'] for v in papers_data['venues']) == len(papers_data['papers']), '会議件数の合計')
comp_sections = {s['id'] for s in comp['sections']}
require(len({i['id'] for i in comp['items']}) == len(comp['items']), '会話キャラ: 重複ID')
require(len({i['repository'].lower() for i in comp['items']}) == len(comp['items']), '会話キャラ: 重複repository')
for i in comp['items']:
    require(i['url'] == 'https://github.com/' + i['repository'] and i['summary_ja'], f"{i['id']}: 会話キャラ項目不備")
    require(i['section_id'] in comp_sections, f"{i['id']}: 未定義セクション")
    require((i['catalog_id'] is None) == (i['repository'].lower() not in {p['repository'].lower() for p in items}) and (i['catalog_id'] is None or i['catalog_id'] in ids), f"{i['id']}: catalog_id不整合")
for name, content in {**render(data), **render_datasets(), **render_sota()}.items():
    require((ROOT / name).read_bytes() == content.encode("utf-8"), f"生成物が古い: {name}")
for path in ROOT.rglob("*.md"):
    if path.relative_to(ROOT).parts[0] == "cloudflare":  # node_modules とビルド生成物 public/
        continue
    for target in re.findall(r"\]\(([^)\s]+)\)", path.read_text(encoding="utf-8")):
        if target.startswith(("https://", "http://", "#", "mailto:")):
            continue
        local = unquote(target.split("#")[0])
        require((path.parent / local).exists(), f"リンク切れ: {path.name} -> {target}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Validated {len(items)} entries, {len(categories)} categories, JSON/JSONL/CSV, sources, model evidence, generated files and local links")
