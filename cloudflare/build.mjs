// 正本JSONと解説Markdownを public/ にコピーし、文書一覧 docs-index.json を作る（Workerの静的アセット）。
import { cpSync, mkdirSync, readdirSync, readFileSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, join, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = dirname(HERE);
const OUT = join(HERE, 'public');
const SOURCES = ['catalog.json', 'sota-catalog.json', 'model-catalog.json', 'companion-catalog.json',
  'research/papers.json', 'reviewed-not-included.json'];
const SKIP = new Set(['.git', 'node_modules', 'cloudflare']);

function* walk(dir) {
  for (const e of readdirSync(dir, { withFileTypes: true }).sort((a, b) => a.name.localeCompare(b.name))) {
    if (SKIP.has(e.name)) continue;
    const p = join(dir, e.name);
    if (e.isDirectory()) yield* walk(p);
    else if (/\.(md|txt)$/.test(e.name)) yield p;
  }
}

rmSync(OUT, { recursive: true, force: true });
for (const f of SOURCES) {
  mkdirSync(dirname(join(OUT, 'data', f)), { recursive: true });
  cpSync(join(ROOT, f), join(OUT, 'data', f));
}
const docs = [];
for (const p of walk(ROOT)) {
  const rel = relative(ROOT, p).split('\\').join('/');
  const text = readFileSync(p, 'utf8');
  const title = text.match(/^#{1,6}\s+(.+)$/m)?.[1].trim() ?? rel;
  docs.push({ path: rel, title, chars: text.length });
  mkdirSync(dirname(join(OUT, 'docs', rel)), { recursive: true });
  cpSync(p, join(OUT, 'docs', rel));
}
writeFileSync(join(OUT, 'docs-index.json'), JSON.stringify(docs));
console.log(`public/: ${SOURCES.length} datasets, ${docs.length} documents`);
