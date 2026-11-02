// Copies the public Terms and Privacy text from the Rodinka app repository
// into data/legal-content.json, which generate_site.py renders as /terms/ and
// /privacy/ on mojerodinka.cz. The app stays the single source of truth: never
// edit the JSON by hand, change Rodinka/src/features/legal/ and run
//
//   node tools/sync_legal_content.mjs ../Rodinka
//
// Only sections meant for the web are kept (`audience` absent or containing
// 'web'), the same filter LegalScreen applies in the browser build.

import { execFileSync } from 'node:child_process'
import { mkdtempSync, readFileSync, rmSync, writeFileSync } from 'node:fs'
import { stripTypeScriptTypes } from 'node:module'
import { tmpdir } from 'node:os'
import { join, resolve } from 'node:path'
import { pathToFileURL } from 'node:url'

const appRoot = resolve(process.argv[2] ?? '../Rodinka')
const legalDir = join(appRoot, 'src/features/legal')
const out = resolve(import.meta.dirname, '../data/legal-content.json')
const work = mkdtempSync(join(tmpdir(), 'rodinka-legal-'))

try {
  const operator = stripTypeScriptTypes(readFileSync(join(legalDir, 'operator.ts'), 'utf8'))
  const content = stripTypeScriptTypes(readFileSync(join(legalDir, 'legalContent.ts'), 'utf8'))
    .replace("from './operator'", "from './operator.mjs'")
  if (/^\s*import\s+(?!type)[^\n]*from\s+'(?!\.\/operator\.mjs')/m.test(content)) {
    throw new Error('legalContent.ts gained a runtime import; extend this script before syncing.')
  }
  writeFileSync(join(work, 'operator.mjs'), operator)
  writeFileSync(join(work, 'legalContent.mjs'), content)
  const { OPERATOR } = await import(pathToFileURL(join(work, 'operator.mjs')).href)
  const { LEGAL_CONTENT } = await import(pathToFileURL(join(work, 'legalContent.mjs')).href)

  const forWeb = (page) => ({
    title: page.title,
    intro: page.intro ?? '',
    sections: page.sections
      .filter((section) => !section.audience || section.audience.includes('web'))
      .map(({ heading, paragraphs, items }) => ({ heading, paragraphs, items: items ?? [] })),
  })
  const languages = Object.fromEntries(Object.entries(LEGAL_CONTENT).map(([language, value]) => [language, {
    operatorHeading: value.operatorHeading,
    registrationLabel: value.registrationLabel,
    lastUpdated: value.lastUpdated,
    terms: forWeb(value.terms),
    privacy: forWeb(value.privacy),
  }]))
  for (const language of ['cs', 'sk', 'en']) {
    if (!languages[language]) throw new Error(`Missing ${language} legal content`)
  }
  if (!OPERATOR.legalName?.trim() || !OPERATOR.contactEmail?.trim()) {
    throw new Error('Operator details are not published in the app; refusing to sync.')
  }

  const commit = execFileSync('git', ['-C', appRoot, 'rev-parse', '--short', 'HEAD'], { encoding: 'utf8' }).trim()
  const payload = {
    source: `iLoopak/Rodinka src/features/legal @ ${commit}`,
    operator: OPERATOR,
    languages,
  }
  writeFileSync(out, `${JSON.stringify(payload, null, 2)}\n`)
  console.log(`Wrote ${out} from ${payload.source}.`)
} finally {
  rmSync(work, { recursive: true, force: true })
}
