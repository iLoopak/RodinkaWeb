"""Generate the static multilingual Rodinka marketing site.

The generated HTML is committed so Vercel can keep serving the repository without
a build command. Run this file after editing shared templates or localized copy.
"""

from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SITE_URL = "https://mojerodinka.cz"
APP_URL = "https://app.mojerodinka.cz"
OG_IMAGE_WIDTH = 1794
OG_IMAGE_HEIGHT = 877
OG_IMAGES = {"cs": "/og-image.png", "sk": "/og-image-sk.png", "en": "/og-image-en.png"}
ASSET_VERSION = "20260901"


LOCALES = {
    "cs": {
        "lang": "cs",
        "og_locale": "cs_CZ",
        "home_path": "/",
        "site_description": "Rodinka je rodinný plánovač pro sdílený kalendář, úkoly, nákupy a plánování jídel.",
        "nav": {"planner": "Rodinný plánovač", "calendar": "Kalendář", "chores": "Úkoly", "shopping": "Nákupy", "meals": "Jídla"},
        "open_app": "Otevřít aplikaci",
        "start": "Začít zdarma",
        "home": "Domů",
        "features": "Funkce",
        "primary_nav": "Hlavní navigace",
        "breadcrumb": "Cesta na webu",
        "about": "Rodinka",
        "learn_more": "Zjistit více",
        "related": "Související témata",
        "related_kicker": "DALŠÍ ČTENÍ",
        "language_label": "Jazyk webu",
        "footer_text": "Pro klidnější každodennost.",
        "copyright": "© 2026 Rodinka",
        "app_label": "O aplikaci Rodinka",
    },
    "sk": {
        "lang": "sk",
        "og_locale": "sk_SK",
        "home_path": "/sk/",
        "site_description": "Rodinka je rodinný plánovač pre zdieľaný kalendár, úlohy, nákupy a plánovanie jedál.",
        "nav": {"planner": "Rodinný plánovač", "calendar": "Kalendár", "chores": "Úlohy", "shopping": "Nákupy", "meals": "Jedlá"},
        "open_app": "Otvoriť aplikáciu",
        "start": "Začať zadarmo",
        "home": "Domov",
        "features": "Funkcie",
        "primary_nav": "Hlavná navigácia",
        "breadcrumb": "Cesta na webe",
        "about": "Rodinka",
        "learn_more": "Zistiť viac",
        "related": "Súvisiace témy",
        "related_kicker": "ĎALŠIE ČÍTANIE",
        "language_label": "Jazyk webu",
        "footer_text": "Pre pokojnejší každý deň.",
        "copyright": "© 2026 Rodinka",
        "app_label": "O aplikácii Rodinka",
    },
    "en": {
        "lang": "en",
        "og_locale": "en_US",
        "home_path": "/en/",
        "site_description": "Rodinka is a family organizer for a shared calendar, chores, shopping lists and meal planning.",
        "nav": {"planner": "Family planner", "calendar": "Calendar", "chores": "Chores", "shopping": "Shopping", "meals": "Meals"},
        "open_app": "Open the app",
        "start": "Start for free",
        "home": "Home",
        "features": "Features",
        "primary_nav": "Primary navigation",
        "breadcrumb": "Breadcrumb",
        "about": "Rodinka",
        "learn_more": "Learn more",
        "related": "Related topics",
        "related_kicker": "KEEP EXPLORING",
        "language_label": "Website language",
        "footer_text": "A calmer way to run family life.",
        "copyright": "© 2026 Rodinka",
        "app_label": "About the Rodinka app",
    },
}


PATHS = {
    "home": {"cs": "/", "sk": "/sk/", "en": "/en/"},
    "planner": {"cs": "/rodinny-planovac/", "sk": "/sk/rodinny-planovac/", "en": "/en/family-planner/"},
    "calendar": {"cs": "/rodinny-kalendar/", "sk": "/sk/rodinny-kalendar/", "en": "/en/family-calendar/"},
    "shopping": {"cs": "/sdileny-nakupni-seznam/", "sk": "/sk/zdielany-nakupny-zoznam/", "en": "/en/shared-shopping-list/"},
    "chores": {"cs": "/ukoly-pro-rodinu/", "sk": "/sk/ulohy-pre-rodinu/", "en": "/en/family-chores/"},
    "meals": {"cs": "/planovani-jidla/", "sk": "/sk/planovanie-jedal/", "en": "/en/meal-planning/"},
    "app": {"cs": "/aplikace-pro-rodinu/", "sk": "/sk/aplikacia-pre-rodinu/", "en": "/en/family-organizer/"},
}


RELATED = {
    "planner": ("calendar", "chores", "app"),
    "calendar": ("planner", "chores", "meals"),
    "shopping": ("meals", "planner", "app"),
    "chores": ("calendar", "planner", "app"),
    "meals": ("shopping", "calendar", "planner"),
    "app": ("planner", "calendar", "shopping"),
}


HOME = {
    "cs": {
        "title": "Rodinka – rodinný plánovač, kalendář, úkoly a nákupy",
        "description": "Rodinný plánovač pro celou domácnost. Sdílejte kalendář, úkoly, nákupní seznam i plán jídel a mějte rodinný život na jednom místě.",
        "og_title": "Rodinka: rodinný život přehledně na jednom místě",
        "og_description": "Společný kalendář, domácí úkoly, nákupy a jídla pro celou rodinu. Méně hledání v chatu, více společného přehledu.",
        "og_alt": "Rodinka – rodinný plánovač s kalendářem, úkoly, nákupy a jídly",
        "eyebrow": "Rodinný život. Konečně pohromadě.",
        "h1": "Rodinný plánovač, který drží domácnost pohromadě.",
        "brand_line": "Všechno, co se doma pořád řeší. Na jednom místě.",
        "lead": "Společný rodinný kalendář, úkoly, jídla a nákupy pro oba rodiče i celou rodinu. Méně zpráv typu „kdo vyzvedává?“ a méně věcí, které musí někdo nosit v hlavě.",
        "how_link": "Podívat se, jak funguje",
        "proof": ("Bez platební karty", "Funguje v prohlížeči", "Na mobilu i počítači"),
        "trust_title": "Jedna domácnost, jeden přehled.",
        "trust_text": "Začněte vy a během chvilky můžete přizvat druhého dospělého.",
        "phone_date": "ÚTERÝ 16. ČERVENCE",
        "phone_greeting": "Dobré ráno, Martine 👋",
        "today": "Dnešní plán",
        "items": "3 položky",
        "agenda": (("8:00", "Školka", "Vyzvedává Klára"), ("16:30", "Plavání", "Ema · Sportcentrum"), ("18:00", "Večeře", "Těstoviny s pestem")),
        "quick": (("Úkoly", "2 hotové"), ("Nákup", "8 položek")),
        "intro_kicker": "ZA PÁR MINUT MÁTE ZÁKLAD HOTOVÝ",
        "intro_title": "Začněte jednou věcí. Zbytek přijde přirozeně.",
        "intro_lead": "Rodinka vás nenutí nastavovat celou domácnost dopředu. Vytvořte rodinu, pozvěte druhého dospělého a přidejte první společnou věc.",
        "steps": (("Vytvořte Rodinku", "Pár základních údajů a máte společný prostor připravený. Bez složité konfigurace."), ("Pozvěte druhého dospělého", "Oba pak vidíte stejný plán a stejné domácí věci."), ("Přidejte první společnou věc", "Kroužek, nákup nebo úkol. Stačí začít tím, co zrovna řešíte.")),
        "note_title": "Ne další aplikace na spravování.",
        "note": "Cílem Rodinky je odstranit část domlouvání, připomínání a hledání informací napříč chaty, kalendáři a poznámkami.",
        "features_kicker": "JEDEN DOMOV PRO VAŠE PLÁNY",
        "features_title": "Co Rodinka drží pohromadě",
        "features_lead": "Rodina ví, co se děje, kdo co řeší a kde najít věci, které jinak mizí v chatu nebo v hlavě.",
        "feature_copy": {
            "calendar": ("KALENDÁŘ", "Kdo kdy kam jde — a kdo koho veze.", "Opakované aktivity, kroužky i jasný doprovod. Od školky po víkend u babičky."),
            "shopping": ("NÁKUPY", "Co koupit už nemusí být ve třech zprávách.", "Přidejte položku doma, odškrtněte ji v obchodě. Seznam má každý po ruce."),
            "chores": ("ÚKOLY", "Je vidět, kdo co doma zařídí.", "Domácí povinnosti mají vlastníka i termín. Děti mohou mít své jednoduché úkoly."),
            "meals": ("JÍDLO", "Co bude k večeři? Nemusí se řešit každý den znovu.", "Naplánujte jídla na týden a suroviny pošlete rovnou do nákupního seznamu."),
        },
        "directory_kicker": "PODLE TOHO, CO DOMA ŘEŠÍTE",
        "directory_title": "Jedna Rodinka, několik cest k většímu klidu",
        "directory_lead": "Začněte kalendářem, povinnostmi nebo nákupy. Každá část funguje samostatně a dohromady tvoří společný rodinný přehled.",
        "quote": "Rodinka není o dokonale zorganizovaném životě. Je o tom, aby organizování neleželo jen na jednom člověku.",
        "quote_by": "Vytvořeno pro skutečné domácnosti",
        "cta_kicker": "MŮŽETE ZAČÍT HNED",
        "cta_title": "Dejte rodinnému chaosu jedno společné místo.",
        "cta_text": "Otevřete Rodinku v prohlížeči, vytvořte rodinu a pozvěte druhého dospělého. Instalace není podmínkou.",
        "login": "Už mám účet",
        "journey": (("1. Vytvořit rodinu", "Základ je hotový během pár minut."), ("2. Pozvat partnera", "Sdílíte jeden rodinný přehled."), ("3. Přidat první věc", "Třeba kroužek, nákup nebo úkol.")),
        "install_title": "Chcete Rodinku jako aplikaci ve Windows?",
        "install_text": "Microsoft Store je alternativní způsob instalace. Na mobilu i ostatních zařízeních můžete používat webovou verzi.",
        "store": "Otevřít Microsoft Store",
        "fine_print": "Bez platební karty. Funguje na mobilu i počítači.",
    },
    "sk": {
        "title": "Rodinka – rodinný plánovač, kalendár, úlohy a nákupy",
        "description": "Rodinný plánovač pre celú domácnosť. Zdieľajte kalendár, úlohy, nákupný zoznam aj plán jedál a majte rodinný život na jednom mieste.",
        "og_title": "Rodinka: spoločný prehľad pre každodenný rodinný život",
        "og_description": "Kalendár, domáce povinnosti, nákupy a jedlá pre celú rodinu. Menej hľadania v správach, viac spoločného prehľadu.",
        "og_alt": "Rodinka – rodinný plánovač s kalendárom, úlohami, nákupmi a jedlami",
        "eyebrow": "Rodinný život. Konečne pokope.",
        "h1": "Rodinný plánovač, ktorý drží domácnosť pokope.",
        "brand_line": "Všetko, čo sa doma stále rieši. Na jednom mieste.",
        "lead": "Spoločný rodinný kalendár, úlohy, jedlá a nákupy pre oboch rodičov aj celú rodinu. Menej správ typu „kto vyzdvihne deti?“ a menej vecí, ktoré musí niekto nosiť v hlave.",
        "how_link": "Pozrieť sa, ako funguje",
        "proof": ("Bez platobnej karty", "Funguje v prehliadači", "V mobile aj počítači"),
        "trust_title": "Jedna domácnosť, jeden prehľad.",
        "trust_text": "Začnite vy a o chvíľu môžete pozvať druhého dospelého.",
        "phone_date": "UTOROK 16. JÚLA",
        "phone_greeting": "Dobré ráno, Martin 👋",
        "today": "Dnešný plán",
        "items": "3 položky",
        "agenda": (("8:00", "Škôlka", "Vyzdvihne Klára"), ("16:30", "Plávanie", "Ema · Športcentrum"), ("18:00", "Večera", "Cestoviny s pestom")),
        "quick": (("Úlohy", "2 hotové"), ("Nákup", "8 položiek")),
        "intro_kicker": "ZA PÁR MINÚT MÁTE ZÁKLAD HOTOVÝ",
        "intro_title": "Začnite jednou vecou. Zvyšok príde prirodzene.",
        "intro_lead": "Rodinka vás nenúti nastaviť celú domácnosť vopred. Vytvorte rodinu, pozvite druhého dospelého a pridajte prvú spoločnú vec.",
        "steps": (("Vytvorte Rodinku", "Pár základných údajov a spoločný priestor je pripravený. Bez zložitého nastavovania."), ("Pozvite druhého dospelého", "Obaja potom vidíte rovnaký plán aj rovnaké domáce veci."), ("Pridajte prvú spoločnú vec", "Krúžok, nákup alebo úlohu. Začnite tým, čo práve riešite.")),
        "note_title": "Nie ďalšia aplikácia na spravovanie.",
        "note": "Rodinka má ubrať z dohadovania, pripomínania a hľadania informácií v správach, kalendároch a poznámkach.",
        "features_kicker": "JEDEN DOMOV PRE VAŠE PLÁNY",
        "features_title": "Čo Rodinka drží pokope",
        "features_lead": "Rodina vie, čo sa deje, kto čo rieši a kde nájde veci, ktoré by inak zapadli v chate alebo zostali iba v hlave.",
        "feature_copy": {
            "calendar": ("KALENDÁR", "Kto kedy kam ide — a kto koho odvezie.", "Opakované aktivity, krúžky aj jasný sprievod. Od škôlky po víkend u starej mamy."),
            "shopping": ("NÁKUPY", "Čo kúpiť už nemusí byť v troch správach.", "Pridajte položku doma, odškrtnite ju v obchode. Zoznam má každý poruke."),
            "chores": ("ÚLOHY", "Je jasné, kto čo doma zariadi.", "Domáce povinnosti majú svojho človeka aj termín. Deti môžu mať jednoduché úlohy."),
            "meals": ("JEDLO", "Čo bude na večeru? Nemusíte to riešiť každý deň.", "Naplánujte jedlá na týždeň a suroviny pošlite rovno do nákupného zoznamu."),
        },
        "directory_kicker": "PODĽA TOHO, ČO DOMA RIEŠITE",
        "directory_title": "Jedna Rodinka, viac ciest k pokojnejšiemu dňu",
        "directory_lead": "Začnite kalendárom, povinnosťami alebo nákupmi. Každá časť funguje samostatne a spolu tvoria spoločný rodinný prehľad.",
        "quote": "Rodinka nie je o dokonale zorganizovanom živote. Je o tom, aby organizovanie neležalo iba na jednom človeku.",
        "quote_by": "Vytvorené pre skutočné domácnosti",
        "cta_kicker": "MÔŽETE ZAČAŤ HNEĎ",
        "cta_title": "Dajte rodinnému chaosu jedno spoločné miesto.",
        "cta_text": "Otvorte Rodinku v prehliadači, vytvorte rodinu a pozvite druhého dospelého. Inštalácia nie je podmienkou.",
        "login": "Už mám účet",
        "journey": (("1. Vytvoriť rodinu", "Základ je hotový za pár minút."), ("2. Pozvať partnera", "Zdieľate jeden rodinný prehľad."), ("3. Pridať prvú vec", "Napríklad krúžok, nákup alebo úlohu.")),
        "install_title": "Chcete Rodinku ako aplikáciu vo Windows?",
        "install_text": "Microsoft Store je alternatívny spôsob inštalácie. V mobile aj na ostatných zariadeniach môžete používať webovú verziu.",
        "store": "Otvoriť Microsoft Store",
        "fine_print": "Bez platobnej karty. Funguje v mobile aj počítači.",
    },
    "en": {
        "title": "Rodinka – family planner, calendar, chores and shopping",
        "description": "A family planner for the whole household. Share a calendar, chores, shopping list and meal plan so family life stays in one clear place.",
        "og_title": "Rodinka: one shared place for everyday family life",
        "og_description": "A family calendar, household chores, shopping and meals in one calm shared view — with fewer details lost in chat.",
        "og_alt": "Rodinka family organizer with a calendar, chores, shopping list and meals",
        "eyebrow": "Family life. Finally in one place.",
        "h1": "A family organizer that keeps home life together.",
        "brand_line": "Everything your household keeps talking about. In one place.",
        "lead": "A shared family calendar, chores, meals and shopping for parents and the whole household. Fewer “who is picking up?” messages and fewer details for one person to keep in their head.",
        "how_link": "See how it works",
        "proof": ("No payment card", "Works in your browser", "Phone and computer"),
        "trust_title": "One household, one clear view.",
        "trust_text": "Get started, then invite the other adult in your family in a moment.",
        "phone_date": "TUESDAY, JULY 16",
        "phone_greeting": "Good morning, Martin 👋",
        "today": "Today’s plan",
        "items": "3 items",
        "agenda": (("8:00", "Daycare", "Klára is picking up"), ("16:30", "Swimming", "Ema · Sports centre"), ("18:00", "Dinner", "Pasta with pesto")),
        "quick": (("Chores", "2 done"), ("Shopping", "8 items")),
        "intro_kicker": "THE BASICS TAKE JUST A FEW MINUTES",
        "intro_title": "Start with one thing. Let the rest follow naturally.",
        "intro_lead": "Rodinka does not make you configure your whole household up front. Create your family, invite another adult and add the first thing you both need.",
        "steps": (("Create your Rodinka", "A few basic details and your shared space is ready. No complicated setup."), ("Invite another adult", "You both see the same plan and the same household details."), ("Add the first shared thing", "An activity, shopping item or chore. Start with whatever needs sorting out today.")),
        "note_title": "Not another app to manage.",
        "note": "Rodinka is meant to reduce the coordinating, reminding and searching spread across chats, calendars and notes.",
        "features_kicker": "ONE HOME FOR YOUR FAMILY PLANS",
        "features_title": "What Rodinka keeps together",
        "features_lead": "Everyone can see what is happening, who is handling it and where to find details that would otherwise disappear into a chat thread.",
        "feature_copy": {
            "calendar": ("CALENDAR", "Who needs to be where — and who is driving.", "Recurring activities, school events and clear pick-up plans, from daycare to a weekend with grandparents."),
            "shopping": ("SHOPPING", "The grocery list no longer lives in three messages.", "Add something at home and check it off in the shop. Everyone has the same list close at hand."),
            "chores": ("CHORES", "It is clear who is handling what at home.", "Household chores have an owner and a due date. Children can have simple responsibilities of their own."),
            "meals": ("MEALS", "What is for dinner? It does not need a new answer every day.", "Plan a week of meals and send ingredients straight to the shared shopping list."),
        },
        "directory_kicker": "START WITH WHAT YOUR FAMILY NEEDS",
        "directory_title": "One Rodinka, several ways to make family life calmer",
        "directory_lead": "Begin with the calendar, chores or shopping. Each part is useful on its own and together they create a shared family overview.",
        "quote": "Rodinka is not about a perfectly organized life. It is about making sure the organizing does not sit with just one person.",
        "quote_by": "Made for real households",
        "cta_kicker": "YOU CAN START RIGHT AWAY",
        "cta_title": "Give family chaos one shared home.",
        "cta_text": "Open Rodinka in your browser, create your family and invite another adult. You do not have to install anything.",
        "login": "I already have an account",
        "journey": (("1. Create a family", "The basics take just a few minutes."), ("2. Invite your partner", "You share one family overview."), ("3. Add the first thing", "An activity, shopping item or chore.")),
        "install_title": "Would you like Rodinka as a Windows app?",
        "install_text": "Microsoft Store is another way to install Rodinka. On phones and other devices, you can use the web version.",
        "store": "Open Microsoft Store",
        "fine_print": "No payment card. Works on phones and computers.",
    },
}


TOPICS = {
    "cs": {
        "planner": {
            "title": "Rodinný plánovač pro klidnější domácnost | Rodinka",
            "description": "Rodinný plánovač spojí kalendář, úkoly, nákupy a jídla do jednoho přehledu. Zjistěte, jak si doma rozdělit plánování bez dalšího chaosu.",
            "og_title": "Rodinný plánovač, který není další domácí projekt",
            "og_description": "Praktický společný přehled pro termíny, povinnosti, nákupy a jídlo — aby organizování neleželo na jednom člověku.",
            "og_alt": "Rodinka jako společný rodinný plánovač pro každodenní domácnost",
            "eyebrow": "SPOLEČNÝ RODINNÝ PŘEHLED",
            "h1": "Rodinný plánovač pro věci, které doma řešíte každý den",
            "lead": "Kroužky, vyzvedávání, nákupy, večeře i úkoly se snadno rozutečou mezi kalendář, chat a papírek na lednici. Rodinný plánovač dává celé domácnosti jedno místo, kam se podívat.",
            "problem_title": "Rodinné plánování není práce pro jednoho člověka",
            "problem": ("V mnoha domácnostech drží termíny a povinnosti v hlavě jeden rodič. Ostatní se ptají, co je dnes potřeba, a odpověď se znovu hledá ve zprávách. Nejde o nedostatek snahy — informace jen nemají společný domov.", "Dobře nastavený plánovač nemá přidávat administrativu. Má během pár vteřin ukázat, kdo dnes vyzvedává dítě, kdy začíná kroužek, co chybí doma a co bude k večeři."),
            "scenarios": (("Ráno bez pátrání", "Před odchodem každý vidí dnešní termíny, doprovod i důležité domácí úkoly."), ("Změna se neztratí", "Když se trénink posune nebo někdo přidá nákup, změna je ve společném přehledu."), ("Méně mentální zátěže", "Plán nemusí hlídat jediný člověk. Rodina si informace i odpovědnost skutečně sdílí.")),
            "help_title": "Jak Rodinka pomáhá organizovat rodinu",
            "help_intro": "Začít můžete jedinou oblastí a další přidat až ve chvíli, kdy dávají smysl. Všechny ale zůstávají propojené v jednom rodinném prostoru.",
            "steps": (("Sdílejte stejný plán", "Rodinný kalendář ukazuje společné i osobní události a pomáhá ujasnit, kdo má co na starosti."), ("Rozdělte konkrétní povinnosti", "Úkol dostane člověka a termín, takže z neurčitého „mělo by se“ vznikne srozumitelná dohoda."), ("Mějte provoz domácnosti při ruce", "Nákupní seznam a plán jídel doplní termíny o praktické věci, které se řeší každý týden.")),
            "answers_title": "Časté otázky o rodinném plánování",
            "answers": (("Co má umět dobrý rodinný plánovač?", "Především rychle ukázat společný kalendář, rozdělené úkoly a praktické seznamy. Ovládání má být natolik jednoduché, aby se zapojili oba rodiče a podle věku i děti."), ("Jak začít, když rodina nechce další aplikaci?", "Vyberte jednu opakovanou bolest — třeba kroužky nebo nákup. Jakmile společný přehled ušetří pár dotazů, přidejte další oblast. Není nutné převádět všechno první den."), ("Jak snížit rodinné domlouvání přes chat?", "Do chatu patří rozhovor, ne dlouhodobý přehled. Termíny, úkoly a položky nákupu zapisujte na společné místo a ve zprávě už jen upozorněte na změnu, pokud je to potřeba.")),
            "card": "Jeden přehled pro termíny, domácí povinnosti, nákupy i jídla.",
            "cta_title": "Začněte tím, co doma řešíte nejčastěji.",
            "cta_text": "Vytvořte Rodinku a přidejte první termín, úkol nebo položku nákupu. Zbytek může přijít postupně.",
        },
        "calendar": {
            "title": "Rodinný kalendář pro rodiče i děti | Rodinka",
            "description": "Sdílený rodinný kalendář pro kroužky, školu, lékaře i vyzvedávání. Všichni vidí, co se děje a kdo má co zařídit.",
            "og_title": "Rodinný kalendář bez dotazů „kdo vyzvedává?“",
            "og_description": "Mějte školu, kroužky, lékaře, návštěvy i doprovod v jednom kalendáři pro celou domácnost.",
            "og_alt": "Sdílený rodinný kalendář Rodinka s termíny a doprovodem",
            "eyebrow": "TERMÍNY PRO CELOU DOMÁCNOST",
            "h1": "Sdílený rodinný kalendář, ve kterém je jasno",
            "lead": "Kdy je besídka, kdo veze na plavání a jestli je sobotní návštěva potvrzená? Rodinný kalendář drží termíny i domluvený doprovod pohromadě, aby se každý mohl podívat sám.",
            "problem_title": "Samotný termín často nestačí",
            "problem": ("Rodinný program není jen seznam hodin. U dětských aktivit je stejně důležité vědět, koho se událost týká, kam se jede a kdo z dospělých zajišťuje cestu. Když část informace zůstane v chatu, kalendář nepomůže naplno.", "Společný kalendář má být rychlý při ranní kontrole i při plánování celého týdne. Opakované kroužky se zapíší jednou, jednorázová změna se ukáže všem a rodina nemusí udržovat několik rozdílných verzí plánu."),
            "scenarios": (("Kroužky dětí", "Plavání, hudebka i trénink mají čas, místo, dítě a domluvený doprovod."), ("Škola a lékaři", "Třídní schůzky, preventivní prohlídky a volné dny nezůstávají jen v e-mailu jednoho rodiče."), ("Víkendy a návštěvy", "Rodinné oslavy nebo víkend u prarodičů jsou vidět dřív, než se naplánuje něco dalšího.")),
            "help_title": "Jak funguje sdílený rodinný kalendář v Rodince",
            "help_intro": "Události zapisujete do stejného rodinného prostoru. Každý dospělý tak pracuje s aktuálním plánem a nemusí čekat, až mu druhý pošle screenshot.",
            "steps": (("Přidejte událost", "Zapište čas, místo a člena rodiny, kterého se událost týká. U pravidelného kroužku nastavte opakování."), ("Ujasněte doprovod", "Přímo u plánu je vidět, kdo dítě přiveze nebo vyzvedne. Praktická část domluvy nezůstane ve vedlejším chatu."), ("Kontrolujte společný týden", "Při plánování návštěvy nebo vlastního programu oba rodiče vidí stejné rodinné závazky.")),
            "answers_title": "Co lidé hledají u rodinného kalendáře",
            "answers": (("Jak sdílet rodinný kalendář mezi rodiči?", "Vytvořte jeden rodinný prostor a pozvěte druhého dospělého. Události zapisujte tam, ne do dvou oddělených kalendářů, a doplňte i informaci o doprovodu, pokud je pro plán důležitá."), ("Jak zorganizovat kroužky dětí?", "U každého kroužku evidujte den, čas, místo, dítě a dopravu. Pravidelné termíny nastavte jako opakované a výjimky upravujte jednotlivě, aby zůstal týdenní plán čitelný."), ("Patří do rodinného kalendáře i úkoly?", "Událost říká, kdy se něco děje. Přípravu — třeba koupit dárek nebo odevzdat přihlášku — je lepší vést jako samostatný úkol s termínem a odpovědnou osobou.")),
            "card": "Kroužky, škola, návštěvy a vyzvedávání ve společném kalendáři.",
            "cta_title": "Ať se na plán nemusí nikdo znovu ptát.",
            "cta_text": "Přidejte do Rodinky první událost a domluvte rovnou i to, kdo ji zajišťuje.",
        },
        "shopping": {
            "title": "Sdílený nákupní seznam pro celou rodinu | Rodinka",
            "description": "Společný nákupní seznam, který může rodina průběžně doplňovat a v obchodě odškrtávat. Bez papírků a položek ztracených v chatu.",
            "og_title": "Společný nákupní seznam, který máte vždy po ruce",
            "og_description": "Přidávejte, co doma dochází, a nakupujte ze stejného aktuálního seznamu.",
            "og_alt": "Sdílený rodinný nákupní seznam v aplikaci Rodinka",
            "eyebrow": "NÁKUPY BEZ ZAPOMENUTÝCH ZPRÁV",
            "h1": "Sdílený nákupní seznam, do kterého může přidat každý",
            "lead": "Mléko došlo ráno, pečivo někdo napsal do chatu a seznam na lednici zůstal doma. Společný nákupní seznam zachytí položku ve chvíli, kdy si na ni někdo vzpomene — a v obchodě je pořád aktuální.",
            "problem_title": "Největší problém nákupu bývá sběr informací",
            "problem": ("Samotné nakupování je jednoduché. Složitější je zjistit, co opravdu chybí, jestli už to někdo přidal a kdo se dnes do obchodu dostane. Papírek funguje jen doma a zpráva v chatu rychle zapadne.", "Když má domácnost jeden seznam, nezáleží tolik na tom, kdo nakonec nakoupí. Položky může průběžně doplňovat každý, hotové věci se odškrtnou a zbytek zůstane pro příště."),
            "scenarios": (("Něco právě došlo", "Poslední mléko nebo prací gel se zapíše hned, ne až při vzpomínání před obchodem."), ("Nakupuje někdo jiný", "Partner cestou z práce otevře stejný seznam a nemusí si vyžádat novou zprávu."), ("Plánujete jídla", "Suroviny k vybraným večeřím se přidají k běžným věcem pro domácnost.")),
            "help_title": "Jak mít společný nákupní seznam v Rodince",
            "help_intro": "Seznam je součástí rodinného prostoru, takže ho vidí pozvaní členové domácnosti na mobilu i počítači.",
            "steps": (("Přidávejte průběžně", "Zapište položku ve chvíli, kdy doma dochází. Krátký aktuální seznam je užitečnější než velké vzpomínání jednou týdně."), ("Nakupujte ze stejné verze", "V obchodě položky odškrtávejte. Ostatní vidí, co je hotové, a nepřidávají stejné věci podruhé."), ("Propojte nákup s jídlem", "Při plánování večeří doplňte potřebné suroviny, aby týdenní jídelníček nezůstal jen přáním.")),
            "answers_title": "Praktické otázky ke společnému nákupu",
            "answers": (("Jak sdílet nákupní seznam s partnerem?", "Používejte jeden seznam ve společném rodinném prostoru. Oba do něj mohou přidávat a při nákupu odškrtávat, takže není potřeba posílat pokaždé novou verzi."), ("Je lepší seznam v aplikaci, nebo na papíře?", "Papír je rychlý, když u něj právě stojíte. Sdílený seznam je ale dostupný i mimo domov a může ho aktualizovat více lidí. Pro domácnost, kde se v nákupech střídáte, bývá praktičtější."), ("Jak nezapomínat suroviny na celý týden?", "Nejdřív si rámcově naplánujte hlavní jídla a potom projděte potřebné suroviny. Přidejte jen to, co doma opravdu není; seznam tak zůstane přehledný.")),
            "card": "Jeden aktuální seznam doma i v obchodě, který doplňuje celá rodina.",
            "cta_title": "Příští nákup nemusí začínat hledáním zpráv.",
            "cta_text": "Otevřete v Rodince společný seznam a přidejte první věc, která doma právě dochází.",
        },
        "chores": {
            "title": "Rodinné úkoly a domácí povinnosti přehledně | Rodinka",
            "description": "Rozdělte domácí úkoly mezi členy rodiny, přidejte termín a mějte jasno, kdo co zařídí. Prakticky pro rodiče i děti.",
            "og_title": "Domácí povinnosti bez nekonečného připomínání",
            "og_description": "Konkrétní rodinné úkoly, jasná odpovědnost a přehled o tom, co je hotové.",
            "og_alt": "Rodinné úkoly a rozdělené domácí povinnosti v Rodince",
            "eyebrow": "KDO CO DOMA ZAŘÍDÍ",
            "h1": "Rodinné úkoly, které neleží jen v hlavě jednoho rodiče",
            "lead": "Objednat dítě k zubaři, vrátit knížky, vynést koš nebo připravit věci na výlet. Když má úkol konkrétního člověka a termín, domácnost se nemusí spoléhat na opakované připomínání.",
            "problem_title": "„Musíme to udělat“ ještě není rozdělený úkol",
            "problem": ("Domácí práce bývají viditelné až ve chvíli, kdy nejsou hotové. Ještě méně viditelné jsou organizační povinnosti: hlídat přihlášku na tábor, koupit dárek nebo zavolat opraváři. Pokud je drží v hlavě jeden člověk, nese i většinu mentální zátěže.", "Smyslem rodinných úkolů není měřit výkon domácnosti. Jde o jednoduchou dohodu: co je potřeba, kdo to převezme a dokdy. Hotový úkol pak nemusí nikdo znovu kontrolovat v chatu."),
            "scenarios": (("Drobné denní povinnosti", "Koš, nádobí nebo příprava aktovky mohou mít jednoduché a srozumitelné zadání."), ("Neviditelná organizace", "Telefonát lékaři, platba kroužku nebo nákup dárku dostanou vlastníka i termín."), ("Zapojení dětí", "Přiměřené úkoly pomáhají dětem vidět, že domácnost je společná věc, ne servis rodičů.")),
            "help_title": "Jak rozdělit domácí úkoly mezi členy rodiny",
            "help_intro": "Rodinka pomáhá převést neurčité povinnosti na malé konkrétní kroky, které jsou vidět ve společném přehledu.",
            "steps": (("Pojmenujte výsledek", "Místo „řešit školu“ napište konkrétně „odeslat přihlášku na výlet“. Každý hned ví, co znamená hotovo."), ("Přiřaďte člověka a termín", "Úkol nemá zůstat společný tak dlouho, až ho udělá ten nejvšímavější. Domluvte odpovědnost rovnou."), ("Nechte hotové věci zmizet z hlavy", "Splnění je vidět ostatním. Není nutné posílat potvrzovací zprávu ani se opakovaně ptát.")),
            "answers_title": "Otázky k domácím úkolům a povinnostem",
            "answers": (("Jak rozdělit domácí práce spravedlivě?", "Nezačínejte jen viditelným úklidem. Sepište i plánování, telefonáty a hlídání termínů. Rozdělení pak posuzujte podle času a zátěže, ne pouze podle počtu položek."), ("Jak zadávat úkoly dětem?", "Úkol má odpovídat věku, být konkrétní a mít dosažitelný termín. Menším dětem pomůže krátké zadání a společná kontrola; cílem je návyk a zapojení, ne dokonalost."), ("Jak připomínat úkoly bez hádek?", "Dohodněte odpovědnost a zapište ji na společné místo. Připomínka pak neznamená, že jeden rodič druhého řídí; oba se mohou opřít o stejnou dohodu.")),
            "card": "Konkrétní povinnosti, jasný člověk a termín pro rodiče i děti.",
            "cta_title": "Rozdělte první úkol dřív, než se ztratí v hlavě.",
            "cta_text": "Přidejte do Rodinky jednu konkrétní povinnost a domluvte, kdo ji převezme.",
        },
        "meals": {
            "title": "Plánování jídel na týden pro celou rodinu | Rodinka",
            "description": "Naplánujte rodinná jídla na celý týden, snižte každodenní rozhodování a přidejte suroviny do společného nákupního seznamu.",
            "og_title": "Týdenní plán jídel bez každodenní otázky „co vařit?“",
            "og_description": "Praktický jídelní plán pro rodinu, který navazuje na společný nákupní seznam.",
            "og_alt": "Týdenní plánování rodinných jídel v aplikaci Rodinka",
            "eyebrow": "MÉNĚ ROZHODOVÁNÍ KOLEM VEČEŘE",
            "h1": "Plánování jídel na týden, které počítá se skutečným životem",
            "lead": "Některé dny je čas vařit, jindy se rodina vrací pozdě z kroužků. Týdenní plán jídel nemusí být dokonalý jídelníček — stačí, když dopředu odpoví na pár večerů a usnadní nákup.",
            "problem_title": "Nejtěžší často není vaření, ale rozhodování",
            "problem": ("Otázka „co bude k večeři?“ přichází obvykle ve chvíli, kdy je hlad a málo času. Bez rámcového plánu se častěji nakupuje narychlo, některé suroviny chybí a jiné se doma nestihnou využít.", "Rodinný plán má respektovat rytmus týdne. Po náročném odpoledni může počítat s rychlou večeří, o volnějším dni s jídlem, které trvá déle. A když se plán změní, není to selhání — jen aktualizace společného přehledu."),
            "scenarios": (("Den plný kroužků", "Na večer se naplánuje rychlé jídlo, které nevyžaduje dlouhou přípravu po návratu domů."), ("Společné víkendové vaření", "Rodina dopředu vidí, kdy je prostor na oblíbené jídlo nebo vaření s dětmi."), ("Nákup bez hádání", "Z plánovaných jídel vzniknou konkrétní suroviny ve společném nákupním seznamu.")),
            "help_title": "Jak plánovat jídlo na celý týden v Rodince",
            "help_intro": "Nejde o detailní dietní program. Rodinka spojuje jednoduchou představu o jídlech s tím, co je potřeba nakoupit.",
            "steps": (("Podívejte se na rodinný kalendář", "Nejdřív zvažte, které dny jsou dlouhé a kdy bude někdo doma dřív. Plán pak vychází z reálného času."), ("Vyberte několik jistých jídel", "Nemusíte vyplnit každý chod. Začněte večeřemi, které běžně vaříte, a nechte prostor na zbytky nebo změnu."), ("Doplňte suroviny do nákupu", "Zkontrolujte, co už doma je, a chybějící věci přidejte do sdíleného seznamu.")),
            "answers_title": "Časté otázky k plánování rodinného jídla",
            "answers": (("Jak plánovat jídlo na celý týden?", "Začněte rodinným programem a vyberte hlavní jídla podle času na přípravu. Neplánujte příliš těsně; jeden volný večer pomůže využít zbytky nebo reagovat na změnu."), ("Jak zapojit rodinu do výběru jídel?", "Nechte každého navrhnout jedno oblíbené jídlo a společně rozhodněte, do kterého dne se hodí. Plán je pak méně práce pro jednoho člověka a má větší šanci, že bude fungovat."), ("Jak propojit jídelníček s nákupním seznamem?", "U každého plánovaného jídla projděte hlavní suroviny a chybějící přidejte do společného seznamu. Před nákupem ještě zkontrolujte zásoby, aby se věci zbytečně nedublovaly.")),
            "card": "Jednoduchý plán večeří podle rodinného týdne a potřebných nákupů.",
            "cta_title": "Naplánujte pár večeří a ulevte zbytku týdne.",
            "cta_text": "Otevřete Rodinku, vyberte první jídlo a doplňte, co k němu bude potřeba koupit.",
        },
        "app": {
            "title": "Aplikace pro rodinu: kalendář, úkoly i nákupy | Rodinka",
            "description": "Rodinka je aplikace pro rodinu, která spojuje kalendář, domácí úkoly, nákupní seznam a plán jídel v jednom společném přehledu.",
            "og_title": "Jedna aplikace pro každodenní organizaci rodiny",
            "og_description": "Místo roztříštěných chatů, poznámek a kalendářů má rodina společný prostor pro to, co právě řeší.",
            "og_alt": "Aplikace Rodinka pro společnou organizaci rodinného života",
            "eyebrow": "APLIKACE PRO KAŽDODENNÍ RODINNÝ PROVOZ",
            "h1": "Aplikace pro rodinu, která spojuje plán i domácí povinnosti",
            "lead": "Kalendář ukazuje termíny, ale ne vždy nákup. Chat obsahuje domluvu, ale špatně se v něm hledá za týden. Rodinka spojuje praktické části rodinného života, aby každý věděl, kam se podívat.",
            "problem_title": "Rodina nepotřebuje více míst, ale méně hledání",
            "problem": ("Každý nástroj může fungovat dobře sám o sobě, přesto se celek rozpadá. Termín je v osobním kalendáři, seznam na papíře, úkol v hlavě a změna ve skupinovém chatu. Informace existují, jen nejsou dostupné všem ve správný okamžik.", "Dobrá aplikace pro rodinu nesmí vyžadovat správce na plný úvazek. Zápis běžné věci má být rychlý, společný přehled srozumitelný a jednotlivé části mají odpovídat situacím, které domácnost opravdu řeší."),
            "scenarios": (("Před odchodem z domu", "Jeden pohled ukáže dnešní program, doprovod a povinnosti, které nesmějí zůstat doma."), ("Během dne", "Kdokoli přidá chybějící nákup nebo označí hotový úkol, aniž by musel psát všem zvlášť."), ("Při plánování týdne", "Kalendář, jídla a domácí úkoly dávají dohromady realistický obraz toho, co rodinu čeká.")),
            "help_title": "Co najdete v aplikaci Rodinka",
            "help_intro": "Jednotlivé části používáte podle potřeby. Jejich výhoda roste ve chvíli, kdy navazují jedna na druhou.",
            "steps": (("Rodinný kalendář", "Společné termíny, opakované aktivity a informace o tom, kdo zajišťuje doprovod."), ("Úkoly a domácnost", "Povinnosti s konkrétním člověkem a termínem, aby organizace neležela jen na jednom rodiči."), ("Nákupy a plán jídel", "Seznam toho, co chybí, a jednoduchý výhled na rodinné večeře v jednom prostoru.")),
            "answers_title": "Jak vybírat aplikaci pro rodinu",
            "answers": (("Co by měla aplikace pro rodinu umět?", "Měla by pokrýt nejčastější společné situace, být rychlá na mobilu i počítači a dovolit více členům pracovat se stejnými aktuálními informacemi."), ("Nahradí Rodinka rodinný chat?", "Ne. Chat je skvělý pro rozhovor. Rodinka slouží jako přehled pro termíny, úkoly a seznamy, které potřebujete najít i později bez procházení historie zpráv."), ("Musí rodina začít používat všechny funkce?", "Nemusí. Nejpraktičtější je začít jednou oblastí, která dnes způsobuje nejvíce dotazů. Další části přidejte až tehdy, když domácnosti opravdu pomohou.")),
            "card": "Kalendář, povinnosti, nákupní seznam a jídla v jednom rodinném prostoru.",
            "cta_title": "Dejte rodinným informacím jedno známé místo.",
            "cta_text": "Rodinka funguje rovnou v prohlížeči. Vytvořte rodinu a začněte první praktickou věcí.",
        },
    },
    "sk": {},
    "en": {},
}


# Slovak and English pages intentionally use native, independently written copy.
TOPICS["sk"] = {
    "planner": {
        "title": "Rodinný plánovač pre pokojnejšiu domácnosť | Rodinka",
        "description": "Rodinný plánovač spojí kalendár, úlohy, nákupy a jedlá do jedného prehľadu. Rozdeľte si domáce plánovanie bez ďalšieho chaosu.",
        "og_title": "Rodinný plánovač, ktorý nie je ďalším domácim projektom",
        "og_description": "Spoločný prehľad termínov, povinností, nákupov a jedál, aby organizovanie neležalo na jednom človeku.",
        "og_alt": "Rodinka ako spoločný rodinný plánovač pre každodennú domácnosť",
        "eyebrow": "SPOLOČNÝ RODINNÝ PREHĽAD", "h1": "Rodinný plánovač pre veci, ktoré doma riešite každý deň",
        "lead": "Krúžky, vyzdvihovanie, nákupy, večere aj úlohy sa ľahko rozdelia medzi kalendár, správy a papierik na chladničke. Rodinný plánovač dá celej domácnosti jedno miesto, kam sa môže pozrieť.",
        "problem_title": "Rodinné plánovanie nemá byť prácou jedného človeka",
        "problem": ("V mnohých domácnostiach drží termíny a povinnosti v hlave jeden rodič. Ostatní sa pýtajú, čo treba vybaviť, a odpoveď sa znovu hľadá v správach. Informácie jednoducho nemajú spoločný domov.", "Dobrý plánovač nepridáva administratívu. Za pár sekúnd má ukázať, kto dnes vyzdvihne dieťa, kedy začína krúžok, čo treba kúpiť a čo bude tento týždeň na večeru."),
        "scenarios": (("Ráno bez pátrania", "Pred odchodom každý vidí dnešné termíny, odvoz aj dôležité domáce úlohy."), ("Zmena sa nestratí", "Keď sa tréning posunie alebo niekto pridá nákup, zmena je v spoločnom prehľade."), ("Menej mentálnej záťaže", "Plán nemusí strážiť jediný človek. Rodina si zdieľa informácie aj zodpovednosť.")),
        "help_title": "Ako Rodinka pomáha organizovať rodinu", "help_intro": "Začnite jednou oblasťou a ďalšie pridajte až vtedy, keď dávajú zmysel. Všetky zostanú prepojené v jednom rodinnom priestore.",
        "steps": (("Zdieľajte rovnaký plán", "Rodinný kalendár ukazuje spoločné aj osobné udalosti a pomáha ujasniť, kto má čo na starosti."), ("Rozdeľte konkrétne povinnosti", "Úloha dostane človeka a termín, takže z neurčitého „mali by sme“ vznikne zrozumiteľná dohoda."), ("Majte chod domácnosti poruke", "Nákupný zoznam a plán jedál doplnia termíny o praktické veci, ktoré sa riešia každý týždeň.")),
        "answers_title": "Časté otázky o rodinnom plánovaní",
        "answers": (("Čo má vedieť dobrý rodinný plánovač?", "Najmä rýchlo ukázať spoločný kalendár, rozdelené úlohy a praktické zoznamy. Ovládanie má byť dosť jednoduché pre oboch rodičov a podľa veku aj pre deti."), ("Ako začať, keď rodina nechce ďalšiu aplikáciu?", "Vyberte jednu opakovanú ťažkosť, napríklad krúžky alebo nákup. Keď spoločný prehľad ušetrí niekoľko otázok, pridajte ďalšiu oblasť."), ("Ako obmedziť rodinné dohadovanie cez chat?", "V chate sa rozprávajte, no termíny, úlohy a nákupné položky ukladajte na spoločné miesto. Dôležitá informácia tak nezapadne medzi ostatné správy.")),
        "card": "Jeden prehľad pre termíny, domáce povinnosti, nákupy aj jedlá.", "cta_title": "Začnite tým, čo doma riešite najčastejšie.", "cta_text": "Vytvorte Rodinku a pridajte prvý termín, úlohu alebo nákupnú položku. Zvyšok môže prísť postupne.",
    },
    "calendar": {
        "title": "Rodinný kalendár pre rodičov aj deti | Rodinka", "description": "Zdieľaný rodinný kalendár na krúžky, školu, lekára aj vyzdvihovanie. Všetci vidia, čo sa deje a kto má čo zariadiť.",
        "og_title": "Rodinný kalendár bez otázok „kto vyzdvihne deti?“", "og_description": "Majte školu, krúžky, lekára, návštevy aj odvoz v jednom kalendári pre celú domácnosť.", "og_alt": "Zdieľaný rodinný kalendár Rodinka s termínmi a odvozom",
        "eyebrow": "TERMÍNY PRE CELÚ DOMÁCNOSŤ", "h1": "Zdieľaný rodinný kalendár, v ktorom je jasno", "lead": "Kedy je besiedka, kto vezie na plávanie a či sobotná návšteva stále platí? Rodinný kalendár drží termíny aj dohodnutý odvoz pokope, aby sa každý mohol pozrieť sám.",
        "problem_title": "Samotný termín často nestačí", "problem": ("Rodinný program nie je iba zoznam hodín. Pri detských aktivitách treba vedieť aj to, koho sa udalosť týka, kam sa ide a ktorý dospelý zabezpečí cestu. Ak časť informácie zostane v chate, kalendár nepomôže naplno.", "Spoločný kalendár má byť rýchly pri rannej kontrole aj plánovaní týždňa. Pravidelné krúžky zapíšete raz, jednorazovú zmenu uvidia všetci a rodina nemusí udržiavať viac verzií plánu."),
        "scenarios": (("Krúžky detí", "Plávanie, hudobná aj tréning majú čas, miesto, dieťa a dohodnutý odvoz."), ("Škola a lekári", "Rodičovské združenia, preventívne prehliadky a voľné dni nezostanú iba v e-maile jedného rodiča."), ("Víkendy a návštevy", "Rodinné oslavy či víkend u starých rodičov sú viditeľné skôr, než niekto naplánuje ďalšiu akciu.")),
        "help_title": "Ako funguje zdieľaný rodinný kalendár v Rodinke", "help_intro": "Udalosti zapisujete do jedného rodinného priestoru. Každý dospelý pracuje s aktuálnym plánom a nemusí čakať na novú snímku obrazovky.",
        "steps": (("Pridajte udalosť", "Zapíšte čas, miesto a člena rodiny, ktorého sa týka. Pri pravidelnom krúžku nastavte opakovanie."), ("Ujasnite odvoz", "Pri pláne je vidieť, kto dieťa privezie alebo vyzdvihne. Praktická dohoda nezostane vo vedľajšom chate."), ("Kontrolujte spoločný týždeň", "Pri plánovaní návštevy alebo vlastného programu obaja rodičia vidia rovnaké rodinné záväzky.")),
        "answers_title": "Čo ľudia hľadajú pri rodinnom kalendári", "answers": (("Ako zdieľať rodinný kalendár medzi rodičmi?", "Vytvorte spoločný rodinný priestor a pozvite druhého dospelého. Udalosti zapisujte tam a pri aktivitách doplňte aj dohodnutý odvoz."), ("Ako zorganizovať krúžky detí?", "Pri každom krúžku evidujte deň, čas, miesto, dieťa a dopravu. Pravidelné termíny nastavte ako opakované a výnimky upravujte samostatne."), ("Patria do rodinného kalendára aj úlohy?", "Udalosť hovorí, kedy sa niečo deje. Prípravu, napríklad kúpiť darček alebo odovzdať prihlášku, veďte ako úlohu s termínom a zodpovednou osobou.")),
        "card": "Krúžky, škola, návštevy a vyzdvihovanie v spoločnom kalendári.", "cta_title": "Nech sa na plán nemusí nikto znovu pýtať.", "cta_text": "Pridajte do Rodinky prvú udalosť a dohodnite rovno aj to, kto ju zabezpečí.",
    },
    "shopping": {
        "title": "Zdieľaný nákupný zoznam pre celú rodinu | Rodinka", "description": "Spoločný nákupný zoznam, ktorý môže rodina priebežne dopĺňať a v obchode odškrtávať. Bez papierikov a položiek stratených v chate.",
        "og_title": "Spoločný nákupný zoznam, ktorý máte vždy poruke", "og_description": "Pridávajte, čo doma dochádza, a nakupujte z rovnakého aktuálneho zoznamu.", "og_alt": "Zdieľaný rodinný nákupný zoznam v aplikácii Rodinka",
        "eyebrow": "NÁKUPY BEZ ZABUDNUTÝCH SPRÁV", "h1": "Zdieľaný nákupný zoznam, do ktorého môže pridať každý", "lead": "Mlieko sa minulo ráno, pečivo niekto napísal do chatu a zoznam na chladničke zostal doma. Spoločný nákupný zoznam zachytí položku vtedy, keď si na ňu niekto spomenie — a v obchode zostáva aktuálny.",
        "problem_title": "Najväčším problémom nákupu býva zber informácií", "problem": ("Samotné nakupovanie je jednoduché. Ťažšie je zistiť, čo naozaj chýba, či to už niekto pridal a kto sa dnes dostane do obchodu. Papierik funguje iba doma a správa v chate rýchlo zapadne.", "Keď má domácnosť jeden zoznam, nezáleží na tom, kto napokon nakúpi. Položky môže pridávať každý, hotové veci sa odškrtnú a zvyšok zostane na neskôr."),
        "scenarios": (("Niečo sa práve minulo", "Posledné mlieko alebo prací gél sa zapíšu hneď, nie až pri spomínaní pred obchodom."), ("Nakupuje niekto iný", "Partner cestou z práce otvorí rovnaký zoznam a nemusí žiadať ďalšiu správu."), ("Plánujete jedlá", "Suroviny k vybraným večeriam sa pridajú k bežným veciam pre domácnosť.")),
        "help_title": "Ako mať spoločný nákupný zoznam v Rodinke", "help_intro": "Zoznam je súčasťou rodinného priestoru, preto ho pozvaní členovia domácnosti vidia v mobile aj počítači.",
        "steps": (("Pridávajte priebežne", "Položku zapíšte vo chvíli, keď doma dochádza. Krátky aktuálny zoznam je užitočnejší než veľké spomínanie raz za týždeň."), ("Nakupujte z rovnakej verzie", "V obchode položky odškrtávajte. Ostatní vidia, čo je hotové, a nepridajú tú istú vec druhýkrát."), ("Prepojte nákup s jedlom", "Pri plánovaní večerí doplňte potrebné suroviny, aby týždenný plán nezostal iba želaním.")),
        "answers_title": "Praktické otázky k spoločnému nákupu", "answers": (("Ako zdieľať nákupný zoznam s partnerom?", "Používajte jeden zoznam v spoločnom rodinnom priestore. Obaja doň môžete pridávať aj odškrtávať, takže netreba posielať novú verziu."), ("Je lepší zoznam v aplikácii alebo na papieri?", "Papier je rýchly pri chladničke. Zdieľaný zoznam je však dostupný mimo domu a aktualizuje ho viac ľudí, čo pomáha, keď sa v nákupoch striedate."), ("Ako nezabudnúť suroviny na celý týždeň?", "Najprv rámcovo naplánujte hlavné jedlá a potom prejdite potrebné suroviny. Pridajte iba to, čo doma naozaj nie je.")),
        "card": "Jeden aktuálny zoznam doma aj v obchode, ktorý dopĺňa celá rodina.", "cta_title": "Ďalší nákup nemusí začať hľadaním správ.", "cta_text": "Otvorte v Rodinke spoločný zoznam a pridajte prvú vec, ktorá doma práve dochádza.",
    },
    "chores": {
        "title": "Úlohy pre rodinu a domáce povinnosti | Rodinka", "description": "Rozdeľte domáce úlohy medzi členov rodiny, pridajte termín a majte jasno, kto čo zariadi. Prakticky pre rodičov aj deti.",
        "og_title": "Domáce povinnosti bez nekonečného pripomínania", "og_description": "Konkrétne rodinné úlohy, jasná zodpovednosť a prehľad o tom, čo je hotové.", "og_alt": "Úlohy pre rodinu a rozdelené domáce povinnosti v Rodinke",
        "eyebrow": "KTO ČO DOMA ZARIADI", "h1": "Úlohy pre rodinu, ktoré nenosí v hlave iba jeden rodič", "lead": "Objednať dieťa k zubárovi, vrátiť knihy, vyniesť kôš alebo pripraviť veci na výlet. Keď má úloha konkrétneho človeka a termín, domácnosť sa nemusí spoliehať na opakované pripomínanie.",
        "problem_title": "„Musíme to urobiť“ ešte nie je rozdelená úloha", "problem": ("Domáce práce si často všimneme až vtedy, keď nie sú hotové. Ešte menej viditeľné sú organizačné povinnosti: sledovať prihlášku do tábora, kúpiť darček či zavolať opravárovi. Ak ich drží jeden človek, nesie aj väčšinu mentálnej záťaže.", "Rodinné úlohy nemajú merať výkon domácnosti. Ide o jednoduchú dohodu: čo treba urobiť, kto to prevezme a dokedy. Hotovú vec potom netreba kontrolovať v chate."),
        "scenarios": (("Drobné denné povinnosti", "Kôš, riad alebo príprava školskej tašky môžu mať jednoduché a zrozumiteľné zadanie."), ("Neviditeľná organizácia", "Telefonát lekárovi, platba za krúžok alebo nákup darčeka dostanú človeka aj termín."), ("Zapojenie detí", "Primerané úlohy ukazujú deťom, že domácnosť je spoločná vec, nie servis rodičov.")),
        "help_title": "Ako rozdeliť domáce úlohy medzi členov rodiny", "help_intro": "Rodinka pomáha premeniť neurčité povinnosti na malé konkrétne kroky, ktoré vidno v spoločnom prehľade.",
        "steps": (("Pomenujte výsledok", "Namiesto „riešiť školu“ napíšte „odoslať prihlášku na výlet“. Každý vie, čo znamená hotovo."), ("Priraďte človeka a termín", "Úloha nemá zostať spoločná dovtedy, kým ju urobí ten najvšímavejší. Zodpovednosť si dohodnite rovno."), ("Nechajte hotové veci odísť z hlavy", "Splnenie vidia ostatní. Netreba posielať potvrdzujúcu správu ani sa opakovane pýtať.")),
        "answers_title": "Otázky k domácim úlohám a povinnostiam", "answers": (("Ako rozdeliť domáce práce spravodlivo?", "Nezačínajte iba viditeľným upratovaním. Spíšte aj plánovanie, telefonáty a sledovanie termínov. Rozdelenie potom posudzujte podľa času a záťaže."), ("Ako zadávať úlohy deťom?", "Úloha má zodpovedať veku, byť konkrétna a mať dosiahnuteľný termín. Cieľom je návyk a zapojenie, nie dokonalosť."), ("Ako pripomínať úlohy bez hádok?", "Dohodnite zodpovednosť a zapíšte ju na spoločné miesto. Obaja rodičia sa tak môžu oprieť o rovnakú dohodu, nie o pamäť jedného z nich.")),
        "card": "Konkrétne povinnosti, jasný človek a termín pre rodičov aj deti.", "cta_title": "Rozdeľte prvú úlohu skôr, než sa stratí v hlave.", "cta_text": "Pridajte do Rodinky jednu konkrétnu povinnosť a dohodnite sa, kto ju prevezme.",
    },
    "meals": {
        "title": "Plánovanie jedál na týždeň pre rodinu | Rodinka", "description": "Naplánujte rodinné jedlá na celý týždeň, obmedzte každodenné rozhodovanie a pridajte suroviny do spoločného nákupného zoznamu.",
        "og_title": "Týždenný plán jedál bez každodennej otázky „čo variť?“", "og_description": "Praktický plán jedál pre rodinu, ktorý nadväzuje na spoločný nákupný zoznam.", "og_alt": "Týždenné plánovanie rodinných jedál v aplikácii Rodinka",
        "eyebrow": "MENEJ ROZHODOVANIA OKOLO VEČERE", "h1": "Plánovanie jedál na týždeň, ktoré počíta so skutočným životom", "lead": "Niektoré dni je čas variť, inokedy sa rodina vracia neskoro z krúžkov. Týždenný plán jedál nemusí byť dokonalý jedálny lístok — stačí, keď vopred vyrieši pár večerov a uľahčí nákup.",
        "problem_title": "Najťažšie často nie je varenie, ale rozhodovanie", "problem": ("Otázka „čo bude na večeru?“ prichádza zvyčajne vtedy, keď je hlad a málo času. Bez rámcového plánu sa častejšie nakupuje narýchlo, niektoré suroviny chýbajú a iné sa nestihnú využiť.", "Rodinný plán má rešpektovať rytmus týždňa. Po náročnom popoludní môže počítať s rýchlym jedlom, vo voľnejší deň s dlhším varením. Zmena plánu nie je zlyhanie, iba aktualizácia spoločného prehľadu."),
        "scenarios": (("Deň plný krúžkov", "Na večer sa naplánuje rýchle jedlo, ktoré po návrate domov nevyžaduje dlhú prípravu."), ("Spoločné víkendové varenie", "Rodina vopred vidí, kedy je priestor na obľúbené jedlo alebo varenie s deťmi."), ("Nákup bez hádania", "Z plánovaných jedál vzniknú konkrétne suroviny v spoločnom nákupnom zozname.")),
        "help_title": "Ako plánovať jedlo na celý týždeň v Rodinke", "help_intro": "Nejde o podrobný diétny program. Rodinka spája jednoduchú predstavu o jedlách s tým, čo treba nakúpiť.",
        "steps": (("Pozrite si rodinný kalendár", "Najskôr zvážte, ktoré dni sú dlhé a kedy bude niekto doma skôr. Plán potom vychádza zo skutočného času."), ("Vyberte niekoľko istých jedál", "Nemusíte vyplniť každý chod. Začnite večerami, ktoré bežne varíte, a nechajte priestor na zvyšky či zmenu."), ("Doplňte suroviny do nákupu", "Skontrolujte, čo už doma máte, a chýbajúce veci pridajte do zdieľaného zoznamu.")),
        "answers_title": "Časté otázky k plánovaniu rodinného jedla", "answers": (("Ako plánovať jedlo na celý týždeň?", "Začnite rodinným programom a hlavné jedlá vyberte podľa času na prípravu. Jeden voľný večer pomôže využiť zvyšky alebo reagovať na zmenu."), ("Ako zapojiť rodinu do výberu jedál?", "Nech každý navrhne jedno obľúbené jedlo a spoločne rozhodnite, do ktorého dňa sa hodí. Plán potom nie je iba prácou jedného človeka."), ("Ako prepojiť jedálny lístok s nákupným zoznamom?", "Pri každom plánovanom jedle prejdite hlavné suroviny a chýbajúce pridajte do spoločného zoznamu. Pred nákupom ešte skontrolujte zásoby.")),
        "card": "Jednoduchý plán večerí podľa rodinného týždňa a potrebných nákupov.", "cta_title": "Naplánujte pár večerí a uľahčite zvyšok týždňa.", "cta_text": "Otvorte Rodinku, vyberte prvé jedlo a doplňte, čo k nemu treba kúpiť.",
    },
    "app": {
        "title": "Aplikácia pre rodinu: kalendár, úlohy a nákupy | Rodinka", "description": "Rodinka je aplikácia pre rodinu, ktorá spája kalendár, domáce úlohy, nákupný zoznam a plán jedál v jednom spoločnom prehľade.",
        "og_title": "Jedna aplikácia na každodennú organizáciu rodiny", "og_description": "Namiesto roztrúsených správ, poznámok a kalendárov má rodina spoločný priestor pre to, čo práve rieši.", "og_alt": "Aplikácia Rodinka na spoločnú organizáciu rodinného života",
        "eyebrow": "APLIKÁCIA PRE KAŽDODENNÝ CHOD RODINY", "h1": "Aplikácia pre rodinu, ktorá spája plán aj domáce povinnosti", "lead": "Kalendár ukazuje termíny, no nie vždy nákup. Chat obsahuje dohodu, ale o týždeň sa v ňom ťažko hľadá. Rodinka spája praktické časti rodinného života, aby každý vedel, kam sa pozrieť.",
        "problem_title": "Rodina nepotrebuje viac miest, ale menej hľadania", "problem": ("Každý nástroj môže fungovať dobre, no celok sa aj tak rozpadá. Termín je v osobnom kalendári, zoznam na papieri, úloha v hlave a zmena v skupinovom chate. Informácie existujú, iba nie sú dostupné všetkým v správnej chvíli.", "Dobrá aplikácia pre rodinu nemá potrebovať správcu na plný úväzok. Bežná vec sa zapíše rýchlo, spoločný prehľad je zrozumiteľný a jednotlivé časti zodpovedajú situáciám zo skutočnej domácnosti."),
        "scenarios": (("Pred odchodom z domu", "Jeden pohľad ukáže dnešný program, odvoz aj povinnosti, ktoré nesmú zostať doma."), ("Počas dňa", "Ktokoľvek pridá chýbajúci nákup alebo označí hotovú úlohu bez správy pre všetkých."), ("Pri plánovaní týždňa", "Kalendár, jedlá a domáce úlohy spolu vytvoria reálny obraz toho, čo rodinu čaká.")),
        "help_title": "Čo nájdete v aplikácii Rodinka", "help_intro": "Jednotlivé časti používate podľa potreby. Najväčší úžitok majú vo chvíli, keď na seba prirodzene nadväzujú.",
        "steps": (("Rodinný kalendár", "Spoločné termíny, opakované aktivity a informácie o tom, kto zabezpečuje odvoz."), ("Úlohy a domácnosť", "Povinnosti s konkrétnym človekom a termínom, aby organizácia neležala iba na jednom rodičovi."), ("Nákupy a plán jedál", "Zoznam toho, čo chýba, a jednoduchý výhľad na rodinné večere v jednom priestore.")),
        "answers_title": "Ako vyberať aplikáciu pre rodinu", "answers": (("Čo by mala vedieť aplikácia pre rodinu?", "Mala by pokrývať najčastejšie spoločné situácie, fungovať rýchlo v mobile aj počítači a dovoliť viacerým členom pracovať s rovnakými aktuálnymi informáciami."), ("Nahradí Rodinka rodinný chat?", "Nie. Chat je výborný na rozhovor. Rodinka je prehľad termínov, úloh a zoznamov, ktoré chcete nájsť aj neskôr bez prechádzania histórie správ."), ("Musí rodina používať všetky funkcie?", "Nemusí. Začnite oblasťou, ktorá dnes spôsobuje najviac otázok. Ďalšie časti pridajte až vtedy, keď domácnosti naozaj pomôžu.")),
        "card": "Kalendár, povinnosti, nákupný zoznam a jedlá v jednom rodinnom priestore.", "cta_title": "Dajte rodinným informáciám jedno známe miesto.", "cta_text": "Rodinka funguje priamo v prehliadači. Vytvorte rodinu a začnite prvou praktickou vecou.",
    },
}


TOPICS["en"] = {
    "planner": {
        "title": "A practical family planner for everyday life | Rodinka", "description": "Bring your family calendar, chores, shopping and meals into one shared planner. Organize home life without creating another job to manage.",
        "og_title": "A family planner that does not become another household project", "og_description": "One practical place for schedules, responsibilities, shopping and meals, shared by the people who run the household.", "og_alt": "Rodinka family planner showing a shared overview of everyday home life",
        "eyebrow": "ONE SHARED FAMILY OVERVIEW", "h1": "A family planner for everything home life asks you to remember", "lead": "Activities, pick-ups, groceries, dinners and chores easily scatter across calendars, chat threads and notes on the fridge. A shared family planner gives everyone one reliable place to look.",
        "problem_title": "Organizing family life should not be one person’s invisible job", "problem": ("In many households, one parent carries the schedule and the mental list of what needs doing. Everyone else asks for updates, and the answer gets searched for in messages again. The problem is rarely effort; the information simply has no shared home.", "A useful planner should reduce admin, not create it. In a few seconds it should answer who is picking up today, when practice starts, what the house needs and which dinners are planned for the week."),
        "scenarios": (("Mornings without detective work", "Before anyone leaves, the day’s events, pick-ups and important chores are clear."), ("Changes stay visible", "A moved practice or newly added grocery item appears in the shared overview."), ("A lighter mental load", "One person no longer has to monitor the entire plan; information and responsibility are genuinely shared.")),
        "help_title": "How Rodinka helps organize family life", "help_intro": "Start with one area and add the others only when they become useful. Everything remains connected inside the same family space.",
        "steps": (("Share the same schedule", "The family calendar brings joint and individual events together and shows who is handling each practical detail."), ("Turn loose intentions into clear chores", "Give a task an owner and a due date so “we should do this” becomes an understandable agreement."), ("Keep the household basics close", "A shopping list and meal plan sit alongside the schedule for the things your family handles every week.")),
        "answers_title": "Common questions about family planners", "answers": (("What should a good family planner include?", "It should quickly show the shared calendar, assigned chores and practical lists. It also needs to be simple enough for both parents, and for children when that suits their age."), ("How do we start if nobody wants another app?", "Choose one repeated source of friction, such as activities or groceries. Once the shared view saves a few messages, add another area. You do not need to move everything on day one."), ("How can a family rely less on group chat?", "Keep the conversation in chat, but put dates, tasks and shopping items somewhere designed for later reference. Important details will no longer disappear between unrelated messages.")),
        "card": "One shared overview for schedules, chores, shopping and meals.", "cta_title": "Start with the thing your household discusses most.", "cta_text": "Create your Rodinka and add the first event, chore or shopping item. Everything else can follow gradually.",
    },
    "calendar": {
        "title": "Shared family calendar for parents and children | Rodinka", "description": "A shared family calendar for school, activities, appointments and pick-ups. Everyone can see what is happening and who is handling it.",
        "og_title": "A family calendar that answers “who is picking up?”", "og_description": "Keep school, activities, appointments, visits and transport in one calendar for the whole household.", "og_alt": "Rodinka shared family calendar with events and pick-up details",
        "eyebrow": "A SCHEDULE FOR THE WHOLE HOUSEHOLD", "h1": "A shared family calendar that includes the practical details", "lead": "When is the school concert, who is driving to swimming and is Saturday’s visit confirmed? A family calendar keeps the dates and the hand-offs together, so everyone can check for themselves.",
        "problem_title": "A date and time are often only half the plan", "problem": ("Family schedules are not just a list of appointments. Children’s activities also need a place, the right child and a clear adult handling transport. If half of that information remains in chat, the calendar cannot do its full job.", "The shared view needs to work for a quick morning check and for planning the week ahead. Recurring activities are added once, exceptions are visible to everyone and nobody maintains a separate version of the family schedule."),
        "scenarios": (("Children’s activities", "Swimming, music lessons and practice include the time, place, child and agreed transport."), ("School and appointments", "Parent meetings, check-ups and days off no longer sit only in one parent’s inbox."), ("Weekends and visits", "Birthdays and time with grandparents are visible before another plan is made.")),
        "help_title": "How a shared family calendar works in Rodinka", "help_intro": "Events live in the same family space, so every invited adult sees the current schedule instead of waiting for a screenshot or forwarded message.",
        "steps": (("Add the full event", "Record the time, place and family member involved. Set regular activities to repeat so they do not need weekly re-entry."), ("Make the hand-off clear", "Show who is driving or picking up beside the event. The practical agreement will not be stranded in another conversation."), ("Review one family week", "When either parent makes plans, both can see the same school events, appointments and family commitments.")),
        "answers_title": "Questions families ask about shared calendars", "answers": (("How do parents share a family calendar?", "Create one family space and invite the other adult. Put shared events there, and include the transport or pick-up detail whenever it affects the plan."), ("How can we organize children’s activities?", "For every activity, record the day, time, place, child and transport. Repeat regular sessions and edit exceptions individually so the weekly view stays accurate."), ("Should chores go in the family calendar?", "Use an event for something that happens at a time. Preparation, such as buying a gift or returning a form, works better as a separate chore with an owner and due date.")),
        "card": "School, activities, visits and pick-ups in one shared calendar.", "cta_title": "Make the plan available without another message.", "cta_text": "Add your first family event in Rodinka and include who is handling the practical side.",
    },
    "shopping": {
        "title": "Shared family shopping list that stays up to date | Rodinka", "description": "A shared shopping list everyone can add to and check off in the store. Keep groceries out of scattered messages and forgotten paper notes.",
        "og_title": "One household shopping list, always close at hand", "og_description": "Add what is running out at home and shop from the same current list.", "og_alt": "Rodinka shared family shopping list for groceries and household items",
        "eyebrow": "SHOPPING WITHOUT THE LOST MESSAGES", "h1": "A shared shopping list the whole family can update", "lead": "The milk ran out this morning, someone mentioned bread in chat and the note on the fridge stayed at home. A shared list catches an item when anyone remembers it — and it is still current in the store.",
        "problem_title": "Collecting the list is often harder than the shopping", "problem": ("Buying groceries is straightforward. Working out what is actually missing, whether someone has already added it and who is going to the store is the messy part. Paper only works where it is left, while a chat message quickly disappears.", "With one household list, it matters less who ends up shopping. Everyone can add items, completed ones are checked off and anything left stays available for later."),
        "scenarios": (("Something just ran out", "The last milk or laundry detergent goes on the list immediately, not during a rushed memory test later."), ("Someone else is shopping", "A partner stopping on the way home opens the same list without asking for an updated message."), ("Meals are planned", "Ingredients for chosen dinners join the regular household items in one place.")),
        "help_title": "How to keep a shared shopping list in Rodinka", "help_intro": "The list belongs to your family space, so invited household members can open and update it on a phone or computer.",
        "steps": (("Add items as they run low", "Capture an item when you notice it. A short current list is more reliable than rebuilding everything once a week."), ("Shop from the same version", "Check things off in the store. Everyone else can see what is done and avoid adding or buying it twice."), ("Connect shopping with meals", "When you choose dinners for the week, add the ingredients you need so the meal plan is practical.")),
        "answers_title": "Practical questions about shared grocery lists", "answers": (("How do I share a grocery list with my partner?", "Use one list inside a shared family space. Both of you can add and check off items, so there is no need to send a fresh version before every trip."), ("Is an app better than a paper shopping list?", "Paper is quick beside the fridge. A shared digital list is also available away from home and can be updated by several people, which helps when different family members shop."), ("How do we remember a full week of ingredients?", "Sketch out the main meals first, then review their ingredients. Add only what is not already at home so the final list remains useful in the store.")),
        "card": "One current list at home and in the store, updated by the whole family.", "cta_title": "Your next shop can start without searching through chat.", "cta_text": "Open the shared list in Rodinka and add the first thing your household is running low on.",
    },
    "chores": {
        "title": "Family chores and household responsibilities | Rodinka", "description": "Assign family chores, add a due date and make it clear who is handling what. A practical shared view for parents and children.",
        "og_title": "Household chores without endless reminders", "og_description": "Clear family tasks, visible responsibility and a shared view of what is done.", "og_alt": "Family chores and household responsibilities assigned in Rodinka",
        "eyebrow": "WHO IS HANDLING WHAT AT HOME", "h1": "Family chores that do not live in one parent’s head", "lead": "Book the dentist, return library books, take out the recycling or pack for a trip. When a task has a person and a due date, the household does not have to run on repeated reminders.",
        "problem_title": "“We need to do that” is not an assigned chore", "problem": ("Housework often becomes visible only when it is not done. Planning work is even easier to miss: watching a camp deadline, buying a birthday gift or calling a repair service. If one person holds those details, they also carry most of the mental load.", "A family task list is not a household performance score. It is a simple agreement about what needs doing, who has taken it and when it matters. Once complete, the task no longer needs another check-in message."),
        "scenarios": (("Small daily responsibilities", "Recycling, dishes or packing a school bag can each have a short, clear definition of done."), ("Invisible organizing work", "A doctor’s call, activity payment or gift purchase gets an owner and a due date."), ("Children taking part", "Age-appropriate chores show children that a home is shared work rather than a service run by parents.")),
        "help_title": "How to divide household chores across the family", "help_intro": "Rodinka turns loose household intentions into small, specific actions that everyone can see in the shared overview.",
        "steps": (("Name the outcome", "Replace “sort out school” with “send the trip form”. A concrete task makes it obvious what completion means."), ("Choose a person and a date", "Do not leave every task shared until the most attentive person does it. Agree on ownership while the need is clear."), ("Let completed work leave your head", "Everyone can see that the chore is done. No confirmation message or repeated question is needed.")),
        "answers_title": "Questions about family chores and responsibilities", "answers": (("How can we divide household work fairly?", "Include planning, calls and deadline tracking as well as visible cleaning. Then consider time and mental effort, not only the number of items each person has."), ("How should we give chores to children?", "Choose something age-appropriate, specific and achievable by a clear time. The aim is participation and a habit of helping, not a perfect result."), ("How can we remind each other without arguing?", "Agree on the owner and put the task in a shared place. A reminder then refers to the same visible agreement instead of one person managing the other.")),
        "card": "Specific responsibilities, a clear owner and a due date for adults and children.", "cta_title": "Assign one task before it disappears into someone’s mental list.", "cta_text": "Add a concrete household responsibility in Rodinka and agree on who will take it.",
    },
    "meals": {
        "title": "Simple weekly meal planning for families | Rodinka", "description": "Plan family meals for the week, reduce daily decisions and add missing ingredients to the same shared shopping list.",
        "og_title": "A weekly family meal plan for fewer “what’s for dinner?” moments", "og_description": "A practical meal plan shaped around the family calendar and connected to your shopping list.", "og_alt": "Weekly family meal planning in the Rodinka organizer app",
        "eyebrow": "FEWER LAST-MINUTE DINNER DECISIONS", "h1": "Weekly meal planning built around real family life", "lead": "Some days leave room to cook; others end late after children’s activities. A weekly meal plan does not need to be perfect — it only needs to settle a few evenings ahead of time and make the next shop easier.",
        "problem_title": "The hardest part is often deciding, not cooking", "problem": ("“What’s for dinner?” tends to arrive when everyone is hungry and short on time. Without a loose plan, the family shops in a rush, useful ingredients are missing and other food goes unused.", "A family meal plan should follow the shape of the week. Busy afternoons call for something quick; a slower day can hold a longer recipe. When plans change, updating the overview is enough — it is not a failed system."),
        "scenarios": (("An activity-packed day", "A quick dinner is planned for the evening when everyone gets home late."), ("Cooking together at the weekend", "The family can see where there is space for a favorite meal or cooking with children."), ("A shopping list with a reason", "Planned dinners become the specific ingredients needed alongside regular household shopping.")),
        "help_title": "How to plan a week of meals in Rodinka", "help_intro": "This is not a detailed diet program. Rodinka connects a simple dinner plan with the groceries required to make it happen.",
        "steps": (("Check the family calendar", "Notice which days are long and when someone will be home earlier. Build the meal plan around the time you actually have."), ("Choose a few reliable meals", "You do not need to fill every slot. Start with familiar dinners and leave room for leftovers or a change of plans."), ("Add missing ingredients", "Check what is already at home, then put everything else on the shared shopping list.")),
        "answers_title": "Common questions about family meal planning", "answers": (("How do I plan meals for the whole week?", "Start with the family schedule and choose main meals by the time available to prepare them. Leave one evening open for leftovers or an unexpected change."), ("How can the whole family help choose meals?", "Ask each person for one favorite and decide together where it fits. The plan becomes less work for one person and more likely to suit the household."), ("How do I connect a meal plan to a grocery list?", "Review the main ingredients for each planned meal and add what is missing to the shared list. Check the cupboards once more before shopping to avoid duplicates.")),
        "card": "A simple dinner plan shaped around the week and the groceries it needs.", "cta_title": "Plan a few dinners and make the rest of the week lighter.", "cta_text": "Open Rodinka, choose the first meal and add anything the family needs to buy.",
    },
    "app": {
        "title": "Family organizer app for calendars, chores and lists | Rodinka", "description": "Rodinka is a family organizer app combining a shared calendar, household chores, shopping lists and meal planning in one practical place.",
        "og_title": "One family organizer for the details of everyday home life", "og_description": "Give schedules, chores, groceries and meals a shared home instead of scattering them across chats and notes.", "og_alt": "Rodinka family organizer app for shared schedules and household tasks",
        "eyebrow": "AN APP FOR THE EVERYDAY WORK OF FAMILY LIFE", "h1": "A family organizer app for schedules, chores, shopping and meals", "lead": "A calendar holds dates but not always groceries. Chat holds conversations but makes last week’s detail hard to find. Rodinka brings the practical parts of family life together so everyone knows where to look.",
        "problem_title": "Families need fewer places to search, not more", "problem": ("Every tool may work on its own while the complete picture still falls apart. An event sits in a personal calendar, a list is on paper, a chore stays in someone’s head and the latest change is in group chat. The information exists, but not for everyone at the right moment.", "A good family organizer should not need its own full-time administrator. Everyday updates must be quick, the shared overview must be easy to read and each part should match a real household situation."),
        "scenarios": (("Before leaving home", "One view shows today’s schedule, pick-ups and the responsibilities that cannot be forgotten."), ("During the day", "Anyone can add a missing grocery item or complete a chore without messaging the entire family."), ("Planning the week", "The calendar, meals and household tasks create a realistic picture of what the family is taking on.")),
        "help_title": "What the Rodinka family organizer includes", "help_intro": "Use each part when it is helpful. Their value grows when one naturally supports the next.",
        "steps": (("A shared family calendar", "Joint events, recurring activities and practical details about who is handling transport or pick-up."), ("Chores and household tasks", "Responsibilities with a clear person and date so the organizing does not remain with one parent."), ("Shopping and meal planning", "A current list of what the household needs and a simple view of the family’s planned dinners.")),
        "answers_title": "How to choose a family organizer app", "answers": (("What should a family organizer app do?", "It should cover the shared situations your household handles most, work well on phones and computers, and let several people use the same current information."), ("Does Rodinka replace family group chat?", "No. Chat is excellent for conversation. Rodinka is the reference point for schedules, chores and lists you want to find later without scrolling through message history."), ("Do we need to use every feature?", "Not at all. Start with the area causing the most repeated questions today. Add another part only when it solves a real need for your household.")),
        "card": "A calendar, household responsibilities, shopping and meals in one family space.", "cta_title": "Give family information one familiar home.", "cta_text": "Rodinka works in the browser. Create your family and start with the first practical thing you need to share.",
    },
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def canonical(path: str) -> str:
    return f"{SITE_URL}{path}"


def og_image_url(locale: str) -> str:
    return canonical(OG_IMAGES[locale])


def output_path(path: str) -> Path:
    if path == "/":
        return ROOT / "index.html"
    return ROOT / path.strip("/") / "index.html"


def alternates(page_key: str) -> str:
    lines = []
    for locale in ("cs", "sk", "en"):
        lines.append(f'    <link rel="alternate" hreflang="{locale}" href="{canonical(PATHS[page_key][locale])}" />')
    lines.append(f'    <link rel="alternate" hreflang="x-default" href="{canonical(PATHS[page_key]["cs"])}" />')
    return "\n".join(lines)


def schema(page_key: str, locale: str, name: str, description: str) -> str:
    path = PATHS[page_key][locale]
    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}/#website",
                "url": f"{SITE_URL}/",
                "name": "Rodinka",
                "description": LOCALES[locale]["site_description"],
                "inLanguage": ["cs", "sk", "en"],
            },
            {
                "@type": "WebApplication",
                "@id": f"{SITE_URL}/#webapp",
                "name": "Rodinka",
                "url": APP_URL,
                "description": LOCALES[locale]["site_description"],
                "applicationCategory": "LifestyleApplication",
                "operatingSystem": "Web",
                "isPartOf": {"@id": f"{SITE_URL}/#website"},
            },
            {
                "@type": "WebPage",
                "@id": f"{canonical(path)}#webpage",
                "url": canonical(path),
                "name": name,
                "description": description,
                "inLanguage": LOCALES[locale]["lang"],
                "isPartOf": {"@id": f"{SITE_URL}/#website"},
                "about": {"@id": f"{SITE_URL}/#webapp"},
                "primaryImageOfPage": {"@id": f"{og_image_url(locale)}#image"},
            },
            {
                "@type": "ImageObject",
                "@id": f"{og_image_url(locale)}#image",
                "url": og_image_url(locale),
                "contentUrl": og_image_url(locale),
                "width": OG_IMAGE_WIDTH,
                "height": OG_IMAGE_HEIGHT,
            },
        ],
    }
    return json.dumps(graph, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def head(page_key: str, locale: str, data: dict) -> str:
    cfg = LOCALES[locale]
    path = PATHS[page_key][locale]
    other_locales = "\n".join(
        f'    <meta property="og:locale:alternate" content="{LOCALES[other]["og_locale"]}" />'
        for other in ("cs", "sk", "en") if other != locale
    )
    return f'''  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{esc(data["title"])}</title>
    <meta name="description" content="{esc(data["description"])}" />
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
    <meta name="theme-color" content="#f7f2e8" />
    <meta name="application-name" content="Rodinka" />
    <link rel="canonical" href="{canonical(path)}" />
{alternates(page_key)}
    <meta property="og:title" content="{esc(data["og_title"])}" />
    <meta property="og:description" content="{esc(data["og_description"])}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{canonical(path)}" />
    <meta property="og:site_name" content="Rodinka" />
    <meta property="og:locale" content="{cfg["og_locale"]}" />
{other_locales}
    <meta property="og:image" content="{og_image_url(locale)}" />
    <meta property="og:image:width" content="{OG_IMAGE_WIDTH}" />
    <meta property="og:image:height" content="{OG_IMAGE_HEIGHT}" />
    <meta property="og:image:alt" content="{esc(data["og_alt"])}" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{esc(data["og_title"])}" />
    <meta name="twitter:description" content="{esc(data["og_description"])}" />
    <meta name="twitter:image" content="{og_image_url(locale)}" />
    <meta name="twitter:image:alt" content="{esc(data["og_alt"])}" />
    <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
    <link rel="icon" href="/favicon-96.png" type="image/png" sizes="96x96" />
    <link rel="apple-touch-icon" href="/apple-touch-icon.png" sizes="180x180" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&amp;family=Manrope:wght@600;700;800&amp;display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="/styles.css?v={ASSET_VERSION}" />
    <script>document.documentElement.classList.add('js');</script>
    <script type="application/ld+json">{schema(page_key, locale, data["title"], data["description"])}</script>
  </head>'''


def language_switcher(page_key: str, locale: str) -> str:
    labels = {"cs": "CZ", "sk": "SK", "en": "EN"}
    names = {"cs": "Čeština", "sk": "Slovenčina", "en": "English"}
    links = []
    for code in ("cs", "sk", "en"):
        current = ' aria-current="page"' if code == locale else ""
        links.append(f'<a href="{PATHS[page_key][code]}" lang="{code}" hreflang="{code}" aria-label="{names[code]}"{current}>{labels[code]}</a>')
    return f'<div class="language-switcher" aria-label="{esc(LOCALES[locale]["language_label"])}">' + '<span aria-hidden="true">·</span>'.join(links) + "</div>"


def site_header(page_key: str, locale: str) -> str:
    cfg = LOCALES[locale]
    nav_keys = ("planner", "calendar", "chores", "shopping", "meals")
    links = "".join(f'<a href="{PATHS[key][locale]}">{esc(cfg["nav"][key])}</a>' for key in nav_keys)
    return f'''    <header class="site-header">
      <a class="brand" href="{cfg["home_path"]}" aria-label="Rodinka, {esc(cfg["home"])}">
        <span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i></span><span>Rodinka</span>
      </a>
      <button class="menu-button" type="button" aria-label="Menu" aria-expanded="false" aria-controls="main-navigation"><span></span><span></span></button>
      <nav class="nav" id="main-navigation" aria-label="{esc(cfg["primary_nav"])}">
        {links}
        <a class="nav-cta" href="{APP_URL}">{esc(cfg["open_app"])} <span aria-hidden="true">→</span></a>
        {language_switcher(page_key, locale)}
      </nav>
    </header>'''


def site_footer(locale: str) -> str:
    cfg = LOCALES[locale]
    feature_links = "".join(f'<li><a href="{PATHS[key][locale]}">{esc(cfg["nav"].get(key, TOPICS[locale][key]["h1"]))}</a></li>' for key in ("planner", "calendar", "chores", "shopping", "meals"))
    return f'''    <footer class="site-footer">
      <div class="footer-brand"><a class="brand" href="{cfg["home_path"]}"><span class="brand-mark" aria-hidden="true"><i></i><i></i><i></i></span><span>Rodinka</span></a><p>{esc(cfg["footer_text"])}</p></div>
      <nav class="footer-nav" aria-label="{esc(cfg["features"])}"><h2>{esc(cfg["features"])}</h2><ul>{feature_links}</ul></nav>
      <nav class="footer-nav" aria-label="{esc(cfg["about"])}"><h2>{esc(cfg["about"])}</h2><ul><li><a href="{PATHS["app"][locale]}">{esc(cfg["app_label"])}</a></li><li><a href="{APP_URL}">{esc(cfg["open_app"])}</a></li></ul></nav>
      <p class="copyright">{esc(cfg["copyright"])}</p>
    </footer>'''


def render_home(locale: str) -> str:
    data = HOME[locale]
    cfg = LOCALES[locale]
    steps = "".join(f'<article class="step reveal"><span class="step-number">0{i}</span><div class="step-icon" aria-hidden="true">{("⌂", "+", "♥")[i-1]}</div><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for i, (title, text) in enumerate(data["steps"], 1))
    feature_classes = {"calendar": "coral-card", "shopping": "yellow-card", "chores": "mint-card", "meals": "blue-card"}
    feature_cards = ""
    for key in ("calendar", "shopping", "chores", "meals"):
        label, title, text_value = data["feature_copy"][key]
        feature_cards += f'<article class="feature-card {feature_classes[key]} reveal"><span class="pill">{esc(label)}</span><h3>{esc(title)}</h3><p>{esc(text_value)}</p><a class="card-link" href="{PATHS[key][locale]}">{esc(cfg["learn_more"])} <span aria-hidden="true">→</span></a></article>'
    directory_cards = "".join(f'<article class="topic-card reveal"><h3><a href="{PATHS[key][locale]}">{esc(TOPICS[locale][key]["h1"])}</a></h3><p>{esc(TOPICS[locale][key]["card"])}</p><a class="card-link" href="{PATHS[key][locale]}">{esc(cfg["learn_more"])} <span aria-hidden="true">→</span></a></article>' for key in ("planner", "calendar", "shopping", "chores", "meals", "app"))
    agenda = "".join(f'<div class="agenda-row"><span class="agenda-time">{esc(time)}</span><i class="dot {("coral", "blue", "yellow")[i]}"></i><div><strong>{esc(title)}</strong><small>{esc(note)}</small></div></div>' for i, (time, title, note) in enumerate(data["agenda"]))
    journey = "".join(f'<div><b>{esc(title)}</b><small>{esc(text)}</small></div>' for title, text in data["journey"])
    proof = "".join(f'<span>{esc(item)}</span>' for item in data["proof"])
    return f'''<!doctype html>
<html lang="{locale}">
{head("home", locale, data)}
  <body>
{site_header("home", locale)}
    <main id="top">
      <section class="hero">
        <div class="hero-copy reveal">
          <p class="eyebrow"><span aria-hidden="true">●</span> {esc(data["eyebrow"])}</p>
          <h1>{esc(data["h1"])}</h1>
          <p class="brand-line">{esc(data["brand_line"])}</p>
          <p class="hero-lead">{esc(data["lead"])}</p>
          <div class="hero-actions"><a class="button button-primary" href="{APP_URL}">{esc(cfg["start"])} <span aria-hidden="true">→</span></a><a class="text-link" href="#jak-to-funguje">{esc(data["how_link"])} <span aria-hidden="true">↓</span></a></div>
          <div class="hero-proof">{proof}</div>
          <div class="trust-row"><span class="trust-icon" aria-hidden="true">♥</span><p><strong>{esc(data["trust_title"])}</strong><br />{esc(data["trust_text"])}</p></div>
        </div>
        <div class="hero-visual reveal" aria-hidden="true">
          <div class="sun-shape"></div><div class="scribble scribble-one">✦</div><div class="scribble scribble-two">⌁</div>
          <div class="phone-shell"><div class="phone-top"><div class="mini-brand"><span class="mini-mark">●</span> Rodinka</div><div class="member-dots"><span>M</span><span>K</span><span>+2</span></div></div><p class="phone-date">{esc(data["phone_date"])}</p><p class="phone-greeting">{esc(data["phone_greeting"])}</p><div class="today-card"><div class="card-title"><strong>{esc(data["today"])}</strong><span>{esc(data["items"])}</span></div>{agenda}</div><div class="quick-grid"><div><span class="quick-icon mint">✓</span><small>{esc(data["quick"][0][0])}</small><strong>{esc(data["quick"][0][1])}</strong></div><div><span class="quick-icon peach">▤</span><small>{esc(data["quick"][1][0])}</small><strong>{esc(data["quick"][1][1])}</strong></div></div></div>
        </div>
      </section>
      <section class="intro" id="jak-to-funguje"><p class="section-kicker reveal">{esc(data["intro_kicker"])}</p><h2 class="section-title reveal">{esc(data["intro_title"])}</h2><p class="section-lead reveal">{esc(data["intro_lead"])}</p><div class="steps">{steps}</div><aside class="activation-note reveal"><span aria-hidden="true">💡</span><div><h3>{esc(data["note_title"])}</h3><p>{esc(data["note"])}</p></div></aside></section>
      <section class="features" id="funkce"><div class="feature-heading reveal"><p class="section-kicker">{esc(data["features_kicker"])}</p><h2 class="section-title">{esc(data["features_title"])}</h2><p class="feature-sublead">{esc(data["features_lead"])}</p></div><div class="feature-grid">{feature_cards}</div></section>
      <section class="topic-directory"><p class="section-kicker reveal">{esc(data["directory_kicker"])}</p><h2 class="section-title reveal">{esc(data["directory_title"])}</h2><p class="section-lead reveal">{esc(data["directory_lead"])}</p><div class="topic-grid">{directory_cards}</div></section>
      <section class="family-section"><figure class="family-quote reveal"><span class="quote-mark" aria-hidden="true">“</span><blockquote><p>{esc(data["quote"])}</p></blockquote><figcaption>{esc(data["quote_by"])}</figcaption></figure></section>
      <section class="cta-section" id="vyzkouset"><div class="cta-card reveal"><div class="cta-doodle" aria-hidden="true">✦</div><p class="section-kicker">{esc(data["cta_kicker"])}</p><h2>{esc(data["cta_title"])}</h2><p>{esc(data["cta_text"])}</p><div class="cta-actions"><a class="app-cta" href="{APP_URL}">{esc(cfg["start"])} <span aria-hidden="true">→</span></a><a class="cta-secondary" href="{APP_URL}">{esc(data["login"])}</a></div><div class="mini-journey">{journey}</div><div class="install-options"><h3>{esc(data["install_title"])}</h3><p>{esc(data["install_text"])}</p><a class="store-link" href="https://get.microsoft.com/installer/download/9nbxf0lqbmbj?referrer=appbadge">{esc(data["store"])} <span aria-hidden="true">→</span></a></div><small class="form-note">{esc(data["fine_print"])}</small></div></section>
    </main>
{site_footer(locale)}
    <script src="/script.js?v={ASSET_VERSION}" defer></script>
  </body>
</html>
'''


def render_topic(page_key: str, locale: str) -> str:
    data = TOPICS[locale][page_key]
    cfg = LOCALES[locale]
    scenarios = "".join(f'<article class="scenario-card"><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for title, text in data["scenarios"])
    steps = "".join(f'<li><span>{i}</span><div><h3>{esc(title)}</h3><p>{esc(text)}</p></div></li>' for i, (title, text) in enumerate(data["steps"], 1))
    answers = "".join(f'<article class="answer"><h3>{esc(question)}</h3><p>{esc(answer)}</p></article>' for question, answer in data["answers"])
    related = "".join(f'<article class="related-card"><h3><a href="{PATHS[key][locale]}">{esc(TOPICS[locale][key]["h1"])}</a></h3><p>{esc(TOPICS[locale][key]["card"])}</p></article>' for key in RELATED[page_key])
    return f'''<!doctype html>
<html lang="{locale}">
{head(page_key, locale, data)}
  <body>
{site_header(page_key, locale)}
    <main>
      <article class="topic-page">
        <header class="topic-hero"><nav class="breadcrumbs" aria-label="{esc(cfg["breadcrumb"])}"><a href="{cfg["home_path"]}">{esc(cfg["home"])}</a><span aria-hidden="true">/</span><span aria-current="page">{esc(data["eyebrow"].title())}</span></nav><p class="section-kicker">{esc(data["eyebrow"])}</p><h1>{esc(data["h1"])}</h1><p class="topic-lead">{esc(data["lead"])}</p><div class="hero-actions"><a class="button button-primary" href="{APP_URL}">{esc(cfg["start"])} <span aria-hidden="true">→</span></a><a class="text-link" href="#jak-pomaha">{esc(data["help_title"])} <span aria-hidden="true">↓</span></a></div></header>
        <section class="content-section problem-section"><div class="section-copy"><p class="section-kicker">{esc(data["eyebrow"])}</p><h2>{esc(data["problem_title"])}</h2>{''.join(f'<p>{esc(paragraph)}</p>' for paragraph in data["problem"])}</div><div class="scenario-grid">{scenarios}</div></section>
        <section class="content-section help-section" id="jak-pomaha"><div class="section-copy"><p class="section-kicker">RODINKA</p><h2>{esc(data["help_title"])}</h2><p>{esc(data["help_intro"])}</p></div><ol class="help-steps">{steps}</ol></section>
        <section class="content-section answers-section"><div class="section-copy"><h2>{esc(data["answers_title"])}</h2></div><div class="answers-list">{answers}</div></section>
        <aside class="related-section"><p class="section-kicker">{esc(cfg["related_kicker"])}</p><h2>{esc(cfg["related"])}</h2><div class="related-grid">{related}</div></aside>
      </article>
      <section class="cta-section"><div class="cta-card"><p class="section-kicker">RODINKA</p><h2>{esc(data["cta_title"])}</h2><p>{esc(data["cta_text"])}</p><a class="app-cta" href="{APP_URL}">{esc(cfg["start"])} <span aria-hidden="true">→</span></a></div></section>
    </main>
{site_footer(locale)}
    <script src="/script.js?v={ASSET_VERSION}" defer></script>
  </body>
</html>
'''


def write_page(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def render_sitemap() -> str:
    page_order = ("home", "planner", "calendar", "shopping", "chores", "meals", "app")
    urls = "\n".join(
        f"  <url><loc>{canonical(PATHS[page_key][locale])}</loc></url>"
        for locale in ("cs", "sk", "en")
        for page_key in page_order
    )
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
'''


def render_llms_txt() -> str:
    return f'''# Rodinka

> Rodinka is a family organizer for a shared calendar, household chores, shopping lists and meal planning. The product name is Rodinka. The canonical website is {SITE_URL}/ and the web application is {APP_URL}.

## Czech (default)
- [Rodinka]({canonical(PATHS["home"]["cs"])})
- [Rodinný plánovač]({canonical(PATHS["planner"]["cs"])})
- [Rodinný kalendář]({canonical(PATHS["calendar"]["cs"])})
- [Sdílený nákupní seznam]({canonical(PATHS["shopping"]["cs"])})
- [Úkoly pro rodinu]({canonical(PATHS["chores"]["cs"])})
- [Plánování jídel]({canonical(PATHS["meals"]["cs"])})
- [Aplikace pro rodinu]({canonical(PATHS["app"]["cs"])})

## Slovak
- [Rodinka]({canonical(PATHS["home"]["sk"])})
- [Rodinný plánovač]({canonical(PATHS["planner"]["sk"])})
- [Rodinný kalendár]({canonical(PATHS["calendar"]["sk"])})
- [Zdieľaný nákupný zoznam]({canonical(PATHS["shopping"]["sk"])})
- [Úlohy pre rodinu]({canonical(PATHS["chores"]["sk"])})
- [Plánovanie jedál]({canonical(PATHS["meals"]["sk"])})
- [Aplikácia pre rodinu]({canonical(PATHS["app"]["sk"])})

## English
- [Rodinka]({canonical(PATHS["home"]["en"])})
- [Family planner]({canonical(PATHS["planner"]["en"])})
- [Family calendar]({canonical(PATHS["calendar"]["en"])})
- [Shared shopping list]({canonical(PATHS["shopping"]["en"])})
- [Family chores]({canonical(PATHS["chores"]["en"])})
- [Meal planning]({canonical(PATHS["meals"]["en"])})
- [Family organizer app]({canonical(PATHS["app"]["en"])})
'''


def main() -> None:
    for locale in ("cs", "sk", "en"):
        write_page(output_path(PATHS["home"][locale]), render_home(locale))
        for page_key in ("planner", "calendar", "shopping", "chores", "meals", "app"):
            write_page(output_path(PATHS[page_key][locale]), render_topic(page_key, locale))
    write_page(ROOT / "sitemap.xml", render_sitemap())
    write_page(ROOT / "llms.txt", render_llms_txt())
    print("Generated 21 localized HTML pages, sitemap.xml and llms.txt.")


if __name__ == "__main__":
    main()
