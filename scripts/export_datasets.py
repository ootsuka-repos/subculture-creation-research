"""research/papers.json と companion-catalog.json から閲覧用Markdown・JSONLを生成する。--checkで生成物の一致を確認。"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def jsonl(rows):
    return "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows)


def cell(text):
    return (text or "").replace("|", "\\|").replace("\n", " ")


def model_links(models):
    out = []
    for m in models:
        u = m["url"]
        host = "HF" if "huggingface.co" in u else "GitHub" if "github.com" in u else "ModelScope" if "modelscope" in u else "配布先"
        out.append(f"[{host}]({u})")
    return " · ".join(out)


def render_papers(data, catalog_category):
    papers, cats = data["papers"], data["categories"]
    names = {c["id"]: c["name_ja"] for c in cats}
    out = {"research/papers.jsonl": jsonl(papers)}

    def table(rows):
        lines = ["| 論文 | 会議 | 何ができるか | 公式コード | モデル | 公開範囲・備考 |", "| --- | --- | --- | --- | --- | --- |"]
        for p in rows:
            title = f"[{cell(p['title'])}]({p['paper_url']})"
            if p["catalog_id"]:
                title += f"<br>[制作カタログ](../../categories/{catalog_category[p['catalog_id']]}.md#{p['catalog_id']})"
            venue = f"{p['venue']} {p['year']}" + (f"<br>{cell(p['venue_status'])}" if p["venue"] != "SIGGRAPH" else "")
            lic = "".join(f" · [条件]({u})" for u in p["code_license_urls"]) or " · 条件は各リポジトリ参照"
            note = " ".join(x for x in (p.get("release_scope_ja"), p.get("notes_ja")) if x)
            lines.append(f"| {title} | {venue} | {cell(p['summary_ja'])} | [{p['code_repository']}]({p['code_url']}){lic} | {model_links(p['models'])} | {cell(note)} |")
        return "\n".join(lines) + "\n"

    for c in cats:
        rows = [p for p in papers if p["category_id"] == c["id"]]
        out[f"research/papers/{c['id']}.md"] = (
            f"# {c['name_ja']}（{len(rows)}件）\n\n[研究一覧の索引](../papers.md) · [機械可読データ](../papers.json)\n\n"
            "公式コードと本研究の学習済み重みの両方が公開されている研究。公開は利用条件・商用利用可・動作確認を意味しない。"
            "各項目のコミット、モデルのrevision・確認ファイル、根拠URLは papers.json / papers.jsonl。\n\n" + table(rows))

    venue_rows = ["| 会議 | 採用年 | 件数 | 年度・確認状況 |", "| --- | --- | --- | --- |"]
    for v in data["venues"]:
        reason = cell(v["reason_ja"]) + (f" [根拠]({v['source_url']})" if v.get("source_url") else "")
        venue_rows.append(f"| {v['conference']} | {v['year']} | {v['included_count']} | {reason} |")
    cat_rows = ["| 分野 | 件数 | 論文 |", "| --- | --- | --- |"]
    for c in cats:
        rows = [p for p in papers if p["category_id"] == c["id"]]
        cat_rows.append(f"| [{c['name_ja']}](papers/{c['id']}.md) | {len(rows)} | " + "、".join(p["short_name"] for p in rows) + " |")
    rni = ["| 候補 | 理由 | 範囲 | 確認日 |", "| --- | --- | --- | --- |"]
    for x in data["reviewed_not_included"]:
        rni.append(f"| [{cell(x['name'])}]({x['code_url']}) | {cell(x['reason_ja'])} | {x['scope']} | {x['checked_on']} |")
    out["research/papers.md"] = (
        f"# アニメ・エンタメ向けAI研究 — 公式コード＋公開重み（{len(papers)}件）\n\n"
        f"最終確認日: {data['checked_on']}。[制作系リポジトリ一覧](../README.md) · [papers.json](papers.json) · [papers.jsonl](papers.jsonl)\n\n"
        + data["scope_ja"] + "\n\n"
        "## 掲載条件\n\n" + "\n".join(f"- {x}" for x in data["inclusion_criteria_ja"]) + "\n\n"
        "## 分野\n\n" + "\n".join(cat_rows) + "\n\n"
        "## 会議と年度\n\n年は採択・発表先の年。2026年大会がない、または採択未確定の会議は2025年を参照。"
        "本会議・Findings・Journal/TOG・開催前の採択告知を区別する。\n\n" + "\n".join(venue_rows) + "\n\n"
        "## 確認範囲と限界\n\n" + "\n".join(f"- {x}" for x in data["verification_limits_ja"]) + "\n\n"
        "## 必須条件を満たさず掲載しなかった候補\n\n" + "\n".join(rni) + "\n")
    return out


def render_companion(data, catalog_category):
    sections = {s["id"]: s["name_ja"] for s in data["sections"]}
    items = data["items"]
    text = (f"# 会話できるアニメ系AIキャラクター（{len(items)}件）\n\n"
            f"最終確認日: {data['checked_on']}。[制作系リポジトリ一覧](../README.md) · [companion-catalog.json](../companion-catalog.json) · [companion-catalog.jsonl](../companion-catalog.jsonl)\n\n"
            + data["scope_ja"] + "\n\n> " + data["notice_ja"] + "\n\n"
            "機能は各リポジトリの説明の要約で、ベンチマーク・動作検証の結果ではない。制作系カタログ（catalog.json）の項目のような固定コミット・メトリクス・入出力の整理は未実施で、一覧レベルの記録。\n\n"
            "## 目的から選ぶ\n\n| 目的 | まず見る | 導入前に確認すること |\n| --- | --- | --- |\n")
    text += "".join(f"| {g['purpose_ja']} | {g['start_with_md']} | {g['check_ja']} |\n" for g in data["selection_guide"])
    for sid, name in sections.items():
        text += f"\n## {name}\n\n"
        for i in items:
            if i["section_id"] == sid:
                ref = f" → [制作カタログ](../categories/{catalog_category[i['catalog_id']]}.md#{i['catalog_id']})" if i["catalog_id"] else ""
                text += f"- [{i['name']}]({i['url']}) — {i['summary_ja']}{ref}\n"
    text += ("\n## 探し方・掲載基準\n\n" + data["discovery_md"] + "\n\n" + "\n".join(f"- {x}" for x in data["criteria_ja"]) + "\n")
    return {"categories/companion.md": text, "companion-catalog.jsonl": jsonl(items)}


def render():
    catalog_category = {p["id"]: p["category"] for p in load("catalog.json")["items"]}
    out = render_papers(load("research/papers.json"), catalog_category)
    out.update(render_companion(load("companion-catalog.json"), catalog_category))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    files = render()
    if ap.parse_args().check:
        stale = [n for n, c in files.items() if not (ROOT / n).exists() or (ROOT / n).read_text(encoding="utf-8") != c]
        if stale:
            raise SystemExit("out of date (run scripts/export_datasets.py): " + ", ".join(stale))
        print(f"Checked {len(files)} files")
    else:
        for n, c in files.items():
            (ROOT / n).parent.mkdir(parents=True, exist_ok=True)
            (ROOT / n).write_text(c, encoding="utf-8")
        print(f"Exported {len(files)} files")
