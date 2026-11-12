"""Verify the generated legal mirrors and refund guide against the app snapshot."""
import json
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / 'data/legal-content.json').read_text(encoding='utf-8'))


class Text(HTMLParser):
    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.feed(html)

    def handle_data(self, data):
        self.parts.append(data)


def normalized(value):
    return ' '.join(value.split())


errors = []
refund_ids = {'availability', 'paddle', 'google-play', 'app-store', 'legacy-bmc',
              'withdrawal', 'withdrawal-model', 'defects', 'complaints', 'adr'}
for locale in ('cs', 'sk', 'en', 'de', 'pl'):
    prefix = '' if locale == 'cs' else locale + '/'
    content = DATA['languages'][locale]
    for key in ('terms', 'privacy', 'refund-policy'):
        path = ROOT / prefix / key / 'index.html'
        html = path.read_text(encoding='utf-8')
        text = normalized(''.join(Text(html).parts))
        page = content['terms' if key == 'refund-policy' else key]
        sections = [s for s in page['sections'] if key != 'refund-policy' or s.get('id') in refund_ids]
        if key == 'refund-policy' and {s.get('id') for s in sections} != refund_ids:
            errors.append(f'{locale}: missing required refund/consumer rights sections')
        for section in sections:
            for value in [*section['paragraphs'], *section['items']]:
                if normalized(value) not in text:
                    errors.append(f'{path}: missing shared copy from {section["heading"]}')
            for link in section.get('links', []):
                if f'href="{link["href"]}"' not in html:
                    errors.append(f'{path}: missing shared link {link["href"]}')
        if key != 'refund-policy':
            for field in ('legalName', 'address', 'registrationNumber', 'contactEmail', 'contactPhone', 'businessRegister'):
                if DATA['operator'][field] not in text:
                    errors.append(f'{path}: missing configured operator field {field}')
            if 'tel:' in html or 'content="telephone=no"' not in html:
                errors.append(f'{path}: phone must remain plain text with auto-link detection disabled')

if errors:
    raise SystemExit('\n'.join(errors))
print('Legal validation passed: shared CS/SK/EN/DE/PL text, consumer rights, links and trader identity.')
