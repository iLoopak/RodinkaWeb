const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const handlers = {};
const choices = {};
class Element {
  constructor(dataset, href) { this.dataset = dataset; this.href = href; }
  closest() { return this; }
}
const panel = {
  querySelectorAll: () => ['granted', 'denied'].map(value => ({
    dataset: { consentChoice: value },
    addEventListener: (_, fn) => { choices[value] = fn; },
  })),
};
const window = {
  location: { href: 'https://mojerodinka.cz/en/' },
  localStorage: { getItem: () => null, setItem() {} },
  rodinkaConsent: { key: 'rodinka_analytics_consent', version: 1, analytics: 'denied' },
  dataLayer: [],
};
const document = {
  documentElement: { lang: 'en' },
  querySelector: selector => selector === '[data-cookie-consent]' ? panel : null,
  querySelectorAll: () => [],
  addEventListener: (name, fn) => { (handlers[name] ||= []).push(fn); },
};
vm.runInNewContext(fs.readFileSync(require('node:path').join(__dirname, '../script.js'), 'utf8'), {
  window, document, Element, HTMLElement: Element, URL,
});
const events = () => window.dataLayer.filter(e => e.event);
const click = (platform, placement = 'hero') => {
  const target = new Element({ storePlatform: platform, analyticsLocation: placement },
    platform ? 'https://example.com/store' : 'https://app.mojerodinka.cz');
  handlers.click.forEach(fn => fn({ target }));
};
click('ios');
assert.equal(events().length, 0, 'no conversion without consent');
choices.denied(); click('android'); click();
assert.equal(events().length, 0, 'no conversion after rejection');
choices.granted();
for (const locale of ['cs', 'sk', 'en', 'de', 'pl']) {
  document.documentElement.lang = locale;
  for (const platform of ['ios', 'android']) {
    const before = events().length; click(platform);
    assert.equal(events().length, before + 1, 'exactly one event per click');
    assert.equal(events().at(-1).event, 'store_cta_click');
    assert.equal(events().at(-1).platform, platform);
    assert.equal(events().at(-1).placement, 'hero');
    assert.equal(events().at(-1).locale, locale);
  }
  click(undefined, 'header');
  assert.equal(events().at(-1).event, 'web_app_cta_click');
  assert.equal(events().at(-1).placement, 'header');
  assert.ok(!('platform' in events().at(-1)));
}
const count = events().length;
choices.denied(); click('ios'); click();
assert.equal(events().length, count, 'revocation stops conversion events');
choices.granted();
window.dataLayer = { push() { throw new Error('analytics blocked'); } };
assert.doesNotThrow(() => click('android'), 'blocked analytics never blocks navigation');
console.log('CTA analytics passed: consent/rejection/revocation, both platforms, five locales, one event per click and blocked analytics.');
