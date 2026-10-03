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

Skript znovu vytvoří 33 statických HTML stránek (11 jazykových rodin × CS/SK/EN), `sitemap.xml` a experimentální `llms.txt`. Vygenerované soubory se commitují; Vercel proto nepotřebuje build command.

## SEO údržba

- Canonical host je výhradně `https://mojerodinka.cz`. Ve Vercelu musí být apex doména nastavena jako Primary; `www` má trvale přesměrovat na variantu bez `www`.
- Čeština zůstává v rootu, slovenština pod `/sk/` a angličtina pod `/en/`. Každá lokalizovaná stránka má vlastní canonical a kompletní reciproční `hreflang` včetně `x-default` na českou verzi.
- Každá indexovatelná stránka musí mít unikátní lokalizovaný `title`, meta description, jeden `h1`, OG/Twitter text a viditelný obsah odpovídající danému vyhledávacímu záměru.
- Novou stránku přidejte jako jednu jazykovou rodinu do `PATHS` a do všech tří částí `TOPICS`, její klíč zařaďte do `TOPIC_KEYS`, doplňte související stránky v `RELATED`, krátký popisek do `LLMS_LABELS` a `DIRECT_ANSWERS` a rodinu přidejte i do `FAMILIES` v `tools/validate_seo.py`. Tím se zapojí do generování, sitemap i tematického přehledu; vždy ještě ověřte, že má přirozený kontextový odkaz a není osiřelá. Potom spusťte generátor a SEO validaci.
- `sitemap.xml` se skládá pouze z canonical URL definovaných v generátoru. Nepřidávejte `changefreq`, priority ani data změn bez spolehlivého zdroje.
- JSON-LD používá jeden stabilní `WebSite` a `WebApplication` identifikátor napříč jazyky. Nevkládejte hodnocení, recenze, počty uživatelů, ceny ani právní údaje, které nejsou ověřené na webu.
- Sociální karty jsou lokální soubory `og-image.png`, `og-image-sk.png` a `og-image-en.png`. Při výměně zachovejte ostrý landscape obrázek, bezpečné okraje, čitelný lokalizovaný text, odpovídající `og:image:width`/`height` v generátoru a lokalizované alt texty.
- Viditelné produktové ukázky jsou optimalizované WebP soubory v `assets/product/`. Český základ používá název bez přípony jazyka, lokalizované varianty končí `-sk.webp` a `-en.webp`. Obrázky převzaté ze store listingu mají v daném jazyce celý obsah včetně UI v telefonu; jen starší `rodinka-expected-child` má lokalizovaný pouze nadpis nad českou ukázkou. Všechny mají jednotný rámec 900 × 1951 px. Jejich přiřazení ke stránkám, lokalizované alternativní texty a popisky spravují `PRODUCT_PROOFS` a samostatné homepage story objekty v generátoru. Každá významová fotografie nebo obrazovka musí mít v HTML rozměry, užitečný lokalizovaný `alt` a viditelný kontext; nevkládejte screenshoty pouze jako CSS pozadí.
- Každá indexovatelná stránka obsahuje nahoře krátkou přímou odpověď definovanou v `DIRECT_ANSWERS`. Při změně funkce upravte odpověď ve všech třech jazycích a držte ji konkrétní, faktickou a v souladu s viditelným produktem.
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
- Tvrzení o funkcích musí odpovídat aktuálnímu stavu aplikace (runtime, ne roadmapě). Moment dne se nepropaguje, protože vyžaduje ručně udělené oprávnění rodiny; hlasové zadávání je vždy „na podporovaných zařízeních“.

### Přegenerování písem

Vygenerované WOFF2 soubory jsou commitnuté, takže nasazení skript nepotřebuje. Spusťte ho jen při změně upstream verze nebo znakové sady:

```bash
pip install fonttools brotli
python tools/build_fonts.py
```

Skript stahuje upstream Manrope 4.505 z repozitáře Google Fonts a ověřuje připnutou verzi. Osa váhy se ořízne na rozsah, který stylesheet skutečně používá (500–800), a znaková sada pokrývá latin-1 plus středoevropskou diakritiku, takže čeština i slovenština renderují z webfontu. Znak `→` v odkazech záměrně součástí není: nebyl ani v původní Google subsetě a vykresluje se systémovým písmem.

### Příprava produktových obrázků

Zdrojové marketingové PNG exporty nejsou součástí produkčního webu. Zdrojem jsou store listing obrázky z aplikačního repozitáře, `Rodinka/promo/store-listing/app-store-6.9/` s podsložkami `cs/`, `sk/` a `en/`. Webové deriváty z nich vytvoří volitelný pomocný skript (vyžaduje Pillow):

```bash
python tools/optimize_product_images.py ../Rodinka/promo/store-listing/app-store-6.9
```

Skript páruje exporty podle čísla na začátku názvu (`01` Dnes, `02` Kalendář, `03` Vzpomínky, `04` Plánovat, `05` Úkoly, `06` Nákup), takže lokalizované názvy souborů nevadí. Výstupem jsou WebP soubory 900 × 1951 px; exporty 1320 × 2868 jsou v této šířce o 4 px vyšší, proto skript ořízne spodní okraj, kde telefon stejně pokračuje mimo obraz. Vercel servíruje commitnuté výstupy přímo; optimalizace není součástí nasazení ani produkční build závislostí.

Store listing obsahuje i `07` Milníky, zatím jen česky. Na web se nedostal, protože SEO validace vyžaduje stejné produktové ukázky ve všech třech jazycích; po doplnění SK a EN verze ho lze přidat do skriptu i do generátoru. Obrázky jsou v `/assets/` cachované týden a jejich názvy nejsou verzované, takže vracející se návštěvník může po výměně ještě chvíli vidět starší verzi.

`rodinka-expected-child` ve store listingu nemá obdobu a zůstává starším exportem. Pro bezpečnou lokalizaci takového plochého marketingového exportu použijte `tools/composite_localized_product_header.py`: vezme pouze lokalizovaný nadpis a štítek z připraveného návrhu, zatímco logo, telefon a celé produktové UI zachová z českého základního WebP. Výsledkem je nový soubor, nikdy přepsání originálu.

### Promo video

Všechny tři homepage mají pod stručnou odpovědí padesátivteřinový spot z `Rodinka/promo/rodinka-spot/video/`. Obsah sekce i použitý soubor (`stem`) spravuje `HOME_SPOT` v generátoru. Každý jazyk má vlastní verzi spotu s lokalizovaným voice-overem. Soubory leží v `assets/video/` (slovenské s příponou `-sk`, anglické `-en`): 16:9 pro širší obrazovky, 9:16 pro telefony do 560 px. Video se stahuje až po kliknutí na plakát. Bez JavaScriptu se zobrazí běžný přehrávač s verzí 16:9.

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

Obsah, přiřazení ke stránkám (`page`, u dílu bez stránky `link`) a zaokrouhlenou délku (`seconds`) spravuje `SERIES` v generátoru. Hlas i texty v obraze jsou české, takže díly jsou zatím jen na českých stránkách; lokalizované rendery stačí přidat jako `SERIES["sk"]` a `SERIES["en"]`. Soubory leží v `assets/video/kazdodenni-rodinka-NN-*.mp4` s plakátem `.webp` širokým 720 px. Stejně jako u spotu se video stahuje až po kliknutí na plakát a naráz hraje vždy jen jedno video na stránce. Webové verze vznikly ze zdrojů `*-1080x1920.mp4` takto (plakát je snímek s úvodní otázkou dílu, u 07 polaroid s popiskem):

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
```

Po změně JSON-LD otestujte reprezentativní URL ve [Schema.org Validatoru](https://validator.schema.org/) a v [Google Rich Results Testu](https://search.google.com/test/rich-results). Rich result není cílem ani zárukou; test má zachytit chybný zápis.

## Analytics a Google Tag Manager

Web má přímo nainstalovaný pouze Google Tag Manager container `GTM-5FM9NJHK`. GA4 Measurement ID `G-LMZQ91Y9NP` patří výhradně do konfigurace tohoto containeru; web samostatný `gtag.js` pro GA4 nenačítá.

Consent Mode se inicializuje synchronně před GTM. `analytics_storage`, `ad_storage`, `ad_user_data` a `ad_personalization` jsou ve výchozím stavu `denied`; při souhlasu se mění pouze `analytics_storage` na `granted`. Volba se ukládá do `localStorage` pod klíčem `rodinka_analytics_consent` ve tvaru:

```json
{"version": 1, "analytics": "granted"}
```

Hodnota `analytics` může být `granted` nebo `denied`. Neplatná, stará nebo nedostupná hodnota úložiště se bezpečně vyhodnotí jako chybějící souhlas a zobrazí se panel. Nastavení lze kdykoli znovu otevřít odkazem v patičce.

### dataLayer událost

Kliknutí na označený odkaz do `https://app.mojerodinka.cz` vloží do `dataLayer` jedinou vlastní marketingovou událost:

```js
{
  event: 'cta_app_click',
  cta_location: 'header' | 'hero' | 'content' | 'video' | 'footer',
  cta_text: 'lokalizovaný viditelný text odkazu',
  page_path: '/aktuální-cesta/',
  page_language: 'cs' | 'sk' | 'en'
}
```

Hodnotu `video` posílá odkaz přes tlačítko „Vyzkoušet Rodinku“ na konci promo videa na homepage. Odkaz je aktivní až od chvíle, kdy se tlačítko ve videu objeví. Událost neobsahuje osobní údaje a navigaci neblokuje. Neznamená úspěšnou registraci, proto se z marketingového webu neposílá `sign_up`; ten patří až do aplikace po dokončeném založení účtu.

### Ruční konfigurace GTM a GA4

V Google Tag Manageru zbývá provést následující kroky:

1. V containeru `GTM-5FM9NJHK` otevřete **Tags → New → Google Tag**, nastavte Tag ID na `G-LMZQ91Y9NP` a jako trigger zvolte **Initialization – All Pages**. Zapněte odesílání automatického `page_view`; další běžné interakce nechte na GA4 Enhanced Measurement.
2. V **Advanced settings → Consent settings** ověřte, že Google Tag uvádí vestavěnou kontrolu `analytics_storage`. U **Additional Consent Checks** zvolte **No additional consent required**; Google Tag má vlastní podporu Consent Mode a při `denied` nesmí ukládat ani číst analytické cookies. Reklamní souhlasy zůstávají vždy `denied`.
3. V **Variables → User-Defined Variables → New → Data Layer Variable** vytvořte čtyři proměnné (Data Layer Variable Version 2): `DLV - cta_location` → `cta_location`, `DLV - cta_text` → `cta_text`, `DLV - page_path` → `page_path`, `DLV - page_language` → `page_language`.
4. V **Triggers → New → Custom Event** vytvořte trigger s názvem například `CE - cta_app_click`, Event name přesně `cta_app_click`, který se spouští na **All Custom Events** tohoto názvu.
5. V **Tags → New → Google Analytics: GA4 Event** (nebo aktuálním ekvivalentu Google Tag eventu) zvolte Google Tag `G-LMZQ91Y9NP`, Event Name `cta_app_click` a přidejte parametry `cta_location`, `cta_text`, `page_path`, `page_language` s hodnotami z odpovídajících DLV proměnných. Připojte trigger `CE - cta_app_click`.
6. Také u event tagu zkontrolujte vestavěnou podporu `analytics_storage` a nastavte **No additional consent required**. Nepřidávejte výjimkové consent triggery ani druhou přímou GA4 instalaci; vestavěná kontrola Google tagů reaguje na příkazy `default` a `update` z webu.
7. Zapněte **Admin → Container Settings → Enable consent overview**, v náhledu ověřte výchozí i aktualizovaný stav a teprve potom container publikujte.
8. V GA4 otevřete **Admin → Data streams → Web → Enhanced measurement** a ponechte zapnuté alespoň Page views. V **Admin → Data display → Custom definitions** vytvořte event-scoped custom dimensions pro `cta_location`, `cta_text` a `page_language` se stejně pojmenovanými event parameters. `page_path` už GA4 poskytuje jako vestavěnou dimenzi Page path, proto ji znovu neregistrujte. `cta_app_click` bez dalšího obchodního rozhodnutí neoznačujte jako `sign_up` ani jako key event.

Jde o pokročilý Consent Mode: GTM se načte i při `denied` a Google Tag může odeslat omezené cookieless consent signály, ale nesmí ukládat ani číst analytické cookies. Pokud právní posouzení vyžaduje nulový přenos dat Googlu před souhlasem, je potřeba samostatně přejít na Basic Consent Mode a změnit strategii spouštění tagů.

### Produkční ověření

V **Preview** režimu GTM / Tag Assistant ověřte, že Consent tab ukazuje výchozí `denied`, po povolení okamžité `granted` pouze pro `analytics_storage` a po odmítnutí opět `denied`. V GA4 **Realtime** a **DebugView** zkontrolujte page view po povolení a `cta_app_click` se všemi čtyřmi parametry. Otestujte novou návštěvu, obě volby, reload, znovuotevření z patičky a CTA alespoň na CS/SK/EN homepage, v hlavičce a na jedné obsahové stránce.

## Google Search Console

1. Ověřte doménovou property `mojerodinka.cz` pomocí DNS.
2. Zkontrolujte, že jako finální URL funguje HTTPS bez `www` a že ostatní varianty vedou jedním 308/301 přesměrováním na canonical host.
3. Odešlete `https://mojerodinka.cz/sitemap.xml`.
4. Přes Kontrolu adresy URL ověřte homepage a jednu CS, SK a EN obsahovou stránku; zkontrolujte canonical, jazyk a indexovatelnost.
5. Po nasazení sledujte Page indexing, Core Web Vitals a výsledky podle země/jazyka. O ruční indexaci žádejte jen u několika reprezentativních URL, ne u všech stránek opakovaně.

## Vercel

Projekt používá framework preset **Other**. Build command ani output directory nejsou potřeba. `vercel.json` sjednocuje trailing slash URL, přidává pragmatické bezpečnostní hlavičky a krátkou cache pro měnitelné CSS/JS; stabilní obrazové identity mají delší cache bez příznaku `immutable`, protože jejich názvy nejsou verzované.
