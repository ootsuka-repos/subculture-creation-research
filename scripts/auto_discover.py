"""DeepSeek に GitHub/HF を検索させ、未収録の制作系リポジトリを catalog.json / companion-catalog.json に、HFモデルを model-catalog.json に追加する。

AIが書くのは分類と日本語の説明文だけで、固定コミット/revision・★/DL数・ライセンス・根拠URLは GitHub/HF API から機械的に埋める。
環境変数: DEEPSEEK_API_KEY（必須）、GITHUB_TOKEN（推奨）、DEEPSEEK_MODEL、MAX_ADDITIONS（リポジトリ）、MAX_MODEL_ADDITIONS（HFモデル）。
"""
import datetime
import json
import os
import re
import urllib.parse
import urllib.request

from refresh_metrics import ROOT, get, load, save

TODAY = datetime.date.today().isoformat()
MODEL = os.environ.get('DEEPSEEK_MODEL', 'deepseek-flash')
MAX_ADDITIONS = int(os.environ.get('MAX_ADDITIONS', '10'))
MAX_MODEL_ADDITIONS = int(os.environ.get('MAX_MODEL_ADDITIONS', '5'))
WEIGHT_EXT = ('.safetensors', '.ckpt', '.bin', '.gguf', '.onnx', '.pth', '.pt')
MAX_TURNS = 80

catalog = load('catalog.json')
companions = load('companion-catalog.json')
sota = load('sota-catalog.json')
papers = load('research/papers.json')
rejected = load('reviewed-not-included.json')
models = load('model-catalog.json')
known = {r.lower() for r in (
    [p['repository'] for p in catalog['items']] + [c.get('repository') or '' for c in companions['items']]
    + [g['repo'] for t in sota['tasks'] for g in t.get('repositories') or []] + [r['repo'] for r in sota['reviewed_not_included']]
    + [p['code_repository'] for p in papers['papers']] + [r.get('repository') or '' for r in rejected['items']]) if r}
added = []
added_models = []
known_models = {r.lower() for r in (
    [m['hub_repository'] for m in models['items']]
    + [t['best']['hub_repository'] for t in sota['tasks'] if t.get('best')]
    + [r['repo'] for t in sota['tasks'] for r in t.get('runner_ups') or []]
    + [t['general_alternative']['repo'] for t in sota['tasks'] if t.get('general_alternative')])}
MODEL_TEXT_FIELDS = ['architecture_ja', 'variants_ja', 'prompting_ja', 'requirements_ja', 'limitations_ja', 'license_notes_ja',
                     'assessment_ja', 'next_validation_ja']

ENUMS = {
    'category': [c['id'] for c in catalog['categories']],
    'kind': sorted({p['kind'] for p in catalog['items']}),
    'ai_role': sorted({p['ai_role'] for p in catalog['items']}),
    'maturity': sorted({p['maturity'] for p in catalog['items']}),
}
TEXT_FIELDS = ['summary_ja', 'inputs_ja', 'outputs_ja', 'assessment_ja', 'status_ja', 'requirements_ja', 'limitations_ja',
               'dependencies_ja', 'production_fit_ja', 'next_validation_ja']


def repo_info(repo):
    info = get(f'https://api.github.com/repos/{repo}')
    if info is None or info['private'] or info['fork']:
        raise ValueError(f'{repo}: 取得できない（非公開・fork・存在しない）')
    return info


def tool_search_github(query, sort='stars'):
    q = urllib.parse.quote(query)
    res = get(f'https://api.github.com/search/repositories?q={q}&sort={sort}&per_page=20') or {'items': []}
    return [{'repo': r['full_name'], 'description': r['description'], 'stars': r['stargazers_count'], 'pushed_at': r['pushed_at'][:10],
             'topics': r.get('topics', [])[:8], 'already_listed': r['full_name'].lower() in known} for r in res['items']]


def tool_search_huggingface(query, sort='trendingScore'):
    q = urllib.parse.quote(query)
    res = get(f'https://huggingface.co/api/models?search={q}&sort={sort}&limit=20') or []
    return [{'model': m['id'], 'pipeline_tag': m.get('pipeline_tag'), 'downloads': m.get('downloads'), 'likes': m.get('likes')} for m in res]


def tool_read_readme(repository):
    info = repo_info(repository)
    readme = get(f'https://api.github.com/repos/{repository}/readme')
    text = ''
    if readme:
        with urllib.request.urlopen(readme['download_url'], timeout=30) as r:
            text = r.read().decode('utf-8', 'replace')
    return {'repo': info['full_name'], 'description': info['description'], 'stars': info['stargazers_count'], 'pushed_at': info['pushed_at'],
            'license': (info.get('license') or {}).get('spdx_id'), 'archived': info['archived'],
            'already_listed': info['full_name'].lower() in known, 'readme': text[:8000]}


def slug(repo):
    base = re.sub(r'[^a-z0-9]+', '-', repo.split('/')[1].lower()).strip('-')
    ids = {p['id'] for p in catalog['items']}
    return base if base not in ids else re.sub(r'[^a-z0-9]+', '-', repo.lower()).strip('-')


def tool_add_catalog_item(repository, category, kind, ai_role, maturity, tags=None, **text):
    if len(added) >= MAX_ADDITIONS:
        raise ValueError('今回のGitHubリポジトリ追加は上限に達した')
    if repository.lower() in known:
        raise ValueError(f'{repository} は収録済み')
    for field, allowed in (('category', category), ('kind', kind), ('ai_role', ai_role), ('maturity', maturity)):
        if allowed not in ENUMS[field]:
            raise ValueError(f'{field}={allowed} は不可。候補: {ENUMS[field]}')
    missing = [f for f in TEXT_FIELDS if not text.get(f)]
    if missing:
        raise ValueError(f'未記入: {missing}')
    info = repo_info(repository)
    repo = info['full_name']
    branch = info['default_branch']
    commit = get(f'https://api.github.com/repos/{repo}/commits/{branch}')
    sha = commit['sha']
    tree = get(f'https://api.github.com/repos/{repo}/git/trees/{sha}?recursive=1') or {'tree': [], 'truncated': False}
    files = [t['path'] for t in tree['tree'] if t['type'] == 'blob']
    entry_files = [f for f in files if re.search(r'(^|/)(main|app|index|cli|run|server|inference|demo)\.(py|ts|tsx|js|rs|go|cpp)$', f)][:3]
    readme = get(f'https://api.github.com/repos/{repo}/readme')
    readme_path = readme['path'] if readme else 'README.md'
    entry_files = entry_files or [readme_path]
    release = get(f'https://api.github.com/repos/{repo}/releases/latest')
    tree_url = f'https://github.com/{repo}/tree/{sha}'
    item = {
        'id': slug(repo), 'name': info['name'], 'repository': repo, 'url': info['html_url'], 'category': category, 'kind': kind,
        'ai_role': ai_role, 'maturity': maturity,
        **{k: text[k] for k in ('inputs_ja', 'outputs_ja', 'summary_ja', 'assessment_ja', 'status_ja', 'requirements_ja', 'limitations_ja', 'dependencies_ja')},
        'checked_on': TODAY, 'code_revision': sha,
        'verification': {'readme_reviewed': True, 'repository_tree_checked': True, 'runtime_tested': False, 'weights_downloaded': False,
                         'weights_file_inventory_verified': False},
        'metrics': {'stars': info['stargazers_count'], 'forks': info['forks_count'], 'created_at': info['created_at'], 'pushed_at': info['pushed_at'],
                    'archived': info['archived'], 'checked_on': TODAY, 'star_growth': None, 'snapshot_path': None},
        'license': {'github_detected_spdx': (info.get('license') or {}).get('spdx_id') or 'NOASSERTION', 'independently_reviewed': False,
                    'commercial_use': 'not_assessed', 'source': tree_url},
        'sources': [
            {'url': f'https://github.com/{repo}/blob/{sha}/{readme_path}', 'supports': '機能・入出力・環境・制約についての公式説明'},
            {'url': f'https://api.github.com/repos/{repo}', 'supports': '累計スター・作成日・最終push・アーカイブ・自動ライセンス判定'},
            {'url': tree_url, 'supports': '確認コミットのファイル構成'},
        ],
        'tags': tags or [category], 'repository_role': 'implementation', 'evidence_files': entry_files,
        'evidence_files_verification': 'tree_presence_only', 'model_resources': [],
        'model_scope_ja': '自動追加。モデル配布先のファイル一覧は未確認。', 'relations': [],
        'deep_dive': {
            'reviewed_on': TODAY, 'production_fit_ja': text['production_fit_ja'], 'next_validation_ja': text['next_validation_ja'],
            'entry_points': [{'path': f, 'url': f'https://github.com/{repo}/blob/{sha}/{f}', 'verification': 'tree_presence_only'} for f in entry_files],
            'latest_github_release': {k: release[k] for k in ('tag_name', 'html_url', 'published_at', 'prerelease')} if release else None,
            'default_branch_commit_at': commit['commit']['committer']['date'], 'tree_truncated': tree['truncated'],
            'repository_file_count': len(files), 'source_inspections': [],
            'scope_note_ja': 'AI（自動調査）がREADMEから要約した項目。人による確認・起動・品質比較は未実施。',
            'license_notes_ja': 'コードのGitHub自動判定のみ。モデル・素材の条件と商用可否は未確認。',
        },
    }
    catalog['items'].append(item)
    known.add(repo.lower())
    added.append(f'catalog:{item["id"]}')
    return {'added': item['id']}


def tool_add_companion(repository, section_id, summary_ja):
    if len(added) >= MAX_ADDITIONS:
        raise ValueError('今回のGitHubリポジトリ追加は上限に達した')
    if repository.lower() in known:
        raise ValueError(f'{repository} は収録済み')
    sections = [s['id'] for s in companions['sections']]
    if section_id not in sections:
        raise ValueError(f'section_id は {sections} のどれか')
    info = repo_info(repository)
    repo = info['full_name']
    item = {'id': re.sub(r'[^a-z0-9]+', '-', repo.lower()).strip('-'), 'name': info['name'], 'url': info['html_url'], 'repository': repo,
            'section_id': section_id, 'summary_ja': summary_ja, 'catalog_id': None, 'checked_on': TODAY}
    companions['items'].append(item)
    known.add(repo.lower())
    added.append(f'companion:{item["id"]}')
    return {'added': item['id']}


def hf_model(model_id):
    info = get(f'https://huggingface.co/api/models/{model_id}?expand[]=sha&expand[]=gated&expand[]=cardData&expand[]=siblings'
               '&expand[]=downloads&expand[]=likes&expand[]=lastModified&expand[]=pipeline_tag&expand[]=createdAt')
    if info is None:
        raise ValueError(f'{model_id}: 取得できない（非公開・削除・存在しない）')
    return info


def tool_read_model_card(model_id):
    info = hf_model(model_id)
    card = ''
    try:
        with urllib.request.urlopen(f"https://huggingface.co/{info['id']}/raw/{info['sha']}/README.md", timeout=30) as r:
            card = r.read().decode('utf-8', 'replace')
    except urllib.error.HTTPError:
        pass
    weights = [s['rfilename'] for s in info.get('siblings', []) if s['rfilename'].endswith(WEIGHT_EXT)]
    return {'model': info['id'], 'pipeline_tag': info.get('pipeline_tag'), 'created': info.get('createdAt'), 'last_modified': info.get('lastModified'),
            'downloads_30d': info.get('downloads'), 'likes': info.get('likes'), 'gated': info.get('gated'),
            'license': (info.get('cardData') or {}).get('license'), 'weight_files': weights[:20],
            'already_listed': info['id'].lower() in known_models, 'model_card': card[:8000]}


def tool_add_hf_model(model_id, category, **text):
    if len(added_models) >= MAX_MODEL_ADDITIONS:
        raise ValueError('今回のHFモデル追加は上限に達した')
    if model_id.lower() in known_models:
        raise ValueError(f'{model_id} は収録済み')
    if category not in ENUMS['category']:
        raise ValueError(f"category は {ENUMS['category']} のどれか")
    missing = [f for f in MODEL_TEXT_FIELDS if not text.get(f)]
    if missing:
        raise ValueError(f'未記入: {missing}')
    info = hf_model(model_id)
    repo, sha = info['id'], info['sha']
    weights = [s['rfilename'] for s in info.get('siblings', []) if s['rfilename'].endswith(WEIGHT_EXT)]
    if not weights:
        raise ValueError(f'{repo}: 重みファイルがない（コードやデータセットだけのリポジトリは対象外）')
    card = info.get('cardData') or {}
    ids = {m['id'] for m in models['items']}
    mid = re.sub(r'[^a-z0-9]+', '-', repo.split('/')[1].lower()).strip('-')
    item = {
        'id': mid if mid not in ids else re.sub(r'[^a-z0-9]+', '-', repo.lower()).strip('-'), 'name': repo.split('/')[1],
        'hub_repository': repo, 'url': f'https://huggingface.co/{repo}', 'category': category, 'checked_on': TODAY,
        **{f: text[f] for f in MODEL_TEXT_FIELDS},
        'distribution': {
            'url': f'https://huggingface.co/{repo}', 'api_url': f'https://huggingface.co/api/models/{repo}', 'checked_on': TODAY,
            'http_status': 200, 'weights_downloaded': False, 'verification': 'file_listing_checked', 'revision': sha,
            'gated': info.get('gated') or False, 'license_metadata': card.get('license'), 'license_name_metadata': card.get('license_name'),
            'evidence_files': weights[:4], 'matching_weight_file_count': len(weights)},
        'verification': {'model_card_reviewed': True, 'file_inventory_checked': True, 'weights_downloaded': False, 'runtime_tested': False},
        'metrics': {'downloads_last_month': info.get('downloads'), 'likes': info.get('likes'), 'last_modified': info.get('lastModified'), 'checked_on': TODAY},
        'sources': [
            {'url': f'https://huggingface.co/{repo}/blob/{sha}/README.md', 'supports': 'モデルカードの能力・系統・推奨設定・利用条件（AI自動調査による要約）'},
            {'url': f'https://huggingface.co/api/models/{repo}', 'supports': 'revision・ファイル一覧・アクセスとライセンスメタデータ'},
        ],
    }
    models['items'].append(item)
    known_models.add(repo.lower())
    added_models.append(f'model:{item["id"]}')
    return {'added': item['id']}

text_props = {f: {'type': 'string'} for f in TEXT_FIELDS}
TOOLS = {
    'search_github': (tool_search_github, 'GitHubリポジトリ検索（GitHub検索構文。例: "anime tts created:>2026-08-01", "live2d llm stars:>50"）。sort=stars|updated',
                      {'query': {'type': 'string'}, 'sort': {'type': 'string', 'enum': ['stars', 'updated']}}, ['query']),
    'search_huggingface': (tool_search_huggingface, 'Hugging Faceモデル検索。関連するGitHub実装を探す手掛かりに使う',
                           {'query': {'type': 'string'}, 'sort': {'type': 'string', 'enum': ['trendingScore', 'downloads', 'likes']}}, ['query']),
    'read_readme': (tool_read_readme, 'リポジトリのREADME・★・ライセンス・収録済みかを読む。追加前に必ず読む', {'repository': {'type': 'string'}}, ['repository']),
    'add_catalog_item': (tool_add_catalog_item, '制作カタログに1件追加。READMEに書かれた事実だけで日本語の各欄を書く（*_jaは短い日本語文）', {
        'repository': {'type': 'string', 'description': 'owner/name'},
        'category': {'type': 'string', 'enum': ENUMS['category']}, 'kind': {'type': 'string', 'enum': ENUMS['kind']},
        'ai_role': {'type': 'string', 'enum': ENUMS['ai_role']}, 'maturity': {'type': 'string', 'enum': ENUMS['maturity']},
        'tags': {'type': 'array', 'items': {'type': 'string'}}, **text_props}, ['repository', 'category', 'kind', 'ai_role', 'maturity', *TEXT_FIELDS]),
    'add_companion': (tool_add_companion, '会話できるアニメ系AIキャラクター（Live2D/VRM/AI VTuber等）一覧に1件追加', {
        'repository': {'type': 'string'}, 'section_id': {'type': 'string', 'enum': [s['id'] for s in companions['sections']]},
        'summary_ja': {'type': 'string'}}, ['repository', 'section_id', 'summary_ja']),
    'read_model_card': (tool_read_model_card, 'HFモデルのモデルカード・重みファイル・DL数・ライセンス・収録済みかを読む。add_hf_model の前に必ず読む',
                        {'model_id': {'type': 'string', 'description': 'owner/name'}}, ['model_id']),
    'add_hf_model': (tool_add_hf_model, 'アニメ・イラスト・キャラ音声などサブカル制作向けのHFモデル（重み配布あり）をモデル一覧に1件追加。モデルカードの事実だけで各欄を書く', {
        'model_id': {'type': 'string'}, 'category': {'type': 'string', 'enum': ENUMS['category']},
        **{f: {'type': 'string'} for f in MODEL_TEXT_FIELDS}}, ['model_id', 'category', *MODEL_TEXT_FIELDS]),
}

SYSTEM = f"""あなたは二次元・サブカル制作（漫画・イラスト・アニメ・ゲーム・3D・TTS/歌声・ASMR・VTuber・翻訳など）向けAI/ツールの調査員。
今日は {TODAY}。GitHub/HFを検索し、まだ収録されていない有用なものを、GitHubリポジトリ最大{MAX_ADDITIONS}件・HFモデル最大{MAX_MODEL_ADDITIONS}件追加する。
- HFモデル: search_huggingface（sort=trendingScore など）でアニメ・イラスト・キャラ音声・歌声・漫画OCR等の新しいモデルを探し、read_model_card → add_hf_model。
  アニメ特化でない汎用基盤モデル、量子化や再アップロードだけのコピー、LoRA単体の大量投稿、成人向け専用は除外。
- 優先: 直近数か月に公開・更新された、制作で実際に使えるもの（アニメ特化モデルの実装、ComfyUIノード、Live2D/VRM、TTS、漫画翻訳など）。
- 除外: already_listed=true、成人向け専用、中身のないリスト・宣伝だけのリポジトリ、archived。
- 追加前に read_readme で内容を確認し、README の事実に基づいて書く。性能の断定や商用可の断定はしない。
- 会話キャラ（LLM+Live2D/VRMのコンパニオン、AI VTuber）は add_companion、それ以外のGitHubリポジトリは add_catalog_item。
- 例（モデル一覧の書き方）: {json.dumps({k: models['items'][0][k] for k in MODEL_TEXT_FIELDS}, ensure_ascii=False)}
- 分野: {json.dumps({c['id']: c['name_ja'] for c in catalog['categories']}, ensure_ascii=False)}
- 例（既存項目の書き方）: {json.dumps({k: catalog['items'][5][k] for k in ['summary_ja', 'inputs_ja', 'outputs_ja', 'assessment_ja', 'status_ja', 'requirements_ja', 'limitations_ja', 'dependencies_ja']}, ensure_ascii=False)}
追加が終わったら、ツールを呼ばずに追加件数を一言で返して終了する。"""


def chat(messages):
    body = {'model': MODEL, 'messages': messages,
            'tools': [{'type': 'function', 'function': {'name': n, 'description': d, 'parameters': {'type': 'object', 'properties': p, 'required': r}}}
                      for n, (_, d, p, r) in TOOLS.items()]}
    req = urllib.request.Request('https://api.deepseek.com/chat/completions', data=json.dumps(body).encode(),
                                 headers={'Authorization': f"Bearer {os.environ['DEEPSEEK_API_KEY']}", 'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=600) as r:
        return json.load(r)['choices'][0]['message']


def main():
    messages = [{'role': 'system', 'content': SYSTEM}, {'role': 'user', 'content': '調査を開始して追加して。'}]
    for _ in range(MAX_TURNS):
        msg = chat(messages)
        messages.append(msg)
        calls = msg.get('tool_calls') or []
        if not calls:
            print('agent:', msg.get('content'))
            break
        for call in calls:
            name = call['function']['name']
            try:
                args = json.loads(call['function']['arguments'] or '{}')
                result = TOOLS[name][0](**args)
            except Exception as e:  # ツールの失敗はAIに返して続行させる
                result = {'error': str(e)}
            print(f'{name}({call["function"]["arguments"][:120]}) -> {json.dumps(result, ensure_ascii=False)[:160]}')
            messages.append({'role': 'tool', 'tool_call_id': call['id'], 'content': json.dumps(result, ensure_ascii=False)})
        if len(added) >= MAX_ADDITIONS and len(added_models) >= MAX_MODEL_ADDITIONS:
            break
    if added:
        catalog['updated_on'] = TODAY
        companions['checked_on'] = TODAY
        save('catalog.json', catalog)
        save('companion-catalog.json', companions)
    if added_models:
        models['updated_on'] = TODAY
        save('model-catalog.json', models)
    print(f'added {len(added)}: {added}')
    print(f'added models {len(added_models)}: {added_models}')


if __name__ == '__main__':
    main()
