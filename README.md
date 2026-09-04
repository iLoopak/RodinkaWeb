# Rodinka marketingový web

Statický vícejazyčný web bez produkčního build procesu a bez aplikačních závislostí. Vercel servíruje commitnuté HTML, CSS, JavaScript a obrázky přímo z repozitáře.

## Lokální spuštění

```bash
python -m http.server 4173
```

Poté otevřete `http://localhost:4173/`. Hlavní CTA a přihlášení vedou na `https://app.mojerodinka.cz`.

## Generování stránek

Společná šablona, překlady a obsah stránek jsou v `generate_site.py`. Po úpravě spusťte:

```bash
python generate_site.py
```

Skript znovu vytvoří 24 statických HTML stránek, `sitemap.xml` a experimentální `llms.txt`. Vygenerované soubory se commitují; Vercel proto nepotřebuje build command.

## SEO údržba

- Canonical host je výhradně `https://mojerodinka.cz`. Ve Vercelu musí být apex doména nastavena jako Primary; `www` má trvale přesměrovat na variantu bez `www`.
- Čeština zůstává v rootu, slovenština pod `/sk/` a angličtina pod `/en/`. Každá lokalizovaná stránka má vlastní canonical a kompletní reciproční `hreflang` včetně `x-default` na českou verzi.
- Každá indexovatelná stránka musí mít unikátní lokalizovaný `title`, meta description, jeden `h1`, OG/Twitter text a viditelný obsah odpovídající danému vyhledávacímu záměru.
- Novou stránku přidejte jako jednu jazykovou rodinu do `PATHS` a do všech tří částí `TOPICS`, její klíč zařaďte do `TOPIC_KEYS` a doplňte související stránky v `RELATED`. Tím se zapojí do generování, sitemap i tematického přehledu; vždy ještě ověřte, že má přirozený kontextový odkaz a není osiřelá. Potom spusťte generátor a SEO validaci.
- `sitemap.xml` se skládá pouze z canonical URL definovaných v generátoru. Nepřidávejte `changefreq`, priority ani data změn bez spolehlivého zdroje.
- JSON-LD používá jeden stabilní `WebSite` a `WebApplication` identifikátor napříč jazyky. Nevkládejte hodnocení, recenze, počty uživatelů, ceny ani právní údaje, které nejsou ověřené na webu.
- Sociální karty jsou lokální soubory `og-image.png`, `og-image-sk.png` a `og-image-en.png`. Při výměně zachovejte ostrý landscape obrázek, bezpečné okraje, čitelný lokalizovaný text, odpovídající `og:image:width`/`height` v generátoru a lokalizované alt texty.
- Viditelné produktové ukázky jsou optimalizované WebP soubory v `assets/product/`. Český základ používá název bez přípony jazyka, marketingově lokalizované varianty končí `-sk.webp` a `-en.webp`; samotné UI v telefonu zůstává věrnou českou produktovou ukázkou. Jejich přiřazení ke stránkám, lokalizované alternativní texty a popisky spravují `PRODUCT_PROOFS` a samostatné homepage story objekty v generátoru. Každá významová fotografie nebo obrazovka musí mít v HTML rozměry, užitečný lokalizovaný `alt` a viditelný kontext; nevkládejte screenshoty pouze jako CSS pozadí.
- Každá indexovatelná stránka obsahuje nahoře krátkou přímou odpověď definovanou v `DIRECT_ANSWERS`. Při změně funkce upravte odpověď ve všech třech jazycích a držte ji konkrétní, faktickou a v souladu s viditelným produktem.
- Favicon vychází z `favicon.svg`; raster fallbacky vytvoří `tools/generate_icons.ps1`.
- `llms.txt` je pouze neškodná experimentální pomůcka pro strojovou orientaci. Není SEO ranking faktor ani náhrada za sitemap, metadata, HTML obsah či strukturovaná data.
- Po změně `styles.css` nebo `script.js` zvyšte `ASSET_VERSION` v generátoru, aby návštěvníci nedostali starou verzi z krátké cache.

### Příprava produktových obrázků

Zdrojové marketingové PNG exporty nejsou součástí produkčního webu. Webové deriváty lze znovu vytvořit volitelným pomocným skriptem (vyžaduje Pillow):

```bash
python tools/optimize_product_images.py "/cesta/ke/screenum"
```

Skript vytváří maximálně 900 px široké WebP soubory. Vercel servíruje commitnuté výstupy přímo; optimalizace není součástí nasazení ani produkční build závislostí.

Pro bezpečnou lokalizaci plochého marketingového exportu použijte `tools/composite_localized_product_header.py`: vezme pouze lokalizovaný nadpis a štítek z připraveného návrhu, zatímco logo, telefon a celé produktové UI zachová z českého základního WebP. Výsledkem je nový soubor, nikdy přepsání originálu.

### IndexNow

Automatické odesílání do IndexNow zatím není zapojené. U tohoto malého statického webu by kvůli několika stabilním URL přidalo klíč a nasazovací automatizaci bez jasného přínosu pro hlavní Google vyhledávání. Po významné změně odešlete sitemapu a reprezentativní URL přes Search Console; IndexNow lze později doplnit jako samostatný Vercel/CI krok, pokud bude důležitá rychlost objevení v podporovaných vyhledávačích.

## Kontrola před nasazením

```bash
python tools/validate_seo.py
```

Po změně JSON-LD otestujte reprezentativní URL ve [Schema.org Validatoru](https://validator.schema.org/) a v [Google Rich Results Testu](https://search.google.com/test/rich-results). Rich result není cílem ani zárukou; test má zachytit chybný zápis.

## Google Search Console

1. Ověřte doménovou property `mojerodinka.cz` pomocí DNS.
2. Zkontrolujte, že jako finální URL funguje HTTPS bez `www` a že ostatní varianty vedou jedním 308/301 přesměrováním na canonical host.
3. Odešlete `https://mojerodinka.cz/sitemap.xml`.
4. Přes Kontrolu adresy URL ověřte homepage a jednu CS, SK a EN obsahovou stránku; zkontrolujte canonical, jazyk a indexovatelnost.
5. Po nasazení sledujte Page indexing, Core Web Vitals a výsledky podle země/jazyka. O ruční indexaci žádejte jen u několika reprezentativních URL, ne u všech stránek opakovaně.

## Vercel

Projekt používá framework preset **Other**. Build command ani output directory nejsou potřeba. `vercel.json` sjednocuje trailing slash URL, přidává pragmatické bezpečnostní hlavičky a krátkou cache pro měnitelné CSS/JS; stabilní obrazové identity mají delší cache bez příznaku `immutable`, protože jejich názvy nejsou verzované.
