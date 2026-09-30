"""既存項目の数値（GitHubの★・fork・最終push・archived・最新Release、HFのDL数・likes・更新日）を最新化する。

固定コミット（code_revision / revision / commit_sha）と本文は変えない。環境変数 GITHUB_TOKEN があれば使う。
"""
import datetime
import json
import os
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.date.today().isoformat()


def get(url):
    """JSONを取得。削除・非公開・gated、または再試行しても失敗したものは None（呼び出し側は前回値を残す）。"""
    headers = {'User-Agent': 'subculture-research-refresh', 'Accept': 'application/vnd.github+json'}
    if 'api.github.com' in url and os.environ.get('GITHUB_TOKEN'):
        headers['Authorization'] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 404, 451):
                return None
        except (urllib.error.URLError, TimeoutError):
            pass
        time.sleep(2 ** attempt)
    print(f'skip (failed 3x): {url}')
    return None


def github(repo):
    info = get(f'https://api.github.com/repos/{repo}')
    if info is None:
        return None
    release = get(f'https://api.github.com/repos/{repo}/releases/latest')
    return info, release


def hf(repo):
    return get(f'https://huggingface.co/api/models/{repo}?expand[]=downloads&expand[]=downloadsAllTime&expand[]=likes&expand[]=lastModified')


def load(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))


def save(name, data):
    """元ファイルのインデント幅と末尾改行を保って書き戻す（差分を値の変更だけにする）。"""
    old = (ROOT / name).read_text(encoding='utf-8')
    second = old.split('\n', 2)[1]
    indent = len(second) - len(second.lstrip(' '))
    (ROOT / name).write_text(json.dumps(data, ensure_ascii=False, indent=indent) + ('\n' if old.endswith('\n') else ''), encoding='utf-8')


def main():
    catalog, sota, models = load('catalog.json'), load('sota-catalog.json'), load('model-catalog.json')
    gh_repos = {p['repository'] for p in catalog['items']}
    gh_repos |= {g['repo'] for t in sota['tasks'] for g in t.get('repositories') or []}
    hf_repos = {t['best']['hub_repository'] for t in sota['tasks'] if t.get('best')} | {m['hub_repository'] for m in models['items']}
    with ThreadPoolExecutor(16) as pool:
        gh = dict(zip(gh_repos, pool.map(github, gh_repos)))
        hub = dict(zip(hf_repos, pool.map(hf, hf_repos)))

    changed = 0
    for p in catalog['items']:
        if not gh.get(p['repository']):
            continue
        info, release = gh[p['repository']]
        m = p['metrics']
        m.update(stars=info['stargazers_count'], forks=info['forks_count'], pushed_at=info['pushed_at'], archived=info['archived'], checked_on=TODAY)
        if release:
            p['deep_dive']['latest_github_release'] = {k: release[k] for k in ('tag_name', 'html_url', 'published_at', 'prerelease')}
        changed += 1
    for t in sota['tasks']:
        for g in t.get('repositories') or []:
            if not gh.get(g['repo']):
                continue
            info, release = gh[g['repo']]
            g.update(stars=info['stargazers_count'], pushed_at=info['pushed_at'][:10], license=(info.get('license') or {}).get('spdx_id') or g.get('license'))
            if release:
                g['latest_release'] = {'tag': release['tag_name'], 'published_at': release['published_at'][:10]}
            changed += 1
        b = t.get('best')
        if b and hub.get(b['hub_repository']):
            h = hub[b['hub_repository']]
            b.update(downloads_30d=h.get('downloads', b['downloads_30d']), downloads_all_time=h.get('downloadsAllTime', b['downloads_all_time']),
                     likes=h.get('likes', b['likes']), last_modified=(h.get('lastModified') or b['last_modified'])[:10])
            changed += 1
    for m in models['items']:
        h = hub.get(m['hub_repository'])
        if h:
            m['metrics'].update(downloads_last_month=h.get('downloads', m['metrics']['downloads_last_month']), likes=h.get('likes', m['metrics']['likes']),
                                last_modified=h.get('lastModified') or m['metrics']['last_modified'], checked_on=TODAY)
            changed += 1
    catalog['metrics_refreshed_on'] = sota['metrics_refreshed_on'] = models['metrics_refreshed_on'] = TODAY
    save('catalog.json', catalog)
    save('sota-catalog.json', sota)
    save('model-catalog.json', models)
    print(f'refreshed {changed} records ({len(gh_repos)} GitHub, {len(hf_repos)} HF)')


if __name__ == '__main__':
    main()
