# Rodinka marketingový web

**Stav: CURRENT.** Pravidla zdroje a ověření generovaného webu.

Statický vícejazyčný web bez produkčního build procesu a bez aplikačních závislostí. Vercel servíruje commitnuté HTML, CSS, JavaScript a obrázky přímo z repozitáře.

## Lokální spuštění

```bash
python -m http.server 4173
```

Poté otevřete `http://localhost:4173/`. Hlavní CTA vedou do App Storu a Google Play. Přihlášení a sekundární webová alternativa vedou na `https://app.mojerodinka.cz`.

## Generování stránek

Společná šablona, překlady a obsah stránek jsou v `generate_site.py`. Po úpravě spusťte:

```bash
python generate_site.py
```

Skript vytvoří lokalizované HTML, `sitemap.xml` a experimentální `llms.txt`. Vygenerované soubory se commitují; Vercel proto nepotřebuje build command.

## SEO údržba

- Canonical marketingových stránek je `https://mojerodinka.cz`; právní deriváty mají canonical na aplikaci podle pravidel níže. Ve Vercelu musí být apex doména nastavena jako Primary; `www` má trvale přesměrovat na variantu bez `www`.
- Čeština zůstává v rootu, slovenština pod `/sk/`, angličtina pod `/en/`, němčina pod `/de/` a polština pod `/pl/`. Každá lokalizovaná stránka má vlastní canonical a kompletní reciproční `hreflang` včetně `x-default` na českou verzi.
- Německé a polské texty i slugy jsou v `locale_de.py` a `locale_pl.py` (stejné struktury jako anglické záznamy v generátoru a v `comparisons.py`); `install_locale()` je při importu zařadí do sdílených struktur. Seznam jazyků je `LOCALE_CODES` v generátoru a `LOCALES` ve validátoru. Názvy funkcí v DE/PL přebírají katalog aplikace (Heute/Dzisiaj, Planen/Planowanie, Rodinka Heute/Rodinka na dziś …).
- Každá indexovatelná stránka musí mít unikátní lokalizovaný `title`, meta description, jeden `h1`, OG/Twitter text a viditelný obsah odpovídající danému vyhledávacímu záměru.
- Novou stránku přidejte jako jednu jazykovou rodinu do `PATHS` (CS/SK/EN) a do `PATHS` v `locale_de.py`/`locale_pl.py`, do všech pěti jazykových částí `TOPICS`, její klíč zařaďte do `TOPIC_KEYS`, doplňte související stránky v `RELATED`, krátký popisek do `LLMS_LABELS` a `DIRECT_ANSWERS` a rodinu přidejte i do `FAMILIES` v `tools/validate_seo.py`. Tím se zapojí do generování, sitemap i tematického přehledu; vždy ještě ověřte, že má přirozený kontextový odkaz a není osiřelá. Potom spusťte generátor a SEO validaci.
- `sitemap.xml` se skládá pouze z canonical URL definovaných v generátoru. Nepřidávejte `changefreq`, priority ani data změn bez spolehlivého zdroje.
- JSON-LD používá jeden stabilní `WebSite` a `WebApplication` identifikátor napříč jazyky. Nevkládejte hodnocení, recenze, počty uživatelů, ceny ani právní údaje, které nejsou ověřené na webu.
- Sociální karty jsou lokální soubory `og-image.png`, `og-image-sk.png`, `og-image-en.png`, `og-image-de.png` a `og-image-pl.png` (DE/PL vznikly z anglické karty výměnou podtitulku). Při výměně zachovejte ostrý landscape obrázek, bezpečné okraje, čitelný lokalizovaný text, odpovídající `og:image:width`/`height` v generátoru a lokalizované alt texty.
- Viditelné produktové ukázky jsou optimalizované WebP soubory v `assets/product/`. Český základ používá název bez přípony jazyka, lokalizované varianty končí `-sk.webp`, `-en.webp`, `-de.webp` a `-pl.webp`. Obrázky převzaté ze store listingu mají v daném jazyce celý obsah včetně UI v telefonu; jen starší `rodinka-expected-child` má lokalizovaný pouze nadpis nad českou ukázkou (i v DE a PL). Všechny mají jednotný rámec 900 × 1951 px. Jejich přiřazení ke stránkám, lokalizované alternativní texty a popisky spravují `PRODUCT_PROOFS` a samostatné homepage story objekty v generátoru. Každá významová fotografie nebo obrazovka musí mít v HTML rozměry, užitečný lokalizovaný `alt` a viditelný kontext; nevkládejte screenshoty pouze jako CSS pozadí.
- Každá indexovatelná stránka obsahuje nahoře krátkou přímou odpověď definovanou v `DIRECT_ANSWERS`. Při změně funkce upravte odpověď ve všech pěti jazycích a držte ji konkrétní, faktickou a v souladu s viditelným produktem.
- Favicon vychází z `favicon.svg`; raster fallbacky vytvoří `tools/generate_icons.ps1`.
- Písmo je self-hostované v `assets/fonts/` a web nesmí volat `fonts.googleapis.com` ani `fonts.gstatic.com`; SEO validace to hlídá. Stejně jako aplikace používá web pro veškerý text jen Manrope: jeden variabilní WOFF2 s osou váhy 500–800. Generátor preloaduje právě tento jeden soubor; další preload nepřidávejte. Serif (Georgia) je systémové písmo pro „hlas rodiny“ — claim, citát a pozdrav v ukázce aplikace — stejně jako v aplikaci. Licence OFL leží vedle fontu a musí zůstat commitnutá.
- `llms.txt` je pouze neškodná experimentální pomůcka pro strojovou orientaci. Není SEO ranking faktor ani náhrada za sitemap, metadata, HTML obsah či strukturovaná data.
- Po změně `styles.css` nebo `script.js` zvyšte `ASSET_VERSION` v generátoru, aby návštěvníci nedostali starou verzi z krátké cache.

### Vzhled sladěný s aplikací

Web přebírá vizuální systém aplikace Rodinka (`Rodinka/visual-identity.md` a `Rodinka/src/styles/tokens.css`), aby stránka a produktové ukázky na ní mluvily jedním jazykem:

- Blok `:root` v `styles.css` je kopie sémantických tokenů aplikace (plochy, text, hranice, jediný accent `--interactive-primary`, vybraný stav, kategorie modulů, radiusy, stíny, pohyb) včetně tmavého motivu přes `prefers-color-scheme`. Při změně tokenů v aplikaci upravte stejné hodnoty i tady; nové lokální barvy nevymýšlejte.
- Barva modulu (`data-tone`) odpovídá kategorii, kterou pro daný modul používá aplikace: úkoly zelená, aktivity levandulová, nákupy medová, doklady tlumená modrá, výlety přírodní zelená, jídla terakota.
- Logo je port `FamilyMark` z aplikace (`family_mark*` v generátoru počítá stejné lístky jako `Rodinka/src/utils/familyMark.ts`). Ikony spodní navigace v ukázce jsou ikony aplikace.
- Telefon v hero sekci, portrét rodiny a plán cesty jsou kresby skutečných komponent aplikace, ne screenshoty. Jsou vždy `aria-hidden` a stejnou informaci nese viditelný text vedle nich. Používají texty aplikace (Dnes, Dnešní Rodinka, Plány cest); když se v aplikaci změní, upravte `HOME_PHONE`, `TRIP_MOCK` a spol.
- Sekce „S čím vám má Rodinka nejvíc pomáhat?“ zrcadlí sedm oblastí z úvodního průvodce aplikace (`HOME_FOCUS`) ve stejném pořadí a znění. Kroky „Jak začít“ odpovídají skutečnému průvodci (Rodina → S čím pomáhat → Portrét).
- Tvrzení o funkcích musí odpovídat aktuálnímu stavu aplikace (runtime, ne roadmapě). Moment dne je součástí Rodinky Pro; hlasové zadávání je vždy „na podporovaných zařízeních“.

### Širší rodina (generace G1–G4a)

Web představuje možnosti, které aplikace přidala ve vlnách G1–G4a (`Rodinka/docs/generations/`): potvrzení doprovodu odkazem bez účtu (G1), pomocníky, kteří vidí jen své doprovody (G2), jeden účet ve více rodinách (G3) a předání dětského profilu vlastnímu účtu (G4a). Obsah žije na třech místech:

- stránka `circle` (`/sirsi-rodina/`, `/sk/sirsia-rodina/`, `/en/extended-family/`) v `TOPICS` a `DIRECT_ANSWERS`, s kreslenou ukázkou veřejné pozvánky `INVITE_MOCK` (texty z `Rodinka/src/features/companions/companionInvitationCopy.ts`);
- sekce „Rodina není jen jedna domácnost“ na homepage (`HOME_CIRCLE`, `render_circle`) mezi sérií videí a „Jak začít“;
- krátké zmínky a otázky na stránkách kalendáře, plánovače, aplikace a vzpomínek, v bloku důvěry a v kartě dětí.

Pravidla pro texty: G4a je **předání profilu, který zůstává dětský** (stejná pravidla viditelnosti, rodiče vidí totéž co dřív). Web nesmí slibovat převzetí do role dospělého ani samostatné soukromí dospělého dítěte (G4b, `ADULT_PRIVACY_PROPOSAL.md`). Pomocníkům aplikace zatím neposílá push a úkoly nevidí; upozornění jednoho zařízení chodí jen z jedné rodiny. Dostupnost v nativních aplikacích (Android/iOS) web neuvádí.

Funkce byly ověřené v produkci 1. 11. 2026 (klient na `app.mojerodinka.cz` obsahuje trasy `/i`, `/helper`, `/takeover` a hlavičku rodiny; produkční databáze má příslušná RPC). Kdyby bylo potřeba obsah stáhnout, odeberte `circle` z `TOPIC_KEYS`, `FOOTER_KEYS`, `RELATED` a `FAMILIES` ve validátoru, vynechejte `render_circle` v `render_home` a vraťte doplněné otázky; pak přegenerujte web.

### Rodinka Pro a dostupnost nákupů

**CURRENT — stav k 5. 11. 2026.** Free je bezplatný rodinný organizér s 200 MiB.
Pro pro konkrétní rodinu přidává 5 GiB, Moment dne, personalizaci a nástroje
podle aktuálních capabilities aplikace. Nové nákupy se připravují; jejich
skutečnou dostupnost určuje nabídka v aplikaci a provider/serverové brány.
Existující předplatné může dál pokračovat. Marketing nezapíná žádný checkout.

Na výslovné rozhodnutí vlastníka z 5. 11. 2026 se placené ceny zatím nikde
nezveřejňují, ani na homepage, v metadatech, sociálních náhledech nebo JSON-LD.
`HOME_PRO`, `INFO_PAGES` a `render_plans` popisují funkce a dostupnost, nikoli
aktuálně prodejný ceník. Znovuzavedení částek vyžaduje potvrzení vlastníkem
pro skutečné produkty a kanály; SEO guard hlídá návrat dosavadních částek.
Úložiště používá přesné jednotky MiB/GiB podle aplikace.

### Srovnání rodinných plánovačů

**CURRENT — ověřeno 9. 11. 2026.** Sekce pomáhá rodičům vybrat aplikaci a férově ukazuje Rodinku vedle konkurence:

| Stránka | CS | SK | EN |
| --- | --- | --- | --- |
| Přehled srovnání | `/srovnani/` | `/sk/porovnanie/` | `/en/compare/` |
| Rodinka vs Familia | `/srovnani/rodinka-vs-familia/` | `/sk/porovnanie/rodinka-vs-familia/` | `/en/compare/rodinka-vs-familia/` |
| Rodinka vs FamilyWall | `/srovnani/rodinka-vs-familywall/` | `/sk/porovnanie/rodinka-vs-familywall/` | `/en/compare/rodinka-vs-familywall/` |
| Rodinka vs Cozi | `/srovnani/rodinka-vs-cozi/` | `/sk/porovnanie/rodinka-vs-cozi/` | `/en/compare/rodinka-vs-cozi/` |
| Průvodce výběrem | `/nejlepsi-rodinne-planovace/` | `/sk/najlepsie-rodinne-planovace/` | `/en/best-family-planner-apps/` |

Obsah je oddělený od šablon: fakta, zdroje i texty jsou v `comparisons.py`, generátor je jen vykresluje (`render_compare_hub`, `render_comparison`, `render_guide`). Další aplikaci přidáte jedním záznamem v `COMPETITORS` a `COMPARISON_PAGES`, klíčem v `COMPETITOR_ORDER`, cestou `vs_<klíč>` v `PATHS`, popiskem v `LLMS_LABELS` a rodinou ve `FAMILIES` validátoru.

Pravidla obsahu:

- Strana Rodinky (`RODINKA`) popisuje vydanou aplikaci, ne roadmapu ani funkce za vypnutým flagem. Propojení s externími kalendáři, Bezpečný příchod se jako dostupný neuvádí. Dostupnost mobilních aplikací potvrzují store odkazy v `STORE_URLS`.
- Tvrzení o konkurenci pocházejí jen z jejích oficiálních webů. Každý řádek tabulky cituje zdroje a celá sada nese `VERIFIED_ON`. Nenalezená funkce je `unverified` („Nepodařilo se ověřit“); `no` jen tehdy, když to konkurent sám uvádí (text pak začíná „Podle…“).
- Ceny jen s ověřenou měnou, intervalem a podmínkami. Částky uvedené jen se symbolem `$` bez kódu měny se nezveřejňují; ceny Rodinky Pro také ne (viz výše).
- Bez skóre, hodnocení a log konkurence. Každá stránka viditelně uvádí, že srovnání publikuje Rodinka, a nabízí kontakt na podporu pro opravy.
- Při aktualizaci znovu ověřte zdroje, upravte `VERIFIED_ON` a `VERIFIED_LABEL` a spusťte generátor, validace a `python -m unittest discover -s tools -p "test_*.py"`.

JSON-LD stránek sekce přidává `BreadcrumbList`, u srovnání a průvodce `Article` (vydavatel Rodinka, `dateModified` = datum ověření), u přehledu `ItemList`. FAQ je jen viditelné; `FAQPage` záměrně nepoužíváme, protože o FAQ rich results Google rozhoduje sám a obsahu nepřidávají hodnotu.

### Podmínky, soukromí a refundace

Autoritativní veřejné dokumenty jsou `https://app.mojerodinka.cz/terms` a
`https://app.mojerodinka.cz/privacy`, pro SK/EN s `?lang=sk` a `?lang=en`.
Patička a právní odkazy vedou přímo tam. Marketingové `/terms/`, `/privacy/`
a jejich lokalizace zůstávají čitelné HTML deriváty pro ověřování domény;
canonical, hreflang, OG URL a viditelný odkaz ukazují na aplikaci. Tyto
nekanonické kopie nejsou v marketingové sitemap. Nevzniká druhý autorský text.

`data/legal-content.json` je generovaný snapshot `legalContent.ts` a
`operator.ts` aplikace. Podmínky veřejně uvádějí Paddle, Google Play, Apple
a BMC pouze jako historický kanál. BMC není nákupní ani donation odkaz;
SEO guard povoluje jeho název jen v informativním právním kontextu a dál
zakazuje odkazy na jeho nákup/donation stránky. Obsah nevytváří tvrzení,
že všechny prodejní kanály už běží.

`/refund-policy/` a lokalizace přebírají z téhož snapshotu celé relevantní
sekce podle stabilních `id`: kanály, obnovování, zákonné odstoupení, vzor,
vady, reklamace a ADR. Pravidla se nepřepisují ručně do `INFO_PAGES`.
Komerční refundace nejsou zaměněné se zákonnými právy ani s běžným zrušením.
Kontakty a status neplátce DPH jsou převzaté z vlastníkem potvrzeného
`operator.ts`; telefon je text bez `tel:` s vypnutou autodetekcí.

Po změně v aplikaci synchronizujte z konkrétního čistého/commitnutého checkoutu:

```bash
node tools/sync_legal_content.mjs ../Rodinka
node tools/sync_legal_content.mjs ../Rodinka --check
python generate_site.py
python tools/validate_seo.py
python tools/validate_analytics.py
python tools/validate_legal.py
```

`source` uvádí commit aplikace. `--check` odmítá drift vůči zvolenému checkoutu;
`validate_legal.py` ověřuje skutečně vygenerované odstavce, odkazy, kontakty
a společné spotřebitelské sekce. Publikujte odpovídající verzi aplikace dříve
než marketing, aby kanonické odkazy vedly na nové texty. Odborné posouzení
checkout souhlasů a online funkce odstoupení vlastní audit v aplikaci
`docs/audits/TERMS_TRADER_AUDIT_2026-11-05.md`; změna webu tento launch gate
nenahrazuje.

### Přegenerování písem

Vygenerované WOFF2 soubory jsou commitnuté, takže nasazení skript nepotřebuje. Spusťte ho jen při změně upstream verze nebo znakové sady:

```bash
pip install fonttools brotli
python tools/build_fonts.py
```

Skript stahuje upstream Manrope 4.505 z repozitáře Google Fonts a ověřuje připnutou verzi. Osa váhy se ořízne na rozsah, který stylesheet skutečně používá (500–800), a znaková sada pokrývá latin-1 plus středoevropskou diakritiku, takže čeština i slovenština renderují z webfontu. Znak `→` v odkazech záměrně součástí není: nebyl ani v původní Google subsetě a vykresluje se systémovým písmem.

### Příprava produktových obrázků

Zdrojové marketingové PNG exporty nejsou součástí produkčního webu. Zdrojem jsou store listing obrázky z aplikačního repozitáře, `Rodinka/promo/store-listing/app-store-6.9/` s podsložkami `cs/`, `sk/`, `en/`, `de/` a `pl/`. DE a PL exporty vznikly vyrenderováním App Store artboardů 1320 × 2868 z designového plátna „Rodinka – store screenshoty“; jednotlivé jazyky lze převést přepínačem `--locales de pl`. Webové deriváty z nich vytvoří volitelný pomocný skript (vyžaduje Pillow):

```bash
python tools/optimize_product_images.py ../Rodinka/promo/store-listing/app-store-6.9
```

Skript páruje exporty podle čísla na začátku názvu (`01` Dnes, `02` Kalendář, `03` Vzpomínky, `04` Plánovat, `05` Úkoly, `06` Nákup), takže lokalizované názvy souborů nevadí. Výstupem jsou WebP soubory 900 × 1951 px; exporty 1320 × 2868 jsou v této šířce o 4 px vyšší, proto skript ořízne spodní okraj, kde telefon stejně pokračuje mimo obraz. Vercel servíruje commitnuté výstupy přímo; optimalizace není součástí nasazení ani produkční build závislostí.

Store listing obsahuje i `07` Milníky, zatím jen česky. Na web se nedostal, protože SEO validace vyžaduje stejné produktové ukázky ve všech jazycích; po doplnění SK a EN verze ho lze přidat do skriptu i do generátoru. Obrázky jsou v `/assets/` cachované týden a jejich názvy nejsou verzované, takže vracející se návštěvník může po výměně ještě chvíli vidět starší verzi.

`rodinka-expected-child` ve store listingu nemá obdobu a zůstává starším exportem. Pro bezpečnou lokalizaci takového plochého marketingového exportu použijte `tools/composite_localized_product_header.py`: vezme pouze lokalizovaný nadpis a štítek z připraveného návrhu, zatímco logo, telefon a celé produktové UI zachová z českého základního WebP. Výsledkem je nový soubor, nikdy přepsání originálu.

### Promo video

Homepage CS, SK a EN mají pod stručnou odpovědí padesátivteřinový spot (DE a PL zatím bez lokalizovaného voice-overu, sekce se nevykreslí) z `Rodinka/promo/rodinka-spot/video/`. Obsah sekce i použitý soubor (`stem`) spravuje `HOME_SPOT` v generátoru. Každý z těchto jazyků má vlastní verzi spotu s lokalizovaným voice-overem. Soubory leží v `assets/video/` (slovenské s příponou `-sk`, anglické `-en`): 16:9 pro širší obrazovky, 9:16 pro telefony do 560 px. Video se stahuje až po kliknutí na plakát. Bez JavaScriptu se zobrazí běžný přehrávač s verzí 16:9.

Webové verze a WebP plakáty vznikly takto; pro 9:16 platí totéž se vstupem `rodinka-spot-1080x1920.mp4` a plakátem širokým 720 px, pro další jazyky vstupy i výstupy `rodinka-spot-sk-*` a `rodinka-spot-en-*`. Plakát je snímek, na kterém je celý titulek („Rodina je ten nejkrásnější chaos na světě.“) a všechny postavičky: 11,4 s u české a anglické verze, 11,02 s u slovenské, která běží o kousek dřív:

```bash
ffmpeg -i rodinka-spot-1080p.mp4 -c:v libx264 -preset slow -crf 26 -r 30 -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart assets/video/rodinka-spot-16x9.mp4
ffmpeg -ss 11.4 -i rodinka-spot-1080p.mp4 -frames:v 1 -vf scale=1600:-1 poster.png && cwebp -q 82 poster.png -o assets/video/rodinka-spot-16x9.webp
```

Lokální `python -m http.server` nepodporuje HTTP Range, takže v něm video nejde přetáčet; na Vercelu to funguje.

### Série Každodenní Rodinka

Sedm krátkých vertikálních dílů (9:16, 14–25 s) z `Rodinka/promo/rodinka-spot/` (`src/episodes/ep01`–`ep07`). Každý díl prodává jednu každodenní chvíli, proto hraje přímo u funkce, o které je: v sekci s popisem problému na odpovídající tematické stránce. Na homepage je pod sekcí „S čím vám má Rodinka nejvíc pomáhat?“ celá série jako jeden přehrávač se seznamem dílů; tam má domov i díl 05, který ukazuje obrazovku Dnes jako celek a vlastní stránku nemá.

| Díl | Stránka | Plakát |
| --- | --- | --- |
| 01 Kdo dnes vyzvedává? | Rodinný kalendář | 1,2 s |
| 02 Co máme koupit? | Sdílený nákupní seznam | 3,0 s |
| 03 V kolik má dneska kroužek? | Rodinný plánovač (kroužky) | 1,0 s |
| 04 Kam jsme to chtěli jet? | Rodinné výlety | 1,2 s |
| 05 Co nás dnes čeká? | jen homepage (odkaz na plánovač) | 0,8 s |
| 06 Kde jsme to řešili? | Aplikace pro rodinu | 1,1 s |
| 07 Tohle si chceme pamatovat. | Rodinné vzpomínky | 7,4 s |

Obsah, přiřazení ke stránkám (`page`, u dílu bez stránky `link`) a zaokrouhlenou délku (`seconds`) spravuje `SERIES` v generátoru. Hlas i texty v obraze jsou české, takže díly jsou zatím jen na českých stránkách; lokalizované rendery stačí přidat jako `SERIES["sk"]`, `SERIES["en"]` atd. Soubory leží v `assets/video/kazdodenni-rodinka-NN-*.mp4` s plakátem `.webp` širokým 720 px. Stejně jako u spotu se video stahuje až po kliknutí na plakát a naráz hraje vždy jen jedno video na stránce. Webové verze vznikly ze zdrojů `*-1080x1920.mp4` takto (plakát je snímek s úvodní otázkou dílu, u 07 polaroid s popiskem):

```bash
ffmpeg -i kazdodenni-rodinka-01-kdo-dnes-vyzvedava-1080x1920.mp4 -c:v libx264 -preset slow -crf 26 -r 30 -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart assets/video/kazdodenni-rodinka-01-kdo-dnes-vyzvedava.mp4
ffmpeg -ss 1.2 -i kazdodenni-rodinka-01-kdo-dnes-vyzvedava-1080x1920.mp4 -frames:v 1 -vf scale=720:-1:flags=lanczos poster.png && cwebp -q 82 poster.png -o assets/video/kazdodenni-rodinka-01-kdo-dnes-vyzvedava.webp
```

### IndexNow

Automatické odesílání do IndexNow zatím není zapojené. U tohoto malého statického webu by kvůli několika stabilním URL přidalo klíč a nasazovací automatizaci bez jasného přínosu pro hlavní Google vyhledávání. Po významné změně odešlete sitemapu a reprezentativní URL přes Search Console; IndexNow lze později doplnit jako samostatný Vercel/CI krok, pokud bude důležitá rychlost objevení v podporovaných vyhledávačích.

## Kontrola před nasazením

```bash
python tools/validate_seo.py
python tools/validate_analytics.py
python tools/validate_legal.py
python -m unittest discover -s tools -p "test_*.py"
```

Po změně JSON-LD otestujte reprezentativní URL ve [Schema.org Validatoru](https://validator.schema.org/) a v [Google Rich Results Testu](https://search.google.com/test/rich-results). Rich result není cílem ani zárukou; test má zachytit chybný zápis.

## Analytics a Google Tag Manager

Web má přímo nainstalovaný pouze Google Tag Manager container `GTM-5FM9NJHK`. GA4 Measurement ID `G-LMZQ91Y9NP` patří výhradně do konfigurace tohoto containeru; web samostatný `gtag.js` pro GA4 nenačítá.

Consent Mode se inicializuje synchronně před GTM. `analytics_storage`, `ad_storage`, `ad_user_data` a `ad_personalization` jsou ve výchozím stavu `denied`; při souhlasu se mění pouze `analytics_storage` na `granted`. Volba se ukládá do `localStorage` pod klíčem `rodinka_analytics_consent` ve tvaru:

```json
{"version": 1, "analytics": "granted"}
```

Hodnota `analytics` může být `granted` nebo `denied`. Neplatná, stará nebo nedostupná hodnota úložiště se bezpečně vyhodnotí jako chybějící souhlas a zobrazí se panel. Nastavení lze kdykoli znovu otevřít odkazem v patičce.

### Store-first CTA a měření

`generate_site.py` centralizuje `STORE_URLS`, lokalizované texty `STORE_COPY` a komponentu `store_buttons(locale, placement)`. Oficiální lokální assety a jejich zdroje jsou v `assets/stores/README.md`. Obě platformy jsou vždy viditelné; nedochází k detekci zařízení ani přesměrování. App Store URL ponechává ověřený `/cz/` storefront pro všechny jazyky.

Hero, závěrečné CTA, tematické a srovnávací stránky, Free plán a patička nabízejí oba obchody. Navigace a kompaktní/video CTA odkazují na společnou nabídku `#download`. Přihlášení a správa existujícího Pro účtu zůstávají webové. Pod badges je slabší textový odkaz na plnohodnotnou webovou verzi. JSON-LD zachovává stabilní WebApplication a přidává iOS/Android MobileApplication s ověřenými installUrl.

Delegovaný click handler vloží právě jednu událost pouze při `analytics === 'granted'`. Bez souhlasu, po odmítnutí a po odvolání neukládá ani zpětně nepřehrává konverze:

```js
{ event: 'store_cta_click', platform: 'ios' /* nebo android */, placement: 'hero', locale: 'cs' }
{ event: 'web_app_cta_click', placement: 'header', locale: 'cs' }
```

Placement: `hero`, `header`, `footer`, `pricing`, `content`. Locale: `cs`, `sk`, `en`, `de`, `pl`. Interní odkazy na nabídku stažení nejsou konverzemi. Právní a podpůrné odkazy se neměří. Starý `cta_app_click` se již neposílá. Události vyjadřují kliknutí, nikoli instalaci nebo registraci.

### Ruční konfigurace GTM a GA4

Web načítá pouze stávající GTM container, nikoli další GA4 instalaci. Stávající pokročilý Consent Mode zůstává zachovaný. K jeho omezeným signálům se bez souhlasu nepřidávají konverzní události.

V containeru `GTM-5FM9NJHK` před nasazením změny:

1. Nahraďte trigger/tag `cta_app_click` dvěma Custom Event triggery `store_cta_click` a `web_app_cta_click`.
2. Pro každou událost nastavte jeden GA4 event tag u stávajícího Google Tag `G-LMZQ91Y9NP`; použijte stejné jméno události a Data Layer Variables `platform`, `placement`, `locale` (platform pouze pro store událost).
3. U event tagů vyžadujte `analytics_storage` jako additional consent check. Odstraňte případné obecné click triggery, které by tyto konverze odesílaly podruhé. Enhanced Measurement `click` může existovat jako samostatná obecná outbound událost; nepřevádějte jej zároveň na stejné konverze.
4. V GA4 případně registrujte event-scoped dimenze `platform`, `placement`, `locale`. Kliknutí automaticky neoznačujte jako `sign_up`.
5. V GTM Preview a GA4 DebugView ověřte nový návštěvník → odmítnutí → souhlas → odvolání, reload a obě platformy ve všech jazycích. Bez souhlasu musí chybět obě vlastní konverzní události; po souhlasu jedno kliknutí znamená jednu událost.

Do produkčního GTM nebylo z repozitáře zasahováno. Samotný dataLayer push nezaručuje doručení do GA4 bez výše uvedené konfigurace.

Kontroly: `python generate_site.py`, `python tools/validate_seo.py`, `python tools/validate_analytics.py`, `python tools/validate_legal.py`, `python -m unittest discover -s tools -p "test_*.py"`, `node --check script.js`, `node tools/test_cta_analytics.cjs`. Projekt nemá samostatný TypeScript typecheck ani lint/build balíček; buildem je generátor a jeho validátory.

## Google Search Console

1. Ověřte doménovou property `mojerodinka.cz` pomocí DNS.
2. Zkontrolujte, že jako finální URL funguje HTTPS bez `www` a že ostatní varianty vedou jedním 308/301 přesměrováním na canonical host.
3. Odešlete `https://mojerodinka.cz/sitemap.xml`.
4. Přes Kontrolu adresy URL ověřte homepage a jednu CS, SK a EN obsahovou stránku; zkontrolujte canonical, jazyk a indexovatelnost.
5. Po nasazení sledujte Page indexing, Core Web Vitals a výsledky podle země/jazyka. O ruční indexaci žádejte jen u několika reprezentativních URL, ne u všech stránek opakovaně.

## Vercel

Projekt používá framework preset **Other**. Build command ani output directory nejsou potřeba. `vercel.json` sjednocuje trailing slash URL, přidává pragmatické bezpečnostní hlavičky a krátkou cache pro měnitelné CSS/JS; stabilní obrazové identity mají delší cache bez příznaku `immutable`, protože jejich názvy nejsou verzované.
