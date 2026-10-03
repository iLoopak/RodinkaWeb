"""Generate the static multilingual Rodinka marketing site.

The generated HTML is committed so Vercel can keep serving the repository without
a build command. Run this file after editing shared templates or localized copy.
"""

from __future__ import annotations

import html
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SITE_URL = "https://mojerodinka.cz"
APP_URL = "https://app.mojerodinka.cz"
SUPPORT_URL = "https://buymeacoffee.com/rodinka"
GTM_CONTAINER_ID = "GTM-5FM9NJHK"
CONSENT_STORAGE_KEY = "rodinka_analytics_consent"
CONSENT_VERSION = 1
OG_IMAGE_WIDTH = 1794
OG_IMAGE_HEIGHT = 877
OG_IMAGES = {"cs": "/og-image.png", "sk": "/og-image-sk.png", "en": "/og-image-en.png"}
ASSET_VERSION = "20260929b"

# Self-hosted webfont, built by tools/build_fonts.py. The app sets every word in
# Manrope, so the site does too: one variable file (wght 500-800) carries body,
# headings and the brand, and it is the only font preload.
MANROPE_WOFF2 = "/assets/fonts/manrope-latin-ext-500-800.woff2"

TOPIC_KEYS = ("planner", "calendar", "chores", "shopping", "meals", "trips", "memories", "documents", "baby", "app")


LOCALES = {
    "cs": {
        "lang": "cs",
        "og_locale": "cs_CZ",
        "home_path": "/",
        "site_description": "Rodinka je rodinný plánovač pro sdílený kalendář, úkoly, nákupy, jídla, výlety a rodinné vzpomínky.",
        "claim": "Ať doma všechno klape.",
        "skip": "Přeskočit na obsah",
        "menu": "Nabídka",
        "nav": {"calendar": "Kalendář", "chores": "Úkoly", "shopping": "Nákupy", "meals": "Jídla", "trips": "Výlety", "memories": "Vzpomínky"},
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
        "theme_light_label": "Přepnout na světlý režim",
        "theme_dark_label": "Přepnout na tmavý režim",
        "footer_text": "Rodinný organizér pro kalendář, úkoly, nákupy, výlety i vzpomínky. Česky, slovensky a anglicky.",
        "copyright": "© 2026 Rodinka",
        "app_label": "O aplikaci Rodinka",
        "support_label": "Podpořit vývoj",
        "cookie_settings": "Nastavení cookies",
        "consent_title": "Analytika webu",
        "consent_text": "Analytiku používáme, abychom porozuměli používání webu Rodinky a mohli ho zlepšovat. Spustí se až po vašem souhlasu.",
        "consent_allow": "Povolit analytiku",
        "consent_reject": "Odmítnout",
    },
    "sk": {
        "lang": "sk",
        "og_locale": "sk_SK",
        "home_path": "/sk/",
        "site_description": "Rodinka je rodinný plánovač pre zdieľaný kalendár, úlohy, nákupy, jedlá, výlety a rodinné spomienky.",
        "claim": "Nech doma všetko klape.",
        "skip": "Preskočiť na obsah",
        "menu": "Ponuka",
        "nav": {"calendar": "Kalendár", "chores": "Úlohy", "shopping": "Nákupy", "meals": "Jedlá", "trips": "Výlety", "memories": "Spomienky"},
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
        "theme_light_label": "Prepnúť na svetlý režim",
        "theme_dark_label": "Prepnúť na tmavý režim",
        "footer_text": "Rodinný organizér pre kalendár, úlohy, nákupy, výlety aj spomienky. Po česky, slovensky a anglicky.",
        "copyright": "© 2026 Rodinka",
        "app_label": "O aplikácii Rodinka",
        "support_label": "Podporiť vývoj",
        "cookie_settings": "Nastavenie cookies",
        "consent_title": "Analytika webu",
        "consent_text": "Analytiku používame, aby sme porozumeli používaniu webu Rodinky a mohli ho zlepšovať. Spustí sa až po vašom súhlase.",
        "consent_allow": "Povoliť analytiku",
        "consent_reject": "Odmietnuť",
    },
    "en": {
        "lang": "en",
        "og_locale": "en_US",
        "home_path": "/en/",
        "site_description": "Rodinka is a family organizer for a shared calendar, chores, shopping, meals, trips and family memories.",
        "claim": "Keep the household running smoothly.",
        "skip": "Skip to content",
        "menu": "Menu",
        "nav": {"calendar": "Calendar", "chores": "Chores", "shopping": "Shopping", "meals": "Meals", "trips": "Trips", "memories": "Memories"},
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
        "theme_light_label": "Switch to light mode",
        "theme_dark_label": "Switch to dark mode",
        "footer_text": "A family organizer for the calendar, chores, shopping, trips and memories. In Czech, Slovak and English.",
        "copyright": "© 2026 Rodinka",
        "app_label": "About the Rodinka app",
        "support_label": "Support development",
        "cookie_settings": "Cookie settings",
        "consent_title": "Website analytics",
        "consent_text": "We use analytics to understand how Rodinka’s website is used and improve it. Analytics will only start after your consent.",
        "consent_allow": "Allow analytics",
        "consent_reject": "Reject",
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
    "baby": {"cs": "/priprava-na-miminko/", "sk": "/sk/priprava-na-babatko/", "en": "/en/preparing-for-a-baby/"},
    "memories": {"cs": "/rodinne-vzpominky/", "sk": "/sk/rodinne-spomienky/", "en": "/en/family-memories/"},
    "documents": {"cs": "/hlidani-platnosti-dokladu/", "sk": "/sk/strazenie-platnosti-dokladov/", "en": "/en/document-expiry-reminders/"},
    "trips": {"cs": "/rodinne-vylety/", "sk": "/sk/rodinne-vylety/", "en": "/en/family-trips/"},
}


RELATED = {
    "planner": ("calendar", "trips", "app"),
    "calendar": ("planner", "chores", "trips"),
    "shopping": ("meals", "planner", "app"),
    "chores": ("calendar", "planner", "app"),
    "meals": ("shopping", "calendar", "planner"),
    "trips": ("memories", "calendar", "documents"),
    "memories": ("trips", "baby", "app"),
    "documents": ("trips", "calendar", "app"),
    "baby": ("memories", "planner", "app"),
    "app": ("planner", "trips", "memories"),
}


PRODUCT_IMAGE_WIDTH = 900
PRODUCT_IMAGE_HEIGHT = 1951

DIRECT_ANSWERS = {
    "cs": {
        "home": (
            "Co je Rodinka a jak pomáhá s organizací rodiny?",
            "Rodinka je rodinný organizér, ve kterém má domácnost společný kalendář, úkoly, nákupní seznam a plán jídel — a k tomu výlety, rodinné vzpomínky a hlídání dokladů. Rodiče pracují se stejným aktuálním přehledem a děti mohou mít vlastní přihlášení se svými úkoly. Začít lze jednou oblastí a další přidat, až je rodina potřebuje.",
        ),
        "planner": (
            "Jak funguje rodinný plánovač?",
            "Rodinný plánovač soustředí společné termíny, povinnosti a praktické seznamy do jednoho rodinného prostoru. V Rodince tak rychle zjistíte, kdo dnes vyzvedává dítě, co je potřeba doma zařídit a co koupit. Každý vidí stejnou aktuální informaci a organizování nemusí ležet jen na jednom člověku.",
        ),
        "calendar": (
            "Jak sdílet rodinný kalendář mezi rodiči?",
            "V Rodince používají rodiče jeden společný rodinný prostor a zapisují události do stejného kalendáře. U kroužku, návštěvy nebo výletu je pak na jednom místě termín, účastníci i domluvený doprovod. Změnu uvidí oba bez přepisování mezi dvěma kalendáři a narozeniny, jmeniny či státní svátky se ukazují jako tichá vrstva, která neblokuje čas.",
        ),
        "shopping": (
            "Jak mít společný nákupní seznam pro celou domácnost?",
            "V Rodince má domácnost jeden sdílený nákupní seznam, do kterého mohou členové průběžně přidávat položky. V obchodě se nakoupené věci odškrtávají ve stejném seznamu, takže všichni vidí aktuální stav. Není potřeba posílat novou verzi seznamu před každým nákupem.",
        ),
        "chores": (
            "Jak rozdělit domácí úkoly mezi členy rodiny?",
            "Nejdřív sepište konkrétní povinnosti a u každé určete, kdo ji má zařídit a do kdy. Rodinka udržuje toto rozdělení viditelné pro domácnost, takže úkoly nezůstávají jen v hlavě jednoho rodiče. Dětem lze vybírat jednoduché povinnosti odpovídající jejich věku.",
        ),
        "meals": (
            "Jak plánovat jídla na celý týden pro rodinu?",
            "Začněte rodinným programem a ke dnům přiřaďte jídla podle času, který bude na přípravu. V Rodince zůstane týdenní plán jídel vedle ostatních rodinných plánů a chybějící suroviny můžete přidat do společného nákupního seznamu. Jeden volnější den pomůže využít zbytky nebo reagovat na změnu programu.",
        ),
        "app": (
            "Jaká aplikace pomůže s organizací rodiny?",
            "Praktická aplikace pro rodinu má na jednom místě odpovědi na běžné otázky: kdo co dnes má, kdo něco zařídí a co je potřeba koupit. Rodinka spojuje rodinný kalendář, úkoly, nákupní seznam a jídelníček a přidává k nim výlety, vzpomínky, doklady, zdravotní termíny i rodinný chat. Funguje v prohlížeči na mobilu i počítači, takže není nutná instalace.",
        ),
        "memories": (
            "Kam ukládat dětské milníky a rodinné vzpomínky?",
            "Rodinka vede rodinné vzpomínky jako jednu společnou kroniku: dětské milníky, rodinné poklady i společné zážitky s fotografií se řadí na jednu časovou osu a každou vzpomínku můžete přiřadit konkrétnímu členovi rodiny. Na obrazovce Dnes se občas připomene, co se stalo v tentýž den v minulých letech, a z milníku si můžete připravit kartičku k vytištění.",
        ),
        "documents": (
            "Jak hlídat platnost pasů a dokladů celé rodiny?",
            "Zapište ke každému dokladu, komu patří a do kdy platí. Rodinka pak ve výchozím nastavení připomene konec platnosti 180, 90, 30 a 7 dní předem, takže na končící pas nebo občanku nepřijdete až týden před dovolenou. Doklady vidí jen dospělí členové rodiny a připomínky respektují tiché hodiny, které si nastavíte.",
        ),
        "baby": (
            "Jak se připravit na miminko společně s partnerem?",
            "Rodinka spojuje orientační cestu po týdnech, praktické přípravy a společný výběr jména v jednom rodinném prostoru. Oba rodiče tak vidí, co už mají připravené, co ještě chtějí zařídit a která jména zvažují. Nejde o zdravotní těhotenský tracker, ale o společnou organizaci před narozením dítěte.",
        ),
        "trips": (
            "Jak naplánovat rodinný výlet, aby rozhodovala celá rodina?",
            "V Rodince si rodina průběžně ukládá tipy na výlety a dovolené — stačí vložit odkaz. Z vybraných tipů složíte plán cesty, každý v rodině u tipu hlasuje a dospělý vybraný tip jedním krokem převede do rodinného kalendáře. Po návratu z výletu uděláte rodinnou vzpomínku.",
        ),
    },
    "sk": {
        "home": (
            "Čo je Rodinka a ako pomáha s organizáciou rodiny?",
            "Rodinka je rodinný organizér, v ktorom má domácnosť spoločný kalendár, úlohy, nákupný zoznam a plán jedál — a k tomu výlety, rodinné spomienky a stráženie dokladov. Rodičia pracujú s rovnakým aktuálnym prehľadom a deti môžu mať vlastné prihlásenie so svojimi úlohami. Začať môžete jednou oblasťou a ďalšie pridať, keď ich rodina potrebuje.",
        ),
        "planner": (
            "Ako funguje rodinný plánovač?",
            "Rodinný plánovač sústreďuje spoločné termíny, povinnosti a praktické zoznamy do jedného rodinného priestoru. V Rodinke tak rýchlo zistíte, kto dnes vyzdvihne dieťa, čo treba doma zariadiť a čo kúpiť. Každý vidí rovnakú aktuálnu informáciu a organizovanie nemusí zostať iba na jednom človeku.",
        ),
        "calendar": (
            "Ako zdieľať rodinný kalendár medzi rodičmi?",
            "V Rodinke rodičia používajú jeden spoločný rodinný priestor a udalosti zapisujú do rovnakého kalendára. Pri krúžku, návšteve alebo výlete je potom na jednom mieste termín, účastníci aj dohodnutý sprievod. Zmenu uvidia obaja bez prepisovania medzi dvoma kalendármi a narodeniny či výročia sa zobrazujú ako tichá vrstva, ktorá neblokuje čas.",
        ),
        "shopping": (
            "Ako mať spoločný nákupný zoznam pre celú domácnosť?",
            "V Rodinke má domácnosť jeden zdieľaný nákupný zoznam, do ktorého môžu členovia priebežne pridávať položky. V obchode sa nakúpené veci odškrtávajú v rovnakom zozname, takže všetci vidia aktuálny stav. Pred každým nákupom netreba posielať novú verziu zoznamu.",
        ),
        "chores": (
            "Ako rozdeliť domáce úlohy medzi členov rodiny?",
            "Najprv spíšte konkrétne povinnosti a pri každej určte, kto ju má zariadiť a dokedy. Rodinka udržiava toto rozdelenie viditeľné pre domácnosť, takže úlohy nezostanú iba v hlave jedného rodiča. Deťom môžete vybrať jednoduché povinnosti primerané ich veku.",
        ),
        "meals": (
            "Ako plánovať jedlá na celý týždeň pre rodinu?",
            "Začnite rodinným programom a ku dňom priraďte jedlá podľa času, ktorý bude na prípravu. V Rodinke zostane týždenný plán jedál vedľa ostatných rodinných plánov a chýbajúce suroviny môžete pridať do spoločného nákupného zoznamu. Jeden voľnejší deň pomôže využiť zvyšky alebo reagovať na zmenu programu.",
        ),
        "app": (
            "Aká aplikácia pomôže s organizáciou rodiny?",
            "Praktická aplikácia pre rodinu má na jednom mieste odpovede na bežné otázky: kto čo dnes má, kto niečo zariadi a čo treba kúpiť. Rodinka spája rodinný kalendár, úlohy, nákupný zoznam a jedálniček a pridáva k nim výlety, spomienky, doklady, zdravotné termíny aj rodinný chat. Funguje v prehliadači v mobile aj počítači, takže inštalácia nie je potrebná.",
        ),
        "memories": (
            "Kam ukladať detské míľniky a rodinné spomienky?",
            "Rodinka vedie rodinné spomienky ako jednu spoločnú kroniku: detské míľniky, rodinné poklady aj spoločné zážitky s fotografiou sa radia na jednu časovú os a každú spomienku môžete priradiť konkrétnemu členovi rodiny. Na obrazovke Dnes sa občas pripomenie, čo sa stalo v ten istý deň v minulých rokoch, a z míľnika si môžete pripraviť kartičku na vytlačenie.",
        ),
        "documents": (
            "Ako strážiť platnosť pasov a dokladov celej rodiny?",
            "Zapíšte ku každému dokladu, komu patrí a dokedy platí. Rodinka potom v predvolenom nastavení pripomenie koniec platnosti 180, 90, 30 a 7 dní vopred, takže na končiaci pas alebo občiansky preukaz neprídete až týždeň pred dovolenkou. Doklady vidia len dospelí členovia rodiny a pripomienky rešpektujú tiché hodiny, ktoré si nastavíte.",
        ),
        "baby": (
            "Ako sa pripraviť na bábätko spoločne s partnerom?",
            "Rodinka spája orientačnú cestu po týždňoch, praktické prípravy a spoločný výber mena v jednom rodinnom priestore. Obaja rodičia tak vidia, čo už majú pripravené, čo ešte chcú zariadiť a ktoré mená zvažujú. Nejde o zdravotný tehotenský tracker, ale o spoločnú organizáciu pred narodením dieťaťa.",
        ),
        "trips": (
            "Ako naplánovať rodinný výlet, aby rozhodovala celá rodina?",
            "V Rodinke si rodina priebežne ukladá tipy na výlety a dovolenky — stačí vložiť odkaz. Z vybraných tipov zostavíte plán cesty, každý v rodine pri tipe hlasuje a dospelý vybraný tip jedným krokom prenesie do rodinného kalendára. Po návrate z výletu z neho spravíte rodinnú spomienku.",
        ),
    },
    "en": {
        "home": (
            "What is Rodinka, and how does it help organize family life?",
            "Rodinka is a family organizer with a shared calendar, chores, shopping list and meal plan — plus trips, family memories and document expiry tracking. Parents work from the same current overview, and children can have their own sign-in with their own chores. A family can start with one area and add the rest when it becomes useful.",
        ),
        "planner": (
            "How does a family planner work?",
            "A family planner keeps shared dates, responsibilities and practical lists in one household space. In Rodinka, you can quickly see who is picking up today, what needs doing at home and what the family needs to buy. Everyone works from the same current information, so the organizing does not have to sit with one person.",
        ),
        "calendar": (
            "How can parents share a family calendar?",
            "Parents use one shared family space in Rodinka and add events to the same calendar. An activity, appointment or trip can keep the date, participants and agreed transport together. Both parents see the change without copying it between separate calendars, and birthdays or anniversaries show up as a quiet layer that does not block time.",
        ),
        "shopping": (
            "How do you keep a shared shopping list for the whole household?",
            "Rodinka gives the household one shared shopping list that family members can update as things run out. Items are checked off in that same list while somebody shops, so everyone sees the current state. There is no need to send a new version before every grocery trip.",
        ),
        "chores": (
            "How can you divide household chores between family members?",
            "Start with specific responsibilities and give each one an owner and a realistic due date. Rodinka keeps that agreement visible to the household, so the list does not live only in one parent’s head. Children can take on simple chores that suit their age.",
        ),
        "meals": (
            "How do you plan a week of meals for a family?",
            "Start with the family schedule and match meals to the time available on each day. Rodinka keeps the weekly meal plan beside the rest of the family plan, and missing ingredients can go onto the shared shopping list. Leaving one flexible evening makes room for leftovers or an unexpected change.",
        ),
        "app": (
            "What kind of app helps organize family life?",
            "A useful family organizer answers everyday questions in one place: what is happening today, who is handling something and what needs to be bought. Rodinka combines a family calendar, chores, a shopping list and a meal plan, and adds trips, memories, documents, health appointments and a family chat. It works in a browser on phones and computers, so installation is optional.",
        ),
        "memories": (
            "Where can a family keep children’s milestones and memories?",
            "Rodinka keeps family memories as one shared chronicle: children’s milestones, family treasures and shared experiences with their photos sit on a single timeline, and every memory can belong to a particular family member. The Today screen occasionally resurfaces what happened on the same date in earlier years, and a milestone can be turned into a card you print at home.",
        ),
        "documents": (
            "How can a family track passport and ID expiry dates?",
            "Record who each document belongs to and when it expires. By default Rodinka then reminds you 180, 90, 30 and 7 days before it expires, so an expiring passport or ID card does not surface a week before the holiday. Documents are visible to adults only, and reminders respect the quiet hours your household sets.",
        ),
        "baby": (
            "How can partners prepare for a baby together?",
            "Rodinka brings a light week-by-week journey, practical preparations and choosing a name into one shared family space. Both parents can see what is ready, what they still want to arrange and which names they are considering. It is not a medical pregnancy tracker; it helps the family organize together before the baby arrives.",
        ),
        "trips": (
            "How can a family plan a trip that everyone gets a say in?",
            "In Rodinka the family collects trip and holiday ideas as they come up — pasting a link is enough. A few ideas become a trip plan, everyone in the family votes on each one, and an adult turns the chosen idea into a calendar event in one step. After the trip, it can become a family memory.",
        ),
    },
}


PRODUCT_PROOFS = {
    "home": {
        "src": "/assets/product/rodinka-today-family-overview.webp",
        "alt": {
            "cs": "Obrazovka Dnes v Rodince s denní linkou rodiny a dnešním programem aktivit a úkolů",
            "sk": "Obrazovka Dnes v Rodinke s dennou linkou rodiny a dnešným programom aktivít a úloh",
            "en": "The Today screen in Rodinka with the family’s day line and today’s schedule of activities and chores",
        },
        "caption": {
            "cs": "Na jedné obrazovce vidíte, kdo má kdy program, a pod denní linkou celý dnešní rozpis aktivit i úkolů.",
            "sk": "Na jednej obrazovke vidíte, kto má kedy program, a pod dennou linkou celý dnešný rozpis aktivít aj úloh.",
            "en": "One screen shows who is busy when and, below the day line, today’s full list of activities and chores.",
        },
    },
    "planner": {
        "src": "/assets/product/rodinka-family-planning.webp",
        "alt": {
            "cs": "Obrazovka Plánovat v Rodince s domácími úkoly, aktivitami, zdravím, jídlem a dokumenty",
            "sk": "Obrazovka Plánovať v Rodinke s domácimi úlohami, aktivitami, zdravím, jedlom a dokumentmi",
            "en": "Rodinka’s Plan screen with household chores, activities, health, meals and documents",
        },
        "caption": {
            "cs": "Přehled Plánovat spojuje oblasti, které rodina řeší opakovaně, a u každé ukazuje nejbližší věc i to, kdo ji má na starosti.",
            "sk": "Prehľad Plánovať spája oblasti, ktoré rodina rieši opakovane, a pri každej ukazuje najbližšiu vec aj to, kto ju má na starosti.",
            "en": "The Plan overview brings recurring parts of family life together and shows the next item in each one and who is handling it.",
        },
    },
    "calendar": {
        "src": "/assets/product/rodinka-shared-family-calendar.webp",
        "alt": {
            "cs": "Měsíční pohled sdíleného rodinného kalendáře v Rodince, kde má každý člen rodiny svou barvu",
            "sk": "Mesačný pohľad zdieľaného rodinného kalendára v Rodinke, kde má každý člen rodiny svoju farbu",
            "en": "Month view of Rodinka’s shared family calendar, where every family member has their own colour",
        },
        "caption": {
            "cs": "V měsíčním kalendáři barevné tečky ukazují, kdo má který den program, a pod mřížkou je rozpis vybraného dne.",
            "sk": "V mesačnom kalendári farebné bodky ukazujú, kto má ktorý deň program, a pod mriežkou je rozpis vybraného dňa.",
            "en": "In the month view, coloured dots show who has plans on which day, with the selected day listed below the grid.",
        },
    },
    "shopping": {
        "src": "/assets/product/rodinka-shared-shopping-list.webp",
        "alt": {
            "cs": "Sdílený nákupní seznam v Rodince s položkami v kategoriích, množstvím a tím, kdo je přidal a kdo je nakoupí",
            "sk": "Zdieľaný nákupný zoznam v Rodinke s položkami v kategóriách, množstvom a tým, kto ich pridal a kto ich nakúpi",
            "en": "Rodinka shared shopping list with items grouped by category, quantities, who added them and who will buy them",
        },
        "caption": {
            "cs": "Seznam je synchronizovaný a rozdělený do kategorií; u položky je vidět množství, kdo ji přidal a kdo ji nakoupí.",
            "sk": "Zoznam je synchronizovaný a rozdelený do kategórií; pri položke vidno množstvo, kto ju pridal a kto ju nakúpi.",
            "en": "The list stays synchronized and grouped by category; each item shows the quantity, who added it and who will buy it.",
        },
    },
    "chores": {
        "src": "/assets/product/rodinka-family-chores.webp",
        "alt": {
            "cs": "Obrazovka Úkoly v Rodince s rychlými úkoly a úkoly přiřazenými dětem, včetně opakování a odměny",
            "sk": "Obrazovka Úlohy v Rodinke s rýchlymi úlohami a úlohami priradenými deťom vrátane opakovania a odmeny",
            "en": "Rodinka’s Tasks screen with quick tasks and chores assigned to children, including repeats and rewards",
        },
        "caption": {
            "cs": "Úkol má člověka, opakování i případnou odměnu. Dítě ho odškrtne, rodič potvrdí splnění a částka se připíše.",
            "sk": "Úloha má človeka, opakovanie aj prípadnú odmenu. Dieťa ju odškrtne, rodič potvrdí splnenie a suma sa pripíše.",
            "en": "Each chore has a person, a repeat and, if you like, a reward. A child ticks it off, a parent confirms and the amount is credited.",
        },
    },
    "app": {
        "src": "/assets/product/rodinka-today-family-overview.webp",
        "alt": {
            "cs": "Obrazovka Dnes v Rodince se společným programem celé rodiny, aktivitami a úkoly na jednom místě",
            "sk": "Obrazovka Dnes v Rodinke so spoločným programom celej rodiny, aktivitami a úlohami na jednom mieste",
            "en": "Rodinka’s Today screen with the whole family’s schedule, activities and chores in one place",
        },
        "caption": {
            "cs": "Obrazovka Dnes odpoví na každodenní otázky: kdo má kdy program, co je potřeba udělat a co rodinu ještě čeká.",
            "sk": "Obrazovka Dnes odpovie na každodenné otázky: kto má kedy program, čo treba urobiť a čo rodinu ešte čaká.",
            "en": "The Today screen answers the everyday questions: who is busy when, what needs doing and what is still ahead.",
        },
    },
    "memories": {
        "src": "/assets/product/rodinka-family-memories.webp",
        "alt": {
            "cs": "Obrazovka Vzpomínky v Rodince s rodinnou časovou osou, fotkou z podzimní procházky a filtry pro milníky a poklady",
            "sk": "Obrazovka Spomienky v Rodinke s rodinnou časovou osou, fotkou z jesennej prechádzky a filtrami pre míľniky a poklady",
            "en": "The Memories screen in Rodinka with the family timeline, a photo from an autumn walk and filters for milestones and treasures",
        },
        "caption": {
            "cs": "Zážitky s fotkou, dětské milníky i rodinné poklady se řadí na jednu společnou časovou osu a dají se filtrovat.",
            "sk": "Zážitky s fotkou, detské míľniky aj rodinné poklady sa radia na jednu spoločnú časovú os a dajú sa filtrovať.",
            "en": "Experiences with a photo, children’s milestones and family treasures share one timeline you can filter.",
        },
    },
    "baby": {
        "src": "/assets/product/rodinka-expected-child.webp",
        "alt": {
            "cs": "Dva telefony s funkcí Miminko na cestě v Rodince, přehledem příprav a společným výběrem jména",
            "sk": "Dva telefóny s funkciou Bábätko na ceste v Rodinke, prehľadom príprav a spoločným výberom mena",
            "en": "Two phones showing Rodinka’s expected-child journey, preparation checklist and shared name choices",
        },
        "caption": {
            "cs": "Rodinka spojuje orientační cestu po týdnech, praktické přípravy a společný výběr jména.",
            "sk": "Rodinka spája orientačnú cestu po týždňoch, praktické prípravy a spoločný výber mena.",
            "en": "Rodinka brings a light week-by-week journey, practical preparations and choosing a name together.",
        },
    },
}


HOME_MEMORY_STORY = {
    "src": "/assets/product/rodinka-family-memories.webp",
    "cs": {
        "kicker": "NEJEN POVINNOSTI",
        "title": "Nejen to, co musíte zařídit. I to, co si chcete pamatovat.",
        "text": "Dětské milníky, rodinné poklady i společné zážitky s fotkou se v Rodince řadí na jednu společnou časovou osu. Každou vzpomínku můžete přiřadit člověku, kterého se týká, na obrazovce Dnes se občas připomene, co se stalo v tentýž den v minulých letech, a z milníku si připravíte kartičku k vytištění.",
        "link": "Rodinné vzpomínky",
        "alt": "Obrazovka Vzpomínky v Rodince s časovou osou rodiny a fotografií z podzimní procházky v lese",
        "caption": "Vzpomínky s fotkou, dětské milníky i rodinné poklady na jedné časové ose celé rodiny.",
    },
    "sk": {
        "kicker": "NIELEN POVINNOSTI",
        "title": "Nielen to, čo musíte zariadiť. Aj to, čo si chcete pamätať.",
        "text": "Detské míľniky, rodinné poklady aj spoločné zážitky s fotkou sa v Rodinke radia na jednu spoločnú časovú os. Každú spomienku môžete priradiť človeku, ktorého sa týka, na obrazovke Dnes sa občas pripomenie, čo sa stalo v ten istý deň v minulých rokoch, a z míľnika si pripravíte kartičku na vytlačenie.",
        "link": "Rodinné spomienky",
        "alt": "Obrazovka Spomienky v Rodinke s časovou osou rodiny a fotografiou z jesennej prechádzky v lese",
        "caption": "Spomienky s fotkou, detské míľniky aj rodinné poklady na jednej časovej osi celej rodiny.",
    },
    "en": {
        "kicker": "MORE THAN ADMIN",
        "title": "Not only what has to be arranged. Also what you want to remember.",
        "text": "Children’s milestones, family treasures and shared experiences with a photo share a single timeline in Rodinka. Every memory can belong to the person it is about, the Today screen occasionally resurfaces what happened on the same date in earlier years, and a milestone can become a card you print at home.",
        "link": "Family memories",
        "alt": "The Memories screen in Rodinka with the family timeline and a photo from an autumn walk in the woods",
        "caption": "Memories with a photo, children’s milestones and family treasures on one shared family timeline.",
    },
}


HOME_BABY_STORY = {
    "src": "/assets/product/rodinka-expected-child.webp",
    "cs": {
        "kicker": "NOVÁ KAPITOLA RODINY",
        "title": "Čekáte miminko? Připravíme se spolu.",
        "text": "Od orientační cesty po týdnech přes praktické přípravy až po jména, která se vám líbí. Rodinka pomůže oběma rodičům držet přípravy pohromadě.",
        "link": "Příprava na miminko",
        "alt": "Dva telefony s funkcí Miminko na cestě v Rodince, cestou po týdnech, přípravami a výběrem jména",
        "caption": "Miminko na cestě dává dospělým společný přehled příprav před příchodem nového člena rodiny.",
    },
    "sk": {
        "kicker": "NOVÁ KAPITOLA RODINY",
        "title": "Čakáte bábätko? Pripravíme sa spolu.",
        "text": "Od orientačnej cesty po týždňoch cez praktické prípravy až po mená, ktoré sa vám páčia. Rodinka pomôže obom rodičom udržať prípravy pokope.",
        "link": "Príprava na bábätko",
        "alt": "Dva telefóny s funkciou Bábätko na ceste v Rodinke, cestou po týždňoch, prípravami a výberom mena",
        "caption": "Bábätko na ceste dáva dospelým spoločný prehľad príprav pred príchodom nového člena rodiny.",
    },
    "en": {
        "kicker": "A NEW CHAPTER FOR YOUR FAMILY",
        "title": "Expecting a baby? Get ready together.",
        "text": "From a light week-by-week journey to practical preparations and names you both like, Rodinka helps parents keep the next chapter in one shared place.",
        "link": "Preparing for a baby",
        "alt": "Two phones showing Rodinka’s expected-child journey, practical preparations and shared name choices",
        "caption": "Expected Child gives adults one shared view of family preparations before the new arrival.",
    },
}


# The promo spot has a localized voice-over for each homepage. "stem" is the
# file prefix in /assets/video/; phones get the 9:16 cut and poster,
# everything else 16:9. The spot ends on a "try Rodinka" pill drawn into the
# picture, and script.js lays a real app link over it: "cta" is the pill's
# label, "cta_from" the second it appears and "cta_width" its width in pixels
# of the 1080 px cuts. Measure all three again whenever a spot is re-rendered.
HOME_SPOT = {
    "cs": {
        "stem": "/assets/video/rodinka-spot",
        "kicker": "RODINKA ZA 50 VTEŘIN",
        "title": "Rodina je ten nejkrásnější chaos.",
        "lead": "Jedno obyčejné ráno — od otázek na lednici po společný víkend.",
        "play": "Pusťte si Rodinku",
        "meta": "Video · 0:50 · se zvukem",
        "label": "Přehrát video o Rodince, 50 sekund se zvukem",
        "cta": "Vyzkoušet Rodinku",
        "cta_from": "43.4",
        "cta_width": "540",
    },
    "sk": {
        "stem": "/assets/video/rodinka-spot-sk",
        "kicker": "RODINKA ZA 50 SEKÚND",
        "title": "Rodina je ten najkrajší chaos.",
        "lead": "Jedno obyčajné ráno — od otázok na chladničke po spoločný víkend.",
        "play": "Pustite si Rodinku",
        "meta": "Video · 0:50 · so zvukom",
        "label": "Prehrať video o Rodinke, 50 sekúnd so zvukom",
        "cta": "Vyskúšať Rodinku",
        "cta_from": "42.9",
        "cta_width": "510",
    },
    "en": {
        "stem": "/assets/video/rodinka-spot-en",
        "kicker": "RODINKA IN 50 SECONDS",
        "title": "Family is the most beautiful chaos.",
        "lead": "One ordinary morning — from questions on the fridge to a weekend together.",
        "play": "Watch Rodinka",
        "meta": "Video · 0:50 · with sound",
        "label": "Play the Rodinka video, 50 seconds with sound",
        "cta": "Try Rodinka",
        "cta_from": "43.8",
        "cta_width": "372",
    },
}
SPOT_TALL_MEDIA = "(max-width: 560px)"


# "Každodenní Rodinka": the short 9:16 episodes from Rodinka/promo/rodinka-spot
# (src/episodes/epNN). Each one sells a single everyday moment, so it plays on
# the topic page whose problem it tells ("page", in the problem section) and all
# of them play on the homepage, where "link" leads to the feature. "Co nás dnes
# čeká?" is about the Today screen as a whole and has no topic page of its own.
# The voices and the words drawn in the picture are Czech, so only the Czech
# pages carry the series until localized renders exist. "stem" is the file name
# in /assets/video/ (.mp4 and a 720 px .webp poster), "seconds" the rounded
# running time; re-measure it whenever an episode is re-rendered.
SERIES = {
    "cs": {
        "kicker": "KAŽDODENNÍ RODINKA",
        "title": "Malé chvíle, které zná každá rodina",
        "lead": "Kdo dnes vyzvedává, co máme koupit, kam pojedeme o víkendu — a co si chceme pamatovat. Sedm krátkých videí o tom, jak s tím pomáhá Rodinka.",
        "list": "Videa ze série Každodenní Rodinka",
        "play": "Přehrát video",
        "meta": "{time} · se zvukem",
        "label": "Přehrát video „{title}“, {seconds} sekund se zvukem",
        "episodes": (
            {
                "stem": "kazdodenni-rodinka-01-kdo-dnes-vyzvedava",
                "seconds": 17,
                "page": "calendar",
                "title": "Kdo dnes vyzvedává?",
                "text": "Máma i táta počítají s tím, že Kubu ze školky vyzvedne ten druhý. V Rodince je u vyzvednutí rovnou vidět, kdo ho doprovází.",
            },
            {
                "stem": "kazdodenni-rodinka-02-co-mame-koupit",
                "seconds": 16,
                "page": "shopping",
                "title": "Co máme koupit?",
                "text": "Odpovědi z rodinného chatu chodí po jedné a máslo až u pokladny. Sdílený nákupní seznam je má pohromadě, roztříděné a k odškrtnutí.",
            },
            {
                "stem": "kazdodenni-rodinka-03-v-kolik-ma-krouzek",
                "seconds": 14,
                "page": "planner",
                "title": "V kolik má dneska kroužek?",
                "text": "Táta s klíči v ruce tipuje, jestli ve čtyři, nebo v pět. Denní linka na obrazovce Dnes ukáže, že Ema má judo v půl páté a kdo ji veze.",
            },
            {
                "stem": "kazdodenni-rodinka-04-kam-jsme-chteli-jet",
                "seconds": 18,
                "page": "trips",
                "title": "Kam jsme to chtěli jet?",
                "text": "Nápady na výlet leží v chatu, ve screenshotech i na babiččině pohlednici. V Rodince se sejdou v Zásobníku nápadů, kde si rodina jeden vybere a naplánuje.",
            },
            {
                "stem": "kazdodenni-rodinka-05-co-nas-dnes-ceka",
                "seconds": 16,
                "page": None,
                "link": "planner",
                "title": "Co nás dnes čeká?",
                "text": "Obyčejné ráno u snídaně. Jeden pohled na obrazovku Dnes a všichni vědí, kdo co má, kdo koho vyzvedne a kde se večer sejdou.",
            },
            {
                "stem": "kazdodenni-rodinka-06-kde-jsme-to-resili",
                "seconds": 14,
                "page": "app",
                "title": "Kde jsme to řešili?",
                "text": "Babiččina sedmdesátka probraná v chatu, v kalendáři, na lepíku i v e-mailu. V Rodince z toho zůstane jedna obrazovka: oslava, dort a co ještě koupit.",
            },
            {
                "stem": "kazdodenni-rodinka-07-tohle-si-chceme-pamatovat",
                "seconds": 25,
                "page": "memories",
                "title": "Tohle si chceme pamatovat.",
                "text": "Kuba jede poprvé sám na kole a máma si fotku uloží do Rodinky. O rok později se k ní rodina vrátí na obrazovce Dnes v sekci V tento den.",
            },
        ),
    },
}
SERIES_POSTER_WIDTH = 720
SERIES_POSTER_HEIGHT = 1280



# The Today screen drawn in the hero. Every string is the app's own wording
# (Rodinka/src/strings/today.ts, shell.ts and the Rodinka Today copy), so the
# drawing says what the product says. The family is illustrative.
HOME_PHONE = {
    "cs": {
        "family": "Novákovi",
        "greeting": "Vítejte, Kláro.",
        "date": "Úterý 6. října",
        "summary": "Dnes vás čekají 3 věci.",
        "program": "Dnešní program",
        "rows": (("7:45", "Školka", "Tobiáš · doprovází Martin"), ("15:00", "Plavání", "Ema · doprovází Klára"), ("18:30", "Večeře: rizoto", "Připraví Martin")),
        "dinner": "večeře",
        "daily_title": "Dnešní Rodinka",
        "daily_eyebrow": "Dnešní hlasování",
        "question": "Kam vyrazíme v sobotu?",
        "options": (("Na hrad", "2 hlasy"), ("Do zoo", "1 hlas"), ("K babičce", "0 hlasů")),
        "voted": "Hlasovali 3 z 4",
        "nav": ("Dnes", "Kalendář", "Vzpomínky", "Plánovat", "Rodina"),
    },
    "sk": {
        "family": "Novákovci",
        "greeting": "Vitajte, Klára.",
        "date": "Utorok 6. októbra",
        "summary": "Dnes vás čakajú 3 veci.",
        "program": "Dnešný program",
        "rows": (("7:45", "Škôlka", "Tobiáš · sprevádza Martin"), ("15:00", "Plávanie", "Ema · sprevádza Klára"), ("18:30", "Večera: rizoto", "Pripraví Martin")),
        "dinner": "večera",
        "daily_title": "Dnešná Rodinka",
        "daily_eyebrow": "Dnešné hlasovanie",
        "question": "Kam vyrazíme v sobotu?",
        "options": (("Na hrad", "2 hlasy"), ("Do zoo", "1 hlas"), ("K babke", "0 hlasov")),
        "voted": "Hlasovali 3 z 4",
        "nav": ("Dnes", "Kalendár", "Spomienky", "Plánovať", "Rodina"),
    },
    "en": {
        "family": "Novák",
        "greeting": "Welcome, Klára.",
        "date": "Tuesday, 6 October",
        "summary": "You have 3 things today.",
        "program": "Today’s schedule",
        "rows": (("7:45", "Nursery", "Tobiáš · accompanied by Martin"), ("15:00", "Swimming", "Ema · accompanied by Klára"), ("18:30", "Dinner: risotto", "Prepared by Martin")),
        "dinner": "dinner",
        "daily_title": "Rodinka Today",
        "daily_eyebrow": "Today’s vote",
        "question": "Where shall we go on Saturday?",
        "options": (("To the castle", "2 votes"), ("To the zoo", "1 vote"), ("To Grandma’s", "0 votes")),
        "voted": "3 of 4 have voted",
        "nav": ("Today", "Calendar", "Memories", "Plan", "Family"),
    },
}


# The seven areas the app asks about right after a family is created
# ("S čím vám má Rodinka nejvíc pomáhat?", Rodinka/src/features/onboarding).
# Same order, same labels; the answer only reorders suggestions in the app, and
# the copy says so rather than implying a setup that locks anything.
# Card: (tone, glyph, title, text, chips, links).
HOME_FOCUS = {
    "cs": {
        "kicker": "S ČÍM ZAČÍT",
        "title": "S čím vám má Rodinka nejvíc pomáhat?",
        "lead": "Stejnou otázku vám Rodinka položí hned po založení rodiny. Sedm oblastí, jedna sdílená domácnost — začněte tou, která vás doma pálí nejvíc.",
        "cards": (
            ("calendar", "calendar", "Rodinný čas a kalendář", "Jeden kalendář pro celou rodinu v pohledu měsíc, týden i agenda. U každé položky je vidět, koho se týká a kdo ji zajišťuje. Narozeniny a svátky se ukážou samy.", ("Opakování", "Doprovod", "Významné dny"), (("calendar", "Rodinný kalendář"),)),
            ("tasks", "chores", "Domácnost a úkoly", "Úkoly s člověkem a termínem, jednorázové i opakované. Dítě úkol odškrtne, dospělý potvrdí a odměna nebo kapesné se připíše.", ("Kapesné", "Schvalování", "Diktování"), (("chores", "Úkoly pro rodinu"),)),
            ("family", "shopping", "Nákupy", "Jeden seznam, do kterého přidá každý, i hlasem. V obchodě funguje bez signálu a suroviny z jídelníčku do něj pošlete jedním krokem.", ("Offline", "Kategorie", "Jídelníček"), (("shopping", "Nákupní seznam"), ("meals", "Plán jídel"))),
            ("activities", "school", "Škola a kroužky", "Kroužek zapíšete jednou i s místem a platbou. Když tento týden veze někdo jiný, změníte jen ten jeden termín. Na dva závazky jednoho člověka ve stejnou chvíli Rodinka upozorní.", ("Platby", "Rodinná místa", "Kolize v programu"), (("planner", "Rodinný plánovač"),)),
            ("travel", "trips", "Výlety a dovolené", "Tipy, kam se chcete podívat, ukládáte průběžně — stačí vložit odkaz. Z nich složíte plán cesty, rodina hlasuje a vybraný tip se propíše do kalendáře.", ("Hlasování", "Mapa tipů", "Plán cesty"), (("trips", "Rodinné výlety"),)),
            ("memories", "memories", "Rodinné vzpomínky", "Jedna rodinná kronika: dětské milníky, poklady a společné zážitky na časové ose. Z milníku připravíte kartičku k tisku.", ("Milníky", "Poklady", "Kartičky k tisku"), (("memories", "Rodinné vzpomínky"),)),
            ("documents", "documents", "Doklady a důležité věci", "Pasy, občanky, řidičáky i pojištění s datem platnosti. Připomínka přijde s předstihem a doklady vidí jen dospělí.", ("180 · 90 · 30 · 7 dní", "Jen pro dospělé", "Tiché hodiny"), (("documents", "Hlídání platnosti dokladů"),)),
        ),
        "cta": ("Vyberte klidně víc.", "Odpověď v aplikaci nic nezamyká ani neskrývá. Rodinka podle ní jen seřadí první návrhy na obrazovce Dnes."),
    },
    "sk": {
        "kicker": "S ČÍM ZAČAŤ",
        "title": "S čím vám má Rodinka najviac pomáhať?",
        "lead": "Rovnakú otázku vám Rodinka položí hneď po založení rodiny. Sedem oblastí, jedna zdieľaná domácnosť — začnite tou, ktorá vás doma páli najviac.",
        "cards": (
            ("calendar", "calendar", "Rodinný čas a kalendár", "Jeden kalendár pre celú rodinu v zobrazení mesiac, týždeň aj agenda. Pri každej položke vidno, koho sa týka a kto ju zabezpečí. Narodeniny a výročia sa ukážu samy.", ("Opakovanie", "Sprievod", "Významné dni"), (("calendar", "Rodinný kalendár"),)),
            ("tasks", "chores", "Domácnosť a úlohy", "Úlohy s človekom a termínom, jednorazové aj opakované. Dieťa úlohu odškrtne, dospelý potvrdí a odmena alebo vreckové sa pripíše.", ("Vreckové", "Schvaľovanie", "Diktovanie"), (("chores", "Úlohy pre rodinu"),)),
            ("family", "shopping", "Nákupy", "Jeden zoznam, do ktorého pridá každý, aj hlasom. V obchode funguje bez signálu a suroviny z jedálnička doň pošlete jedným krokom.", ("Offline", "Kategórie", "Jedálniček"), (("shopping", "Nákupný zoznam"), ("meals", "Plán jedál"))),
            ("activities", "school", "Škola a krúžky", "Krúžok zapíšete raz aj s miestom a platbou. Keď tento týždeň vezie niekto iný, zmeníte iba ten jeden termín. Na dva záväzky jedného človeka v rovnakom čase vás Rodinka upozorní.", ("Platby", "Rodinné miesta", "Kolízie v programe"), (("planner", "Rodinný plánovač"),)),
            ("travel", "trips", "Výlety a dovolenky", "Tipy, kam sa chcete pozrieť, ukladáte priebežne — stačí vložiť odkaz. Z nich zostavíte plán cesty, rodina hlasuje a vybraný tip sa prenesie do kalendára.", ("Hlasovanie", "Mapa tipov", "Plán cesty"), (("trips", "Rodinné výlety"),)),
            ("memories", "memories", "Rodinné spomienky", "Jedna rodinná kronika: detské míľniky, poklady a spoločné zážitky na časovej osi. Z míľnika pripravíte kartičku na tlač.", ("Míľniky", "Poklady", "Kartičky na tlač"), (("memories", "Rodinné spomienky"),)),
            ("documents", "documents", "Doklady a dôležité veci", "Pasy, občianske preukazy, vodičáky aj poistenie s dátumom platnosti. Pripomienka príde s predstihom a doklady vidia len dospelí.", ("180 · 90 · 30 · 7 dní", "Len pre dospelých", "Tiché hodiny"), (("documents", "Stráženie platnosti dokladov"),)),
        ),
        "cta": ("Vyberte pokojne viac.", "Odpoveď v aplikácii nič nezamyká ani neskrýva. Rodinka podľa nej iba zoradí prvé návrhy na obrazovke Dnes."),
    },
    "en": {
        "kicker": "WHERE TO START",
        "title": "What should Rodinka help you with most?",
        "lead": "Rodinka asks this right after you create your family. Seven areas, one shared household — start with the one that causes the most back-and-forth at home.",
        "cards": (
            ("calendar", "calendar", "Family time and calendar", "One calendar for the whole family in month, week and agenda views. Every entry shows who it is about and who is handling it. Birthdays and holidays appear on their own.", ("Recurring", "Companions", "Special days"), (("calendar", "Family calendar"),)),
            ("tasks", "chores", "Home and chores", "Chores with a person and a due date, one-off or repeating. A child ticks one off, an adult confirms it and the reward or pocket money is credited.", ("Pocket money", "Approval", "Dictation"), (("chores", "Family chores"),)),
            ("family", "shopping", "Shopping", "One list everyone can add to, by voice too. It works in the shop without a signal, and ingredients from the meal plan go onto it in one step.", ("Offline", "Categories", "Meal plan"), (("shopping", "Shopping list"), ("meals", "Meal planning"))),
            ("activities", "school", "School and clubs", "Add an activity once, with its place and payment. When someone else drives this week, change just that one session. Rodinka warns you when one person has two commitments at once.", ("Payments", "Family places", "Clash warnings"), (("planner", "Family planner"),)),
            ("travel", "trips", "Trips and holidays", "Save ideas for places you want to go as they come up — pasting a link is enough. Turn them into a trip plan, let the family vote, and the chosen idea lands in the calendar.", ("Voting", "Idea map", "Trip plans"), (("trips", "Family trips"),)),
            ("memories", "memories", "Family memories", "One family chronicle: children’s milestones, treasures and shared experiences on a timeline. A milestone can become a card you print at home.", ("Milestones", "Treasures", "Printable cards"), (("memories", "Family memories"),)),
            ("documents", "documents", "Documents and important things", "Passports, ID cards, driving licences and insurance with their expiry dates. Reminders arrive well ahead, and only adults can see documents.", ("180 · 90 · 30 · 7 days", "Adults only", "Quiet hours"), (("documents", "Document expiry reminders"),)),
        ),
        "cta": ("Pick as many as you like.", "Your answer in the app never locks or hides anything. Rodinka simply uses it to order the first suggestions on the Today screen."),
    },
}


# The first run as the app ships it (Rodinka/docs/modules/ONBOARDING.md §0):
# who belongs to the family, what it should help with, then the family's own
# portrait. The first entry, invitations and the rest wait for the checklist.
HOME_START = {
    "cs": {
        "kicker": "ZAČÁTEK ZABERE PÁR MINUT",
        "title": "Dvě otázky a Rodinka ví, kdo jste",
        "lead": "Úvodní průvodce se ptá jen na to, co aplikace sama vědět nemůže. První záznam, pozvánky i všechno ostatní počká na chvíli, kdy to budete potřebovat.",
        "steps": (
            ("Kdo do Rodinky patří?", "Přidejte děti, mazlíčka i miminko, které teprve čekáte. Druhého dospělého pozvete odkazem — jméno si vyplní sám."),
            ("S čím vám má Rodinka nejvíc pomáhat?", "Vyberte oblasti, které doma řešíte nejčastěji. Nic se tím nezamyká, jen se podle toho seřadí první návrhy."),
            ("Tohle je vaše Rodinka", "Z členů rodiny se složí její vlastní znak. Na obrazovce Dnes pak čeká krátký seznam nejvýš tří dalších kroků."),
        ),
        "kit": ("Připravené sady místo prázdné obrazovky", "Škola, domácnost, auto nebo doklady: sada ukáže, co by v Rodince vzniklo, a nechá vás to upravit. Nic se nezapíše, dokud to nepotvrdíte."),
        "family": "Novákovi",
        "pet": "Bady",
        "caption": "Znak rodiny se skládá z jejích členů. Každý má svou barvu, dospělí stojí o kousek výš a mazlíček je menší lístek na konci řady.",
    },
    "sk": {
        "kicker": "ZAČIATOK ZABERIE PÁR MINÚT",
        "title": "Dve otázky a Rodinka vie, kto ste",
        "lead": "Úvodný sprievodca sa pýta len na to, čo aplikácia sama vedieť nemôže. Prvý záznam, pozvánky aj všetko ostatné počká na chvíľu, keď to budete potrebovať.",
        "steps": (
            ("Kto do Rodinky patrí?", "Pridajte deti, zvieratko aj bábätko, ktoré ešte čakáte. Druhého dospelého pozvete odkazom — meno si vyplní sám."),
            ("S čím vám má Rodinka najviac pomáhať?", "Vyberte oblasti, ktoré doma riešite najčastejšie. Nič sa tým nezamyká, iba sa podľa toho zoradia prvé návrhy."),
            ("Toto je vaša Rodinka", "Z členov rodiny sa zloží jej vlastný znak. Na obrazovke Dnes potom čaká krátky zoznam najviac troch ďalších krokov."),
        ),
        "kit": ("Pripravené sady namiesto prázdnej obrazovky", "Škola, domácnosť, auto alebo doklady: sada ukáže, čo by v Rodinke vzniklo, a nechá vás to upraviť. Nič sa nezapíše, kým to nepotvrdíte."),
        "family": "Novákovci",
        "pet": "Bady",
        "caption": "Znak rodiny sa skladá z jej členov. Každý má svoju farbu, dospelí stoja o kúsok vyššie a zvieratko je menší lupeň na konci radu.",
    },
    "en": {
        "kicker": "GETTING STARTED TAKES MINUTES",
        "title": "Two questions and Rodinka knows who you are",
        "lead": "The welcome flow only asks what the app cannot work out by itself. The first entry, invitations and everything else wait until you actually need them.",
        "steps": (
            ("Who is in your Rodinka?", "Add your children, a pet, even a baby still on the way. Invite the second adult with a link — they fill in their own name."),
            ("What should Rodinka help you with most?", "Pick the areas your household deals with most. Nothing is locked by it; it only decides which suggestions come first."),
            ("This is your Rodinka", "Your family’s own mark is drawn from its members. On the Today screen a short checklist of no more than three next steps is waiting."),
        ),
        "kit": ("Ready-made kits instead of an empty screen", "School, home, car or documents: a kit shows what it would add to Rodinka and lets you change it first. Nothing is saved until you confirm."),
        "family": "Nováks",
        "pet": "Bady",
        "caption": "The family mark is made of its members. Everyone has their own colour, adults stand a little taller, and a pet is a smaller petal at the end of the row.",
    },
}


# The layer beyond the core utilities. Claims are limited to what the app does
# today: Rodinka Today has no streak, score or leaderboard by design, and Moment
# dne needs a per-family entitlement granted by hand, so it is not marketed.
# Card: (tone, glyph, title, text, page).
HOME_FAMILY_LAYER = {
    "cs": {
        "kicker": "RODINA NENÍ JEN PROVOZ DOMÁCNOSTI",
        "title": "Kromě toho, co je potřeba zařídit",
        "lead": "Kalendář, úkoly a nákupy řeší provoz. Rodinka k nim přidává věci, kvůli kterým ji otevřete rádi — a pár těch, na které se jinak zapomíná.",
        "cards": (
            ("memories", "sparkle", "Každý den malý důvod být spolu", "Dnešní Rodinka nabídne jednu otázku pro celou rodinu, krátké hlasování, hádanku nebo vzpomínku z minulých let. Není to povinnost: žádné série, body ani žebříčky.", "memories"),
            ("tasks", "child", "Děti mají vlastní Rodinku", "Přihlášení bez e-mailu, vlastní úkoly, nákupní seznam a kalendář. Za splněné úkoly odměna nebo kapesné — a pak pět rodinných her, které fungují i offline.", "chores"),
            ("calendar", "chat", "Domluva u toho, čeho se týká", "Rodinný chat i přímé zprávy. Do konverzace pošlete konkrétní úkol, nákup nebo událost a ze zprávy rovnou vytvoříte úkol.", "app"),
            ("health", "health", "Zdraví a mazlíčci", "Prohlídky, očkování a další dávky celé rodiny s včasnou připomínkou. Mazlíček má vlastní profil, péči i veterinární historii. Slouží k plánování, ne ke zdravotní dokumentaci.", "app"),
        ),
    },
    "sk": {
        "kicker": "RODINA NIE JE LEN PREVÁDZKA DOMÁCNOSTI",
        "title": "Okrem toho, čo treba zariadiť",
        "lead": "Kalendár, úlohy a nákupy riešia prevádzku. Rodinka k nim pridáva veci, kvôli ktorým ju otvoríte radi — a zopár tých, na ktoré sa inak zabúda.",
        "cards": (
            ("memories", "sparkle", "Každý deň malý dôvod byť spolu", "Dnešná Rodinka ponúkne jednu otázku pre celú rodinu, krátke hlasovanie, hádanku alebo spomienku z minulých rokov. Nie je to povinnosť: žiadne série, body ani rebríčky.", "memories"),
            ("tasks", "child", "Deti majú vlastnú Rodinku", "Prihlásenie bez e-mailu, vlastné úlohy, nákupný zoznam a kalendár. Za splnené úlohy odmena alebo vreckové — a potom päť rodinných hier, ktoré fungujú aj offline.", "chores"),
            ("calendar", "chat", "Dohoda pri tom, čoho sa týka", "Rodinný chat aj priame správy. Do konverzácie pošlete konkrétnu úlohu, nákup alebo udalosť a zo správy rovno vytvoríte úlohu.", "app"),
            ("health", "health", "Zdravie a zvieratká", "Prehliadky, očkovania a ďalšie dávky celej rodiny s včasnou pripomienkou. Zvieratko má vlastný profil, starostlivosť aj veterinárnu históriu. Slúži na plánovanie, nie na zdravotnú dokumentáciu.", "app"),
        ),
    },
    "en": {
        "kicker": "A FAMILY IS MORE THAN LOGISTICS",
        "title": "Beyond the things that simply need doing",
        "lead": "A calendar, chores and shopping keep a household running. Rodinka adds the things you open it for gladly — and a few that are otherwise easy to forget.",
        "cards": (
            ("memories", "sparkle", "A small reason to be together each day", "Rodinka Today offers one question for the whole family, a short vote, a riddle or a memory from earlier years. It is not a task: no streaks, points or leaderboards.", "memories"),
            ("tasks", "child", "Children get their own Rodinka", "A sign-in without an email address, their own chores, the shopping list and the calendar. A reward or pocket money for finished chores — then five family games that work offline too.", "chores"),
            ("calendar", "chat", "Talk next to what it is about", "A family chat and direct messages. Share a specific chore, shopping item or event into the conversation, and turn a message into a chore in one step.", "app"),
            ("health", "health", "Health and pets", "Check-ups, vaccinations and next doses for the whole family, with a timely reminder. A pet gets its own profile, care routines and vet history. It is for planning, not medical records.", "app"),
        ),
    },
}


# The trip plan drawn next to the trips story and on the trips page. Wording
# follows Rodinka/src/strings/tripPlans.ts; the places are illustrative.
TRIP_MOCK = {
    "cs": {
        "kicker": "Plán cesty",
        "title": "Podzimní víkend",
        "pills": ("17.–18. 10.", "Vysočina", "Připnuto na Dnes"),
        "note": "Vezmeme i Badyho?",
        "tips": (("Hrad Pernštejn", "Nedvědice", (3, 1, 0)), ("Rozhledna Harusův kopec", "Nové Město na Moravě", (2, 1, 1)), ("Zoo Jihlava", "Jihlava", (1, 2, 1))),
        "selected": "Vybráno",
        "caption": "Plán cesty: termín, oblast, tipy a hlasování celé rodiny. Vybraný tip se propíše do rodinného kalendáře.",
    },
    "sk": {
        "kicker": "Plán cesty",
        "title": "Jesenný víkend",
        "pills": ("17.–18. 10.", "Liptov", "Pripnuté na Dnes"),
        "note": "Vezmeme aj Badyho?",
        "tips": (("Hrad Likava", "Ružomberok", (3, 1, 0)), ("Demänovská jaskyňa slobody", "Demänovská Dolina", (2, 1, 1)), ("Tatralandia", "Liptovský Mikuláš", (1, 2, 1))),
        "selected": "Vybrané",
        "caption": "Plán cesty: termín, oblasť, tipy a hlasovanie celej rodiny. Vybraný tip sa prenesie do rodinného kalendára.",
    },
    "en": {
        "kicker": "Trip plan",
        "title": "Autumn weekend",
        "pills": ("17–18 Oct", "Vysočina", "Pinned to Today"),
        "note": "Shall we bring Bady?",
        "tips": (("Pernštejn Castle", "Nedvědice", (3, 1, 0)), ("Harusův kopec lookout", "Nové Město na Moravě", (2, 1, 1)), ("Jihlava Zoo", "Jihlava", (1, 2, 1))),
        "selected": "Chosen",
        "caption": "A trip plan: dates, area, ideas and the whole family’s votes. The chosen idea becomes an event in the family calendar.",
    },
}


HOME_TRIPS_STORY = {
    "cs": {
        "kicker": "VÝLETY A DOVOLENÉ",
        "title": "Kam pojedeme? Rozhodne celá rodina.",
        "text": "Tipy na výlety ukládáte průběžně — stačí vložit odkaz a Rodinka si z něj vezme název i náhled. Když přijde volný víkend, složíte z tipů plán cesty, každý dá svůj hlas a vybraný tip se propíše do kalendáře.",
        "points": ("Zásobník nápadů v kartách i na mapě.", "Plán cesty připnete na obrazovku Dnes.", "Po návratu klepnete na Byli jsme a z výletu je vzpomínka.", "A než vyrazíte, děti si zahrají Nacpi kufr."),
        "link": "Rodinné výlety",
    },
    "sk": {
        "kicker": "VÝLETY A DOVOLENKY",
        "title": "Kam pôjdeme? Rozhodne celá rodina.",
        "text": "Tipy na výlety ukladáte priebežne — stačí vložiť odkaz a Rodinka si z neho vezme názov aj náhľad. Keď príde voľný víkend, zostavíte z tipov plán cesty, každý dá svoj hlas a vybraný tip sa prenesie do kalendára.",
        "points": ("Zásobník nápadov v kartách aj na mape.", "Plán cesty pripnete na obrazovku Dnes.", "Po návrate ťuknete na Boli sme a z výletu je spomienka.", "A kým vyrazíte, deti si zahrajú Napchaj kufor."),
        "link": "Rodinné výlety",
    },
    "en": {
        "kicker": "TRIPS AND HOLIDAYS",
        "title": "Where shall we go? The whole family decides.",
        "text": "Save trip ideas as they come up — paste a link and Rodinka picks up the title and a preview. When a free weekend arrives, turn a few ideas into a trip plan, everyone casts a vote, and the chosen idea lands in the calendar.",
        "points": ("An idea backlog as cards or on a map.", "Pin the trip plan to the Today screen.", "Back home, tap Been there and the trip becomes a memory.", "And before you leave, the kids can play Pack the Trunk."),
        "link": "Family trips",
    },
}


HOME_TRUST = {
    "cs": {
        "kicker": "SOUKROMÍ A SPOLEHLIVOST",
        "title": "Rodinné věci patří rodině",
        "lead": "Rodinka je postavená pro skutečný provoz: s dětmi, se slabým signálem i s údaji, které nepatří nikomu dalšímu.",
        "items": (
            ("lock", "Každá rodina má uzavřený prostor", "Data jednotlivých domácností jsou oddělená už v databázi. Sdílení mezi rodinami neexistuje."),
            ("shield", "Děti vidí jen to, co mají", "Dětský účet nevidí doklady ani správu rodiny — a to nejen v rozhraní, ale ani v databázi."),
            ("image", "Fotky v soukromém úložišti", "Fotografie a skeny se členům rodiny zobrazují jen přes dočasné zabezpečené odkazy."),
            ("offline", "Funguje i bez signálu", "Dnes, kalendář, úkoly a nákup jdou měnit i offline a změny se po připojení dorovnají. Jídelníček, vzpomínky a tipy na výlety si přečtete i bez připojení."),
            ("bell", "Připomínky, které respektují noc", "Každý si nastaví tiché hodiny, kategorie připomínek i denní nebo týdenní souhrn."),
            ("languages", "Česky, slovensky i anglicky", "Rozhraní je ve třech jazycích, ve světlém i tmavém vzhledu, na mobilu, tabletu i počítači."),
        ),
    },
    "sk": {
        "kicker": "SÚKROMIE A SPOĽAHLIVOSŤ",
        "title": "Rodinné veci patria rodine",
        "lead": "Rodinka je postavená na skutočnú prevádzku: s deťmi, so slabým signálom aj s údajmi, ktoré nepatria nikomu ďalšiemu.",
        "items": (
            ("lock", "Každá rodina má uzavretý priestor", "Dáta jednotlivých domácností sú oddelené už v databáze. Zdieľanie medzi rodinami neexistuje."),
            ("shield", "Deti vidia len to, čo majú", "Detský účet nevidí doklady ani správu rodiny — a to nielen v rozhraní, ale ani v databáze."),
            ("image", "Fotky v súkromnom úložisku", "Fotografie a skeny sa členom rodiny zobrazujú len cez dočasné zabezpečené odkazy."),
            ("offline", "Funguje aj bez signálu", "Dnes, kalendár, úlohy a nákup sa dajú meniť aj offline a zmeny sa po pripojení dorovnajú. Jedálniček, spomienky a tipy na výlety si prečítate aj bez pripojenia."),
            ("bell", "Pripomienky, ktoré rešpektujú noc", "Každý si nastaví tiché hodiny, kategórie pripomienok aj denný alebo týždenný súhrn."),
            ("languages", "Po česky, slovensky aj anglicky", "Rozhranie je v troch jazykoch, vo svetlom aj tmavom vzhľade, v mobile, tablete aj počítači."),
        ),
    },
    "en": {
        "kicker": "PRIVACY AND RELIABILITY",
        "title": "Family matters stay in the family",
        "lead": "Rodinka is built for real households: with children, patchy signal and details that belong to nobody else.",
        "items": (
            ("lock", "Every family has its own closed space", "Each household’s data is separated in the database itself. There is no sharing between families."),
            ("shield", "Children see only what is theirs", "A child account cannot see documents or family administration — not in the interface, and not in the database either."),
            ("image", "Photos in private storage", "Photos and scans are shown to family members only through temporary secured links."),
            ("offline", "Works without a signal", "Today, the calendar, chores and shopping can be changed offline and catch up once you reconnect. The meal plan, memories and trip ideas stay readable without a connection."),
            ("bell", "Reminders that respect the night", "Everyone sets their own quiet hours, reminder categories and a daily or weekly digest."),
            ("languages", "Czech, Slovak and English", "The interface comes in three languages, in light and dark themes, on phones, tablets and computers."),
        ),
    },
}


HOME = {
    "cs": {
        "title": "Rodinka – rodinný plánovač, kalendář, úkoly a nákupy",
        "description": "Rodinný plánovač pro celou domácnost: sdílený kalendář, úkoly, nákupy a jídla, k tomu výlety, vzpomínky i hlídání dokladů. Na mobilu i počítači.",
        "og_title": "Rodinka: rodinný život přehledně na jednom místě",
        "og_description": "Společný kalendář, úkoly, nákupy, jídla, výlety i vzpomínky pro celou rodinu. Méně hledání v chatu, víc společného přehledu.",
        "og_alt": "Rodinka – rodinný plánovač s kalendářem, úkoly, nákupy a jídly",
        "eyebrow": "Rodinný organizér pro celou domácnost",
        "h1": "Rodinný plánovač, který drží domácnost pohromadě.",
        "lead": "Společný kalendář, úkoly, nákupy a jídla pro oba rodiče — a k tomu výlety, vzpomínky a doklady, na které se jinak zapomíná. Děti mají vlastní přihlášení a Rodinka běží na mobilu i počítači.",
        "how_link": "Podívat se, jak začít",
        "proof": ("Bez platební karty", "Na mobilu i počítači", "Nákup i bez signálu"),
        "trust_title": "Jedna domácnost, jeden přehled.",
        "trust_text": "Založíte rodinu a druhého dospělého pozvete odkazem.",
        "directory_kicker": "VŠECHNA TÉMATA",
        "directory_title": "Průvodce podle toho, co doma řešíte",
        "directory_lead": "Každá stránka popisuje jednu oblast Rodinky: jak funguje, komu pomáhá a na co se lidé nejčastěji ptají.",
        "quote": "Rodinka není o dokonale zorganizovaném životě. Je o tom, aby organizování neleželo jen na jednom člověku.",
        "quote_by": "Vytvořeno pro skutečné domácnosti",
        "cta_kicker": "MŮŽETE ZAČÍT HNED",
        "cta_title": "Dejte rodinnému chaosu jedno společné místo.",
        "cta_text": "Otevřete Rodinku v prohlížeči, řekněte, kdo do rodiny patří a s čím má pomáhat. Instalace není podmínkou.",
        "login": "Už mám účet",
        "journey": (("1. Kdo do Rodinky patří", "Děti, druhý dospělý, mazlíček."), ("2. S čím má pomáhat", "Podle toho seřadíme první kroky."), ("3. Tohle je vaše Rodinka", "Znak rodiny a pár návrhů na Dnes.")),
        "install_title": "Chcete Rodinku jako aplikaci ve Windows?",
        "install_text": "Microsoft Store je alternativní způsob instalace. Na mobilu si webovou verzi přidáte na plochu jako aplikaci.",
        "store": "Otevřít Microsoft Store",
        "fine_print": "Bez platební karty. Funguje na mobilu i počítači.",
    },
    "sk": {
        "title": "Rodinka – rodinný plánovač, kalendár, úlohy a nákupy",
        "description": "Rodinný plánovač pre celú domácnosť: zdieľaný kalendár, úlohy, nákupy a jedlá, k tomu výlety, spomienky aj stráženie dokladov. V mobile aj počítači.",
        "og_title": "Rodinka: spoločný prehľad pre každodenný rodinný život",
        "og_description": "Kalendár, úlohy, nákupy, jedlá, výlety aj spomienky pre celú rodinu. Menej hľadania v správach, viac spoločného prehľadu.",
        "og_alt": "Rodinka – rodinný plánovač s kalendárom, úlohami, nákupmi a jedlami",
        "eyebrow": "Rodinný organizér pre celú domácnosť",
        "h1": "Rodinný plánovač, ktorý drží domácnosť pokope.",
        "lead": "Spoločný kalendár, úlohy, nákupy a jedlá pre oboch rodičov — a k tomu výlety, spomienky a doklady, na ktoré sa inak zabúda. Deti majú vlastné prihlásenie a Rodinka beží v mobile aj počítači.",
        "how_link": "Pozrieť sa, ako začať",
        "proof": ("Bez platobnej karty", "V mobile aj počítači", "Nákup aj bez signálu"),
        "trust_title": "Jedna domácnosť, jeden prehľad.",
        "trust_text": "Založíte rodinu a druhého dospelého pozvete odkazom.",
        "directory_kicker": "VŠETKY TÉMY",
        "directory_title": "Sprievodca podľa toho, čo doma riešite",
        "directory_lead": "Každá stránka opisuje jednu oblasť Rodinky: ako funguje, komu pomáha a na čo sa ľudia najčastejšie pýtajú.",
        "quote": "Rodinka nie je o dokonale zorganizovanom živote. Je o tom, aby organizovanie neležalo iba na jednom človeku.",
        "quote_by": "Vytvorené pre skutočné domácnosti",
        "cta_kicker": "MÔŽETE ZAČAŤ HNEĎ",
        "cta_title": "Dajte rodinnému chaosu jedno spoločné miesto.",
        "cta_text": "Otvorte Rodinku v prehliadači, povedzte, kto do rodiny patrí a s čím má pomáhať. Inštalácia nie je podmienkou.",
        "login": "Už mám účet",
        "journey": (("1. Kto do Rodinky patrí", "Deti, druhý dospelý, zvieratko."), ("2. S čím má pomáhať", "Podľa toho zoradíme prvé kroky."), ("3. Toto je vaša Rodinka", "Znak rodiny a pár návrhov na Dnes.")),
        "install_title": "Chcete Rodinku ako aplikáciu vo Windows?",
        "install_text": "Microsoft Store je alternatívny spôsob inštalácie. V mobile si webovú verziu pridáte na plochu ako aplikáciu.",
        "store": "Otvoriť Microsoft Store",
        "fine_print": "Bez platobnej karty. Funguje v mobile aj počítači.",
    },
    "en": {
        "title": "Rodinka – family planner, calendar, chores and shopping",
        "description": "A family planner for the whole household: a shared calendar, chores, shopping and meals, plus trips, memories and document expiry tracking. On phones and computers.",
        "og_title": "Rodinka: one shared place for everyday family life",
        "og_description": "A family calendar, chores, shopping, meals, trips and memories in one calm shared view — with fewer details lost in chat.",
        "og_alt": "Rodinka family organizer with a calendar, chores, shopping list and meals",
        "eyebrow": "A family organizer for the whole household",
        "h1": "A family organizer that keeps home life together.",
        "lead": "A shared calendar, chores, shopping and meals for both parents — plus trips, memories and documents that otherwise slip. Children get their own sign-in, and Rodinka runs on phones and computers.",
        "how_link": "See how to start",
        "proof": ("No payment card", "Phone and computer", "Shopping without a signal"),
        "trust_title": "One household, one clear view.",
        "trust_text": "Create your family and invite the other adult with a link.",
        "directory_kicker": "EVERY TOPIC",
        "directory_title": "A guide to what your household deals with",
        "directory_lead": "Each page covers one area of Rodinka: how it works, who it helps and the questions people ask most.",
        "quote": "Rodinka is not about a perfectly organized life. It is about making sure the organizing does not sit with just one person.",
        "quote_by": "Made for real households",
        "cta_kicker": "YOU CAN START RIGHT AWAY",
        "cta_title": "Give family chaos one shared home.",
        "cta_text": "Open Rodinka in your browser, say who is in your family and what it should help with. You do not have to install anything.",
        "login": "I already have an account",
        "journey": (("1. Who is in your Rodinka", "Children, the other adult, a pet."), ("2. What it should help with", "We order the first steps by it."), ("3. This is your Rodinka", "Your family mark and a few ideas for Today.")),
        "install_title": "Would you like Rodinka as a Windows app?",
        "install_text": "Microsoft Store is another way to install Rodinka. On a phone, add the web version to your home screen like an app.",
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
            "steps": (("Přidejte událost", "Zapište čas, místo a člena rodiny, kterého se událost týká. U pravidelného kroužku nastavte opakování."), ("Oddělte, koho se to týká, od toho, kdo to zajišťuje", "U události je zvlášť vidět účastník — třeba dítě, které jde na plavání — a zvlášť dospělý, který ho tam doveze. Jsou to dvě různé informace a Rodinka je nesbaluje do jedné."), ("Kontrolujte společný týden", "Přepnete si měsíc, týden nebo agendu podle naléhavosti. Při plánování vlastního programu oba rodiče vidí stejné rodinné závazky."), ("Nechte důležité dny přijít samy", "Narozeniny a jmeniny členů rodiny, výročí, vlastní dny i státní svátky se v kalendáři ukazují jako tichá vrstva, která neblokuje čas. Na ty důležité vám Rodinka může připomenout s předstihem.")),
            "answers_title": "Co lidé hledají u rodinného kalendáře",
            "answers": (("Jak sdílet rodinný kalendář mezi rodiči?", "Vytvořte jeden rodinný prostor a pozvěte druhého dospělého. Události zapisujte tam, ne do dvou oddělených kalendářů, a doplňte i informaci o doprovodu, pokud je pro plán důležitá."), ("Jak zorganizovat kroužky dětí?", "U každého kroužku evidujte den, čas, místo, dítě a dopravu. Pravidelné termíny nastavte jako opakované a výjimky upravujte jednotlivě, aby zůstal týdenní plán čitelný."), ("Co když jeden týden veze dítě někdo jiný?", "Změníte doprovod jen u toho jednoho termínu. Opakovaná aktivita zůstane nedotčená, takže kvůli jedné výjimce nemusíte rozbíjet celou sérii ani ji zakládat znovu."), ("Patří do rodinného kalendáře i úkoly?", "Událost říká, kdy se něco děje. Přípravu — třeba koupit dárek nebo odevzdat přihlášku — je lepší vést jako samostatný úkol s termínem a odpovědnou osobou."), ("Upozorní kalendář na kolizi?", "Ano, když by jeden člen rodiny měl dva závazky ve stejnou dobu — třeba kroužek a lékaře. Dvě děti na dvou kroužcích najednou kolize nejsou, pokud každé veze někdo jiný. Upozornění nikdy nebrání uložení.")),
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
            "scenarios": (("Něco právě došlo", "Poslední mléko nebo prací gel se zapíše hned, ne až při vzpomínání před obchodem."), ("V obchodě bez signálu", "Seznam funguje, i když telefon signál nechytá. Odškrtnuté položky se dorovnají, jakmile se připojení vrátí."), ("Nakupuje někdo jiný", "Partner cestou z práce otevře stejný seznam a nemusí si vyžádat novou zprávu.")),
            "help_title": "Jak mít společný nákupní seznam v Rodince",
            "help_intro": "Seznam je součástí rodinného prostoru, takže ho vidí pozvaní členové domácnosti na mobilu i počítači.",
            "steps": (("Přidávejte průběžně — psaním i hlasem", "Zapište položku ve chvíli, kdy doma dochází. Na podporovaných zařízeních nemusíte psát: řekněte, co chybí, a Rodinka z toho připraví položky, které před přidáním ještě uvidíte a můžete upravit."), ("Nakupujte ze stejné verze, i bez signálu", "V obchodě položky odškrtávejte. Ostatní vidí, co je hotové, a nepřidávají stejné věci podruhé. Seznam funguje i offline a změny se dorovnají po návratu připojení."), ("Propojte nákup s jídlem", "Při plánování večeří doplňte potřebné suroviny, aby týdenní jídelníček nezůstal jen přáním.")),
            "answers_title": "Praktické otázky ke společnému nákupu",
            "answers": (("Jak sdílet nákupní seznam s partnerem?", "Používejte jeden seznam ve společném rodinném prostoru. Oba do něj mohou přidávat a při nákupu odškrtávat, takže není potřeba posílat pokaždé novou verzi."), ("Je lepší seznam v aplikaci, nebo na papíře?", "Papír je rychlý, když u něj právě stojíte. Sdílený seznam je ale dostupný i mimo domov a může ho aktualizovat více lidí. Pro domácnost, kde se v nákupech střídáte, bývá praktičtější."), ("Dá se nákupní seznam nadiktovat?", "Na podporovaných zařízeních ano. Řeknete, co chybí, Rodinka z toho připraví jednotlivé položky a ukáže je k potvrzení — teprve pak se přidají do seznamu. Rozpoznané položky můžete před přidáním upravit nebo smazat a nahrávka ani přepis se nikam neukládají."), ("Funguje seznam i bez signálu?", "Ano. Nákupní seznam je navržený tak, aby šel používat offline: v obchodě přidáváte i odškrtáváte položky dál a změny se dorovnají, jakmile se telefon připojí.")),
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
            "scenarios": (("Drobné denní povinnosti", "Koš, nádobí nebo příprava aktovky mohou mít jednoduché a srozumitelné zadání."), ("Neviditelná organizace", "Telefonát lékaři, platba kroužku nebo nákup dárku dostanou vlastníka i termín."), ("Úkoly pro děti", "Dítě může mít vlastní přihlášení a v něm jen svoje úkoly. K úkolu lze přidat odměnu nebo kapesné a splnění potvrdí dospělý.")),
            "help_title": "Jak rozdělit domácí úkoly mezi členy rodiny",
            "help_intro": "Rodinka pomáhá převést neurčité povinnosti na malé konkrétní kroky, které jsou vidět ve společném přehledu.",
            "steps": (("Pojmenujte výsledek", "Místo „řešit školu“ napište konkrétně „odeslat přihlášku na výlet“. Každý hned ví, co znamená hotovo."), ("Přiřaďte člověka a termín", "Úkol nemá zůstat společný tak dlouho, až ho udělá ten nejvšímavější. Domluvte odpovědnost rovnou."), ("Opakujte, co se opakuje", "Vynést koš každé úterý nastavíte jednou. Jednorázová poznámka bez termínu i pravidelná povinnost jsou přitom stejný typ úkolu."), ("Nechte hotové věci zmizet z hlavy", "Splnění je vidět ostatním. U úkolů s odměnou ho dospělý potvrdí a částka se dítěti připíše.")),
            "answers_title": "Otázky k domácím úkolům a povinnostem",
            "answers": (("Jak rozdělit domácí práce spravedlivě?", "Nezačínejte jen viditelným úklidem. Sepište i plánování, telefonáty a hlídání termínů. Rozdělení pak posuzujte podle času a zátěže, ne pouze podle počtu položek."), ("Jak zadávat úkoly dětem?", "Úkol má odpovídat věku, být konkrétní a mít dosažitelný termín. Menším dětem pomůže krátké zadání a společná kontrola; cílem je návyk a zapojení, ne dokonalost."), ("Jak připomínat úkoly bez hádek?", "Dohodněte odpovědnost a zapište ji na společné místo. Připomínka pak neznamená, že jeden rodič druhého řídí; oba se mohou opřít o stejnou dohodu."), ("Jak fungují odměny a kapesné za úkoly?", "K úkolu můžete přidat odměnu a vyžadovat schválení dospělým. Dítě úkol odškrtne, rodič potvrdí splnění a částka se připíše. Pravidelné kapesné může být podmíněné tím, že jsou domluvené úkoly hotové."), ("Dá se rychlý úkol nadiktovat?", "Na podporovaných zařízeních ano — přímo na obrazovce Dnes. Řeknete, co je potřeba udělat, Rodinka z toho připraví návrhy úkolů a ukáže je k úpravě. Nic nevznikne dřív, než potvrdíte.")),
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
            "steps": (("Podívejte se na rodinný kalendář", "Nejdřív zvažte, které dny jsou dlouhé a kdy bude někdo doma dřív. Plán pak vychází z reálného času."), ("Vyberte několik jistých jídel", "Nemusíte vyplnit každý chod. Jídla, která běžně vaříte, si uložte do knihovny a příště je vyberete jedním klepnutím."), ("Nechte rodinu rozhodnout", "Když se doma nemůžete shodnout, vypište pár možností a nechte o víkendovém obědě hlasovat. Hlasovat můžou i děti."), ("Pošlete suroviny do nákupu", "U naplánovaného jídla přenesete potřebné suroviny do sdíleného nákupního seznamu jedním krokem, takže se nepřepisují ručně.")),
            "answers_title": "Časté otázky k plánování rodinného jídla",
            "answers": (("Jak plánovat jídlo na celý týden?", "Začněte rodinným programem a vyberte hlavní jídla podle času na přípravu. Neplánujte příliš těsně; jeden volný večer pomůže využít zbytky nebo reagovat na změnu."), ("Jak zapojit rodinu do výběru jídel?", "V Rodince můžete otevřít hlasování o jídle: vypíšete možnosti a každý člen rodiny včetně dětí dá svůj hlas. Rozhodnutí tak není na jednom člověku a plán má větší šanci, že bude fungovat."), ("Jak propojit jídelníček s nákupním seznamem?", "U každého plánovaného jídla projděte hlavní suroviny a chybějící přidejte do společného seznamu. Před nákupem ještě zkontrolujte zásoby, aby se věci zbytečně nedublovaly.")),
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
            "help_intro": "Rodinka není jen kalendář s úkoly. Níže jsou tři vrstvy, ze kterých se skládá — používáte z nich jen to, co vaší domácnosti dává smysl.",
            "steps": (("Každodenní provoz", "Obrazovka Dnes s programem, denní linkou a tím, co potřebuje pozornost. Sdílený kalendář s opakovanými aktivitami a doprovodem, úkoly s vlastníkem a termínem, nákupní seznam fungující i offline a jídelníček s rodinným hlasováním."), ("Rodina, ne jen logistika", "Vzpomínky s dětskými milníky, poklady a společnými zážitky, Dnešní Rodinka s otázkou nebo hlasováním pro celou domácnost, tipy a plány výletů, dětské účty s vlastními úkoly a kapesným, pět rodinných her a rodinný chat."), ("Věci, na které se zapomíná", "Připomínky s tichými hodinami, doklady s hlídáním platnosti, zdravotní termíny a očkování, mazlíčci s veterinární historií, narozeniny a významné dny, rodinná místa s navigací a Miminko na cestě.")),
            "answers_title": "Jak vybírat aplikaci pro rodinu",
            "answers": (("Co by měla aplikace pro rodinu umět?", "Měla by pokrýt nejčastější společné situace, být rychlá na mobilu i počítači a dovolit více členům pracovat se stejnými aktuálními informacemi."), ("Nahradí Rodinka rodinný chat?", "Ne. Chat je skvělý pro rozhovor. Rodinka slouží jako přehled pro termíny, úkoly a seznamy, které potřebujete najít i později bez procházení historie zpráv."), ("Musí rodina začít používat všechny funkce?", "Nemusí. Nejpraktičtější je začít jednou oblastí, která dnes způsobuje nejvíce dotazů. Další části přidejte až tehdy, když domácnosti opravdu pomohou."), ("Funguje Rodinka bez internetu?", "Z velké části ano. Dnes, kalendář, úkoly a nákupní seznam jdou používat i měnit offline a změny se po připojení dorovnají. Jídelníček, vzpomínky nebo tipy na výlety si přečtete; zprávy a zdravotní záznamy potřebují připojení.")),
            "card": "Kalendář, povinnosti, nákupní seznam a jídla v jednom rodinném prostoru.",
            "cta_title": "Dejte rodinným informacím jedno známé místo.",
            "cta_text": "Rodinka funguje rovnou v prohlížeči. Vytvořte rodinu a začněte první praktickou věcí.",
        },
        "baby": {
            "title": "Příprava na miminko společně | Rodinka",
            "description": "Připravujte se na miminko společně. Orientační cesta po týdnech, praktické přípravy a výběr jména v rodinném plánovači Rodinka.",
            "og_title": "Čekáte miminko? Připravíme se spolu.",
            "og_description": "Cesta po týdnech, praktické přípravy i společný výběr jména v jednom rodinném prostoru.",
            "og_alt": "Miminko na cestě v Rodince s přehledem příprav a výběrem jména",
            "eyebrow": "MIMINKO NA CESTĚ",
            "h1": "Čekáte miminko? Připravíme se spolu.",
            "lead": "Cesta po týdnech, praktické přípravy i společný výběr jména. Rodinka pomůže držet věci pohromadě ještě předtím, než se nový člen rodiny narodí.",
            "problem_title": "Přípravy snadno skončí v poznámkách, chatu a několika seznamech",
            "problem": ("Něco je v poznámkách, nákupy na jiném seznamu a důležitou drobnost si pamatuje jen jeden rodič. Kandidátní jména mezitím mizí mezi běžnými zprávami a není jasné, co už je připravené.", "Společný prostor nepřidává další povinný plán. Dává oběma rodičům klidné místo pro věci, které chtějí před příchodem miminka řešit společně a vlastním tempem."),
            "scenarios": (("Seznamy na několika místech", "Výbava na cesty, spaní nebo první dny nemusí být rozdělená mezi papír, poznámky a chat."), ("Jména v chatu", "Nápady na jména zůstávají pohromadě s preferencemi zapojených dospělých."), ("Co už je připravené?", "Oba rodiče vidí stejný přehled a mohou navázat tam, kde ten druhý skončil.")),
            "help_title": "Jak Rodinka pomůže s přípravou na miminko",
            "help_intro": "Miminko na cestě je organizační část Rodinky, ne zdravotní aplikace. Nabízí lehkou orientaci a praktický prostor pro společné přípravy.",
            "steps": (("Cesta po týdnech", "Orientační týden, jednoduchý průběh a vybrané momenty pomohou zasadit přípravy do času. Nejde o medicínské měření ani hodnocení zdravotního stavu."), ("Přípravy podle témat", "Inspiraci najdete v oblastech na cesty, spaní, krmení a kojení, hygiena a přebalování, oblečení, doma, porodnice a první dny nebo administrativa. Z položky checklistu navíc uděláte běžný úkol, nákup nebo událost, takže příprava nezůstane v odděleném seznamu."), ("Jména, která řešíte spolu", "Zapisujte si kandidátní jména, označte favority a sdílejte preference jako líbí se mi, možná nebo spíš ne. Nejde o soutěž ani skóre.")),
            "answers_title": "Časté otázky k přípravě na miminko",
            "answers": (("Je Rodinka těhotenská aplikace?", "Ne. Rodinka nenahrazuje zdravotní aplikaci ani doporučení lékaře. Pomáhá rodině s orientační cestou a praktickou organizací příprav."), ("Musíme použít celý checklist?", "Nemusíte. Seznam je inspirace a přehled, ne povinný nákupní plán. Každá rodina si ponechá jen to, co odpovídá jejím potřebám."), ("Můžeme společně vybírat jméno?", "Ano. Můžete si vést kandidátní jména, označit favority a u každého zachytit preference zapojených dospělých bez vyhlašování vítěze."), ("Uvidí informace automaticky děti?", "Ne. Část Miminko na cestě je určená dospělým v rodině, takže přípravy a citlivé informace zůstávají v jejich společném prostoru.")),
            "card": "Cesta po týdnech, praktické přípravy a společný výběr jména na jednom místě.",
            "cta_title": "Připravujte se na nového člena rodiny společně.",
            "cta_text": "Otevřete Rodinku, přidejte Miminko na cestě a začněte tím, co chcete mít připravené jako první.",
        },
        "memories": {
            "title": "Rodinné vzpomínky a dětské milníky na jednom místě | Rodinka",
            "description": "Dětské milníky, rodinné poklady a fotografie na jedné časové ose. Vzpomínku přiřadíte členovi rodiny a z milníku si můžete vytisknout kartičku.",
            "og_title": "Rodinné vzpomínky, které nezapadnou v galerii telefonu",
            "og_description": "Jedna společná kronika rodiny: dětské milníky, poklady a okamžiky, ke kterým se chcete vracet.",
            "og_alt": "Rodinné vzpomínky a dětské milníky v aplikaci Rodinka",
            "eyebrow": "RODINNÁ PAMĚŤ",
            "h1": "Rodinné vzpomínky a dětské milníky, které nezapadnou",
            "lead": "První krok, vysvědčení, kamínek z dovolené i fotka, u které se pokaždé smějete. Většina těchhle věcí skončí v galerii telefonu jednoho rodiče mezi tisíci dalšími snímky. Rodinka jim dává společné místo, kde je najde celá rodina.",
            "problem_title": "Vzpomínky se neztrácejí naráz, ale postupně",
            "problem": ("Fotek přibývá rychleji, než stíháme třídit. Za dva roky se k prvnímu kroku nedostanete přes dovolenou, Vánoce a stovky náhodných snímků — a příběh k té fotce zná jen ten, kdo ji vyfotil. Druhý rodič často nemá přístup vůbec.", "Rodinná paměť nepotřebuje další galerii. Potřebuje pár vět u fotky, datum, jméno člověka, kterého se to týká, a jedno místo, kam se dá vrátit. Rodinka proto vede vzpomínky jako společnou kroniku, ne jako úložiště souborů."),
            "scenarios": (("Dětské milníky", "První krok, první slovo, první den ve škole. Zapíšete, co se stalo a kdy, a přidáte fotku."), ("Rodinné poklady", "Obrázek, mušle z výletu nebo dopis od babičky. Fotografie, krátký popis a datum z nich udělají exponát rodinné sbírky."), ("Společné zážitky", "Výlet do zoo nebo obyčejný večer doma. Rodinné vzpomínce stačí pár vět, datum a klidně jedna fotka — a vznikne i z výletu nebo události v kalendáři.")),
            "help_title": "Jak Rodinka vede rodinné vzpomínky",
            "help_intro": "Vzpomínky jsou jedna sekce, ne rozcestník. Milníky, poklady i společné zážitky se prolínají na jedné ose, řazené rok za rokem, a každou položku můžete přiřadit konkrétnímu členovi rodiny.",
            "steps": (("Přidejte vzpomínku", "Fotografie, krátký popis a datum stačí. Nic dalšího není povinné a uložení nic neblokuje."), ("Přiřaďte ji člověku", "U milníku i pokladu je vidět, koho se týká. Každé dítě tak má vlastní časovou osu v rámci rodinné kroniky."), ("Vracejte se k nim", "Na obrazovce Dnes se občas připomene, co se stalo v tentýž den v minulých letech. Z milníku si můžete připravit kartičku k vytištění.")),
            "answers_title": "Časté otázky o rodinných vzpomínkách",
            "answers": (("Je Rodinka náhrada za fotogalerii nebo cloud?", "Ne. Rodinka není úložiště na všechny fotky z telefonu a nesnaží se jím být. Je to místo pro vybrané okamžiky, které chcete mít popsané, zařazené v čase a dostupné celé rodině — ne pro zálohu celé galerie."), ("Sledují dětské milníky, jestli je dítě „napřed“ nebo „pozadu“?", "Ne. Milník je vzpomínka na něco, co se stalo, ne tvrzení o tom, kdy by to dítě mělo umět. Rodinka proto nemá očekávaný věk, normy ani porovnávání dětí mezi sebou a nikdy neupozorní na to, že nějaký milník chybí."), ("Můžou vzpomínky vidět i děti?", "Ano, kronika je pro celou rodinu ke čtení. Zakládání a úpravy zůstávají na dospělých, takže se dítě může dívat, ale nic nesmaže.")),
            "card": "Dětské milníky, poklady a rodinné okamžiky na jedné časové ose.",
            "cta_title": "Dejte rodinným vzpomínkám společné místo.",
            "cta_text": "Otevřete v Rodince Vzpomínky a přidejte první milník nebo poklad. Stačí fotka, pár vět a datum.",
        },
        "documents": {
            "title": "Hlídání platnosti dokladů celé rodiny | Rodinka",
            "description": "Evidujte pasy, občanky a další doklady s datem platnosti. Rodinka pošle připomínku s předstihem, takže končící doklad nezjistíte až před dovolenou.",
            "og_title": "Platnost dokladů, kterou nemusíte nosit v hlavě",
            "og_description": "U každého dokladu je vidět, komu patří a do kdy platí. Připomínka přijde včas, ne na poslední chvíli.",
            "og_alt": "Přehled rodinných dokladů a jejich platnosti v aplikaci Rodinka",
            "eyebrow": "DOKLADY A JEJICH PLATNOST",
            "h1": "Platnost pasů a dokladů celé rodiny na jednom místě",
            "lead": "Pas se nedá vyřídit ze dne na den. Přesto se na jeho platnost obvykle přijde ve chvíli, kdy je zarezervovaná dovolená. U čtyřčlenné rodiny je to osm dokladů a osm různých dat, která si nikdo nepamatuje.",
            "problem_title": "Termín, na který si nikdo nevzpomene včas",
            "problem": ("Doklady mají jednu nepříjemnou vlastnost: mezi vyřízením a další potřebou uplyne pět nebo deset let. Připomínka v kalendáři se za tu dobu ztratí, telefon se vymění a papír ve šuplíku nikdo nečte. Platnost se tak nejčastěji řeší pod tlakem.", "Přitom stačí zapsat dvě informace — komu doklad patří a do kdy platí — a nechat je hlídat něco jiného než vlastní paměť. Rodinka je proto vede u rodiny, ne u jednoho člověka, a ozve se dřív, než je pozdě."),
            "scenarios": (("Před dovolenou", "Platnost pasů celé rodiny zkontrolujete na jedné obrazovce, ne přebíráním šuplíku."), ("Doklady dětí", "Dětské pasy a průkazy mají kratší platnost než ty vaše. U každého je vidět, komu patří."), ("Nejen doklady totožnosti", "Řidičský průkaz, technická nebo kartička pojišťovny — hlídat se dá cokoli, co má datum platnosti.")),
            "help_title": "Jak hlídání platnosti v Rodince funguje",
            "help_intro": "Doklady jsou v Rodince dostupné jen dospělým členům rodiny. Model je postavený kolem jediné otázky: co brzy přestane platit a čí to je.",
            "steps": (("Zapište doklad", "Název, majitel a datum platnosti. Volitelně datum vydání a poznámka, kde doklad fyzicky je."), ("Nechte si připomenout", "Ve výchozím nastavení přijde připomínka 180, 90, 30 a 7 dní před koncem platnosti a v den, kdy platnost končí; po vypršení se Rodinka ozve jednou týdně. Předstihy si můžete upravit a připomínky respektují tiché hodiny."), ("Mějte přehled o stavu", "Doklady jsou rozdělené podle toho, čemu brzy končí platnost, co už prošlo a co je v pořádku.")),
            "answers_title": "Časté otázky o dokladech a připomínkách",
            "answers": (("Kdy má připomínka na končící doklad přijít?", "U cestovního pasu nebo občanského průkazu se vyplatí vědět o blížícím se konci platnosti několik měsíců dopředu — vyřízení má svou lhůtu a před prázdninami bývají fronty delší. Rodinka proto upozorňuje s předstihem, ne až v posledním týdnu."), ("Vidí doklady i děti?", "Ne. Doklady jsou v Rodince dostupné jen dospělým členům rodiny. Dítě se na tuto část aplikace nedostane."), ("Musím do Rodinky nahrávat sken dokladu?", "Ne. K hlídání platnosti stačí název, majitel a datum — sken není podmínkou. Rodinka je postavená na tom, aby vám připomněla termín, ne aby nahradila místo, kde doklady fyzicky máte.")),
            "card": "Pasy, občanky a další doklady s datem platnosti a včasnou připomínkou.",
            "cta_title": "Ať vás končící pas nepřekvapí před odletem.",
            "cta_text": "Přidejte do Rodinky první doklad s datem platnosti a nechte připomenutí na aplikaci.",
        },
        "trips": {
            "title": "Plánování rodinných výletů a dovolených | Rodinka",
            "description": "Ukládejte tipy na výlety s dětmi, složte z nich plán cesty a nechte rodinu hlasovat. Vybraný tip se propíše do kalendáře a z výletu bude vzpomínka.",
            "og_title": "Rodinné výlety, o kterých rozhoduje celá rodina",
            "og_description": "Zásobník tipů, plán cesty, hlasování a kalendář na jednom místě — od nápadu po vzpomínku.",
            "og_alt": "Plánování rodinných výletů a hlasování o tipech v aplikaci Rodinka",
            "eyebrow": "VÝLETY A DOVOLENÉ",
            "h1": "Rodinné výlety od prvního nápadu po společnou vzpomínku",
            "lead": "Tip na hrad přišel v chatu, rozhledna je v záložkách jednoho rodiče a na zoo se čeká, „až bude čas“. Rodinka dává nápadům na výlety jedno místo, ze kterého se dá opravdu vyrazit — a o cíli rozhoduje celá rodina.",
            "problem_title": "Nápadů je dost. Chybí místo, kde vydrží do víkendu",
            "problem": ("Tipy na výlety přicházejí nahodile: odkaz od kamarádky, článek, doporučení u školní brány. Když pak přijde volná sobota, nikdo si nevzpomene, kam se vlastně chtěli podívat, a rozhodování začíná znovu od nuly.", "Rodinný výlet navíc není rozhodnutí jednoho člověka. Děti chtějí do zoo, jeden rodič na hrad a druhý potřebuje vědět, jestli se to stihne za den. Společný zásobník tipů a jednoduché hlasování udělají z debaty v autě domluvu předem."),
            "scenarios": (("Tip z odkazu", "Někdo pošle odkaz na zajímavé místo. Vložíte ho do Rodinky a tip má název, náhled i místo na mapě."), ("Volný víkend", "Z několika tipů složíte plán cesty s orientačním termínem a rodina hlasuje, co se komu líbí."), ("Po návratu", "Klepnete na Byli jsme a z výletu uděláte rodinnou vzpomínku s fotkou a datem.")),
            "help_title": "Jak Rodinka pomáhá s rodinnými výlety",
            "help_intro": "Tipy a plány cest jsou jedno místo pro celou rodinu. Všichni je vidí a reagují na ně, plánování a zápis do kalendáře zůstávají na dospělých.",
            "steps": (("Ukládejte tipy průběžně", "Výlet nebo dovolená s odkazem, místem a krátkým popisem. Zásobník nápadů si prohlédnete v kartách nebo na mapě, a když se nemůžete rozhodnout, Rodinka vybere náhodný tip."), ("Složte plán cesty", "Plán má název, orientační termín, oblast a vybrané tipy. Jeden tip může patřit do více plánů a aktivní plán si připnete na obrazovku Dnes."), ("Nechte rodinu hlasovat", "U každého tipu v plánu dá každý svůj hlas: líbí se, neutrální, nelíbí se. Dospělý pak vybraný tip jedním krokem převede na událost v rodinném kalendáři."), ("Uchovejte, co jste zažili", "Po výletu označíte Byli jsme a Rodinka nabídne uložit ho jako rodinnou vzpomínku — s názvem, datem i místem už předvyplněnými.")),
            "answers_title": "Časté otázky k plánování rodinných výletů",
            "answers": (("Jak vybrat výlet, se kterým budou spokojení všichni?", "Sepište několik tipů předem a nechte každého hlasovat. Když rozhodnutí nestojí na jednom člověku, výlet má větší šanci bavit děti i dospělé — a debata se nepřesune až do auta."), ("Kam ukládat tipy na výlety s dětmi?", "Na jedno místo, které vidí celá rodina. V Rodince stačí vložit odkaz a tip se uloží s náhledem, takže nápady nezapadnou v chatu ani v záložkách jednoho telefonu."), ("Řeší Rodinka podrobný itinerář, rezervace nebo dopravu?", "Ne. Plán cesty je záměrně lehký: termín, oblast, tipy a hlasování. Hodinový program, rezervace ani jízdenky neřeší — vybraný tip se ale propíše do rodinného kalendáře jako běžná událost."), ("Můžou hlasovat i děti?", "Ano. Tipy a plány vidí celá rodina a každý člen s vlastním přihlášením může u tipu v plánu hlasovat a reagovat. Zakládání, úpravy a zápis do kalendáře zůstávají na dospělých.")),
            "card": "Zásobník tipů, plán cesty a hlasování celé rodiny — od nápadu po vzpomínku.",
            "cta_title": "Uložte první tip, kam se chcete podívat.",
            "cta_text": "Otevřete v Rodince Tipy na výlety a dovolené a vložte odkaz na místo, kam byste rádi vyrazili.",
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
        "steps": (("Pridajte udalosť", "Zapíšte čas, miesto a člena rodiny, ktorého sa týka. Pri pravidelnom krúžku nastavte opakovanie."), ("Oddeľte, koho sa to týka, od toho, kto to zabezpečí", "Pri udalosti je zvlášť vidieť účastníka — napríklad dieťa, ktoré ide na plávanie — a zvlášť dospelého, ktorý ho tam odvezie. Sú to dve rôzne informácie a Rodinka ich nezlučuje do jednej."), ("Kontrolujte spoločný týždeň", "Prepnete si mesiac, týždeň alebo agendu podľa naliehavosti. Pri plánovaní vlastného programu obaja rodičia vidia rovnaké rodinné záväzky."), ("Nechajte dôležité dni prísť samy", "Narodeniny členov rodiny, výročia aj vlastné dni sa v kalendári zobrazujú ako tichá vrstva, ktorá neblokuje čas. Na tie dôležité vám Rodinka môže pripomenúť s predstihom.")),
        "answers_title": "Čo ľudia hľadajú pri rodinnom kalendári", "answers": (("Ako zdieľať rodinný kalendár medzi rodičmi?", "Vytvorte spoločný rodinný priestor a pozvite druhého dospelého. Udalosti zapisujte tam a pri aktivitách doplňte aj dohodnutý odvoz."), ("Ako zorganizovať krúžky detí?", "Pri každom krúžku evidujte deň, čas, miesto, dieťa a dopravu. Pravidelné termíny nastavte ako opakované a výnimky upravujte samostatne."), ("Čo keď jeden týždeň vezie dieťa niekto iný?", "Zmeníte odvoz len pri tom jednom termíne. Opakovaná aktivita zostane nedotknutá, takže kvôli jednej výnimke nemusíte rozbíjať celú sériu ani ju zakladať nanovo."), ("Patria do rodinného kalendára aj úlohy?", "Udalosť hovorí, kedy sa niečo deje. Prípravu, napríklad kúpiť darček alebo odovzdať prihlášku, veďte ako úlohu s termínom a zodpovednou osobou."), ("Upozorní kalendár na kolíziu?", "Áno, keď by jeden člen rodiny mal dva záväzky v rovnakom čase — napríklad krúžok a lekára. Dve deti na dvoch krúžkoch naraz kolízia nie sú, ak každé vezie niekto iný. Upozornenie nikdy nebráni uloženiu.")),
        "card": "Krúžky, škola, návštevy a vyzdvihovanie v spoločnom kalendári.", "cta_title": "Nech sa na plán nemusí nikto znovu pýtať.", "cta_text": "Pridajte do Rodinky prvú udalosť a dohodnite rovno aj to, kto ju zabezpečí.",
    },
    "shopping": {
        "title": "Zdieľaný nákupný zoznam pre celú rodinu | Rodinka", "description": "Spoločný nákupný zoznam, ktorý môže rodina priebežne dopĺňať a v obchode odškrtávať. Bez papierikov a položiek stratených v chate.",
        "og_title": "Spoločný nákupný zoznam, ktorý máte vždy poruke", "og_description": "Pridávajte, čo doma dochádza, a nakupujte z rovnakého aktuálneho zoznamu.", "og_alt": "Zdieľaný rodinný nákupný zoznam v aplikácii Rodinka",
        "eyebrow": "NÁKUPY BEZ ZABUDNUTÝCH SPRÁV", "h1": "Zdieľaný nákupný zoznam, do ktorého môže pridať každý", "lead": "Mlieko sa minulo ráno, pečivo niekto napísal do chatu a zoznam na chladničke zostal doma. Spoločný nákupný zoznam zachytí položku vtedy, keď si na ňu niekto spomenie — a v obchode zostáva aktuálny.",
        "problem_title": "Najväčším problémom nákupu býva zber informácií", "problem": ("Samotné nakupovanie je jednoduché. Ťažšie je zistiť, čo naozaj chýba, či to už niekto pridal a kto sa dnes dostane do obchodu. Papierik funguje iba doma a správa v chate rýchlo zapadne.", "Keď má domácnosť jeden zoznam, nezáleží na tom, kto napokon nakúpi. Položky môže pridávať každý, hotové veci sa odškrtnú a zvyšok zostane na neskôr."),
        "scenarios": (("Niečo sa práve minulo", "Posledné mlieko alebo prací gél sa zapíšu hneď, nie až pri spomínaní pred obchodom."), ("V obchode bez signálu", "Zoznam funguje, aj keď telefón nechytá signál. Odškrtnuté položky sa dorovnajú, len čo sa pripojenie vráti."), ("Nakupuje niekto iný", "Partner cestou z práce otvorí rovnaký zoznam a nemusí žiadať ďalšiu správu.")),
        "help_title": "Ako mať spoločný nákupný zoznam v Rodinke", "help_intro": "Zoznam je súčasťou rodinného priestoru, preto ho pozvaní členovia domácnosti vidia v mobile aj počítači.",
        "steps": (("Pridávajte priebežne — písaním aj hlasom", "Položku zapíšte vo chvíli, keď doma dochádza. Na podporovaných zariadeniach nemusíte písať: povedzte, čo chýba, a Rodinka z toho pripraví položky, ktoré pred pridaním ešte uvidíte a môžete upraviť."), ("Nakupujte z rovnakej verzie, aj bez signálu", "V obchode položky odškrtávajte. Ostatní vidia, čo je hotové, a nepridajú tú istú vec druhýkrát. Zoznam funguje aj offline a zmeny sa dorovnajú po návrate pripojenia."), ("Prepojte nákup s jedlom", "Pri plánovaní večerí doplňte potrebné suroviny, aby týždenný plán nezostal iba želaním.")),
        "answers_title": "Praktické otázky k spoločnému nákupu", "answers": (("Ako zdieľať nákupný zoznam s partnerom?", "Používajte jeden zoznam v spoločnom rodinnom priestore. Obaja doň môžete pridávať aj odškrtávať, takže netreba posielať novú verziu."), ("Je lepší zoznam v aplikácii alebo na papieri?", "Papier je rýchly pri chladničke. Zdieľaný zoznam je však dostupný mimo domu a aktualizuje ho viac ľudí, čo pomáha, keď sa v nákupoch striedate."), ("Dá sa nákupný zoznam nadiktovať?", "Na podporovaných zariadeniach áno. Poviete, čo chýba, Rodinka z toho pripraví jednotlivé položky a ukáže ich na potvrdenie — až potom sa pridajú do zoznamu. Rozpoznané položky môžete pred pridaním upraviť alebo zmazať a nahrávka ani prepis sa nikam neukladajú."), ("Funguje zoznam aj bez signálu?", "Áno. Nákupný zoznam je navrhnutý tak, aby sa dal používať offline: v obchode pridávate aj odškrtávate položky ďalej a zmeny sa dorovnajú, len čo sa telefón pripojí.")),
        "card": "Jeden aktuálny zoznam doma aj v obchode, ktorý dopĺňa celá rodina.", "cta_title": "Ďalší nákup nemusí začať hľadaním správ.", "cta_text": "Otvorte v Rodinke spoločný zoznam a pridajte prvú vec, ktorá doma práve dochádza.",
    },
    "chores": {
        "title": "Úlohy pre rodinu a domáce povinnosti | Rodinka", "description": "Rozdeľte domáce úlohy medzi členov rodiny, pridajte termín a majte jasno, kto čo zariadi. Prakticky pre rodičov aj deti.",
        "og_title": "Domáce povinnosti bez nekonečného pripomínania", "og_description": "Konkrétne rodinné úlohy, jasná zodpovednosť a prehľad o tom, čo je hotové.", "og_alt": "Úlohy pre rodinu a rozdelené domáce povinnosti v Rodinke",
        "eyebrow": "KTO ČO DOMA ZARIADI", "h1": "Úlohy pre rodinu, ktoré nenosí v hlave iba jeden rodič", "lead": "Objednať dieťa k zubárovi, vrátiť knihy, vyniesť kôš alebo pripraviť veci na výlet. Keď má úloha konkrétneho človeka a termín, domácnosť sa nemusí spoliehať na opakované pripomínanie.",
        "problem_title": "„Musíme to urobiť“ ešte nie je rozdelená úloha", "problem": ("Domáce práce si často všimneme až vtedy, keď nie sú hotové. Ešte menej viditeľné sú organizačné povinnosti: sledovať prihlášku do tábora, kúpiť darček či zavolať opravárovi. Ak ich drží jeden človek, nesie aj väčšinu mentálnej záťaže.", "Rodinné úlohy nemajú merať výkon domácnosti. Ide o jednoduchú dohodu: čo treba urobiť, kto to prevezme a dokedy. Hotovú vec potom netreba kontrolovať v chate."),
        "scenarios": (("Drobné denné povinnosti", "Kôš, riad alebo príprava školskej tašky môžu mať jednoduché a zrozumiteľné zadanie."), ("Neviditeľná organizácia", "Telefonát lekárovi, platba za krúžok alebo nákup darčeka dostanú človeka aj termín."), ("Úlohy pre deti", "Dieťa môže mať vlastné prihlásenie a v ňom len svoje úlohy. K úlohe sa dá pridať odmena alebo vreckové a splnenie potvrdí dospelý.")),
        "help_title": "Ako rozdeliť domáce úlohy medzi členov rodiny", "help_intro": "Rodinka pomáha premeniť neurčité povinnosti na malé konkrétne kroky, ktoré vidno v spoločnom prehľade.",
        "steps": (("Pomenujte výsledok", "Namiesto „riešiť školu“ napíšte „odoslať prihlášku na výlet“. Každý vie, čo znamená hotovo."), ("Priraďte človeka a termín", "Úloha nemá zostať spoločná dovtedy, kým ju urobí ten najvšímavejší. Zodpovednosť si dohodnite rovno."), ("Opakujte, čo sa opakuje", "Vyniesť kôš každý utorok nastavíte raz. Jednorazová poznámka bez termínu aj pravidelná povinnosť sú pritom rovnaký typ úlohy."), ("Nechajte hotové veci odísť z hlavy", "Splnenie vidia ostatní. Pri úlohách s odmenou ho dospelý potvrdí a suma sa dieťaťu pripíše.")),
        "answers_title": "Otázky k domácim úlohám a povinnostiam", "answers": (("Ako rozdeliť domáce práce spravodlivo?", "Nezačínajte iba viditeľným upratovaním. Spíšte aj plánovanie, telefonáty a sledovanie termínov. Rozdelenie potom posudzujte podľa času a záťaže."), ("Ako zadávať úlohy deťom?", "Úloha má zodpovedať veku, byť konkrétna a mať dosiahnuteľný termín. Cieľom je návyk a zapojenie, nie dokonalosť."), ("Ako pripomínať úlohy bez hádok?", "Dohodnite zodpovednosť a zapíšte ju na spoločné miesto. Obaja rodičia sa tak môžu oprieť o rovnakú dohodu, nie o pamäť jedného z nich."), ("Ako fungujú odmeny a vreckové za úlohy?", "K úlohe môžete pridať odmenu a vyžadovať schválenie dospelým. Dieťa úlohu odškrtne, rodič potvrdí splnenie a suma sa pripíše. Pravidelné vreckové môže byť podmienené tým, že sú dohodnuté úlohy hotové."), ("Dá sa rýchla úloha nadiktovať?", "Na podporovaných zariadeniach áno — priamo na obrazovke Dnes. Poviete, čo treba spraviť, Rodinka z toho pripraví návrhy úloh a ukáže ich na úpravu. Nič nevznikne skôr, než potvrdíte.")),
        "card": "Konkrétne povinnosti, jasný človek a termín pre rodičov aj deti.", "cta_title": "Rozdeľte prvú úlohu skôr, než sa stratí v hlave.", "cta_text": "Pridajte do Rodinky jednu konkrétnu povinnosť a dohodnite sa, kto ju prevezme.",
    },
    "meals": {
        "title": "Plánovanie jedál na týždeň pre rodinu | Rodinka", "description": "Naplánujte rodinné jedlá na celý týždeň, obmedzte každodenné rozhodovanie a pridajte suroviny do spoločného nákupného zoznamu.",
        "og_title": "Týždenný plán jedál bez každodennej otázky „čo variť?“", "og_description": "Praktický plán jedál pre rodinu, ktorý nadväzuje na spoločný nákupný zoznam.", "og_alt": "Týždenné plánovanie rodinných jedál v aplikácii Rodinka",
        "eyebrow": "MENEJ ROZHODOVANIA OKOLO VEČERE", "h1": "Plánovanie jedál na týždeň, ktoré počíta so skutočným životom", "lead": "Niektoré dni je čas variť, inokedy sa rodina vracia neskoro z krúžkov. Týždenný plán jedál nemusí byť dokonalý jedálny lístok — stačí, keď vopred vyrieši pár večerov a uľahčí nákup.",
        "problem_title": "Najťažšie často nie je varenie, ale rozhodovanie", "problem": ("Otázka „čo bude na večeru?“ prichádza zvyčajne vtedy, keď je hlad a málo času. Bez rámcového plánu sa častejšie nakupuje narýchlo, niektoré suroviny chýbajú a iné sa nestihnú využiť.", "Rodinný plán má rešpektovať rytmus týždňa. Po náročnom popoludní môže počítať s rýchlym jedlom, vo voľnejší deň s dlhším varením. Zmena plánu nie je zlyhanie, iba aktualizácia spoločného prehľadu."),
        "scenarios": (("Deň plný krúžkov", "Na večer sa naplánuje rýchle jedlo, ktoré po návrate domov nevyžaduje dlhú prípravu."), ("Spoločné víkendové varenie", "Rodina vopred vidí, kedy je priestor na obľúbené jedlo alebo varenie s deťmi."), ("Nákup bez hádania", "Z plánovaných jedál vzniknú konkrétne suroviny v spoločnom nákupnom zozname.")),
        "help_title": "Ako plánovať jedlo na celý týždeň v Rodinke", "help_intro": "Nejde o podrobný diétny program. Rodinka spája jednoduchú predstavu o jedlách s tým, čo treba nakúpiť.",
        "steps": (("Pozrite si rodinný kalendár", "Najskôr zvážte, ktoré dni sú dlhé a kedy bude niekto doma skôr. Plán potom vychádza zo skutočného času."), ("Vyberte niekoľko istých jedál", "Nemusíte vyplniť každý chod. Jedlá, ktoré bežne varíte, si uložte do knižnice a nabudúce ich vyberiete jedným klepnutím."), ("Nechajte rodinu rozhodnúť", "Keď sa doma neviete zhodnúť, vypíšte pár možností a nechajte o víkendovom obede hlasovať. Hlasovať môžu aj deti."), ("Pošlite suroviny do nákupu", "Pri naplánovanom jedle prenesiete potrebné suroviny do zdieľaného nákupného zoznamu jedným krokom, takže sa neprepisujú ručne.")),
        "answers_title": "Časté otázky k plánovaniu rodinného jedla", "answers": (("Ako plánovať jedlo na celý týždeň?", "Začnite rodinným programom a hlavné jedlá vyberte podľa času na prípravu. Jeden voľný večer pomôže využiť zvyšky alebo reagovať na zmenu."), ("Ako zapojiť rodinu do výberu jedál?", "V Rodinke môžete otvoriť hlasovanie o jedle: vypíšete možnosti a každý člen rodiny vrátane detí dá svoj hlas. Rozhodnutie tak nie je na jednom človeku a plán má väčšiu šancu fungovať."), ("Ako prepojiť jedálny lístok s nákupným zoznamom?", "Pri každom plánovanom jedle prejdite hlavné suroviny a chýbajúce pridajte do spoločného zoznamu. Pred nákupom ešte skontrolujte zásoby.")),
        "card": "Jednoduchý plán večerí podľa rodinného týždňa a potrebných nákupov.", "cta_title": "Naplánujte pár večerí a uľahčite zvyšok týždňa.", "cta_text": "Otvorte Rodinku, vyberte prvé jedlo a doplňte, čo k nemu treba kúpiť.",
    },
    "app": {
        "title": "Aplikácia pre rodinu: kalendár, úlohy a nákupy | Rodinka", "description": "Rodinka je aplikácia pre rodinu, ktorá spája kalendár, domáce úlohy, nákupný zoznam a plán jedál v jednom spoločnom prehľade.",
        "og_title": "Jedna aplikácia na každodennú organizáciu rodiny", "og_description": "Namiesto roztrúsených správ, poznámok a kalendárov má rodina spoločný priestor pre to, čo práve rieši.", "og_alt": "Aplikácia Rodinka na spoločnú organizáciu rodinného života",
        "eyebrow": "APLIKÁCIA PRE KAŽDODENNÝ CHOD RODINY", "h1": "Aplikácia pre rodinu, ktorá spája plán aj domáce povinnosti", "lead": "Kalendár ukazuje termíny, no nie vždy nákup. Chat obsahuje dohodu, ale o týždeň sa v ňom ťažko hľadá. Rodinka spája praktické časti rodinného života, aby každý vedel, kam sa pozrieť.",
        "problem_title": "Rodina nepotrebuje viac miest, ale menej hľadania", "problem": ("Každý nástroj môže fungovať dobre, no celok sa aj tak rozpadá. Termín je v osobnom kalendári, zoznam na papieri, úloha v hlave a zmena v skupinovom chate. Informácie existujú, iba nie sú dostupné všetkým v správnej chvíli.", "Dobrá aplikácia pre rodinu nemá potrebovať správcu na plný úväzok. Bežná vec sa zapíše rýchlo, spoločný prehľad je zrozumiteľný a jednotlivé časti zodpovedajú situáciám zo skutočnej domácnosti."),
        "scenarios": (("Pred odchodom z domu", "Jeden pohľad ukáže dnešný program, odvoz aj povinnosti, ktoré nesmú zostať doma."), ("Počas dňa", "Ktokoľvek pridá chýbajúci nákup alebo označí hotovú úlohu bez správy pre všetkých."), ("Pri plánovaní týždňa", "Kalendár, jedlá a domáce úlohy spolu vytvoria reálny obraz toho, čo rodinu čaká.")),
        "help_title": "Čo nájdete v aplikácii Rodinka", "help_intro": "Rodinka nie je len kalendár s úlohami. Nižšie sú tri vrstvy, z ktorých sa skladá — použijete z nich len to, čo vašej domácnosti dáva zmysel.",
        "steps": (("Každodenná prevádzka", "Obrazovka Dnes s programom, dennou linkou a tým, čo potrebuje pozornosť. Zdieľaný kalendár s opakovanými aktivitami a odvozom, úlohy s vlastníkom a termínom, nákupný zoznam fungujúci aj offline a jedálniček s rodinným hlasovaním."), ("Rodina, nie iba logistika", "Spomienky s detskými míľnikmi, pokladmi a spoločnými zážitkami, Dnešná Rodinka s otázkou alebo hlasovaním pre celú domácnosť, tipy a plány výletov, detské účty s vlastnými úlohami a vreckovým, päť rodinných hier a rodinný chat."), ("Veci, na ktoré sa zabúda", "Pripomienky s tichými hodinami, doklady so strážením platnosti, zdravotné termíny a očkovania, zvieratká s veterinárnou históriou, narodeniny a významné dni, rodinné miesta s navigáciou a Bábätko na ceste.")),
        "answers_title": "Ako vyberať aplikáciu pre rodinu", "answers": (("Čo by mala vedieť aplikácia pre rodinu?", "Mala by pokrývať najčastejšie spoločné situácie, fungovať rýchlo v mobile aj počítači a dovoliť viacerým členom pracovať s rovnakými aktuálnymi informáciami."), ("Nahradí Rodinka rodinný chat?", "Nie. Chat je výborný na rozhovor. Rodinka je prehľad termínov, úloh a zoznamov, ktoré chcete nájsť aj neskôr bez prechádzania histórie správ."), ("Musí rodina používať všetky funkcie?", "Nemusí. Začnite oblasťou, ktorá dnes spôsobuje najviac otázok. Ďalšie časti pridajte až vtedy, keď domácnosti naozaj pomôžu."), ("Funguje Rodinka bez internetu?", "Z veľkej časti áno. Dnes, kalendár, úlohy a nákupný zoznam sa dajú používať aj meniť offline a zmeny sa po pripojení dorovnajú. Jedálniček, spomienky alebo tipy na výlety si prečítate; správy a zdravotné záznamy potrebujú pripojenie.")),
        "card": "Kalendár, povinnosti, nákupný zoznam a jedlá v jednom rodinnom priestore.", "cta_title": "Dajte rodinným informáciám jedno známe miesto.", "cta_text": "Rodinka funguje priamo v prehliadači. Vytvorte rodinu a začnite prvou praktickou vecou.",
    },
    "baby": {
        "title": "Príprava na bábätko spoločne | Rodinka",
        "description": "Pripravujte sa na bábätko spoločne. Orientačná cesta po týždňoch, praktické prípravy a výber mena v rodinnom plánovači Rodinka.",
        "og_title": "Čakáte bábätko? Pripravíme sa spolu.",
        "og_description": "Cesta po týždňoch, praktické prípravy aj spoločný výber mena v jednom rodinnom priestore.",
        "og_alt": "Bábätko na ceste v Rodinke s prehľadom príprav a výberom mena",
        "eyebrow": "BÁBÄTKO NA CESTE",
        "h1": "Príprava na bábätko, ktorú zvládnete spolu",
        "lead": "Cesta po týždňoch, praktické prípravy aj spoločný výber mena. Rodinka pomôže udržať veci pokope ešte predtým, než sa nový člen rodiny narodí.",
        "problem_title": "Prípravy ľahko skončia v poznámkach, chate a niekoľkých zoznamoch",
        "problem": ("Výbava je v poznámkach, nákupy na inom zozname a dôležitú drobnosť si pamätá iba jeden rodič. Mená, o ktorých sa rozprávate, zatiaľ miznú medzi bežnými správami a nie je jasné, čo už máte pripravené.", "Spoločný priestor nepridáva ďalší povinný plán. Dáva obom rodičom pokojné miesto pre veci, ktoré chcú pred príchodom bábätka riešiť spolu a vlastným tempom."),
        "scenarios": (("Zoznamy na viacerých miestach", "Výbava na cesty, spánok alebo prvé dni nemusí zostať rozdelená medzi papier, poznámky a chat."), ("Mená v chate", "Nápady na mená zostávajú pokope aj s preferenciami zapojených dospelých."), ("Čo je už pripravené?", "Obaja rodičia vidia rovnaký prehľad a môžu pokračovať tam, kde ten druhý skončil.")),
        "help_title": "Ako Rodinka pomôže s prípravou na bábätko",
        "help_intro": "Bábätko na ceste je organizačná časť Rodinky, nie zdravotná aplikácia. Ponúka ľahkú orientáciu a praktický priestor na spoločné prípravy.",
        "steps": (("Cesta po týždňoch", "Orientačný týždeň, jednoduchý priebeh a vybrané momenty pomôžu zaradiť prípravy do času. Nejde o medicínske meranie ani hodnotenie zdravotného stavu."), ("Prípravy podľa tém", "Inšpiráciu nájdete v oblastiach na cesty, spánok, kŕmenie a dojčenie, hygienu a prebaľovanie, oblečenie, domov, pôrodnicu a prvé dni alebo administratívu. Z položky checklistu navyše spravíte bežnú úlohu, nákup alebo udalosť, takže príprava nezostane v oddelenom zozname."), ("Mená, ktoré riešite spolu", "Zapisujte si kandidátne mená, označte favoritov a zdieľajte preferencie ako páči sa mi, možno alebo skôr nie. Nejde o súťaž ani skóre.")),
        "answers_title": "Časté otázky k príprave na bábätko",
        "answers": (("Je Rodinka tehotenská aplikácia?", "Nie. Rodinka nenahrádza zdravotnú aplikáciu ani odporúčania lekára. Pomáha rodine s orientačnou cestou a praktickou organizáciou príprav."), ("Musíme použiť celý checklist?", "Nemusíte. Zoznam je inšpirácia a prehľad, nie povinný nákupný plán. Každá rodina si ponechá iba to, čo zodpovedá jej potrebám."), ("Môžeme spoločne vyberať meno?", "Áno. Môžete si viesť kandidátne mená, označiť favoritov a pri každom zachytiť preferencie zapojených dospelých bez vyhlasovania víťaza."), ("Uvidia informácie automaticky deti?", "Nie. Časť Bábätko na ceste je určená dospelým v rodine, takže prípravy a citlivé informácie zostávajú v ich spoločnom priestore.")),
        "card": "Cesta po týždňoch, praktické prípravy a spoločný výber mena na jednom mieste.",
        "cta_title": "Pripravujte sa na nového člena rodiny spoločne.",
        "cta_text": "Otvorte Rodinku, pridajte Bábätko na ceste a začnite tým, čo chcete mať pripravené ako prvé.",
    },
    "memories": {
        "title": "Rodinné spomienky a detské míľniky na jednom mieste | Rodinka",
        "description": "Detské míľniky, rodinné poklady a fotografie na jednej časovej osi. Spomienku priradíte členovi rodiny a z míľnika si môžete vytlačiť kartičku.",
        "og_title": "Rodinné spomienky, ktoré nezapadnú v galérii telefónu",
        "og_description": "Jedna spoločná kronika rodiny: detské míľniky, poklady a okamihy, ku ktorým sa chcete vracať.",
        "og_alt": "Rodinné spomienky a detské míľniky v aplikácii Rodinka",
        "eyebrow": "RODINNÁ PAMÄŤ",
        "h1": "Rodinné spomienky a detské míľniky, ktoré nezapadnú",
        "lead": "Prvý krok, vysvedčenie, kamienok z dovolenky aj fotka, na ktorej sa zakaždým smejete. Väčšina týchto vecí skončí v galérii telefónu jedného rodiča medzi tisíckami ďalších snímok. Rodinka im dáva spoločné miesto, kde ich nájde celá rodina.",
        "problem_title": "Spomienky sa nestrácajú naraz, ale postupne",
        "problem": ("Fotiek pribúda rýchlejšie, než ich stíhame triediť. O dva roky sa k prvému kroku nedostanete cez dovolenku, Vianoce a stovky náhodných snímok — a príbeh k tej fotke pozná len ten, kto ju odfotil. Druhý rodič často nemá prístup vôbec.", "Rodinná pamäť nepotrebuje ďalšiu galériu. Potrebuje pár viet pri fotke, dátum, meno človeka, ktorého sa to týka, a jedno miesto, kam sa dá vrátiť. Rodinka preto vedie spomienky ako spoločnú kroniku, nie ako úložisko súborov."),
        "scenarios": (("Detské míľniky", "Prvý krok, prvé slovo, prvý deň v škole. Zapíšete, čo sa stalo a kedy, a pridáte fotku."), ("Rodinné poklady", "Obrázok, mušľa z výletu alebo list od starej mamy. Fotografia, krátky popis a dátum z nich spravia exponát rodinnej zbierky."), ("Spoločné zážitky", "Výlet do zoo alebo obyčajný večer doma. Rodinnej spomienke stačí pár viet, dátum a pokojne jedna fotka — a vznikne aj z výletu alebo udalosti v kalendári.")),
        "help_title": "Ako Rodinka vedie rodinné spomienky",
        "help_intro": "Spomienky sú jedna sekcia, nie rázcestník. Míľniky, poklady aj spoločné zážitky sa prelínajú na jednej osi, zoradené rok po roku, a každú položku môžete priradiť konkrétnemu členovi rodiny.",
        "steps": (("Pridajte spomienku", "Fotografia, krátky popis a dátum stačia. Nič ďalšie nie je povinné a uloženie nič neblokuje."), ("Priraďte ju človeku", "Pri míľniku aj poklade vidieť, koho sa týka. Každé dieťa tak má vlastnú časovú os v rámci rodinnej kroniky."), ("Vracajte sa k nim", "Na obrazovke Dnes sa občas pripomenie, čo sa stalo v ten istý deň v minulých rokoch. Z míľnika si môžete pripraviť kartičku na vytlačenie.")),
        "answers_title": "Časté otázky o rodinných spomienkach",
        "answers": (("Je Rodinka náhrada za fotogalériu alebo cloud?", "Nie. Rodinka nie je úložisko na všetky fotky z telefónu a ani sa ním nesnaží byť. Je to miesto pre vybrané okamihy, ktoré chcete mať popísané, zaradené v čase a dostupné celej rodine — nie pre zálohu celej galérie."), ("Sledujú detské míľniky, či je dieťa „napred“ alebo „pozadu“?", "Nie. Míľnik je spomienka na niečo, čo sa stalo, nie tvrdenie o tom, kedy by to dieťa malo vedieť. Rodinka preto nemá očakávaný vek, normy ani porovnávanie detí medzi sebou a nikdy neupozorní na to, že nejaký míľnik chýba."), ("Môžu spomienky vidieť aj deti?", "Áno, kronika je pre celú rodinu na čítanie. Zakladanie a úpravy zostávajú na dospelých, takže dieťa sa môže pozerať, ale nič nezmaže.")),
        "card": "Detské míľniky, poklady a rodinné okamihy na jednej časovej osi.",
        "cta_title": "Dajte rodinným spomienkam spoločné miesto.",
        "cta_text": "Otvorte v Rodinke Spomienky a pridajte prvý míľnik alebo poklad. Stačí fotka, pár viet a dátum.",
    },
    "documents": {
        "title": "Stráženie platnosti dokladov celej rodiny | Rodinka",
        "description": "Evidujte pasy, občianske preukazy a ďalšie doklady s dátumom platnosti. Rodinka pošle pripomienku s predstihom, takže končiaci doklad nezistíte až pred dovolenkou.",
        "og_title": "Platnosť dokladov, ktorú nemusíte nosiť v hlave",
        "og_description": "Pri každom doklade vidieť, komu patrí a dokedy platí. Pripomienka príde včas, nie na poslednú chvíľu.",
        "og_alt": "Prehľad rodinných dokladov a ich platnosti v aplikácii Rodinka",
        "eyebrow": "DOKLADY A ICH PLATNOSŤ",
        "h1": "Platnosť pasov a dokladov celej rodiny na jednom mieste",
        "lead": "Pas sa nedá vybaviť zo dňa na deň. Napriek tomu sa na jeho platnosť obvykle príde vo chvíli, keď je dovolenka zarezervovaná. Pri štvorčlennej rodine je to osem dokladov a osem rôznych dátumov, ktoré si nikto nepamätá.",
        "problem_title": "Termín, na ktorý si nikto nespomenie včas",
        "problem": ("Doklady majú jednu nepríjemnú vlastnosť: medzi vybavením a ďalšou potrebou uplynie päť alebo desať rokov. Pripomienka v kalendári sa za ten čas stratí, telefón sa vymení a papier v zásuvke nikto nečíta. Platnosť sa tak najčastejšie rieši pod tlakom.", "Pritom stačí zapísať dve informácie — komu doklad patrí a dokedy platí — a nechať ich strážiť niečo iné než vlastnú pamäť. Rodinka ich preto vedie pri rodine, nie pri jednom človeku, a ozve sa skôr, než je neskoro."),
        "scenarios": (("Pred dovolenkou", "Platnosť pasov celej rodiny skontrolujete na jednej obrazovke, nie preberaním zásuvky."), ("Doklady detí", "Detské pasy a preukazy majú kratšiu platnosť než tie vaše. Pri každom vidieť, komu patrí."), ("Nielen doklady totožnosti", "Vodičský preukaz, technická alebo kartička poisťovne — strážiť sa dá čokoľvek, čo má dátum platnosti.")),
        "help_title": "Ako stráženie platnosti v Rodinke funguje",
        "help_intro": "Doklady sú v Rodinke dostupné len dospelým členom rodiny. Model je postavený okolo jedinej otázky: čo čoskoro prestane platiť a čie to je.",
        "steps": (("Zapíšte doklad", "Názov, majiteľ a dátum platnosti. Voliteľne dátum vydania a poznámka, kde doklad fyzicky je."), ("Nechajte si pripomenúť", "V predvolenom nastavení príde pripomienka 180, 90, 30 a 7 dní pred koncom platnosti a v deň, keď platnosť končí; po vypršaní sa Rodinka ozve raz týždenne. Predstihy si môžete upraviť a pripomienky rešpektujú tiché hodiny."), ("Majte prehľad o stave", "Doklady sú rozdelené podľa toho, čomu čoskoro končí platnosť, čo už prešlo a čo je v poriadku.")),
        "answers_title": "Časté otázky o dokladoch a pripomienkach",
        "answers": (("Kedy má pripomienka na končiaci doklad prísť?", "Pri cestovnom pase alebo občianskom preukaze sa oplatí vedieť o blížiacom sa konci platnosti niekoľko mesiacov dopredu — vybavenie má svoju lehotu a pred prázdninami bývajú rady dlhšie. Rodinka preto upozorňuje s predstihom, nie až v poslednom týždni."), ("Vidia doklady aj deti?", "Nie. Doklady sú v Rodinke dostupné len dospelým členom rodiny. Dieťa sa do tejto časti aplikácie nedostane."), ("Musím do Rodinky nahrávať sken dokladu?", "Nie. Na stráženie platnosti stačí názov, majiteľ a dátum — sken nie je podmienkou. Rodinka je postavená na tom, aby vám pripomenula termín, nie aby nahradila miesto, kde doklady fyzicky máte.")),
        "card": "Pasy, občianske preukazy a ďalšie doklady s dátumom platnosti a včasnou pripomienkou.",
        "cta_title": "Nech vás končiaci pas neprekvapí pred odletom.",
        "cta_text": "Pridajte do Rodinky prvý doklad s dátumom platnosti a pripomenutie nechajte na aplikácii.",
    },
    "trips": {
        "title": "Plánovanie rodinných výletov a dovoleniek | Rodinka",
        "description": "Ukladajte tipy na výlety s deťmi, zostavte z nich plán cesty a nechajte rodinu hlasovať. Vybraný tip sa prenesie do kalendára a z výletu bude spomienka.",
        "og_title": "Rodinné výlety, o ktorých rozhoduje celá rodina",
        "og_description": "Zásobník tipov, plán cesty, hlasovanie a kalendár na jednom mieste — od nápadu po spomienku.",
        "og_alt": "Plánovanie rodinných výletov a hlasovanie o tipoch v aplikácii Rodinka",
        "eyebrow": "VÝLETY A DOVOLENKY",
        "h1": "Rodinné výlety od prvého nápadu po spoločnú spomienku",
        "lead": "Tip na hrad prišiel v chate, rozhľadňa je v záložkách jedného rodiča a na zoo sa čaká, „až bude čas“. Rodinka dáva nápadom na výlety jedno miesto, z ktorého sa dá naozaj vyraziť — a o cieli rozhoduje celá rodina.",
        "problem_title": "Nápadov je dosť. Chýba miesto, kde vydržia do víkendu",
        "problem": ("Tipy na výlety prichádzajú náhodne: odkaz od kamarátky, článok, odporúčanie pri školskej bráne. Keď potom príde voľná sobota, nikto si nespomenie, kam sa vlastne chceli pozrieť, a rozhodovanie sa začína odznova.", "Rodinný výlet navyše nie je rozhodnutie jedného človeka. Deti chcú do zoo, jeden rodič na hrad a druhý potrebuje vedieť, či sa to stihne za deň. Spoločný zásobník tipov a jednoduché hlasovanie urobia z debaty v aute dohodu vopred."),
        "scenarios": (("Tip z odkazu", "Niekto pošle odkaz na zaujímavé miesto. Vložíte ho do Rodinky a tip má názov, náhľad aj miesto na mape."), ("Voľný víkend", "Z niekoľkých tipov zostavíte plán cesty s orientačným termínom a rodina hlasuje, čo sa komu páči."), ("Po návrate", "Ťuknete na Boli sme a z výletu spravíte rodinnú spomienku s fotkou a dátumom.")),
        "help_title": "Ako Rodinka pomáha s rodinnými výletmi",
        "help_intro": "Tipy a plány ciest sú jedno miesto pre celú rodinu. Všetci ich vidia a reagujú na ne, plánovanie a zápis do kalendára zostávajú na dospelých.",
        "steps": (("Ukladajte tipy priebežne", "Výlet alebo dovolenka s odkazom, miestom a krátkym popisom. Zásobník nápadov si prezriete v kartách alebo na mape, a keď sa neviete rozhodnúť, Rodinka vyberie náhodný tip."), ("Zostavte plán cesty", "Plán má názov, orientačný termín, oblasť a vybrané tipy. Jeden tip môže patriť do viacerých plánov a aktívny plán si pripnete na obrazovku Dnes."), ("Nechajte rodinu hlasovať", "Pri každom tipe v pláne dá každý svoj hlas: páči sa, neutrálne, nepáči sa. Dospelý potom vybraný tip jedným krokom prenesie do rodinného kalendára ako udalosť."), ("Uchovajte, čo ste zažili", "Po výlete označíte Boli sme a Rodinka ponúkne uložiť ho ako rodinnú spomienku — s názvom, dátumom aj miestom už predvyplnenými.")),
        "answers_title": "Časté otázky k plánovaniu rodinných výletov",
        "answers": (("Ako vybrať výlet, s ktorým budú spokojní všetci?", "Spíšte niekoľko tipov vopred a nechajte každého hlasovať. Keď rozhodnutie nestojí na jednom človeku, výlet má väčšiu šancu baviť deti aj dospelých — a debata sa nepresunie až do auta."), ("Kam ukladať tipy na výlety s deťmi?", "Na jedno miesto, ktoré vidí celá rodina. V Rodinke stačí vložiť odkaz a tip sa uloží s náhľadom, takže nápady nezapadnú v chate ani v záložkách jedného telefónu."), ("Rieši Rodinka podrobný itinerár, rezervácie alebo dopravu?", "Nie. Plán cesty je zámerne ľahký: termín, oblasť, tipy a hlasovanie. Hodinový program, rezervácie ani lístky nerieši — vybraný tip sa však prenesie do rodinného kalendára ako bežná udalosť."), ("Môžu hlasovať aj deti?", "Áno. Tipy a plány vidí celá rodina a každý člen s vlastným prihlásením môže pri tipe v pláne hlasovať a reagovať. Zakladanie, úpravy a zápis do kalendára zostávajú na dospelých.")),
        "card": "Zásobník tipov, plán cesty a hlasovanie celej rodiny — od nápadu po spomienku.",
        "cta_title": "Uložte prvý tip, kam sa chcete pozrieť.",
        "cta_text": "Otvorte v Rodinke Tipy na výlety a dovolenky a vložte odkaz na miesto, kam by ste radi vyrazili.",
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
        "steps": (("Add the full event", "Record the time, place and family member involved. Set regular activities to repeat so they do not need weekly re-entry."), ("Separate who it is about from who is handling it", "An event shows the participant — the child going to swimming — separately from the adult driving them there. They are two different facts and Rodinka does not collapse them into one."), ("Review one family week", "Switch between a month, a week or an agenda grouped by urgency. When either parent makes plans, both see the same family commitments."), ("Let the important days turn up on their own", "Family birthdays, anniversaries and your own special days appear in the calendar as a quiet layer that does not block time, and Rodinka can remind you ahead of the ones that matter.")),
        "answers_title": "Questions families ask about shared calendars", "answers": (("How do parents share a family calendar?", "Create one family space and invite the other adult. Put shared events there, and include the transport or pick-up detail whenever it affects the plan."), ("How can we organize children’s activities?", "For every activity, record the day, time, place, child and transport. Repeat regular sessions and edit exceptions individually so the weekly view stays accurate."), ("What if someone else drives just one week?", "Change the companion on that single occurrence. The repeating activity itself is untouched, so one exception does not mean breaking up the series or recreating it."), ("Should chores go in the family calendar?", "Use an event for something that happens at a time. Preparation, such as buying a gift or returning a form, works better as a separate chore with an owner and due date."), ("Does the calendar warn about clashes?", "Yes, when one family member would have two commitments at the same time — say an activity and a doctor’s appointment. Two children at two activities at once is not a clash as long as someone different takes each of them. The warning never stops you from saving.")),
        "card": "School, activities, visits and pick-ups in one shared calendar.", "cta_title": "Make the plan available without another message.", "cta_text": "Add your first family event in Rodinka and include who is handling the practical side.",
    },
    "shopping": {
        "title": "Shared family shopping list that stays up to date | Rodinka", "description": "A shared shopping list everyone can add to and check off in the store. Keep groceries out of scattered messages and forgotten paper notes.",
        "og_title": "One household shopping list, always close at hand", "og_description": "Add what is running out at home and shop from the same current list.", "og_alt": "Rodinka shared family shopping list for groceries and household items",
        "eyebrow": "SHOPPING WITHOUT THE LOST MESSAGES", "h1": "A shared shopping list the whole family can update", "lead": "The milk ran out this morning, someone mentioned bread in chat and the note on the fridge stayed at home. A shared list catches an item when anyone remembers it — and it is still current in the store.",
        "problem_title": "Collecting the list is often harder than the shopping", "problem": ("Buying groceries is straightforward. Working out what is actually missing, whether someone has already added it and who is going to the store is the messy part. Paper only works where it is left, while a chat message quickly disappears.", "With one household list, it matters less who ends up shopping. Everyone can add items, completed ones are checked off and anything left stays available for later."),
        "scenarios": (("Something just ran out", "The last milk or laundry detergent goes on the list immediately, not during a rushed memory test later."), ("In a shop with no signal", "The list keeps working when the phone has no reception. Items you tick off catch up as soon as the connection returns."), ("Someone else is shopping", "A partner stopping on the way home opens the same list without asking for an updated message.")),
        "help_title": "How to keep a shared shopping list in Rodinka", "help_intro": "The list belongs to your family space, so invited household members can open and update it on a phone or computer.",
        "steps": (("Add items by typing or by voice", "Capture an item when you notice it. On supported devices you do not have to type: say what has run out and Rodinka turns it into items you review, edit and confirm before anything is added."), ("Shop from the same version, signal or not", "Check things off in the store. Everyone else can see what is done and avoid adding or buying it twice, and the list keeps working offline until the connection returns."), ("Connect shopping with meals", "When you choose dinners for the week, add the ingredients you need so the meal plan is practical.")),
        "answers_title": "Practical questions about shared grocery lists", "answers": (("How do I share a grocery list with my partner?", "Use one list inside a shared family space. Both of you can add and check off items, so there is no need to send a fresh version before every trip."), ("Is an app better than a paper shopping list?", "Paper is quick beside the fridge. A shared digital list is also available away from home and can be updated by several people, which helps when different family members shop."), ("Can I dictate the shopping list?", "On supported devices, yes. You say what is missing, Rodinka turns it into separate items and shows them for confirmation — only then are they added. You can edit or remove anything it got wrong first, and no recording or transcript is stored."), ("Does the list work without a signal?", "Yes. The shopping list is built to be used offline: you can keep adding and ticking off items in the shop, and the changes catch up once the phone reconnects.")),
        "card": "One current list at home and in the store, updated by the whole family.", "cta_title": "Your next shop can start without searching through chat.", "cta_text": "Open the shared list in Rodinka and add the first thing your household is running low on.",
    },
    "chores": {
        "title": "Family chores and household responsibilities | Rodinka", "description": "Assign family chores, add a due date and make it clear who is handling what. A practical shared view for parents and children.",
        "og_title": "Household chores without endless reminders", "og_description": "Clear family tasks, visible responsibility and a shared view of what is done.", "og_alt": "Family chores and household responsibilities assigned in Rodinka",
        "eyebrow": "WHO IS HANDLING WHAT AT HOME", "h1": "Family chores that do not live in one parent’s head", "lead": "Book the dentist, return library books, take out the recycling or pack for a trip. When a task has a person and a due date, the household does not have to run on repeated reminders.",
        "problem_title": "“We need to do that” is not an assigned chore", "problem": ("Housework often becomes visible only when it is not done. Planning work is even easier to miss: watching a camp deadline, buying a birthday gift or calling a repair service. If one person holds those details, they also carry most of the mental load.", "A family task list is not a household performance score. It is a simple agreement about what needs doing, who has taken it and when it matters. Once complete, the task no longer needs another check-in message."),
        "scenarios": (("Small daily responsibilities", "Recycling, dishes or packing a school bag can each have a short, clear definition of done."), ("Invisible organizing work", "A doctor’s call, activity payment or gift purchase gets an owner and a due date."), ("Chores for children", "A child can have their own sign-in showing only their chores. A chore can carry a reward or pocket money, and an adult confirms it is done.")),
        "help_title": "How to divide household chores across the family", "help_intro": "Rodinka turns loose household intentions into small, specific actions that everyone can see in the shared overview.",
        "steps": (("Name the outcome", "Replace “sort out school” with “send the trip form”. A concrete task makes it obvious what completion means."), ("Choose a person and a date", "Do not leave every task shared until the most attentive person does it. Agree on ownership while the need is clear."), ("Let repeating work repeat itself", "Taking the bins out every Tuesday is set up once. A one-off note with no due date and a standing weekly duty are the same kind of task here."), ("Let completed work leave your head", "Everyone can see that the chore is done, and where a reward is attached an adult confirms it and the amount is credited.")),
        "answers_title": "Questions about family chores and responsibilities", "answers": (("How can we divide household work fairly?", "Include planning, calls and deadline tracking as well as visible cleaning. Then consider time and mental effort, not only the number of items each person has."), ("How should we give chores to children?", "Choose something age-appropriate, specific and achievable by a clear time. The aim is participation and a habit of helping, not a perfect result."), ("How can we remind each other without arguing?", "Agree on the owner and put the task in a shared place. A reminder then refers to the same visible agreement instead of one person managing the other."), ("How do rewards and pocket money work?", "A chore can carry a reward and require an adult to approve it. The child ticks it off, a parent confirms, and the amount is credited. Regular pocket money can depend on the agreed chores being done."), ("Can a quick task be dictated?", "On supported devices, yes — straight from the Today screen. You say what needs doing, Rodinka turns it into draft tasks and shows them for editing. Nothing is created until you confirm.")),
        "card": "Specific responsibilities, a clear owner and a due date for adults and children.", "cta_title": "Assign one task before it disappears into someone’s mental list.", "cta_text": "Add a concrete household responsibility in Rodinka and agree on who will take it.",
    },
    "meals": {
        "title": "Simple weekly meal planning for families | Rodinka", "description": "Plan family meals for the week, reduce daily decisions and add missing ingredients to the same shared shopping list.",
        "og_title": "A weekly family meal plan for fewer “what’s for dinner?” moments", "og_description": "A practical meal plan shaped around the family calendar and connected to your shopping list.", "og_alt": "Weekly family meal planning in the Rodinka organizer app",
        "eyebrow": "FEWER LAST-MINUTE DINNER DECISIONS", "h1": "Weekly meal planning built around real family life", "lead": "Some days leave room to cook; others end late after children’s activities. A weekly meal plan does not need to be perfect — it only needs to settle a few evenings ahead of time and make the next shop easier.",
        "problem_title": "The hardest part is often deciding, not cooking", "problem": ("“What’s for dinner?” tends to arrive when everyone is hungry and short on time. Without a loose plan, the family shops in a rush, useful ingredients are missing and other food goes unused.", "A family meal plan should follow the shape of the week. Busy afternoons call for something quick; a slower day can hold a longer recipe. When plans change, updating the overview is enough — it is not a failed system."),
        "scenarios": (("An activity-packed day", "A quick dinner is planned for the evening when everyone gets home late."), ("Cooking together at the weekend", "The family can see where there is space for a favorite meal or cooking with children."), ("A shopping list with a reason", "Planned dinners become the specific ingredients needed alongside regular household shopping.")),
        "help_title": "How to plan a week of meals in Rodinka", "help_intro": "This is not a detailed diet program. Rodinka connects a simple dinner plan with the groceries required to make it happen.",
        "steps": (("Check the family calendar", "Notice which days are long and when someone will be home earlier. Build the meal plan around the time you actually have."), ("Choose a few reliable meals", "You do not need to fill every slot. Save the dinners you cook often to the meal library and pick them again in one tap."), ("Let the family decide", "When nobody can agree, list a few options and put the weekend lunch to a vote. Children get a vote too."), ("Send ingredients to the shopping list", "From a planned meal, move the ingredients you need into the shared shopping list in one step instead of retyping them.")),
        "answers_title": "Common questions about family meal planning", "answers": (("How do I plan meals for the whole week?", "Start with the family schedule and choose main meals by the time available to prepare them. Leave one evening open for leftovers or an unexpected change."), ("How can the whole family help choose meals?", "Rodinka can open a vote on a meal: you list the options and every family member, children included, casts a vote. The decision stops resting on one person and the plan is more likely to stick."), ("How do I connect a meal plan to a grocery list?", "Review the main ingredients for each planned meal and add what is missing to the shared list. Check the cupboards once more before shopping to avoid duplicates.")),
        "card": "A simple dinner plan shaped around the week and the groceries it needs.", "cta_title": "Plan a few dinners and make the rest of the week lighter.", "cta_text": "Open Rodinka, choose the first meal and add anything the family needs to buy.",
    },
    "app": {
        "title": "Family organizer app for calendars, chores and lists | Rodinka", "description": "Rodinka is a family organizer app combining a shared calendar, household chores, shopping lists and meal planning in one practical place.",
        "og_title": "One family organizer for the details of everyday home life", "og_description": "Give schedules, chores, groceries and meals a shared home instead of scattering them across chats and notes.", "og_alt": "Rodinka family organizer app for shared schedules and household tasks",
        "eyebrow": "AN APP FOR THE EVERYDAY WORK OF FAMILY LIFE", "h1": "A family organizer app for schedules, chores, shopping and meals", "lead": "A calendar holds dates but not always groceries. Chat holds conversations but makes last week’s detail hard to find. Rodinka brings the practical parts of family life together so everyone knows where to look.",
        "problem_title": "Families need fewer places to search, not more", "problem": ("Every tool may work on its own while the complete picture still falls apart. An event sits in a personal calendar, a list is on paper, a chore stays in someone’s head and the latest change is in group chat. The information exists, but not for everyone at the right moment.", "A good family organizer should not need its own full-time administrator. Everyday updates must be quick, the shared overview must be easy to read and each part should match a real household situation."),
        "scenarios": (("Before leaving home", "One view shows today’s schedule, pick-ups and the responsibilities that cannot be forgotten."), ("During the day", "Anyone can add a missing grocery item or complete a chore without messaging the entire family."), ("Planning the week", "The calendar, meals and household tasks create a realistic picture of what the family is taking on.")),
        "help_title": "What the Rodinka family organizer includes", "help_intro": "Rodinka is not just a calendar with chores attached. These are the three layers it is built from — use only the parts that earn their place in your household.",
        "steps": (("Everyday logistics", "A Today screen with the day’s schedule, a day line and whatever needs attention. A shared calendar with recurring activities and companions, chores with an owner and a due date, a shopping list that works offline and a meal plan the family can vote on."), ("Family, not just logistics", "Memories holding children’s milestones, treasures and shared experiences, Rodinka Today with a question or vote for the household, trip ideas and plans, child accounts with their own chores and pocket money, five family games and a family chat."), ("The things that slip", "Reminders with quiet hours, documents with expiry tracking, health appointments and vaccinations, pets with their vet history, birthdays and special days, family places with navigation, and Expected Child.")),
        "answers_title": "How to choose a family organizer app", "answers": (("What should a family organizer app do?", "It should cover the shared situations your household handles most, work well on phones and computers, and let several people use the same current information."), ("Does Rodinka replace family group chat?", "No. Chat is excellent for conversation. Rodinka is the reference point for schedules, chores and lists you want to find later without scrolling through message history."), ("Do we need to use every feature?", "Not at all. Start with the area causing the most repeated questions today. Add another part only when it solves a real need for your household."), ("Does Rodinka work without an internet connection?", "Largely, yes. Today, the calendar, chores and the shopping list can be used and changed offline, and the changes catch up once you reconnect. The meal plan, memories and trip ideas stay readable; messages and health records need a connection.")),
        "card": "A calendar, household responsibilities, shopping and meals in one family space.", "cta_title": "Give family information one familiar home.", "cta_text": "Rodinka works in the browser. Create your family and start with the first practical thing you need to share.",
    },
    "baby": {
        "title": "Preparing for a baby together | Rodinka",
        "description": "Prepare for a baby together with a light week-by-week journey, practical checklists and shared name choices in the Rodinka family organizer.",
        "og_title": "Expecting a baby? Get ready together.",
        "og_description": "A week-by-week journey, practical preparation and shared name choices in one family space.",
        "og_alt": "Rodinka expected-child journey with preparation checklists and shared name choices",
        "eyebrow": "EXPECTED CHILD",
        "h1": "Prepare for your baby together, one practical step at a time",
        "lead": "A gentle week-by-week journey, practical preparation and a shared place for possible names. Rodinka keeps the organizing together before your new family member arrives.",
        "problem_title": "Preparation easily scatters across notes, chats and several lists",
        "problem": ("Travel gear may sit in one note, first-week essentials in another list and one important detail only in a parent’s head. Possible names disappear between ordinary messages, while neither person has a clear view of what is already prepared.", "A shared space is not another compulsory plan. It gives both parents a calm place for the things they want to arrange together, in an order and at a pace that suits their family."),
        "scenarios": (("Lists in too many places", "Ideas for travel, sleep and the first days can stay together instead of being split across paper, notes and chat."), ("Names lost in messages", "Possible names and each adult’s preferences remain easy to find when you return to the conversation."), ("What have we already handled?", "Both parents see the same overview and can pick up where the other person stopped.")),
        "help_title": "How Rodinka helps you prepare for a baby",
        "help_intro": "Expected Child is an organizing space inside Rodinka, not a health or pregnancy-tracking app. It offers light orientation and a practical place to prepare together.",
        "steps": (("A week-by-week journey", "An approximate week, simple progress and selected moments help place preparation in time. This is not medical measurement, monitoring or health advice."), ("Preparation by topic", "Browse optional ideas for travel, sleep, feeding and breastfeeding, hygiene and changing, clothing, home, hospital and the first days, or administration. A checklist item can also become an ordinary chore, shopping item or event, so preparation does not stay in a list of its own."), ("Names you consider together", "Collect possible names, mark favorites and share preferences such as like, maybe or probably not. It is a conversation aid, not a contest or score.")),
        "answers_title": "Common questions about preparing for a baby",
        "answers": (("Is Rodinka a pregnancy tracker?", "No. Rodinka does not replace a medical app, professional guidance or advice from your doctor. It helps a family organize practical preparation with a light, approximate journey."), ("Do we have to complete the whole checklist?", "No. It is optional inspiration and an overview, not a required shopping plan. Every family can keep only what matches its own needs."), ("Can we choose a name together?", "Yes. You can collect possible names, mark favorites and capture each participating adult’s preference without turning the choice into a leaderboard."), ("Will children automatically see this information?", "No. Expected Child is for the adults in the family, so preparation and sensitive information stay in their shared adult space.")),
        "card": "A week-by-week journey, practical preparation and shared name choices in one place.",
        "cta_title": "Get ready for your new family member together.",
        "cta_text": "Open Rodinka, add Expected Child and start with the first thing you would like to have ready.",
    },
    "memories": {
        "title": "Family memories and children\u2019s milestones in one place | Rodinka",
        "description": "Children\u2019s milestones, family treasures and photos on a single timeline. Assign a memory to a family member and turn a milestone into a card you can print.",
        "og_title": "Family memories that do not disappear into a camera roll",
        "og_description": "One shared family chronicle: children\u2019s milestones, treasures and the moments you want to come back to.",
        "og_alt": "Family memories and children\u2019s milestones in the Rodinka app",
        "eyebrow": "YOUR FAMILY\u2019S MEMORY",
        "h1": "Family memories and milestones that do not get lost",
        "lead": "A first step, a school report, a pebble from a holiday, the photo that still makes everyone laugh. Most of it ends up in one parent\u2019s camera roll among thousands of other pictures. Rodinka gives those moments a shared home the whole family can reach.",
        "problem_title": "Memories are not lost all at once",
        "problem": ("Photos pile up faster than anyone can sort them. Two years later the first step sits behind a holiday, a Christmas and several hundred incidental shots \u2014 and the story behind the picture is known only to whoever took it. The other parent often has no access at all.", "A family\u2019s memory does not need another gallery. It needs a few sentences next to the photo, a date, the name of the person it belongs to, and one place to return to. That is why Rodinka keeps memories as a shared chronicle rather than a file store."),
        "scenarios": (("Children\u2019s milestones", "A first step, a first word, a first day at school. Record what happened and when, and add a photo."), ("Family treasures", "A drawing, a shell from a trip, a letter from a grandparent. A photo, a short description and a date turn it into part of the family collection."), ("Shared experiences", "A trip to the zoo or an ordinary evening at home. A family memory needs only a few sentences, a date and perhaps one photo — and it can start from a trip or a calendar event.")),
        "help_title": "How Rodinka keeps family memories",
        "help_intro": "Memories are one section, not a menu of separate tools. Milestones, treasures and shared experiences share a single timeline, year by year, and each entry can belong to a particular family member.",
        "steps": (("Add a memory", "A photo, a short description and a date are enough. Nothing else is required and nothing blocks saving."), ("Give it a person", "Milestones and treasures show who they belong to, so each child has their own thread within the family chronicle."), ("Come back to them", "The Today screen occasionally resurfaces what happened on the same date in earlier years, and a milestone can become a card you print at home.")),
        "answers_title": "Common questions about family memories",
        "answers": (("Does Rodinka replace a photo gallery or cloud backup?", "No. Rodinka is not storage for every photo on your phone and does not try to be. It is a place for chosen moments you want described, placed in time and available to the whole family \u2014 not a backup of your camera roll."), ("Do milestones track whether a child is ahead or behind?", "No. A milestone records something that happened; it is not a statement about when a child should be able to do it. There is no expected age, no norm, no comparison between children, and Rodinka never flags a milestone as missing."), ("Can children see the memories too?", "Yes, the chronicle is readable by the whole family. Creating and editing stays with adults, so a child can look through it without changing anything.")),
        "card": "Children\u2019s milestones, treasures and family moments on one timeline.",
        "cta_title": "Give your family memories a shared home.",
        "cta_text": "Open Memories in Rodinka and add a first milestone or treasure. A photo, a few sentences and a date are enough.",
    },
    "documents": {
        "title": "Track passport and ID expiry for the whole family | Rodinka",
        "description": "Record passports, ID cards and other documents with their expiry dates. Rodinka reminds you in good time, so an expiring document does not surface days before a trip.",
        "og_title": "Document expiry dates you do not have to remember",
        "og_description": "Every document shows who it belongs to and when it runs out, with a reminder that arrives early enough to act on.",
        "og_alt": "An overview of family documents and their expiry dates in the Rodinka app",
        "eyebrow": "DOCUMENTS AND THEIR EXPIRY",
        "h1": "Passport and ID expiry dates for the whole family",
        "lead": "A passport cannot be renewed overnight. Yet most households discover an expiry date right after the holiday is booked. For a family of four that is eight documents and eight different dates nobody is keeping track of.",
        "problem_title": "A deadline nobody remembers in time",
        "problem": ("Documents have an awkward property: five or ten years pass between getting one and needing it again. A calendar reminder does not survive that long, the phone gets replaced and nobody reads the paper in the drawer. So expiry dates tend to be handled under pressure.", "Two pieces of information are enough \u2014 who the document belongs to and when it expires \u2014 as long as something other than your memory is watching them. Rodinka keeps them with the family rather than with one person, and speaks up before it is too late."),
        "scenarios": (("Before a holiday", "Check every passport in the household on one screen instead of going through a drawer."), ("Children\u2019s documents", "Children\u2019s passports and ID cards expire sooner than yours, and each one shows who it belongs to."), ("Not only identity documents", "A driving licence, a vehicle inspection or an insurance card \u2014 anything with an expiry date can be tracked the same way.")),
        "help_title": "How expiry tracking works in Rodinka",
        "help_intro": "Documents are available to adult family members only. The model is built around a single question: what stops being valid soon, and whose is it?",
        "steps": (("Record the document", "A name, an owner and an expiry date. The issue date and a note about where the document physically lives are optional."), ("Let it remind you", "By default a reminder arrives 180, 90, 30 and 7 days before the expiry date and on the day itself; once a document has lapsed, Rodinka nudges once a week. You can change the lead times, and reminders respect your quiet hours."), ("See where things stand", "Documents are grouped by what expires soon, what has already lapsed and what is still fine.")),
        "answers_title": "Common questions about documents and reminders",
        "answers": (("How far ahead should a document reminder arrive?", "For a passport or an ID card it helps to know several months in advance \u2014 processing takes its own time and queues get longer before the summer. Rodinka raises it early rather than in the final week."), ("Can children see the documents?", "No. Documents in Rodinka are available to adult family members only; a child account cannot open that part of the app."), ("Do I have to upload a scan of each document?", "No. A name, an owner and a date are enough to track expiry \u2014 a scan is optional. Rodinka is built to remind you of the deadline, not to replace wherever you keep the documents themselves.")),
        "card": "Passports, ID cards and other documents with expiry dates and timely reminders.",
        "cta_title": "Do not let an expiring passport surprise you at the airport.",
        "cta_text": "Add your first document with its expiry date and let Rodinka handle the reminder.",
    },
    "trips": {
        "title": "Plan family trips and holidays together | Rodinka",
        "description": "Save ideas for days out with the kids, turn them into a trip plan and let the family vote. The chosen idea lands in the calendar and the trip becomes a memory.",
        "og_title": "Family trips the whole family gets a say in",
        "og_description": "An idea backlog, trip plans, voting and the calendar in one place — from first idea to shared memory.",
        "og_alt": "Planning family trips and voting on ideas in the Rodinka app",
        "eyebrow": "TRIPS AND HOLIDAYS",
        "h1": "Family trips, from the first idea to a shared memory",
        "lead": "The castle idea arrived in a chat, the lookout tower sits in one parent’s bookmarks and the zoo waits for “when we have time”. Rodinka gives trip ideas one place you can actually set off from — and the whole family decides where to go.",
        "problem_title": "There are plenty of ideas. They just need to last until the weekend",
        "problem": ("Trip ideas turn up at random: a link from a friend, an article, a tip at the school gate. When a free Saturday finally comes, nobody remembers where they wanted to go, and the decision starts from scratch.", "A family trip is not one person’s decision either. The children want the zoo, one parent wants a castle and the other needs to know whether it fits into a day. A shared idea backlog and a simple vote turn the argument in the car into a plan made in advance."),
        "scenarios": (("An idea from a link", "Someone sends a link to an interesting place. Paste it into Rodinka and the idea has a title, a preview and a spot on the map."), ("A free weekend", "Turn a few ideas into a trip plan with rough dates, and the family votes on what they like."), ("Back home", "Tap Been there and turn the trip into a family memory with a photo and a date.")),
        "help_title": "How Rodinka helps with family trips",
        "help_intro": "Trip ideas and plans are one place for the whole family. Everyone can see them and react; planning and adding to the calendar stay with the adults.",
        "steps": (("Save ideas as they come", "A day trip or a holiday, with a link, a place and a short note. Browse the idea backlog as cards or on a map, and when nobody can decide, Rodinka picks a random idea."), ("Build a trip plan", "A plan has a name, rough dates, an area and the ideas you picked. One idea can belong to several plans, and an active plan can be pinned to the Today screen."), ("Let the family vote", "Everyone gives each idea in the plan a vote: like, neutral or dislike. An adult then turns the chosen idea into an event in the family calendar in one step."), ("Keep what you lived", "After the trip, mark it Been there and Rodinka offers to save it as a family memory — with the title, date and place already filled in.")),
        "answers_title": "Common questions about planning family trips",
        "answers": (("How do we pick a trip everyone is happy with?", "Collect a few ideas in advance and let everyone vote. When the decision does not rest on one person, the trip is more likely to work for children and adults alike — and the debate does not move into the car."), ("Where should we keep ideas for days out with the kids?", "In one place the whole family can see. In Rodinka, pasting a link saves the idea with a preview, so ideas do not get lost in chat or in the bookmarks of one phone."), ("Does Rodinka handle itineraries, bookings or transport?", "No. A trip plan is deliberately light: dates, area, ideas and votes. There is no hour-by-hour schedule, no bookings and no tickets — but the chosen idea becomes an ordinary event in the family calendar."), ("Can children vote too?", "Yes. The whole family can see ideas and plans, and every member with their own sign-in can vote and react on ideas in a plan. Creating, editing and adding to the calendar stay with the adults.")),
        "card": "An idea backlog, trip plans and the whole family’s vote — from first idea to memory.",
        "cta_title": "Save the first place you would like to visit.",
        "cta_text": "Open Trip ideas in Rodinka and paste a link to somewhere you would love to go.",
    },
}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def canonical(path: str) -> str:
    return f"{SITE_URL}{path}"


def og_image_url(locale: str) -> str:
    return canonical(OG_IMAGES[locale])


def localized_product_src(base_src: str, locale: str) -> str:
    if locale == "cs":
        return base_src
    return f"{base_src.removesuffix('.webp')}-{locale}.webp"


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
    proof = PRODUCT_PROOFS.get(page_key)
    if proof:
        proof_url = canonical(localized_product_src(proof["src"], locale))
        webpage = next(item for item in graph["@graph"] if item.get("@type") == "WebPage")
        webpage["associatedMedia"] = {"@id": f"{proof_url}#product-image"}
        graph["@graph"].append(
            {
                "@type": "ImageObject",
                "@id": f"{proof_url}#product-image",
                "url": proof_url,
                "contentUrl": proof_url,
                "encodingFormat": "image/webp",
                "width": PRODUCT_IMAGE_WIDTH,
                "height": PRODUCT_IMAGE_HEIGHT,
                "name": proof["alt"][locale],
                "caption": proof["caption"][locale],
                "inLanguage": LOCALES[locale]["lang"],
            }
        )
    return json.dumps(graph, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def analytics_head() -> str:
    return f'''    <!-- Consent Mode defaults must be queued before Google Tag Manager loads. -->
    <script>
      window.dataLayer = window.dataLayer || [];
      window.gtag = window.gtag || function() {{ window.dataLayer.push(arguments); }};
      window.rodinkaConsent = {{ key: "{CONSENT_STORAGE_KEY}", version: {CONSENT_VERSION}, analytics: "denied" }};
      (function () {{
        var analyticsConsent = "denied";
        try {{
          var savedConsent = JSON.parse(window.localStorage.getItem(window.rodinkaConsent.key));
          if (savedConsent && savedConsent.version === window.rodinkaConsent.version &&
              (savedConsent.analytics === "granted" || savedConsent.analytics === "denied")) {{
            analyticsConsent = savedConsent.analytics;
          }}
        }} catch (error) {{}}
        window.rodinkaConsent.analytics = analyticsConsent;
        window.gtag("consent", "default", {{
          analytics_storage: analyticsConsent,
          ad_storage: "denied",
          ad_user_data: "denied",
          ad_personalization: "denied"
        }});
      }})();
    </script>
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
    new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    }})(window,document,'script','dataLayer','{GTM_CONTAINER_ID}');</script>
    <!-- End Google Tag Manager -->'''


def analytics_body() -> str:
    return f'''    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_CONTAINER_ID}"
    height="0" width="0" style="display:none;visibility:hidden" title="Google Tag Manager"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->'''


def consent_panel(locale: str) -> str:
    cfg = LOCALES[locale]
    return f'''    <section class="cookie-consent" data-cookie-consent hidden role="region" aria-live="polite" aria-labelledby="cookie-consent-title" aria-describedby="cookie-consent-description">
      <div class="cookie-consent-copy">
        <h2 id="cookie-consent-title">{esc(cfg["consent_title"])}</h2>
        <p id="cookie-consent-description">{esc(cfg["consent_text"])}</p>
      </div>
      <div class="cookie-consent-actions">
        <button class="consent-button consent-allow" type="button" data-consent-choice="granted">{esc(cfg["consent_allow"])}</button>
        <button class="consent-button consent-reject" type="button" data-consent-choice="denied">{esc(cfg["consent_reject"])}</button>
      </div>
    </section>'''


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
{analytics_head()}
    <title>{esc(data["title"])}</title>
    <meta name="description" content="{esc(data["description"])}" />
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1" />
    <meta name="color-scheme" content="light dark" />
    <meta name="theme-color" content="#fffdf8" />
    <script>
      (function () {{
        var choice;
        try {{ choice = localStorage.getItem('rodinka_theme'); }} catch (error) {{}}
        var dark = choice === 'dark' || (choice !== 'light' && matchMedia('(prefers-color-scheme: dark)').matches);
        document.documentElement.dataset.theme = dark ? 'dark' : 'light';
        document.querySelector('meta[name="theme-color"]').content = dark ? '#282b24' : '#fffdf8';
      }})();
    </script>
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
    <link rel="preload" href="{MANROPE_WOFF2}" as="font" type="font/woff2" crossorigin />
    <link rel="stylesheet" href="/styles.css?v={ASSET_VERSION}" />
    <script>document.documentElement.classList.add('js');</script>
    <script type="application/ld+json">{schema(page_key, locale, data["title"], data["description"])}</script>
  </head>'''


# ---------------------------------------------------------------------------
# Brand and icons. Both are ports of the app, not look-alikes: the family mark
# is Rodinka/src/utils/familyMark.ts drawn with the same petal geometry, and the
# four navigation glyphs are the app's own navigation icons.

FAMILY_MARK_BOX = 64
STATIC_FAMILY_MARK_COLORS = ("#e9785e", "#f2c85b", "#8bc6ad")


def _num(value: float) -> str:
    text = f"{value:.3f}".rstrip("0").rstrip(".")
    return "0" if text in ("", "-0") else text


def _clamp(value: float, low: float, high: float) -> float:
    return min(high, max(low, value))


def static_family_mark_slots() -> list[dict]:
    scale = 1.355
    widths = [value * scale for value in (11, 12, 11)]
    heights = [value * scale for value in (18, 27, 21)]
    rotations = (-14, 0, 12)
    gap = 2 * scale
    cursor = FAMILY_MARK_BOX / 2 - (sum(widths) + gap * 2) / 2
    slots = []
    for width, height, rotation in zip(widths, heights, rotations):
        slots.append({"cx": cursor + width / 2, "cy": FAMILY_MARK_BOX / 2, "width": width, "height": height, "rotation": rotation})
        cursor += width + gap
    return slots


def family_mark_slots(roles: list[str]) -> list[dict]:
    """createFamilyMarkSlots(): one petal per person, adults a little taller."""
    total = max(1, len(roles))
    width = _clamp(54 / (1 + (total - 1) * 1.16), 9.5, 15.5)
    step = min(width * 1.16, (54 - width) / (total - 1)) if total > 1 else 0
    tallest = _clamp(width * 2.6, 28, 42)
    first = FAMILY_MARK_BOX / 2 - (width + step * (total - 1)) / 2 + width / 2
    center = (total - 1) / 2
    spread = center or 1
    wobble = (0, 0.04, -0.03, 0.02, -0.04, 0.03, -0.02, 0.05)
    role_height = {"parent": 1.06, "child": 0.9}
    slots = []
    for index, role in enumerate(roles):
        offset = (index - center) / spread
        height = tallest * (1 - 0.24 * abs(offset)) * role_height[role] * (1 + wobble[index % len(wobble)])
        slots.append({"cx": first + step * index, "cy": FAMILY_MARK_BOX / 2, "width": width, "height": _clamp(height, tallest * 0.6, 42), "rotation": 13 * offset})
    return slots


def _bounds(slots: list[dict]) -> tuple[float, float]:
    lefts, rights = [], []
    for slot in slots:
        radians = math.radians(abs(slot["rotation"]))
        half = (slot["width"] * math.cos(radians) + slot["height"] * math.sin(radians)) / 2
        lefts.append(slot["cx"] - half)
        rights.append(slot["cx"] + half)
    return min(lefts), max(rights)


def family_mark_row(roles: list[str], pets: int) -> tuple[list[dict], list[dict]]:
    """layoutFamilyMarkRow(): the people, then at most two smaller pet petals."""
    members = family_mark_slots(roles)
    pets = min(max(0, pets), 2)
    if not pets:
        return members, []
    box = FAMILY_MARK_BOX / 2
    member_width = members[0]["width"]

    def compose(scale: float) -> tuple[list[dict], list[dict]]:
        scaled = [dict(slot, cx=box + (slot["cx"] - box) * scale, width=slot["width"] * scale, height=slot["height"] * scale) for slot in members]
        cursor = _bounds(scaled)[1]
        tallest = max(slot["height"] for slot in scaled)
        pet_slots = []
        for index in range(pets):
            width = member_width * 0.48 * scale
            height = tallest * (0.5, 0.38)[index]
            rotation = (5, 7)[index]
            radians = math.radians(rotation)
            half = (width * math.cos(radians) + height * math.sin(radians)) / 2
            cx = cursor + member_width * 0.16 * scale + half
            cursor = cx + half
            pet_slots.append({"cx": cx, "cy": box, "width": width, "height": height, "rotation": rotation})
        return scaled, pet_slots

    scaled, pet_slots = compose(1)
    left, right = _bounds(scaled + pet_slots)
    scale = min(1, 60 / (right - left))
    if scale < 1:
        scaled, pet_slots = compose(scale)
    left, right = _bounds(scaled + pet_slots)
    shift = box - (left + right) / 2
    return [dict(slot, cx=slot["cx"] + shift) for slot in scaled], [dict(slot, cx=slot["cx"] + shift) for slot in pet_slots]


def _petal(slot: dict, fill: str, extra: str = "") -> str:
    half_width, half_height = slot["width"] / 2, slot["height"] / 2
    corner_x, corner_y = slot["width"] * 0.45, slot["height"] * 0.45
    left, right, bottom = -half_width, half_width, half_height
    path = (
        f"M {_num(left)} 0 A {_num(half_width)} {_num(half_height)} 0 0 1 {_num(right)} 0 "
        f"L {_num(right)} {_num(bottom - corner_y)} A {_num(corner_x)} {_num(corner_y)} 0 0 1 {_num(right - corner_x)} {_num(bottom)} "
        f"L {_num(left + corner_x)} {_num(bottom)} A {_num(corner_x)} {_num(corner_y)} 0 0 1 {_num(left)} {_num(bottom - corner_y)} Z"
    )
    return f'<path d="{path}" transform="translate({_num(slot["cx"])} {_num(slot["cy"])}) rotate({_num(slot["rotation"])})" fill="{fill}"{extra}/>'


def family_mark(slots: list[dict], fills: list[str], pet_slots: list[dict] | None = None) -> str:
    petals = "".join(_petal(slot, fill) for slot, fill in zip(slots, fills))
    petals += "".join(_petal(slot, "var(--text-muted)", ' opacity=".55"') for slot in pet_slots or [])
    return f'<svg class="family-mark" viewBox="0 0 64 64" aria-hidden="true" focusable="false">{petals}</svg>'


STATIC_MARK = family_mark(static_family_mark_slots(), list(STATIC_FAMILY_MARK_COLORS))

# The illustrative household the homepage draws: two adults, two children and a
# dog, in member identity colours. Only ever decorative (aria-hidden).
DEMO_FAMILY = (
    ("Martin", "MA", "parent", "var(--member-blue)"),
    ("Klára", "KL", "parent", "var(--member-coral)"),
    ("Ema", "EM", "child", "var(--member-honey)"),
    ("Tobiáš", "TO", "child", "var(--member-mint)"),
)
DEMO_FILLS = [member[3] for member in DEMO_FAMILY]
DEMO_MARK = family_mark(family_mark_slots([member[2] for member in DEMO_FAMILY]), DEMO_FILLS)
_PORTRAIT_SLOTS, _PORTRAIT_PETS = family_mark_row([member[2] for member in DEMO_FAMILY], 1)
DEMO_PORTRAIT = family_mark(_PORTRAIT_SLOTS, DEMO_FILLS, _PORTRAIT_PETS)

ICONS = {
    # The app's navigation glyphs (Rodinka/src/components/icons/navigation).
    "today": '<path d="M4.75 10.25 12 4.5l7.25 5.75V18c0 .97-.78 1.75-1.75 1.75h-11c-.97 0-1.75-.78-1.75-1.75v-7.75Z"/><path d="M9.5 19.75v-5h5v5"/><circle cx="18.6" cy="6.1" r="1.7" fill="var(--nav-icon-accent)" stroke="none"/>',
    "calendar": '<rect x="4.25" y="5.75" width="15.5" height="14" rx="3.2"/><path d="M7.75 3.9v3.45M16.25 3.9v3.45M4.9 9.5h14.2"/><rect x="9.2" y="12.2" width="5.6" height="4.8" rx="1.4" fill="var(--nav-icon-accent)" stroke="none"/>',
    "memories": '<path d="M7.6 5.35h9.15a2.85 2.85 0 0 1 2.85 2.85v7.3"/><rect x="4.4" y="8" width="13.2" height="11.4" rx="2.9"/><path d="M11 15.9c-2.05-1.35-3.05-2.4-3.05-3.5a1.7 1.7 0 0 1 3.05-1 1.7 1.7 0 0 1 3.05 1c0 1.1-1 2.15-3.05 3.5Z" stroke="var(--nav-icon-accent)" stroke-width="1.5"/>',
    "planning": '<rect x="5" y="3.75" width="14" height="16.5" rx="3.2"/><path d="m8.3 8.65 1.15 1.15 2.1-2.1" stroke="var(--nav-icon-accent)" stroke-width="2"/><path d="M13.35 8.75h2.75"/><path d="m8.3 13 1.15 1.15 2.1-2.1" stroke="var(--nav-icon-accent)" stroke-width="2"/><path d="M13.35 13.1h2.75M8.3 17.35h7.8"/>',
    # Module glyphs in the same 24-unit, 1.9 stroke language.
    "chores": '<rect x="4.5" y="4.5" width="15" height="15" rx="4"/><path d="m8.6 12.2 2.3 2.3 4.6-4.9"/>',
    "shopping": '<path d="M4.5 9.5h15l-1.5 8.2a2.2 2.2 0 0 1-2.2 1.8H8.2A2.2 2.2 0 0 1 6 17.7L4.5 9.5Z"/><path d="m9 9.5 2.2-5M15 9.5l-2.2-5M9.5 13.5v2.5M14.5 13.5v2.5"/>',
    "school": '<path d="M7 9.5a5 5 0 0 1 10 0v9a1.5 1.5 0 0 1-1.5 1.5h-7A1.5 1.5 0 0 1 7 18.5v-9Z"/><path d="M10 4.6h4M9.5 13h5v3.5h-5z"/>',
    "trips": '<path d="M9 5.5 4.5 7.2v11.3L9 16.8l6 1.7 4.5-1.7V5.5L15 7.2 9 5.5Z"/><path d="M9 5.5v11.3M15 7.2v11.3"/>',
    "documents": '<rect x="3.5" y="5.5" width="17" height="13" rx="2.6"/><circle cx="9" cy="11" r="2"/><path d="M6.4 15.6c.6-1.2 1.5-1.8 2.6-1.8s2 .6 2.6 1.8M14 10h3.5M14 13.3h3.5"/>',
    "meals": '<path d="M4.5 11h15v4.5a4 4 0 0 1-4 4h-7a4 4 0 0 1-4-4V11Z"/><path d="M3 11h18M9.2 7.6c0-1 .8-1.3.8-2.3M13 7.6c0-1 .8-1.3.8-2.3"/>',
    "sparkle": '<path d="M12 4.5 13.6 9l4.4 1.5-4.4 1.6L12 16.5l-1.6-4.4L6 10.5 10.4 9 12 4.5Z"/><path d="M18 16.2v3.2M16.4 17.8h3.2"/>',
    "child": '<circle cx="12" cy="12" r="7.8"/><path d="M9 13.8c.8.9 1.8 1.4 3 1.4s2.2-.5 3-1.4M9.4 10h.01M14.6 10h.01"/>',
    "chat": '<path d="M5 7a2.5 2.5 0 0 1 2.5-2.5h9A2.5 2.5 0 0 1 19 7v6.5a2.5 2.5 0 0 1-2.5 2.5H11l-4 3.5V16a2 2 0 0 1-2-2V7Z"/><path d="M9 9.5h6M9 12.5h4"/>',
    "health": '<path d="M12 19.5s-7.2-4.3-7.2-9.4A3.9 3.9 0 0 1 12 7.9a3.9 3.9 0 0 1 7.2 2.2c0 5.1-7.2 9.4-7.2 9.4Z"/><path d="M8 12.6h2l1.1-2 1.8 3.8 1.1-1.8h2"/>',
    "lock": '<rect x="5" y="10.5" width="14" height="9.5" rx="2.6"/><path d="M8.5 10.5V8a3.5 3.5 0 0 1 7 0v2.5M12 14.2v2.3"/>',
    "shield": '<path d="M12 4 5.5 6.6v5c0 4 2.8 7 6.5 8.4 3.7-1.4 6.5-4.4 6.5-8.4v-5L12 4Z"/><path d="m9.2 12 2 2 3.8-4"/>',
    "image": '<rect x="4" y="5" width="16" height="14" rx="3"/><circle cx="9" cy="10" r="1.6"/><path d="m5 17 4.5-4 3 2.5 2.5-2 4 3.5"/>',
    "offline": '<path d="M5 9.6a10.4 10.4 0 0 1 14 0M7.8 12.7a6.4 6.4 0 0 1 8.4 0M10.5 15.7a2.4 2.4 0 0 1 3 0M12 19h.01"/>',
    "languages": '<path d="M4.5 6.2h9M9 4.2v2c0 4-2.2 7-4.5 8.5M6.6 10.2c1.3 2 3.3 3.5 5.4 4.4"/><path d="m13 20 3.5-8 3.5 8M14.2 17.4h4.6"/>',
    "bell": '<path d="M6.5 16.5V11a5.5 5.5 0 0 1 11 0v5.5l1.5 1.5H5l1.5-1.5Z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>',
    "devices": '<rect x="3.5" y="5" width="12.5" height="9.5" rx="2"/><path d="M7 19h5.5M9.75 14.5V19"/><rect x="16" y="9" width="5" height="10.5" rx="1.6"/>',
    "box": '<path d="M4.5 8 12 4.5 19.5 8v8L12 19.5 4.5 16V8Z"/><path d="M4.5 8 12 11.5 19.5 8M12 11.5v8"/>',
}


def icon(name: str) -> str:
    return (
        '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" '
        f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'
    )


def tone_icon(tone: str, name: str) -> str:
    return f'<span class="tone-icon" data-tone="{tone}" aria-hidden="true">{icon(name)}</span>'


# Module tone and glyph per topic page: the category token the app uses for that
# module, so a page reads in the same colour as the screen it describes.
TOPIC_TONES = {
    "planner": ("activities", "planning"),
    "calendar": ("calendar", "calendar"),
    "shopping": ("family", "shopping"),
    "chores": ("tasks", "chores"),
    "meals": ("meals", "meals"),
    "trips": ("travel", "trips"),
    "memories": ("memories", "memories"),
    "documents": ("documents", "documents"),
    "baby": ("memories", "child"),
    "app": ("calendar", "today"),
}


# ---------------------------------------------------------------------------
# Page chrome

def language_switcher(page_key: str, locale: str) -> str:
    labels = {"cs": "CZ", "sk": "SK", "en": "EN"}
    names = {"cs": "Čeština", "sk": "Slovenčina", "en": "English"}
    links = []
    for code in ("cs", "sk", "en"):
        current = ' aria-current="page"' if code == locale else ""
        links.append(f'<a href="{PATHS[page_key][code]}" lang="{code}" hreflang="{code}" aria-label="{names[code]}"{current}>{labels[code]}</a>')
    return f'<div class="language-switcher" role="group" aria-label="{esc(LOCALES[locale]["language_label"])}">' + '<span aria-hidden="true">·</span>'.join(links) + "</div>"


NAV_KEYS = ("calendar", "chores", "shopping", "meals", "trips", "memories")


def site_header(page_key: str, locale: str) -> str:
    cfg = LOCALES[locale]
    current = ' aria-current="page"'
    links = "".join(
        f'<a href="{PATHS[key][locale]}"{current if key == page_key else ""}>{esc(cfg["nav"][key])}</a>'
        for key in NAV_KEYS
    )
    return f'''    <a class="skip-link" href="#main">{esc(cfg["skip"])}</a>
    <header class="site-header">
      <div class="site-header-inner">
        <a class="brand" href="{cfg["home_path"]}" aria-label="Rodinka, {esc(cfg["home"])}">{STATIC_MARK}<span>Rodinka</span></a>
        <button class="menu-button" type="button" aria-label="{esc(cfg["menu"])}" aria-expanded="false" aria-controls="main-navigation"><span></span><span></span></button>
        <nav class="nav" id="main-navigation" aria-label="{esc(cfg["primary_nav"])}">
          {links}
          <a class="nav-cta" href="{APP_URL}" data-analytics-location="header">{esc(cfg["open_app"])} <span aria-hidden="true">→</span></a>
          <div class="nav-preferences">
            {language_switcher(page_key, locale)}
            <button class="theme-switcher" type="button" data-theme-switch data-light-label="{esc(cfg['theme_light_label'])}" data-dark-label="{esc(cfg['theme_dark_label'])}" aria-label="{esc(cfg['theme_dark_label'])}" aria-pressed="false"><svg class="theme-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5 8.5 8.5 0 1 0 20.5 14.5Z"/></svg><svg class="theme-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M4.93 4.93l1.42 1.42m11.3 11.3 1.42 1.42M2 12h2m16 0h2M4.93 19.07l1.42-1.42m11.3-11.3 1.42-1.42"/></svg></button>
          </div>
        </nav>
      </div>
    </header>'''


FOOTER_KEYS = ("planner", "calendar", "chores", "shopping", "meals", "trips", "memories", "documents", "baby")


def site_footer(locale: str) -> str:
    cfg = LOCALES[locale]
    feature_links = "".join(f'<li><a href="{PATHS[key][locale]}">{esc(LLMS_LABELS[locale][key])}</a></li>' for key in FOOTER_KEYS)
    return f'''    <footer class="site-footer">
      <div class="site-footer-inner">
        <div class="footer-brand"><a class="brand" href="{cfg["home_path"]}">{STATIC_MARK}<span>Rodinka</span></a><span class="serif">{esc(cfg["claim"])}</span><p>{esc(cfg["footer_text"])}</p></div>
        <nav class="footer-nav" aria-label="{esc(cfg["features"])}"><h2>{esc(cfg["features"])}</h2><ul>{feature_links}</ul></nav>
        <nav class="footer-nav" aria-label="{esc(cfg["about"])}"><h2>{esc(cfg["about"])}</h2><ul><li><a href="{PATHS["app"][locale]}">{esc(cfg["app_label"])}</a></li><li><a href="{APP_URL}" data-analytics-location="footer">{esc(cfg["open_app"])}</a></li><li><a href="{SUPPORT_URL}" target="_blank" rel="noopener">{esc(cfg["support_label"])}</a></li><li><button class="footer-link" type="button" data-cookie-settings>{esc(cfg["cookie_settings"])}</button></li></ul></nav>
      </div>
      <p class="copyright">{esc(cfg["copyright"])}</p>
    </footer>'''


def page_shell(page_key: str, locale: str, data: dict, main: str) -> str:
    return f'''<!doctype html>
<html lang="{locale}">
{head(page_key, locale, data)}
  <body>
{analytics_body()}
{site_header(page_key, locale)}
    <main id="main">
{main}
    </main>
{site_footer(locale)}
{consent_panel(locale)}
    <script src="/script.js?v={ASSET_VERSION}" defer></script>
  </body>
</html>
'''


# ---------------------------------------------------------------------------
# Product proof: real screenshots where the repository has them, and drawings of
# the app's own components where it does not (always aria-hidden, with the same
# information in visible text next to them).

def product_figure(page_key: str, locale: str) -> str:
    proof = PRODUCT_PROOFS[page_key]
    src = localized_product_src(proof["src"], locale)
    return f'''<figure class="proof-figure">
          <img class="proof-image" src="{src}" width="{PRODUCT_IMAGE_WIDTH}" height="{PRODUCT_IMAGE_HEIGHT}" loading="lazy" decoding="async" alt="{esc(proof["alt"][locale])}" />
          <figcaption>{esc(proof["caption"][locale])}</figcaption>
        </figure>'''


def trip_mock(locale: str) -> str:
    mock = TRIP_MOCK[locale]
    tips = ""
    mine, pinned = ' class="is-mine"', ' class="is-pinned"'
    for index, (title, place, votes) in enumerate(mock["tips"]):
        selected = index == 0
        vote_pills = "".join(
            f'<span{mine if selected and slot == 0 else ""}>{symbol} {count}</span>'
            for slot, (symbol, count) in enumerate(zip(("👍", "😐", "👎"), votes))
        )
        badge = f'<span class="mock-tip-badge">{esc(mock["selected"])}</span>' if selected else ""
        tips += f'<div class="mock-tip{" is-selected" if selected else ""}"><div class="mock-tip-head"><div><strong>{esc(title)}</strong><small>{esc(place)}</small></div>{badge}</div><div class="mock-votes">{vote_pills}</div></div>'
    pills = "".join(f'<span{pinned if index == len(mock["pills"]) - 1 else ""}>{esc(pill)}</span>' for index, pill in enumerate(mock["pills"]))
    return f'''<figure class="app-mock">
          <div aria-hidden="true"><div class="mock-card"><p class="mock-kicker">{esc(mock["kicker"])}</p><p class="mock-title">{esc(mock["title"])}</p><div class="mock-pills">{pills}</div><p class="mock-note"><b>Klára:</b> {esc(mock["note"])}</p><div class="mock-tips">{tips}</div></div></div>
          <figcaption class="mock-caption">{esc(mock["caption"])}</figcaption>
        </figure>'''


def render_direct_answer(page_key: str, locale: str) -> str:
    labels = {"cs": "STRUČNÁ ODPOVĚĎ", "sk": "STRUČNÁ ODPOVEĎ", "en": "DIRECT ANSWER"}
    question, answer = DIRECT_ANSWERS[locale][page_key]
    if page_key in PRODUCT_PROOFS:
        figure = product_figure(page_key, locale)
    elif page_key == "trips":
        figure = trip_mock(locale)
    else:
        figure = ""
    modifier = "" if figure else " proof-section--text"
    figure_markup = f"\n        {figure}" if figure else ""
    return f'''      <section class="proof-section direct-answer{modifier}" aria-labelledby="direct-answer-{page_key}">
        <div class="proof-copy">
          <p class="section-kicker">{labels[locale]}</p>
          <h2 id="direct-answer-{page_key}">{esc(question)}</h2>
          <p>{esc(answer)}</p>
        </div>{figure_markup}
      </section>'''


def _petals(members: tuple[int, ...]) -> str:
    return "".join(
        f'<i class="petal{" is-child" if DEMO_FAMILY[index][2] == "child" else ""}" style="--c:{DEMO_FAMILY[index][3]}"></i>'
        for index in members
    )


def _day_at(hour: float) -> str:
    # The app's day line runs 7–21 h.
    return f"{(hour - 7) / 14 * 100:.2f}%"


def render_phone(locale: str) -> str:
    """The Today screen as the app draws it: header, hero with the day line,
    today's programme, the Rodinka Today card and the five-tab navigation."""
    phone = HOME_PHONE[locale]
    stops = ""
    for hour, people, time, who in ((7.75, (3, 0), "7:45", phone["rows"][0][2].split(" · ")[0]), (15, (2, 1), "15:00", phone["rows"][1][2].split(" · ")[0]), (18.5, (), "18:30", phone["dinner"])):
        figure = _petals(people) if people else '<i class="day-line-meal"></i>'
        stops += f'<span class="day-line-stop" style="--at:{_day_at(hour)}"><span class="day-line-figure">{figure}</span><span class="day-line-label"><b>{time}</b><span>{esc(who)}</span></span></span>'
    avatars = ((3, 0), (2, 1), None)
    rows = ""
    for (time, title, meta), people in zip(phone["rows"], avatars):
        faces = (
            "".join(f'<i class="avatar" style="--c:{DEMO_FAMILY[index][3]}">{DEMO_FAMILY[index][1]}</i>' for index in people)
            if people else f'<i class="avatar is-meal">{icon("meals")}</i>'
        )
        rows += f'<div class="app-row"><span class="app-row-time">{time}</span><span class="avatars">{faces}</span><span><strong>{esc(title)}</strong><small>{esc(meta)}</small></span></div>'
    options = "".join(
        f'<div class="daily-option{" is-selected" if index == 0 else ""}"><span>{esc(label)}</span><small>{esc(tally)}</small></div>'
        for index, (label, tally) in enumerate(phone["options"])
    )
    nav_icons = ("today", "calendar", "memories", "planning")
    active = ' class="is-active"'
    nav = "".join(f'<span{active if index == 0 else ""}>{icon(name)}{esc(label)}</span>' for index, (name, label) in enumerate(zip(nav_icons, phone["nav"])))
    nav += f'<span>{DEMO_MARK}{esc(phone["nav"][4])}</span>'
    return f'''<div class="phone">
            <div class="phone-screen">
              <div class="phone-status"><span>9:41</span><i><b></b></i></div>
              <div class="app-header">{DEMO_MARK}<span class="app-title">Rodinka<span>{esc(phone["family"])}</span></span><span class="app-header-actions"><span class="app-icon">{icon("chat")}</span><span class="app-icon">{icon("bell")}<b>1</b></span></span></div>
              <div class="app-body">
                <div class="today-card"><p class="today-greeting">{esc(phone["greeting"])}</p><p class="today-date">{esc(phone["date"])}</p><p class="today-summary">{esc(phone["summary"])}</p><div class="day-line"><span class="day-line-past" style="--at:{_day_at(12.5)}"></span><span class="day-line-now" style="--at:{_day_at(12.5)}"></span>{stops}</div></div>
                <p class="app-section-title">{esc(phone["program"])}</p>
                <div class="app-list">{rows}</div>
                <p class="app-section-title">{DEMO_MARK}{esc(phone["daily_title"])}</p>
                <div class="daily-card"><p class="daily-eyebrow">{esc(phone["daily_eyebrow"])}</p><p class="daily-question">{esc(phone["question"])}</p><div class="daily-options">{options}</div><p class="daily-meta">{esc(phone["voted"])}</p></div>
              </div>
              <div class="bottom-nav">{nav}</div>
            </div>
          </div>'''


def render_focus(locale: str) -> str:
    data = HOME_FOCUS[locale]
    cfg = LOCALES[locale]
    cards = ""
    for tone, glyph, title, text, chips, links in data["cards"]:
        chip_items = "".join(f"<li>{esc(chip)}</li>" for chip in chips)
        link_items = "".join(f'<a class="card-link" href="{PATHS[key][locale]}">{esc(label)} <span aria-hidden="true">→</span></a>' for key, label in links)
        cards += f'<article class="focus-card reveal" data-tone="{tone}">{tone_icon(tone, glyph)}<h3>{esc(title)}</h3><p>{esc(text)}</p><ul class="chips">{chip_items}</ul><div class="card-links">{link_items}</div></article>'
    cta_title, cta_text = data["cta"]
    cards += f'<article class="focus-card focus-card--cta reveal"><h3>{esc(cta_title)}</h3><p>{esc(cta_text)}</p><a class="button button-primary" href="{APP_URL}" data-analytics-location="content">{esc(cfg["start"])} <span aria-hidden="true">→</span></a></article>'
    return f'''      <section class="section" id="funkce" aria-labelledby="focus-title">
        <div class="section-inner">
          <div class="section-head reveal"><p class="section-kicker">{esc(data["kicker"])}</p><h2 class="section-title" id="focus-title">{esc(data["title"])}</h2><p class="section-lead">{esc(data["lead"])}</p></div>
          <div class="focus-grid">{cards}</div>
        </div>
      </section>'''


def render_start(locale: str) -> str:
    data = HOME_START[locale]
    steps = "".join(f'<li class="start-step"><div><h3>{esc(title)}</h3><p>{esc(text)}</p></div></li>' for title, text in data["steps"])
    members = "".join(f'<li><i class="petal" style="--c:{member[3]}"></i>{esc(member[0])}</li>' for member in DEMO_FAMILY)
    members += f'<li><i class="petal" style="--c:var(--text-muted);opacity:.55"></i>{esc(data["pet"])}</li>'
    kit_title, kit_text = data["kit"]
    return f'''      <section class="section band" id="jak-to-funguje" aria-labelledby="start-title">
        <div class="section-inner">
          <div class="section-head reveal"><p class="section-kicker">{esc(data["kicker"])}</p><h2 class="section-title" id="start-title">{esc(data["title"])}</h2><p class="section-lead">{esc(data["lead"])}</p></div>
          <div class="start-grid">
            <div class="reveal"><ol class="start-steps">{steps}</ol><aside class="kit-note">{tone_icon("family", "box")}<div><h3>{esc(kit_title)}</h3><p>{esc(kit_text)}</p></div></aside></div>
            <figure class="portrait reveal">{DEMO_PORTRAIT}<p class="portrait-name" aria-hidden="true">{esc(data["family"])}</p><ul class="portrait-members" aria-hidden="true">{members}</ul><figcaption>{esc(data["caption"])}</figcaption></figure>
          </div>
        </div>
      </section>'''


def render_family_layer(locale: str) -> str:
    data = HOME_FAMILY_LAYER[locale]
    cfg = LOCALES[locale]
    cards = "".join(
        f'<article class="layer-card reveal" data-tone="{tone}">{tone_icon(tone, glyph)}<div><h3>{esc(title)}</h3><p>{esc(text)}</p>'
        f'<a class="card-link" href="{PATHS[key][locale]}">{esc(cfg["learn_more"])} <span aria-hidden="true">→</span></a></div></article>'
        for tone, glyph, title, text, key in data["cards"]
    )
    return f'''      <section class="section" aria-labelledby="family-layer-title">
        <div class="section-inner">
          <div class="section-head reveal"><p class="section-kicker">{esc(data["kicker"])}</p><h2 class="section-title" id="family-layer-title">{esc(data["title"])}</h2><p class="section-lead">{esc(data["lead"])}</p></div>
          <div class="layer-grid">{cards}</div>
        </div>
      </section>'''


def render_story(story_id: str, story: dict, figure: str, link_key: str, locale: str, reverse: bool = False) -> str:
    modifier = " proof-section--reverse" if reverse else ""
    points = ""
    if story.get("points"):
        points = '<ul class="story-points">' + "".join(f'<li style="--c:{color}">{esc(point)}</li>' for point, color in zip(story["points"], ("var(--brand-coral)", "var(--brand-honey)", "var(--brand-mint)", "var(--brand-blue)"))) + "</ul>"
    return f'''      <section class="proof-section product-story{modifier} reveal" aria-labelledby="{story_id}">
        <div class="proof-copy">
          <p class="section-kicker">{esc(story["kicker"])}</p>
          <h2 id="{story_id}">{esc(story["title"])}</h2>
          <p>{esc(story["text"])}</p>{points}
          <a class="card-link" href="{PATHS[link_key][locale]}">{esc(story["link"])} <span aria-hidden="true">→</span></a>
        </div>
        {figure}
      </section>'''


def story_figure(src: str, story: dict, locale: str) -> str:
    return f'''<figure class="proof-figure">
          <img class="proof-image" src="{localized_product_src(src, locale)}" width="{PRODUCT_IMAGE_WIDTH}" height="{PRODUCT_IMAGE_HEIGHT}" loading="lazy" decoding="async" alt="{esc(story["alt"])}" />
          <figcaption>{esc(story["caption"])}</figcaption>
        </figure>'''


def render_stories(locale: str) -> str:
    trips = render_story("trips-story-title", HOME_TRIPS_STORY[locale], trip_mock(locale), "trips", locale)
    baby = render_story("baby-story-title", HOME_BABY_STORY[locale], story_figure(HOME_BABY_STORY["src"], HOME_BABY_STORY[locale], locale), "baby", locale, reverse=True)
    memories = render_story("memory-story-title", HOME_MEMORY_STORY[locale], story_figure(HOME_MEMORY_STORY["src"], HOME_MEMORY_STORY[locale], locale), "memories", locale)
    return f'''      <div class="section stories">
{trips}
{memories}
{baby}
      </div>'''


def render_trust(locale: str) -> str:
    data = HOME_TRUST[locale]
    items = "".join(f'<li>{tone_icon("neutral", glyph)}<div><h3>{esc(title)}</h3><p>{esc(text)}</p></div></li>' for glyph, title, text in data["items"])
    return f'''      <section class="section band" aria-labelledby="trust-title">
        <div class="section-inner">
          <div class="section-head reveal"><p class="section-kicker">{esc(data["kicker"])}</p><h2 class="section-title" id="trust-title">{esc(data["title"])}</h2><p class="section-lead">{esc(data["lead"])}</p></div>
          <ul class="trust-grid reveal">{items}</ul>
        </div>
      </section>'''


def render_directory(locale: str) -> str:
    data = HOME[locale]
    items = "".join(
        f'<li><a href="{PATHS[key][locale]}"><strong>{esc(TOPICS[locale][key]["h1"])}</strong><span>{esc(TOPICS[locale][key]["card"])}</span></a></li>'
        for key in TOPIC_KEYS
    )
    return f'''      <section class="section" aria-labelledby="directory-title">
        <div class="section-inner">
          <div class="section-head reveal"><p class="section-kicker">{esc(data["directory_kicker"])}</p><h2 class="section-title" id="directory-title">{esc(data["directory_title"])}</h2><p class="section-lead">{esc(data["directory_lead"])}</p></div>
          <ul class="directory-list reveal">{items}</ul>
        </div>
      </section>'''


def render_home_spot(locale: str) -> str:
    spot = HOME_SPOT.get(locale)
    if not spot:
        return ""
    stem = spot["stem"]
    return f'''      <section class="spot-section" aria-labelledby="spot-title">
        <div class="section-head reveal"><p class="section-kicker">{esc(spot["kicker"])}</p><h2 class="section-title" id="spot-title">{esc(spot["title"])}</h2><p class="section-lead">{esc(spot["lead"])}</p></div>
        <div class="spot reveal">
          <div class="spot-frame">
            <video class="spot-video" controls playsinline preload="none" aria-labelledby="spot-title" data-src-tall="{stem}-9x16.mp4"><source src="{stem}-16x9.mp4" type="video/mp4" /></video>
            <a class="spot-cta" href="{APP_URL}" data-analytics-location="video" data-from="{spot["cta_from"]}" data-width="{spot["cta_width"]}" hidden>{esc(spot["cta"])}</a>
            <button class="spot-cover" type="button" aria-label="{esc(spot["label"])}">
              <picture><source media="{SPOT_TALL_MEDIA}" srcset="{stem}-9x16.webp" width="720" height="1280" /><img src="{stem}-16x9.webp" width="1600" height="900" alt="" loading="lazy" decoding="async" /></picture>
              <span class="spot-play" aria-hidden="true"><span class="spot-play-icon"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z" /></svg></span><span><strong>{esc(spot["play"])}</strong><small>{esc(spot["meta"])}</small></span></span>
            </button>
          </div>
        </div>
      </section>'''


def series_time(seconds: int) -> str:
    return f"{seconds // 60}:{seconds % 60:02d}"


def render_short(episode: dict, locale: str, tone: str, link: str = "", attrs: str = "") -> str:
    """One Každodenní Rodinka episode: a 9:16 frame whose poster is a play
    button until the first click (the video is fetched only then), with the
    episode's question and what happens in it underneath."""
    series = SERIES[locale]
    stem = f"/assets/video/{episode['stem']}"
    label = series["label"].format(title=episode["title"], seconds=episode["seconds"])
    meta = series["meta"].format(time=series_time(episode["seconds"]))
    return f'''<figure class="short" data-tone="{tone}"{attrs}>
          <div class="short-frame">
            <video class="short-video" controls playsinline preload="none" aria-label="{esc(episode["title"])}"><source src="{stem}.mp4" type="video/mp4" /></video>
            <button class="short-cover" type="button" aria-label="{esc(label)}">
              <img src="{stem}.webp" width="{SERIES_POSTER_WIDTH}" height="{SERIES_POSTER_HEIGHT}" alt="" loading="lazy" decoding="async" />
              <span class="short-play" aria-hidden="true"><span class="short-play-icon"><svg viewBox="0 0 24 24"><path d="M8 5.5v13l10.5-6.5z" /></svg></span><span><strong>{esc(series["play"])}</strong><small>{esc(meta)}</small></span></span>
            </button>
          </div>
          <figcaption><strong>{esc(episode["title"])}</strong> {esc(episode["text"])}{link}</figcaption>
        </figure>'''


def topic_short(page_key: str, locale: str) -> str:
    series = SERIES.get(locale)
    episode = next((item for item in series["episodes"] if item["page"] == page_key), None) if series else None
    if not episode:
        return ""
    return render_short(episode, locale, TOPIC_TONES[page_key][0])


def render_series(locale: str) -> str:
    """The whole series on the homepage: one player showing the chosen episode
    and the list of episodes next to it. Without JavaScript the list is hidden
    and every episode stays in the page as its own player."""
    series = SERIES.get(locale)
    if not series:
        return ""
    shorts, picks = [], ""
    for index, episode in enumerate(series["episodes"]):
        key = episode.get("link") or episode["page"]
        panel = f"series-{index + 1:02d}"
        active = index == 0
        link = f' <a class="card-link" href="{PATHS[key][locale]}">{esc(LLMS_LABELS[locale][key])} <span aria-hidden="true">→</span></a>'
        shorts.append(render_short(episode, locale, TOPIC_TONES[key][0], link, f' id="{panel}"{" data-active" if active else ""}'))
        picks += (
            f'<li><button class="series-pick" type="button" aria-controls="{panel}" aria-current="{"true" if active else "false"}">'
            f'<span class="series-pick-text"><span class="series-question">{esc(episode["title"])}</span><span class="series-topic">{esc(LLMS_LABELS[locale][key])}</span></span>'
            f'<span class="series-time"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l10.5-6.5z" /></svg>{series_time(episode["seconds"])}</span></button></li>'
        )
    stage = "\n        ".join(shorts)
    return f'''      <section class="section series-section" aria-labelledby="series-title">
        <div class="section-inner">
          <div class="section-head reveal"><p class="section-kicker">{esc(series["kicker"])}</p><h2 class="section-title" id="series-title">{esc(series["title"])}</h2><p class="section-lead">{esc(series["lead"])}</p></div>
          <div class="series reveal">
            <div class="series-stage">
        {stage}
            </div>
            <ol class="series-list" aria-label="{esc(series["list"])}">{picks}</ol>
          </div>
        </div>
      </section>'''


def render_home(locale: str) -> str:
    data = HOME[locale]
    cfg = LOCALES[locale]
    proof = "".join(f"<li>{esc(item)}</li>" for item in data["proof"])
    journey = "".join(f"<li><b>{esc(title)}</b><small>{esc(text)}</small></li>" for title, text in data["journey"])
    main = f'''      <div class="home-hero">
        <section class="hero">
          <div class="hero-copy reveal">
            <p class="eyebrow">{STATIC_MARK}{esc(data["eyebrow"])}</p>
            <h1>{esc(data["h1"])}</h1>
            <p class="brand-line">{esc(cfg["claim"])}</p>
            <p class="hero-lead">{esc(data["lead"])}</p>
            <div class="hero-actions"><a class="button button-primary button-lg" href="{APP_URL}" data-analytics-location="hero">{esc(cfg["start"])} <span aria-hidden="true">→</span></a><a class="text-link" href="#jak-to-funguje">{esc(data["how_link"])} <span aria-hidden="true">↓</span></a></div>
            <ul class="hero-proof">{proof}</ul>
            <div class="trust-row">{DEMO_MARK}<p><strong>{esc(data["trust_title"])}</strong><br />{esc(data["trust_text"])}</p></div>
          </div>
          <div class="hero-visual" aria-hidden="true">
          {render_phone(locale)}
          </div>
        </section>
      </div>
{render_direct_answer("home", locale)}
{render_home_spot(locale)}
{render_focus(locale)}
{render_series(locale)}
{render_start(locale)}
{render_family_layer(locale)}
{render_stories(locale)}
{render_trust(locale)}
{render_directory(locale)}
      <section class="section band"><figure class="family-quote reveal">{STATIC_MARK}<blockquote><p>{esc(data["quote"])}</p></blockquote><figcaption>{esc(data["quote_by"])}</figcaption></figure></section>
      <section class="cta-section" id="vyzkouset"><div class="cta-card reveal"><p class="section-kicker">{esc(data["cta_kicker"])}</p><h2>{esc(data["cta_title"])}</h2><p>{esc(data["cta_text"])}</p><div class="cta-actions"><a class="app-cta" href="{APP_URL}" data-analytics-location="content">{esc(cfg["start"])} <span aria-hidden="true">→</span></a><a class="cta-secondary" href="{APP_URL}" data-analytics-location="content">{esc(data["login"])}</a></div><ol class="mini-journey">{journey}</ol><div class="install-options"><h3>{esc(data["install_title"])}</h3><p>{esc(data["install_text"])}</p><a class="store-link" href="https://get.microsoft.com/installer/download/9nbxf0lqbmbj?referrer=appbadge">{esc(data["store"])} <span aria-hidden="true">→</span></a></div><small class="form-note">{esc(data["fine_print"])}</small></div></section>'''
    return page_shell("home", locale, data, main)


def render_topic(page_key: str, locale: str) -> str:
    data = TOPICS[locale][page_key]
    cfg = LOCALES[locale]
    tone, glyph = TOPIC_TONES[page_key]
    scenarios = "".join(f'<article class="scenario-card"><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for title, text in data["scenarios"])
    steps = "".join(f'<li><span>{i}</span><div><h3>{esc(title)}</h3><p>{esc(text)}</p></div></li>' for i, (title, text) in enumerate(data["steps"], 1))
    answers = "".join(f'<article class="answer"><h3>{esc(question)}</h3><p>{esc(answer)}</p></article>' for question, answer in data["answers"])
    related = "".join(
        f'<li><a href="{PATHS[key][locale]}"><strong>{esc(TOPICS[locale][key]["h1"])}</strong><span>{esc(TOPICS[locale][key]["card"])}</span><em>{esc(cfg["learn_more"])} →</em></a></li>'
        for key in RELATED[page_key]
    )
    # The series episode about this topic tells the problem section's story, so
    # it plays right next to it.
    short = topic_short(page_key, locale)
    problem_class = "content-section problem-section" + (" problem-section--short" if short else "")
    main = f'''      <article class="topic-page">
        <div class="topic-hero-wrap">
          <header class="topic-hero"><nav class="breadcrumbs" aria-label="{esc(cfg["breadcrumb"])}"><a href="{cfg["home_path"]}">{esc(cfg["home"])}</a><span aria-hidden="true">/</span><span aria-current="page">{esc(LLMS_LABELS[locale][page_key])}</span></nav><p class="section-kicker">{tone_icon(tone, glyph)}{esc(data["eyebrow"])}</p><h1>{esc(data["h1"])}</h1><p class="topic-lead">{esc(data["lead"])}</p><div class="hero-actions"><a class="button button-primary button-lg" href="{APP_URL}" data-analytics-location="hero">{esc(cfg["start"])} <span aria-hidden="true">→</span></a><a class="text-link" href="#jak-pomaha">{esc(data["help_title"])} <span aria-hidden="true">↓</span></a></div></header>
        </div>
{render_direct_answer(page_key, locale)}
        <section class="{problem_class}"><div class="section-copy"><p class="section-kicker">{esc(data["eyebrow"])}</p><h2>{esc(data["problem_title"])}</h2>{"".join(f"<p>{esc(paragraph)}</p>" for paragraph in data["problem"])}</div>{short}<div class="scenario-grid">{scenarios}</div></section>
        <section class="help-section" id="jak-pomaha"><div class="section-copy"><p class="section-kicker">Rodinka</p><h2>{esc(data["help_title"])}</h2><p>{esc(data["help_intro"])}</p></div><ol class="help-steps">{steps}</ol></section>
        <section class="content-section answers-section"><div class="section-copy"><h2>{esc(data["answers_title"])}</h2></div><div class="answers-list">{answers}</div></section>
        <aside class="related-section" aria-labelledby="related-title"><p class="section-kicker">{esc(cfg["related_kicker"])}</p><h2 id="related-title">{esc(cfg["related"])}</h2><ul class="related-grid">{related}</ul></aside>
      </article>
      <section class="cta-section"><div class="cta-card"><p class="section-kicker">Rodinka</p><h2>{esc(data["cta_title"])}</h2><p>{esc(data["cta_text"])}</p><div class="cta-actions"><a class="app-cta" href="{APP_URL}" data-analytics-location="content">{esc(cfg["start"])} <span aria-hidden="true">→</span></a></div></div></section>'''
    return page_shell(page_key, locale, data, main)


def write_page(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def render_sitemap() -> str:
    page_order = ("home", *TOPIC_KEYS)
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


# Short labels for llms.txt, breadcrumbs and the footer. Kept next to the paths so
# a new topic family cannot be added to PATHS and silently skipped here.
LLMS_LABELS = {
    "cs": {"home": "Rodinka", "planner": "Rodinný plánovač", "calendar": "Rodinný kalendář", "shopping": "Sdílený nákupní seznam", "chores": "Úkoly pro rodinu", "meals": "Plánování jídel", "trips": "Rodinné výlety", "memories": "Rodinné vzpomínky", "documents": "Hlídání platnosti dokladů", "baby": "Příprava na miminko", "app": "Aplikace pro rodinu"},
    "sk": {"home": "Rodinka", "planner": "Rodinný plánovač", "calendar": "Rodinný kalendár", "shopping": "Zdieľaný nákupný zoznam", "chores": "Úlohy pre rodinu", "meals": "Plánovanie jedál", "trips": "Rodinné výlety", "memories": "Rodinné spomienky", "documents": "Stráženie platnosti dokladov", "baby": "Príprava na bábätko", "app": "Aplikácia pre rodinu"},
    "en": {"home": "Rodinka", "planner": "Family planner", "calendar": "Family calendar", "shopping": "Shared shopping list", "chores": "Family chores", "meals": "Meal planning", "trips": "Family trips", "memories": "Family memories", "documents": "Document expiry reminders", "baby": "Preparing for a baby", "app": "Family organizer app"},
}

LLMS_SECTIONS = (("cs", "Czech (default)"), ("sk", "Slovak"), ("en", "English"))


def render_llms_txt() -> str:
    sections = []
    for locale, heading in LLMS_SECTIONS:
        links = "\n".join(
            f'- [{LLMS_LABELS[locale][key]}]({canonical(PATHS[key][locale])})'
            for key in ("home", *TOPIC_KEYS)
        )
        sections.append(f"## {heading}\n{links}")
    body = "\n\n".join(sections)
    return f"""# Rodinka

> Rodinka is a family organizer for a shared calendar, household chores, shopping lists, meal planning, family trips, family memories, document expiry reminders and practical preparation for a new family member. The product name is Rodinka. The canonical website is {SITE_URL}/ and the web application is {APP_URL}.

{body}
"""


def main() -> None:
    for locale in ("cs", "sk", "en"):
        write_page(output_path(PATHS["home"][locale]), render_home(locale))
        for page_key in TOPIC_KEYS:
            write_page(output_path(PATHS[page_key][locale]), render_topic(page_key, locale))
    write_page(ROOT / "sitemap.xml", render_sitemap())
    write_page(ROOT / "llms.txt", render_llms_txt())
    print(f"Generated {3 * (1 + len(TOPIC_KEYS))} localized HTML pages, sitemap.xml and llms.txt.")


if __name__ == "__main__":
    main()
