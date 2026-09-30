"""sota-catalog.json からタスク別アニメ系SOTA資料（Markdown・JSONL・モデル用短縮版）を生成する。--checkで生成物の一致を確認。"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = {'selected': 'アニメ特化の最良', 'general_only': '汎用モデルのみ（アニメ特化なし）', 'none': 'モデルなし'}
CONF = {'high': '高', 'medium': '中', 'low': '低'}


def is_empty(t):
    return t['status'] == 'none' and not t.get('repositories')


def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def cell(text):
    return str(text if text is not None else '').replace('|', '\\|').replace('\n', ' ')


def anchor(t):
    return t['task_id'] + (f"--{t['subtask']}" if t.get('subtask') else '')


def title(t):
    return t['label_ja']


def license_short(b):
    lic = b.get('license_metadata') or '未記載'
    name = b.get('license_name_metadata')
    return f"{lic}/{name}" if name else lic


def model_link(b):
    return f"[{b['hub_repository']}]({b['url']}/tree/{b['revision']})"


def repo_line(g, catalog, up):
    rel = g.get('latest_release')
    rel_text = f" / release {rel['tag']} ({rel['published_at']})" if rel else ''
    cat = f" / 制作カタログ: [{g['catalog_id']}]({up}categories/{catalog[g['catalog_id']]}.md#{g['catalog_id']})" if g.get('catalog_id') else ''
    return (f"- [{g['repo']}]({g['url']}) — {g['role_ja']}（★{g['stars']:,} / {g.get('license') or 'ライセンス未表示'} / 最終push {g['pushed_at']}{rel_text} / "
            f"確認コミット [`{g['commit_sha'][:8]}`]({g['evidence_url']}){cat}）\n  - {g['why_ja']}\n")


def task_section(t, level, catalog, up):
    out = f"\n{level} {title(t)}\n\n<a id=\"{anchor(t)}\"></a>\n"
    out += f"- **判定**: {STATUS[t['status']]} / 確度 {CONF[t['confidence']]}\n"
    b = t.get('best')
    if b:
        out += f"- **最良**: {model_link(b)}（revision `{b['revision'][:8]}` / 作成 {b['created']} / 更新 {b['last_modified']}）\n"
        out += f"- **利用条件**: {license_short(b)}" + (' / gated' if b.get('gated') else '') + f"。{b['license_notes_ja']}\n"
    out += f"- **選定根拠**: {t['decision_ja']}\n"
    if b:
        out += (f"- **指標（確認日時点）**: DL累計 {b['downloads_all_time']:,}"
                + (f" / 直近30日 {b['downloads_30d']:,}" if b.get('downloads_30d') is not None else '')
                + f" / likes {b['likes']:,}" + (f" / Spaces {b['spaces']}" if b.get('spaces') is not None else '') + '\n')
        for label, key in [('概要', 'summary_ja'), ('入力', 'inputs_ja'), ('出力', 'outputs_ja'), ('必要環境', 'requirements_ja'), ('制約', 'limitations_ja'), ('使う版・派生', 'variants_ja')]:
            out += f"- **{label}**: {b[key]}\n"
        out += '- **根拠**: ' + ' / '.join(f"[{cell(e['supports'])}]({e['url']})" for e in b['evidence']) + '\n'
    if t.get('general_alternative'):
        g = t['general_alternative']
        out += f"- **強い汎用モデル（アニメ特化ではない・収録外）**: `{g['repo']}` — {g['note_ja']}\n"
    if t.get('runner_ups'):
        out += '- **次点**: ' + ' / '.join(f"`{r['repo']}`（{r['why_not_ja']}）" for r in t['runner_ups']) + '\n'
    if t.get('repositories'):
        out += '\n関連リポジトリ:\n\n' + ''.join(repo_line(g, catalog, up) for g in t['repositories'])
    return out


def render(data=None):
    data = data or load('sota-catalog.json')
    tasks = data['tasks']
    slices = data['slices']
    catalog = {p['id']: p['category'] for p in load('catalog.json')['items']}
    model_tasks = [t for t in tasks if not t['task_id'].startswith('repos-')]
    repo_tasks = [t for t in tasks if t['task_id'].startswith('repos-')]
    model_slices = [s for s in slices if any(t['slice'] == s['id'] for t in model_tasks)]
    n_best = sum(1 for t in model_tasks if t.get('best'))
    n_repo = len({g['repo'] for t in tasks for g in t.get('repositories', [])})
    empty = [t for t in model_tasks if is_empty(t)]
    shown = [t for t in model_tasks if not is_empty(t)]
    names = {s['id']: s['name_ja'] for s in slices}
    outputs = {}

    head = (f"# タスク別アニメ系SOTAモデル・関連リポジトリ（{data['updated_on']}）\n\n[一覧へ](../README.md) · [正本JSON](../sota-catalog.json) · [JSONL](../sota-catalog.jsonl) · [短縮版](../SOTA_CONTEXT.md) · [リポジトリ全体像](anime-repositories.md)\n\n"
            + data['scope_ja'] + '\n\n## 選定基準\n\n' + '\n'.join(f"{i}. {x}" for i, x in enumerate(data['criteria_ja'], 1)) + '\n\n'
            + '## 注意\n\n' + '\n'.join(f"- {x}" for x in data['caveats_ja'])
            + f"\n\n収録: モデル判定{len(model_tasks)}タスク（最良モデルあり{n_best}）、関連リポジトリ{n_repo}件（重複除く）。詳細は分野別ページ: "
            + ' · '.join(f"[{s['name_ja']}](sota/{s['id']}.md)" for s in model_slices) + ' · [検討したが選ばなかったもの](sota/not-included.md)\n')
    summary = '\n## 一覧\n\n| 分野 | タスク | 最良モデル | 利用条件 | 確度 | 判定 |\n| --- | --- | --- | --- | --- | --- |\n'
    for t in shown:
        b = t.get('best')
        summary += (f"| {names[t['slice']]} | [{cell(title(t))}](sota/{t['slice']}.md#{anchor(t)}) | " + (model_link(b) if b else 'モデルなし（リポジトリのみ）') + " | "
                    + (cell(license_short(b)) if b else '—') + f" | {CONF[t['confidence']]} | {STATUS[t['status']]} |\n")
    if empty:
        summary += '\n## 該当なし（アニメ特化モデルも実用的な汎用モデルも見つからなかったタスク）\n\n| タスク | 確認した範囲と理由 |\n| --- | --- |\n' + ''.join(f"| {cell(title(t))} | {cell(t['decision_short_ja'])} |\n" for t in empty)
    outputs['models/anime-task-sota.md'] = head + summary

    for s in model_slices:
        page = (f"# {s['name_ja']}のアニメ系SOTA（{data['updated_on']}）\n\n[一覧へ](../anime-task-sota.md) · [リポジトリ全体像](../anime-repositories.md) · [正本JSON](../../sota-catalog.json)\n\n"
                '選定基準・注意は[一覧ページ](../anime-task-sota.md)。各項目の「最良」は確度付きの編集判断で、重み取得・推論実行は未実施。\n')
        for t in shown:
            if t['slice'] == s['id']:
                page += task_section(t, '###', catalog, '../../')
        outputs[f"models/sota/{s['id']}.md"] = page

    rej = data.get('reviewed_not_included', [])
    rpage = f"# 検討したが選ばなかったもの（{data['updated_on']}）\n\n[一覧へ](../anime-task-sota.md)\n\n最良に選ばなかった理由の記録。成人向け専用モデル、ライセンス・由来が不明なもの、停滞、用途違いなど。\n"
    for s in slices:
        rs = [r for r in rej if r['slice'] == s['id']]
        if rs:
            rpage += f"\n## {s['name_ja']}\n\n| 対象 | 理由 |\n| --- | --- |\n" + ''.join(f"| `{cell(r['repo'])}` | {cell(r['reason_ja'])} |\n" for r in rs)
    outputs['models/sota/not-included.md'] = rpage

    rhead = (f"# アニメ・サブカル制作のリポジトリ全体像（{data['updated_on']}）\n\n[SOTA一覧へ](anime-task-sota.md) · [正本JSON](../sota-catalog.json)\n\n"
             '制作工程ごとに、採用実績・更新状況・ライセンスを確認して選んだ代表リポジトリ。'
             '星数は累計。更新状況は確認コミットと最終pushを併記し、12か月以上更新がないものは停滞として注記。起動・動作検証は未実施。\n')
    for t in repo_tasks:
        rhead += task_section(t, '##', catalog, '../').replace('- **判定**: モデルなし / 確度', '- **確度**:').replace('- **選定根拠**', '- **選定基準と順位の根拠**')
    outputs['models/anime-repositories.md'] = rhead
    outputs['sota-catalog.jsonl'] = ''.join(json.dumps(t, ensure_ascii=False, separators=(',', ':')) + '\n' for t in tasks)

    ctx = (f"# アニメ系タスク別SOTA・開発コンテキスト（{data['updated_on']}）\n\nHFのタスク分類ごとのアニメ系最良モデルと関連リポジトリの短縮版（一括投入用）。"
           '選定根拠の詳細は models/anime-task-sota.md と models/sota/<分野>.md、機械可読は sota-catalog.jsonl。\n\n'
           + '\n'.join(f"- {x}" for x in data['caveats_ja']) + '\n')
    for s in slices:
        ts = [t for t in tasks if t['slice'] == s['id']]
        if not ts:
            continue
        ctx += f"\n## {s['name_ja']}\n"
        for t in ts:
            b = t.get('best')
            if t['task_id'].startswith('repos-'):
                ctx += f"\n- **{title(t)}**: " + ' / '.join(f"{g['repo']}(★{g['stars']:,},{g.get('license') or '未表示'},push {g['pushed_at']})" for g in t['repositories']) + f"\n  - {t['decision_short_ja']}\n"
                continue
            if is_empty(t):
                ctx += f"\n- **{title(t)}**: 該当なし。{t['decision_short_ja']}\n"
                continue
            ctx += f"\n- **{title(t)}** [{STATUS[t['status']]} / 確度{CONF[t['confidence']]}]: "
            if b:
                ctx += f"`{b['hub_repository']}`@{b['revision'][:8]}（{license_short(b)}、DL累計{b['downloads_all_time']:,}、likes {b['likes']:,}）{b['summary_ja']}\n"
            else:
                ctx += 'モデルなし（リポジトリのみ）\n'
            ctx += f"  - 選定: {t['decision_short_ja']}\n"
            if t.get('repositories'):
                ctx += '  - リポジトリ: ' + ' / '.join(f"{g['repo']}(★{g['stars']:,},{g.get('license') or '未表示'})" for g in t['repositories']) + '\n'
    outputs['SOTA_CONTEXT.md'] = ctx
    return outputs


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    files = render()
    if ap.parse_args().check:
        stale = [n for n, c in files.items() if not (ROOT / n).exists() or (ROOT / n).read_text(encoding='utf-8') != c]
        if stale:
            raise SystemExit('out of date (run scripts/export_sota.py): ' + ', '.join(stale))
        print(f'Checked {len(files)} files')
    else:
        for n, c in files.items():
            (ROOT / n).parent.mkdir(parents=True, exist_ok=True)
            (ROOT / n).write_text(c, encoding='utf-8')
        print(f'Exported {len(files)} files')
