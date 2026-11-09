"""Content of the "Compare family planners" section.

This module holds data only; generate_site.py renders it. Adding another
competitor means adding one entry to COMPETITORS (verified rows and sources),
one entry to COMPARISON_PAGES (localized copy) and its paths in generate_site.py.

Rules for every claim in this file (see README "Srovnání rodinných plánovačů"):

- Rodinka facts describe the released app (runtime), never the roadmap or a
  feature behind a disabled flag.
- Competitor facts come only from the competitor's official website, each row
  cites its sources and the whole set carries VERIFIED_ON.
- A feature we could not find is "unverified" ("Nepodařilo se ověřit"), never
  "no". Use "no" only when the competitor's own site says it is not supported.
- Prices appear only with a verified currency, interval and conditions.
"""

from __future__ import annotations

# ISO date of the last check of every competitor source and of Rodinka's own facts.
VERIFIED_ON = "2026-11-09"
VERIFIED_LABEL = {"cs": "9.\u00a011.\u00a02026", "sk": "9.\u00a011.\u00a02026", "en": "9\u00a0November 2026"}


def t(cs: str, sk: str, en: str) -> dict[str, str]:
    return {"cs": cs, "sk": sk, "en": en}


# Status of one cell. "info" rows carry facts that are not a yes/no question
# (platforms, languages, plans), so they show no badge.
STATUSES = ("yes", "paid", "limited", "no", "unverified", "info")

STATUS_LABELS = {
    "cs": {"yes": "Ano", "paid": "V placené verzi", "limited": "Zčásti", "no": "Ne", "unverified": "Nepodařilo se ověřit"},
    "sk": {"yes": "Áno", "paid": "V platenej verzii", "limited": "Čiastočne", "no": "Nie", "unverified": "Nepodarilo sa overiť"},
    "en": {"yes": "Yes", "paid": "Paid plan", "limited": "Partly", "no": "No", "unverified": "Could not verify"},
}

AREAS = {
    "calendar": t("Sdílený rodinný kalendář", "Zdieľaný rodinný kalendár", "Shared family calendar"),
    "recurring": t("Opakované aktivity a úkoly", "Opakované aktivity a úlohy", "Recurring activities and tasks"),
    "shopping": t("Nákupní seznamy", "Nákupné zoznamy", "Shopping lists"),
    "meals": t("Plánování jídelníčku", "Plánovanie jedálnička", "Meal planning"),
    "chores": t("Domácí povinnosti", "Domáce povinnosti", "Household chores"),
    "kids": t("Dětské profily a kapesné", "Detské profily a vreckové", "Children’s profiles and pocket money"),
    "pets": t("Mazlíčci", "Domáce zvieratá", "Pets"),
    "memories": t("Vzpomínky a milníky", "Spomienky a míľniky", "Memories and milestones"),
    "trips": t("Rodinné výlety", "Rodinné výlety", "Family trips"),
    "documents": t("Doklady a dokumenty", "Doklady a dokumenty", "Documents"),
    "chat": t("Rodinné zprávy", "Rodinné správy", "Family messaging"),
    "location": t("Sdílení polohy", "Zdieľanie polohy", "Location sharing"),
    "roles": t("Oprávnění a spolupráce členů", "Oprávnenia a spolupráca členov", "Permissions and collaboration"),
    "ai": t("Rychlé zadávání a návrhy", "Rýchle zadávanie a návrhy", "Quick capture and suggestions"),
    "calendar_sync": t("Propojení s jinými kalendáři", "Prepojenie s inými kalendármi", "Connecting other calendars"),
    "platforms": t("Web, PWA, iOS a Android", "Web, PWA, iOS a Android", "Web, PWA, iOS and Android"),
    "offline": t("Práce offline", "Práca offline", "Working offline"),
    "languages": t("Čeština a slovenština", "Čeština a slovenčina", "Czech and Slovak"),
    "ads": t("Reklamy", "Reklamy", "Ads"),
    "plans": t("Free a placená verze", "Free a platená verzia", "Free and paid plans"),
}

# Rodinka's side of every table, checked against the released app on VERIFIED_ON
# (production client bundle and Rodinka/docs/PRODUCT_OVERVIEW.md). Native store
# apps, external calendar sync and Safe arrival are not released and must not
# be presented as available.
RODINKA = {
    "calendar": ("yes", t(
        "Měsíční, týdenní i agendový pohled. U události je vidět, koho se týká a kdo ji zajišťuje.",
        "Mesačný, týždenný aj agendový pohľad. Pri udalosti vidno, koho sa týka a kto ju zabezpečuje.",
        "Month, week and agenda views. Each event shows who it is for and who is taking care of it.",
    )),
    "recurring": ("yes", t(
        "Opakované aktivity i úkoly. Změna jednoho termínu nemění celou sérii.",
        "Opakované aktivity aj úlohy. Zmena jedného termínu nemení celú sériu.",
        "Recurring activities and tasks. Changing one occurrence leaves the rest of the series as it is.",
    )),
    "shopping": ("yes", t(
        "Jeden sdílený seznam rozdělený do kategorií, odškrtávání i bez signálu.",
        "Jeden zdieľaný zoznam rozdelený do kategórií, odškrtávanie aj bez signálu.",
        "One shared list grouped by category; items can be checked off without signal.",
    )),
    "meals": ("yes", t(
        "Týdenní plán, knihovna jídel, rodinné hlasování a přenos surovin do nákupu.",
        "Týždenný plán, knižnica jedál, rodinné hlasovanie a prenos surovín do nákupu.",
        "A weekly plan, a meal library, family voting and ingredients sent to the shopping list.",
    )),
    "chores": ("yes", t(
        "Úkol má člověka, termín a případně opakování. Dítě odškrtne, dospělý potvrdí.",
        "Úloha má človeka, termín a prípadne opakovanie. Dieťa odškrtne, dospelý potvrdí.",
        "A task has a person, a due date and optionally a repeat. A child ticks it off, an adult confirms.",
    )),
    "kids": ("yes", t(
        "Dětské přihlášení bez e-mailu, odměny za úkoly, kapesné a cíle spoření.",
        "Detské prihlásenie bez e-mailu, odmeny za úlohy, vreckové a ciele sporenia.",
        "Child sign-in without an email address, rewards for chores, pocket money and savings goals.",
    )),
    "pets": ("yes", t(
        "Profil mazlíčka, pravidelná péče a veterinární termíny s historií.",
        "Profil zvieratka, pravidelná starostlivosť a veterinárne termíny s históriou.",
        "A pet profile, care routines and vet appointments with their history.",
    )),
    "memories": ("yes", t(
        "Společná kronika: milníky, vzpomínky s fotografií a dětské hlášky na jedné časové ose.",
        "Spoločná kronika: míľniky, spomienky s fotografiou a detské hlášky na jednej časovej osi.",
        "One shared chronicle: milestones, memories with photos and things kids say on a single timeline.",
    )),
    "trips": ("yes", t(
        "Tipy na výlety z odkazu, plán cesty a rodinné hlasování; vybraný tip jde do kalendáře.",
        "Tipy na výlety z odkazu, plán cesty a rodinné hlasovanie; vybraný tip ide do kalendára.",
        "Trip ideas saved from a link, a trip plan and family voting; the chosen idea goes to the calendar.",
    )),
    "documents": ("yes", t(
        "Doklady s připomínkou konce platnosti. Vidí je jen dospělí.",
        "Doklady s pripomienkou konca platnosti. Vidia ich len dospelí.",
        "Documents with expiry reminders, visible to adults only.",
    )),
    "chat": ("yes", t(
        "Rodinný chat i přímé zprávy, do kterých lze sdílet úkol nebo položku nákupu. Jen online.",
        "Rodinný chat aj priame správy, do ktorých možno zdieľať úlohu alebo položku nákupu. Len online.",
        "Family and direct messages that can share a task or a shopping item. Online only.",
    )),
    "location": ("no", t(
        "Sdílení polohy Rodinka nenabízí. Rodinná místa slouží k plánování a navigaci.",
        "Zdieľanie polohy Rodinka neponúka. Rodinné miesta slúžia na plánovanie a navigáciu.",
        "Rodinka does not share locations. Family places are there for planning and directions.",
    )),
    "roles": ("yes", t(
        "Role dospělý a dítě. Dítě nevidí doklady ani správu rodiny; pomocník vidí jen termíny, kam doprovází.",
        "Roly dospelý a dieťa. Dieťa nevidí doklady ani správu rodiny; pomocník vidí len termíny, kam sprevádza.",
        "Adult and child roles. Children do not see documents or family settings; a helper sees only the sessions they accompany.",
    )),
    "ai": ("info", t(
        "Hlasové zadání úkolů a nákupu na podporovaných zařízeních. V Rodince Pro návrh nákupu a jídelníčku z dat vaší rodiny.",
        "Hlasové zadanie úloh a nákupu na podporovaných zariadeniach. V Rodinke Pro návrh nákupu a jedálnička z údajov vašej rodiny.",
        "Voice entry for tasks and shopping on supported devices. Rodinka Pro suggests shopping and meals from your own family’s data.",
    )),
    "calendar_sync": ("no", t(
        "Propojení s Google, Apple ani Outlook kalendářem Rodinka zatím nemá.",
        "Prepojenie s Google, Apple ani Outlook kalendárom Rodinka zatiaľ nemá.",
        "Rodinka does not connect to Google, Apple or Outlook calendars yet.",
    )),
    "platforms": ("info", t(
        "Webová aplikace na telefonu, tabletu i počítači; na plochu ji přidáte jako aplikaci (PWA). Ve Windows také z Microsoft Store.",
        "Webová aplikácia v telefóne, tablete aj počítači; na plochu ju pridáte ako aplikáciu (PWA). Vo Windows aj z Microsoft Store.",
        "A web app on phones, tablets and computers that you can add to your home screen (PWA). On Windows, also from the Microsoft Store.",
    )),
    "offline": ("yes", t(
        "Dnes, kalendář, úkoly a nákup jdou měnit offline; jídelníček, vzpomínky a výlety si přečtete.",
        "Dnes, kalendár, úlohy a nákup sa dajú meniť offline; jedálniček, spomienky a výlety si prečítate.",
        "Today, the calendar, chores and shopping can be edited offline; meals, memories and trips stay readable.",
    )),
    "languages": ("info", t(
        "Celé rozhraní česky, slovensky a anglicky.",
        "Celé rozhranie po česky, slovensky a anglicky.",
        "The whole interface in Czech, Slovak and English.",
    )),
    "ads": ("info", t(
        "Bez reklam, i ve verzi zdarma.",
        "Bez reklám, aj vo verzii zadarmo.",
        "No ads, including the free version.",
    )),
    "plans": ("info", t(
        "Free zdarma a bez karty (200 MiB na fotky). Pro pro celou rodinu přidává další nástroje a 5 GiB; ceny zatím nezveřejňujeme.",
        "Free zadarmo a bez karty (200 MiB na fotky). Pro pre celú rodinu pridáva ďalšie nástroje a 5 GiB; ceny zatiaľ nezverejňujeme.",
        "Free costs nothing and needs no card (200 MiB for photos). Pro, for the whole family, adds more tools and 5 GiB; prices are not published yet.",
    )),
}


# Competitors. Each row: (area, status, localized note, source keys). Sources are
# official pages only; their labels are page names, so they are not translated.
COMPETITORS = {
    "familia": {
        "name": "Familia",
        "site": "https://familiaplanner.com/",
        "operator": "Asynq Labs LLC",
        "sources": {
            "home": ("https://familiaplanner.com/", "familiaplanner.com — homepage and FAQ"),
            "pricing": ("https://familiaplanner.com/pricing", "familiaplanner.com — Pricing"),
            "tasks": ("https://familiaplanner.com/family-tasks-and-chores", "familiaplanner.com — Family tasks and chores"),
            "ai": ("https://familiaplanner.com/ai-facts", "familiaplanner.com — AI facts"),
        },
        "rows": (
            ("calendar", "limited", t(
                "Plány, připomínky a rodinné termíny; web o Familii píše, že nejde o klasický kalendář.",
                "Plány, pripomienky a rodinné termíny; web o Familii píše, že nejde o klasický kalendár.",
                "Plans, reminders and family dates; the website says Familia is not a traditional calendar.",
            ), ("home", "ai")),
            ("recurring", "yes", t(
                "Úkol může mít opakování a připomínky.",
                "Úloha môže mať opakovanie a pripomienky.",
                "A task can have a recurring schedule and reminders.",
            ), ("tasks",)),
            ("chores", "yes", t(
                "Rodinné úkoly a povinnosti, každá s odpovědným člověkem.",
                "Rodinné úlohy a povinnosti, každá so zodpovedným človekom.",
                "Family tasks and chores, each with someone responsible.",
            ), ("tasks",)),
            ("shopping", "yes", t(
                "Web zmiňuje nákupy a samostatné seznamy vedle úkolů.",
                "Web spomína nákupy a samostatné zoznamy popri úlohách.",
                "The website mentions groceries and separate lists next to tasks.",
            ), ("home", "tasks")),
            ("meals", "unverified", t(
                "Plánování jídel ani recepty jsme na webu Familie nenašli.",
                "Plánovanie jedál ani recepty sme na webe Familie nenašli.",
                "We did not find meal planning or recipes on Familia’s website.",
            ), ("home", "pricing")),
            ("kids", "unverified", t(
                "Dětské profily, odměny ani kapesné jsme na webu nenašli.",
                "Detské profily, odmeny ani vreckové sme na webe nenašli.",
                "We did not find children’s profiles, rewards or pocket money on the website.",
            ), ("home", "tasks")),
            ("memories", "unverified", t(
                "K položce lze připojit fotografii (Free 1, Smart až 9). Rodinnou kroniku ani milníky jsme nenašli.",
                "K položke možno pripojiť fotografiu (Free 1, Smart až 9). Rodinnú kroniku ani míľniky sme nenašli.",
                "Items can carry photo attachments (1 on Free, up to 9 on Smart). We did not find a family chronicle or milestones.",
            ), ("pricing",)),
            ("roles", "unverified", t(
                "Úkoly mají přiřazeného člověka. Role a oprávnění členů rodiny jsme na webu nenašli.",
                "Úlohy majú priradeného človeka. Roly a oprávnenia členov rodiny sme na webe nenašli.",
                "Tasks have an assignee. We did not find family member roles or permissions on the website.",
            ), ("tasks",)),
            ("ai", "yes", t(
                "Zadání hlasem, textem nebo fotkou vytvoří návrh ke kontrole. Free 10 kreditů měsíčně, Smart bez limitu v rámci férového užívání.",
                "Zadanie hlasom, textom alebo fotkou vytvorí návrh na kontrolu. Free 10 kreditov mesačne, Smart bez limitu v rámci férového používania.",
                "Voice, text or photo capture drafts items for review. 10 credits a month on Free, unlimited with fair use on Smart.",
            ), ("home", "pricing")),
            ("calendar_sync", "yes", t(
                "Propojení s Google Kalendářem. Apple a Outlook jsme na webu nenašli.",
                "Prepojenie s Google Kalendárom. Apple a Outlook sme na webe nenašli.",
                "Connects to Google Calendar. We did not find Apple or Outlook on the website.",
            ), ("home",)),
            ("platforms", "info", t(
                "Aplikace pro iPhone, iPad a Android. Webová verze jen se Smart a po spárování přes QR kód z mobilu.",
                "Aplikácia pre iPhone, iPad a Android. Webová verzia len so Smart a po spárovaní cez QR kód z mobilu.",
                "Apps for iPhone, iPad and Android. The web companion needs Smart and QR pairing from the phone.",
            ), ("home", "pricing", "tasks")),
            ("offline", "unverified", t(
                "Informaci o práci offline jsme na webu nenašli.",
                "Informáciu o práci offline sme na webe nenašli.",
                "We did not find information about working offline on the website.",
            ), ("home",)),
            ("languages", "info", t(
                "Mimo jiné čeština. Slovenštinu se nepodařilo ověřit.",
                "Okrem iného čeština. Slovenčinu sa nepodarilo overiť.",
                "Czech among others. We could not verify Slovak.",
            ), ("tasks",)),
            ("plans", "info", t(
                "Free zdarma; Smart je měsíční předplatné pro celou rodinu. Web uvádí cenu se symbolem $ bez kódu měny a ceny v App Store se liší podle země, proto částku neuvádíme.",
                "Free zadarmo; Smart je mesačné predplatné pre celú rodinu. Web uvádza cenu so symbolom $ bez kódu meny a ceny v App Store sa líšia podľa krajiny, preto sumu neuvádzame.",
                "Free costs nothing; Smart is a monthly subscription for the whole family. The site shows the price with a $ sign and no currency code, and App Store prices vary by country, so we do not quote an amount.",
            ), ("pricing",)),
        ),
    },
    "familywall": {
        "name": "FamilyWall",
        "site": "https://www.familywall.com/",
        "operator": "FamilyWall",
        "sources": {
            "home": ("https://www.familywall.com/", "familywall.com — homepage"),
            "premium": ("https://www.familywall.com/premium.html", "familywall.com — Premium"),
            "about": ("https://www.familywall.com/about.html", "familywall.com — About"),
            "help_about": ("https://support.familywall.com/en/support/solutions/articles/47001013681-about-familywall", "FamilyWall Help Center — About FamilyWall"),
            "help_premium": ("https://support.familywall.com/en/support/solutions/articles/47001239196-what-is-included-in-familywall-premium-", "FamilyWall Help Center — What is included in FamilyWall Premium"),
            "help_gcal": ("https://support.familywall.com/en/support/solutions/articles/47001239518-display-familywall-events-in-google-calendar", "FamilyWall Help Center — Display FamilyWall events in Google Calendar"),
            "help": ("https://support.familywall.com/", "FamilyWall Help Center"),
        },
        "rows": (
            ("calendar", "yes", t(
                "Sdílený kalendář pro rozvrhy, aktivity a schůzky celé rodiny.",
                "Zdieľaný kalendár pre rozvrhy, aktivity a stretnutia celej rodiny.",
                "A shared calendar for the whole family’s schedules, activities and appointments.",
            ), ("home", "help_about")),
            ("recurring", "unverified", t(
                "Rozvrh pro pravidelné nebo střídavé týdny (Timetable) je v Premium. Obecné opakování událostí a úkolů jsme na webu nenašli.",
                "Rozvrh pre pravidelné alebo striedavé týždne (Timetable) je v Premium. Všeobecné opakovanie udalostí a úloh sme na webe nenašli.",
                "A timetable for recurring or alternating weeks is part of Premium. We did not find general recurring events or tasks on the website.",
            ), ("premium",)),
            ("shopping", "yes", t(
                "Sdílené nákupní seznamy pro celou rodinu.",
                "Zdieľané nákupné zoznamy pre celú rodinu.",
                "Shopping lists shared with the whole family.",
            ), ("help_about", "premium")),
            ("meals", "paid", t(
                "Plánovač jídel a recepty včetně importu z webu; podle nápovědy FamilyWall součást Premium.",
                "Plánovač jedál a recepty vrátane importu z webu; podľa nápovedy FamilyWall súčasť Premium.",
                "A meal planner and recipes, including import from the web; part of Premium according to FamilyWall’s help center.",
            ), ("home", "help_premium")),
            ("chores", "yes", t(
                "Sdílené i soukromé seznamy úkolů s přiřazením členům, včetně seznamu povinností pro děti.",
                "Zdieľané aj súkromné zoznamy úloh s priradením členom vrátane zoznamu povinností pre deti.",
                "Shared or private to-do lists assigned to family members, including chore checklists for kids.",
            ), ("help_about", "premium")),
            ("kids", "unverified", t(
                "Samostatné dětské profily, odměny ani kapesné jsme nenašli. Premium nabízí sledování rozpočtu domácnosti.",
                "Samostatné detské profily, odmeny ani vreckové sme nenašli. Premium ponúka sledovanie rozpočtu domácnosti.",
                "We did not find separate children’s profiles, rewards or pocket money. Premium includes a household budget tracker.",
            ), ("help_about", "help_premium")),
            ("memories", "yes", t(
                "Rodinná galerie fotek a videí; Premium přidává víc úložiště. Milníky jsme nenašli.",
                "Rodinná galéria fotiek a videí; Premium pridáva viac úložiska. Míľniky sme nenašli.",
                "A family gallery for photos and videos; Premium adds storage. We did not find milestones.",
            ), ("home", "help_about", "premium")),
            ("documents", "paid", t(
                "Sdílení dokumentů v Premium.",
                "Zdieľanie dokumentov v Premium.",
                "Document sharing in Premium.",
            ), ("help_premium",)),
            ("location", "yes", t(
                "Poloha na mapě a upozornění na příchod a odchod z míst; rozdělení mezi Free a Premium web neuvádí jednoznačně.",
                "Poloha na mape a upozornenia na príchod a odchod z miest; rozdelenie medzi Free a Premium web neuvádza jednoznačne.",
                "Locations on a map and arrival and departure alerts; the website is not consistent about what is Free and what is Premium.",
            ), ("home", "help_about", "premium")),
            ("chat", "yes", t(
                "Rodinný messenger; hlasové a video zprávy v Premium.",
                "Rodinný messenger; hlasové a video správy v Premium.",
                "A family messenger; audio and video messages in Premium.",
            ), ("home", "help_premium")),
            ("roles", "unverified", t(
                "Každý člen si nastaví, s kým sdílí polohu. Role dospělých a dětí jsme na webu nenašli.",
                "Každý člen si nastaví, s kým zdieľa polohu. Roly dospelých a detí sme na webe nenašli.",
                "Each member chooses who sees their location. We did not find adult and child roles on the website.",
            ), ("help_about",)),
            ("calendar_sync", "paid", t(
                "Import kalendářů Google a Outlook a zobrazení událostí v Google Kalendáři v Premium.",
                "Import kalendárov Google a Outlook a zobrazenie udalostí v Google Kalendári v Premium.",
                "Google and Outlook calendar import and showing events in Google Calendar, in Premium.",
            ), ("help_premium", "help_gcal")),
            ("platforms", "info", t(
                "Web, iPhone, iPad a Android.",
                "Web, iPhone, iPad a Android.",
                "Web, iPhone, iPad and Android.",
            ), ("about", "help_about")),
            ("offline", "limited", t(
                "Seznamy lze procházet a odškrtávat offline v obchodě. U dalších částí se offline režim nepodařilo ověřit.",
                "Zoznamy možno prechádzať a odškrtávať offline v obchode. Pri ďalších častiach sa offline režim nepodarilo overiť.",
                "Lists can be browsed and checked off offline in the shop. We could not verify offline use for other parts.",
            ), ("help_about",)),
            ("languages", "info", t(
                "Češtinu ani slovenštinu se nepodařilo ověřit; nápověda je anglicky, francouzsky, německy, portugalsky a španělsky.",
                "Češtinu ani slovenčinu sa nepodarilo overiť; nápoveda je v angličtine, francúzštine, nemčine, portugalčine a španielčine.",
                "We could not verify Czech or Slovak; the help center is in English, French, German, Portuguese and Spanish.",
            ), ("help",)),
            ("ads", "info", t(
                "Podle webu bez reklam.",
                "Podľa webu bez reklám.",
                "Ad-free, according to the website.",
            ), ("about",)),
            ("plans", "info", t(
                "Základ zdarma; Premium pro celou rodinu měsíčně nebo ročně, se 30denní zkušební verzí. Web uvádí cenu se symbolem $ bez kódu měny, proto částku neuvádíme.",
                "Základ zadarmo; Premium pre celú rodinu mesačne alebo ročne, s 30-dňovou skúšobnou verziou. Web uvádza cenu so symbolom $ bez kódu meny, preto sumu neuvádzame.",
                "A free core; Premium for the whole family, monthly or yearly, with a 30-day trial. The site shows the price with a $ sign and no currency code, so we do not quote an amount.",
            ), ("premium", "help_premium")),
        ),
    },
    "cozi": {
        "name": "Cozi",
        "site": "https://www.cozi.com/",
        "operator": "Cozi, Inc.",
        "sources": {
            "home": ("https://www.cozi.com/", "cozi.com — homepage"),
            "calendar": ("https://www.cozi.com/calendar/", "cozi.com — Calendar"),
            "overview": ("https://www.cozi.com/feature-overview/", "cozi.com — Feature overview"),
            "meals": ("https://www.cozi.com/meals-and-recipe-box/", "cozi.com — Meals and recipe box"),
            "faq": ("https://www.cozi.com/faq/", "cozi.com — FAQ"),
            "plans": ("https://www.cozi.com/compare-plans/", "cozi.com — Compare plans"),
            "gold": ("https://www.cozi.com/cozi-gold/", "cozi.com — Cozi Gold"),
        },
        "rows": (
            ("calendar", "yes", t(
                "Sdílený rodinný kalendář až pro 12 členů.",
                "Zdieľaný rodinný kalendár až pre 12 členov.",
                "A shared family calendar for up to 12 members.",
            ), ("calendar",)),
            ("recurring", "yes", t(
                "Opakované události; povinnosti (Chores) s denním nebo týdenním opakováním.",
                "Opakované udalosti; povinnosti (Chores) s denným alebo týždenným opakovaním.",
                "Recurring events; chores repeat daily or weekly.",
            ), ("calendar", "faq")),
            ("shopping", "yes", t(
                "Sdílené nákupní seznamy, které vidí celý účet.",
                "Zdieľané nákupné zoznamy, ktoré vidí celý účet.",
                "Shopping lists shared with everyone in the account.",
            ), ("overview", "faq")),
            ("meals", "yes", t(
                "Kniha receptů, plánování jídel a přenos surovin na seznam. AI plánovač jídel ve vyšším tarifu Max.",
                "Kniha receptov, plánovanie jedál a prenos surovín na zoznam. AI plánovač jedál vo vyššom tarife Max.",
                "A recipe box, meal scheduling and ingredients to the list. An AI meal planner in the higher Max plan.",
            ), ("meals", "plans")),
            ("chores", "yes", t(
                "Cozi Chores: každý člen má vlastní seznam povinností (v mobilních aplikacích).",
                "Cozi Chores: každý člen má vlastný zoznam povinností (v mobilných aplikáciách).",
                "Cozi Chores: each person gets their own chore list (in the mobile apps).",
            ), ("overview", "faq")),
            ("kids", "unverified", t(
                "Samostatné dětské profily, odměny ani kapesné jsme na webu nenašli.",
                "Samostatné detské profily, odmeny ani vreckové sme na webe nenašli.",
                "We did not find separate children’s profiles, rewards or pocket money on the website.",
            ), ("faq", "overview")),
            ("memories", "no", t(
                "Podle FAQ nelze k událostem a seznamům přikládat obrázky ani soubory. Rodinný deník ani milníky jsme nenašli.",
                "Podľa FAQ nemožno k udalostiam a zoznamom prikladať obrázky ani súbory. Rodinný denník ani míľniky sme nenašli.",
                "According to the FAQ, images and files cannot be attached to events or lists. We did not find a journal or milestones.",
            ), ("faq",)),
            ("roles", "no", t(
                "Podle FAQ Cozi nenabízí omezený přístup: každý v účtu může vše zobrazit, přidat, upravit i smazat.",
                "Podľa FAQ Cozi neponúka obmedzený prístup: každý v účte môže všetko zobraziť, pridať, upraviť aj zmazať.",
                "According to the FAQ, Cozi has no restricted access: everyone in the account can view, add, edit and delete everything.",
            ), ("faq",)),
            ("calendar_sync", "yes", t(
                "Zobrazení kalendářů Google, Apple, Outlook a dalších v Cozi i odeslání Cozi do jiných kalendářů; obojí jen pro čtení.",
                "Zobrazenie kalendárov Google, Apple, Outlook a ďalších v Cozi aj odoslanie Cozi do iných kalendárov; oboje len na čítanie.",
                "Google, Apple, Outlook and other calendars shown in Cozi, and Cozi sent to other calendars; both read-only.",
            ), ("calendar", "faq")),
            ("platforms", "info", t(
                "Web, iPhone a Android.",
                "Web, iPhone a Android.",
                "Web, iPhone and Android.",
            ), ("home", "faq")),
            ("offline", "limited", t(
                "Nákupní seznam lze odškrtávat offline. U dalších částí se offline režim nepodařilo ověřit.",
                "Nákupný zoznam možno odškrtávať offline. Pri ďalších častiach sa offline režim nepodarilo overiť.",
                "Shopping lists can be checked off offline. We could not verify offline use for other parts.",
            ), ("overview",)),
            ("languages", "info", t(
                "Češtinu ani slovenštinu se nepodařilo ověřit.",
                "Češtinu ani slovenčinu sa nepodarilo overiť.",
                "We could not verify Czech or Slovak.",
            ), ("home", "faq")),
            ("ads", "info", t(
                "Verze zdarma obsahuje reklamy; Cozi Gold je bez reklam.",
                "Verzia zadarmo obsahuje reklamy; Cozi Gold je bez reklám.",
                "The free version shows ads; Cozi Gold is ad-free.",
            ), ("faq", "gold")),
            ("plans", "info", t(
                "Free zdarma s reklamami. Cozi Gold stojí 39 USD ročně za celý účet, dvoutýdenní zkušební verze platí jen při objednání na webu. Vyšší tarif Max přidává AI funkce.",
                "Free zadarmo s reklamami. Cozi Gold stojí 39 USD ročne za celý účet, dvojtýždňová skúšobná verzia platí len pri objednaní na webe. Vyšší tarif Max pridáva AI funkcie.",
                "Free with ads. Cozi Gold costs USD 39 a year for the whole account; the two-week trial applies only to web sign-ups. A higher Max plan adds AI features.",
            ), ("plans", "faq")),
        ),
    },
}

# The order in which comparison pages are listed and linked.
COMPETITOR_ORDER = ("familia", "familywall", "cozi")


# ---------------------------------------------------------------------------
# Shared section copy.

COMMON = {
    "cs": {
        "section": "Srovnání",
        "disclosure_title": "Kdo srovnání připravil",
        "disclosure": "Srovnání připravila a publikuje Rodinka, tedy jedna z porovnávaných aplikací. U ostatních aplikací vycházíme jen z jejich oficiálních webů a co se ověřit nepodařilo, výslovně tak označujeme. Když najdete nepřesnost, napište nám a opravíme ji.",
        "verified": "Naposledy ověřeno {date}.",
        "support": "Napsat podpoře Rodinky",
        "area": "Oblast",
        "table_title": "Funkce vedle sebe",
        "table_caption": "Srovnání funkcí aplikací Rodinka a {name}",
        "legend": "„Nepodařilo se ověřit“ znamená, že jsme informaci na oficiálním webu nenašli, ne že funkce neexistuje. Čísla odkazují na zdroje na konci stránky.",
        "fit_title": "Pro koho se která aplikace hodí",
        "fit_rodinka": "Rodinka se hodí, když…",
        "fit_comp": "{name} se hodí, když…",
        "scenarios_title": "Jak to vypadá v běžném týdnu",
        "pros_title": "Výhody a omezení",
        "pros": "Silné stránky",
        "cons": "Omezení",
        "pricing_title": "Platformy a ceny",
        "faq_title": "Časté otázky",
        "verdict_title": "Co si vybrat",
        "sources_title": "Zdroje a ověření",
        "sources_intro": "Údaje o aplikaci {name} pocházejí z těchto oficiálních stránek. Údaje o Rodince odpovídají aktuálně vydané verzi aplikace, ne plánům.",
        "source_ref": "zdroj",
        "more_title": "Další srovnání",
        "guide_card": "Na co se při výběru rodinného plánovače dívat a pro jakou rodinu se hodí která aplikace.",
        "hub_card": "Všechna srovnání Rodinky s dalšími rodinnými plánovači na jednom místě.",
        "read_compare": "Přečíst srovnání",
    },
    "sk": {
        "section": "Porovnanie",
        "disclosure_title": "Kto porovnanie pripravil",
        "disclosure": "Porovnanie pripravila a zverejňuje Rodinka, teda jedna z porovnávaných aplikácií. Pri ostatných aplikáciách vychádzame len z ich oficiálnych webov a čo sa overiť nepodarilo, výslovne tak označujeme. Keď nájdete nepresnosť, napíšte nám a opravíme ju.",
        "verified": "Naposledy overené {date}.",
        "support": "Napísať podpore Rodinky",
        "area": "Oblasť",
        "table_title": "Funkcie vedľa seba",
        "table_caption": "Porovnanie funkcií aplikácií Rodinka a {name}",
        "legend": "„Nepodarilo sa overiť“ znamená, že sme informáciu na oficiálnom webe nenašli, nie že funkcia neexistuje. Čísla odkazujú na zdroje na konci stránky.",
        "fit_title": "Pre koho sa ktorá aplikácia hodí",
        "fit_rodinka": "Rodinka sa hodí, keď…",
        "fit_comp": "{name} sa hodí, keď…",
        "scenarios_title": "Ako to vyzerá v bežnom týždni",
        "pros_title": "Výhody a obmedzenia",
        "pros": "Silné stránky",
        "cons": "Obmedzenia",
        "pricing_title": "Platformy a ceny",
        "faq_title": "Časté otázky",
        "verdict_title": "Čo si vybrať",
        "sources_title": "Zdroje a overenie",
        "sources_intro": "Údaje o aplikácii {name} pochádzajú z týchto oficiálnych stránok. Údaje o Rodinke zodpovedajú aktuálne vydanej verzii aplikácie, nie plánom.",
        "source_ref": "zdroj",
        "more_title": "Ďalšie porovnania",
        "guide_card": "Na čo sa pri výbere rodinného plánovača pozerať a pre akú rodinu sa hodí ktorá aplikácia.",
        "hub_card": "Všetky porovnania Rodinky s ďalšími rodinnými plánovačmi na jednom mieste.",
        "read_compare": "Prečítať porovnanie",
    },
    "en": {
        "section": "Compare",
        "disclosure_title": "Who wrote this comparison",
        "disclosure": "This comparison is written and published by Rodinka, one of the apps being compared. For the other apps we rely only on their official websites, and anything we could not verify is labelled as such. If you spot an inaccuracy, tell us and we will correct it.",
        "verified": "Last checked on {date}.",
        "support": "Contact Rodinka support",
        "area": "Area",
        "table_title": "Features side by side",
        "table_caption": "Feature comparison of Rodinka and {name}",
        "legend": "“Could not verify” means we did not find the information on the official website, not that the feature does not exist. Numbers point to the sources at the end of the page.",
        "fit_title": "Which app suits which family",
        "fit_rodinka": "Rodinka suits you if…",
        "fit_comp": "{name} suits you if…",
        "scenarios_title": "What it looks like in an ordinary week",
        "pros_title": "Strengths and limitations",
        "pros": "Strengths",
        "cons": "Limitations",
        "pricing_title": "Platforms and pricing",
        "faq_title": "Frequently asked questions",
        "verdict_title": "Which one to choose",
        "sources_title": "Sources and verification",
        "sources_intro": "Information about {name} comes from these official pages. Information about Rodinka reflects the currently released app, not plans.",
        "source_ref": "source",
        "more_title": "More comparisons",
        "guide_card": "What to look for in a family planner, and which app suits which kind of family.",
        "hub_card": "Every comparison of Rodinka with other family planners in one place.",
        "read_compare": "Read the comparison",
    },
}


# ---------------------------------------------------------------------------
# Hub page: /srovnani/

HUB = {
    "cs": {
        "title": "Srovnání rodinných plánovačů: Rodinka, Familia, FamilyWall, Cozi | Rodinka",
        "description": "Férové srovnání rodinných plánovačů a sdílených rodinných kalendářů. Rodinka vedle aplikací Familia, FamilyWall a Cozi, se zdroji a datem ověření.",
        "og_title": "Srovnání rodinných plánovačů",
        "og_description": "Rodinka vedle aplikací Familia, FamilyWall a Cozi: funkce, platformy a ceny podle oficiálních zdrojů.",
        "og_alt": "Srovnání rodinných plánovačů od Rodinky",
        "eyebrow": "SROVNÁNÍ APLIKACÍ",
        "h1": "Srovnání rodinných plánovačů",
        "lead": "Každá rodina potřebuje od plánovače něco jiného. Tady najdete Rodinku vedle dalších aplikací pro rodinu: co umí, pro koho se hodí a kde má která svá omezení.",
        "answer": ("Jak vybrat mezi Rodinkou, Familií, FamilyWall a Cozi?", "Rozhoduje hlavně to, co doma řešíte nejčastěji. Rodinka se soustředí na každodenní provoz celé rodiny v češtině a slovenštině: kalendář s doprovodem, úkoly s odměnami pro děti, nákupy, jídla, výlety a vzpomínky. Familia staví na rychlém zadávání s pomocí AI, FamilyWall přidává sdílení polohy a Cozi propojení s dalšími kalendáři. Každé srovnání uvádí zdroje a datum ověření."),
        "method_title": "Jak srovnáváme",
        "method": (
            ("Jen oficiální zdroje", "U ostatních aplikací čerpáme z jejich webů a nápovědy, ne z recenzí ani dohadů. Každý řádek tabulky odkazuje na zdroj."),
            ("Neověřené neznamená chybějící", "Když informaci nenajdeme, napíšeme „Nepodařilo se ověřit“. Nepřítomnost na webu nevydáváme za absenci funkce."),
            ("Rodinka bez příkras", "U Rodinky uvádíme jen to, co je v aplikaci dnes, včetně věcí, které zatím neumí."),
            ("Bez bodování", "Nedáváme skóre ani hvězdičky. Popisujeme rozdíly a necháváme rozhodnutí na vás."),
        ),
        "list_title": "Srovnání podle aplikace",
        "cta_title": "Vyzkoušejte, jestli Rodinka sedí vaší rodině.",
        "cta_text": "Založení je zdarma a bez platební karty. Začněte jednou věcí, třeba společným kalendářem, a uvidíte, jestli vám vyhovuje.",
    },
    "sk": {
        "title": "Porovnanie rodinných plánovačov: Rodinka, Familia, FamilyWall, Cozi | Rodinka",
        "description": "Férové porovnanie rodinných plánovačov a zdieľaných rodinných kalendárov. Rodinka vedľa aplikácií Familia, FamilyWall a Cozi, so zdrojmi a dátumom overenia.",
        "og_title": "Porovnanie rodinných plánovačov",
        "og_description": "Rodinka vedľa aplikácií Familia, FamilyWall a Cozi: funkcie, platformy a ceny podľa oficiálnych zdrojov.",
        "og_alt": "Porovnanie rodinných plánovačov od Rodinky",
        "eyebrow": "POROVNANIE APLIKÁCIÍ",
        "h1": "Porovnanie rodinných plánovačov",
        "lead": "Každá rodina potrebuje od plánovača niečo iné. Tu nájdete Rodinku vedľa ďalších aplikácií pre rodinu: čo vedia, pre koho sa hodia a kde má ktorá svoje obmedzenia.",
        "answer": ("Ako vybrať medzi Rodinkou, Familiou, FamilyWall a Cozi?", "Rozhoduje hlavne to, čo doma riešite najčastejšie. Rodinka sa sústreďuje na každodennú prevádzku celej rodiny po slovensky a po česky: kalendár so sprievodom, úlohy s odmenami pre deti, nákupy, jedlá, výlety a spomienky. Familia stavia na rýchlom zadávaní s pomocou AI, FamilyWall pridáva zdieľanie polohy a Cozi prepojenie s ďalšími kalendármi. Každé porovnanie uvádza zdroje a dátum overenia."),
        "method_title": "Ako porovnávame",
        "method": (
            ("Len oficiálne zdroje", "Pri ostatných aplikáciách čerpáme z ich webov a nápovedy, nie z recenzií ani dohadov. Každý riadok tabuľky odkazuje na zdroj."),
            ("Neoverené neznamená chýbajúce", "Keď informáciu nenájdeme, napíšeme „Nepodarilo sa overiť“. Neprítomnosť na webe nevydávame za absenciu funkcie."),
            ("Rodinka bez prikrášľovania", "Pri Rodinke uvádzame len to, čo je v aplikácii dnes, vrátane vecí, ktoré zatiaľ nevie."),
            ("Bez bodovania", "Nedávame skóre ani hviezdičky. Opisujeme rozdiely a rozhodnutie nechávame na vás."),
        ),
        "list_title": "Porovnania podľa aplikácie",
        "cta_title": "Vyskúšajte, či Rodinka sedí vašej rodine.",
        "cta_text": "Založenie je zadarmo a bez platobnej karty. Začnite jednou vecou, napríklad spoločným kalendárom, a uvidíte, či vám vyhovuje.",
    },
    "en": {
        "title": "Family planner comparison: Rodinka, Familia, FamilyWall, Cozi | Rodinka",
        "description": "A fair comparison of family planner and shared family calendar apps. Rodinka next to Familia, FamilyWall and Cozi, with sources and the date each fact was checked.",
        "og_title": "Family planner comparison",
        "og_description": "Rodinka next to Familia, FamilyWall and Cozi: features, platforms and pricing from official sources.",
        "og_alt": "Family planner comparison by Rodinka",
        "eyebrow": "COMPARE APPS",
        "h1": "Family planner comparison",
        "lead": "Every family needs something different from a planner. Here you will find Rodinka next to other family organizer apps: what each one does, who it suits and where its limits are.",
        "answer": ("How do you choose between Rodinka, Familia, FamilyWall and Cozi?", "It mostly comes down to what your family deals with most often. Rodinka focuses on everyday family life in Czech, Slovak and English: a calendar that shows who is taking whom, chores with rewards for children, shopping, meals, trips and memories. Familia is built around quick AI-assisted capture, FamilyWall adds location sharing, and Cozi connects to other calendars. Every comparison lists its sources and when they were checked."),
        "method_title": "How we compare",
        "method": (
            ("Official sources only", "For the other apps we use their own websites and help centers, not reviews or guesses. Every table row links to a source."),
            ("Unverified is not missing", "When we cannot find something, we say “Could not verify”. We never treat silence on a website as a missing feature."),
            ("Rodinka as it is", "For Rodinka we list only what the app does today, including what it does not do yet."),
            ("No scores", "We do not hand out ratings or stars. We describe the differences and leave the decision to you."),
        ),
        "list_title": "Comparisons by app",
        "cta_title": "See whether Rodinka fits your family.",
        "cta_text": "Signing up is free and needs no payment card. Start with one thing, such as the shared calendar, and see how it feels.",
    },
}


# ---------------------------------------------------------------------------
# Editorial guide: /nejlepsi-rodinne-planovace/

GUIDE = {
    "cs": {
        "title": "Nejlepší aplikace pro rodinu: jak vybrat rodinný plánovač | Rodinka",
        "description": "Jak vybrat rodinný plánovač nebo sdílený rodinný kalendář. Šest otázek, které pomohou rozhodnout, a přehled aplikací Rodinka, Familia, FamilyWall a Cozi.",
        "og_title": "Jak vybrat nejlepší aplikaci pro rodinu",
        "og_description": "Šest otázek pro výběr rodinného plánovače a stručný přehled Rodinky, Familie, FamilyWall a Cozi.",
        "og_alt": "Průvodce výběrem rodinného plánovače od Rodinky",
        "eyebrow": "PRŮVODCE VÝBĚREM",
        "h1": "Nejlepší rodinný plánovač je ten, který rodina opravdu používá",
        "lead": "Univerzální vítěz neexistuje. Rodina se dvěma školáky a babičkou na hlídání potřebuje něco jiného než pár, který chce hlavně sdílený kalendář. Tento průvodce vám pomůže ujasnit si, co od aplikace čekáte.",
        "answer": ("Jaká je nejlepší aplikace pro organizaci rodiny?", "Ta, kterou budou používat všichni dospělí a podle věku i děti. Než začnete vybírat, ujasněte si, jestli potřebujete hlavně sdílený rodinný kalendář, nebo celý rodinný plánovač s úkoly, nákupy a jídly, jestli se mají zapojit děti a prarodiče, v jakém jazyce a na jakých zařízeních. Podle toho dává smysl jiná aplikace."),
        "criteria_title": "Šest otázek před výběrem",
        "criteria": (
            ("Kdo všechno se má zapojit?", "Jen dva dospělí, nebo i děti, babička či chůva? Zjistěte, jestli aplikace umí dětské účty a jestli lze pomocníkům ukázat jen část plánu."),
            ("Co doma řešíte nejčastěji?", "Kroužky a vyzvedávání, nákupy, vaření, domácí povinnosti? Vyberte aplikaci, která dobře zvládá právě vaši nejčastější starost, ne tu s nejdelším seznamem funkcí."),
            ("Potřebujete propojit jiné kalendáře?", "Pokud máte pracovní kalendář v Google nebo Outlooku a chcete ho vidět vedle rodinného, ověřte, jestli a jak aplikace propojení podporuje."),
            ("V jakém jazyce a na čem?", "Bude se aplikace líbit i prarodičům v češtině nebo slovenštině? Běží na všech telefonech, které doma máte, i na počítači?"),
            ("Jak se chová bez signálu?", "Nákup ve sklepním supermarketu nebo úkol v autě. Ověřte, které části fungují offline."),
            ("Co je zdarma a co placené?", "Podívejte se, co obsahuje bezplatná verze, jestli se placená verze platí za rodinu, nebo za člena, a v jaké měně a v jakém intervalu."),
        ),
        "apps_title": "Stručný přehled aplikací",
        "apps_intro": "Údaje o ostatních aplikacích pocházejí z jejich oficiálních webů. Podrobnosti a zdroje najdete v jednotlivých srovnáních.",
        "fit_label": "Hodí se, když",
        "watch_label": "Myslete na to, že",
        "apps": {
            "rodinka": ("chcete jeden prostor pro celý rodinný provoz v češtině nebo slovenštině: kalendář s doprovodem, úkoly s odměnami a kapesným pro děti, nákupy, jídla, výlety, mazlíčky a vzpomínky. Zapojit můžete i prarodiče a pomocníky.", "zatím nepropojí Google ani Outlook kalendář a na telefonu běží jako webová aplikace přidaná na plochu."),
            "familia": ("chcete úkoly a plány zadávat co nejrychleji hlasem, textem nebo fotkou a výsledek jen zkontrolovat. Familia má i českou verzi.", "webová verze vyžaduje placený Smart a plánování jídel ani dětské profily jsme na jejím webu nenašli."),
            "familywall": ("vedle kalendáře a seznamů chcete i rodinný messenger, galerii fotek a sdílení polohy.", "plánovač jídel a propojení kalendářů jsou v Premium a češtinu ani slovenštinu se nám ověřit nepodařilo."),
            "cozi": ("máte hlavně kalendář a seznamy, chcete vidět i pracovní a školní kalendáře a vyhovuje vám angličtina.", "verze zdarma má reklamy a podle FAQ Cozi nelze omezit, co kdo v rodinném účtu vidí."),
        },
        "faq": (
            ("Je lepší rodinný kalendář, nebo celý rodinný plánovač?", "Pokud vám jde jen o termíny, stačí sdílený rodinný kalendář. Jakmile se doma řeší i úkoly, nákupy a jídla, ušetří vám plánovač přepínání mezi několika aplikacemi a chaty."),
            ("Stačí sdílený Google Kalendář?", "Pro dva dospělé často ano. Rodinné aplikace přidávají to, co obecný kalendář nemá: dětské účty, rodinné úkoly, nákupní seznam nebo informaci o tom, kdo dítě kam veze."),
            ("Mají děti používat rodinnou aplikaci?", "Od školního věku to pomáhá: dítě vidí svůj program a úkoly a nemusí se ptát. Důležité je, aby aplikace umožnila dětem ukázat jen to, co je pro ně."),
            ("Kolik stojí rodinný plánovač?", "Všechny aplikace v tomto přehledu mají bezplatnou verzi. Placené verze se liší obsahem, měnou i způsobem placení, proto je porovnáváme v jednotlivých srovnáních."),
        ),
        "cta_title": "Vyzkoušejte Rodinku na jednom týdnu.",
        "cta_text": "Přidejte kroužky, pár úkolů a nákup a podívejte se, jestli vám společný přehled pomáhá. Rodinka Free je zdarma a bez karty.",
    },
    "sk": {
        "title": "Najlepšia aplikácia pre rodinu: ako vybrať rodinný plánovač | Rodinka",
        "description": "Ako vybrať rodinný plánovač alebo zdieľaný rodinný kalendár. Šesť otázok, ktoré pomôžu rozhodnúť, a prehľad aplikácií Rodinka, Familia, FamilyWall a Cozi.",
        "og_title": "Ako vybrať najlepšiu aplikáciu pre rodinu",
        "og_description": "Šesť otázok na výber rodinného plánovača a stručný prehľad Rodinky, Familie, FamilyWall a Cozi.",
        "og_alt": "Sprievodca výberom rodinného plánovača od Rodinky",
        "eyebrow": "SPRIEVODCA VÝBEROM",
        "h1": "Najlepší rodinný plánovač je ten, ktorý rodina naozaj používa",
        "lead": "Univerzálny víťaz neexistuje. Rodina s dvoma školákmi a starou mamou na stráženie potrebuje niečo iné ako pár, ktorý chce hlavne zdieľaný kalendár. Tento sprievodca vám pomôže ujasniť si, čo od aplikácie čakáte.",
        "answer": ("Aká je najlepšia aplikácia na organizáciu rodiny?", "Tá, ktorú budú používať všetci dospelí a podľa veku aj deti. Skôr než začnete vyberať, ujasnite si, či potrebujete hlavne zdieľaný rodinný kalendár, alebo celý rodinný plánovač s úlohami, nákupmi a jedlami, či sa majú zapojiť deti a starí rodičia, v akom jazyku a na akých zariadeniach. Podľa toho dáva zmysel iná aplikácia."),
        "criteria_title": "Šesť otázok pred výberom",
        "criteria": (
            ("Kto všetko sa má zapojiť?", "Len dvaja dospelí, alebo aj deti, stará mama či opatrovateľka? Zistite, či aplikácia vie detské účty a či možno pomocníkom ukázať len časť plánu."),
            ("Čo doma riešite najčastejšie?", "Krúžky a vyzdvihovanie, nákupy, varenie, domáce povinnosti? Vyberte aplikáciu, ktorá dobre zvláda práve vašu najčastejšiu starosť, nie tú s najdlhším zoznamom funkcií."),
            ("Potrebujete prepojiť iné kalendáre?", "Ak máte pracovný kalendár v Google alebo Outlooku a chcete ho vidieť vedľa rodinného, overte, či a ako aplikácia prepojenie podporuje."),
            ("V akom jazyku a na čom?", "Bude sa aplikácia páčiť aj starým rodičom po slovensky? Beží na všetkých telefónoch, ktoré doma máte, aj na počítači?"),
            ("Ako sa správa bez signálu?", "Nákup v pivničnom supermarkete alebo úloha v aute. Overte, ktoré časti fungujú offline."),
            ("Čo je zadarmo a čo platené?", "Pozrite sa, čo obsahuje bezplatná verzia, či sa platená verzia platí za rodinu, alebo za člena, a v akej mene a v akom intervale."),
        ),
        "apps_title": "Stručný prehľad aplikácií",
        "apps_intro": "Údaje o ostatných aplikáciách pochádzajú z ich oficiálnych webov. Podrobnosti a zdroje nájdete v jednotlivých porovnaniach.",
        "fit_label": "Hodí sa, keď",
        "watch_label": "Myslite na to, že",
        "apps": {
            "rodinka": ("chcete jeden priestor pre celú rodinnú prevádzku po slovensky alebo po česky: kalendár so sprievodom, úlohy s odmenami a vreckovým pre deti, nákupy, jedlá, výlety, zvieratká a spomienky. Zapojiť môžete aj starých rodičov a pomocníkov.", "zatiaľ neprepojí Google ani Outlook kalendár a v telefóne beží ako webová aplikácia pridaná na plochu."),
            "familia": ("chcete úlohy a plány zadávať čo najrýchlejšie hlasom, textom alebo fotkou a výsledok len skontrolovať. Familia má aj českú verziu.", "webová verzia vyžaduje platený Smart a plánovanie jedál ani detské profily sme na jej webe nenašli."),
            "familywall": ("popri kalendári a zoznamoch chcete aj rodinný messenger, galériu fotiek a zdieľanie polohy.", "plánovač jedál a prepojenie kalendárov sú v Premium a češtinu ani slovenčinu sa nám overiť nepodarilo."),
            "cozi": ("máte hlavne kalendár a zoznamy, chcete vidieť aj pracovné a školské kalendáre a vyhovuje vám angličtina.", "verzia zadarmo má reklamy a podľa FAQ Cozi nemožno obmedziť, čo kto v rodinnom účte vidí."),
        },
        "faq": (
            ("Je lepší rodinný kalendár, alebo celý rodinný plánovač?", "Ak vám ide len o termíny, stačí zdieľaný rodinný kalendár. Keď sa doma riešia aj úlohy, nákupy a jedlá, ušetrí vám plánovač prepínanie medzi niekoľkými aplikáciami a chatmi."),
            ("Stačí zdieľaný Google Kalendár?", "Pre dvoch dospelých často áno. Rodinné aplikácie pridávajú to, čo bežný kalendár nemá: detské účty, rodinné úlohy, nákupný zoznam alebo informáciu o tom, kto dieťa kam vezie."),
            ("Majú deti používať rodinnú aplikáciu?", "Od školského veku to pomáha: dieťa vidí svoj program a úlohy a nemusí sa pýtať. Dôležité je, aby aplikácia umožnila deťom ukázať len to, čo je pre ne."),
            ("Koľko stojí rodinný plánovač?", "Všetky aplikácie v tomto prehľade majú bezplatnú verziu. Platené verzie sa líšia obsahom, menou aj spôsobom platenia, preto ich porovnávame v jednotlivých porovnaniach."),
        ),
        "cta_title": "Vyskúšajte Rodinku na jednom týždni.",
        "cta_text": "Pridajte krúžky, pár úloh a nákup a pozrite sa, či vám spoločný prehľad pomáha. Rodinka Free je zadarmo a bez karty.",
    },
    "en": {
        "title": "Best family organizer apps: how to choose a family planner | Rodinka",
        "description": "How to choose a family planner or shared family calendar app. Six questions that help you decide, and an overview of Rodinka, Familia, FamilyWall and Cozi.",
        "og_title": "How to choose the best family organizer app",
        "og_description": "Six questions for choosing a family planner, and a short overview of Rodinka, Familia, FamilyWall and Cozi.",
        "og_alt": "A guide to choosing a family planner, by Rodinka",
        "eyebrow": "CHOOSING A PLANNER",
        "h1": "The best family planner is the one your family actually uses",
        "lead": "There is no single winner. A family with two school-age children and a grandmother who babysits needs something different from a couple who mainly want a shared calendar. This guide helps you work out what you need from an app.",
        "answer": ("What is the best app for organizing family life?", "The one that every adult, and children as they grow, will actually use. Before you compare apps, decide whether you mainly need a shared family calendar or a full family planner with chores, shopping and meals, whether children and grandparents should take part, and which languages and devices matter. The right app follows from that."),
        "criteria_title": "Six questions before you choose",
        "criteria": (
            ("Who needs to take part?", "Just two adults, or children, a grandparent or a nanny too? Check whether the app supports children’s accounts and whether helpers can see only part of the plan."),
            ("What takes up most of your time?", "Activities and pick-ups, shopping, cooking, chores? Choose the app that handles your most common worry well, not the one with the longest feature list."),
            ("Do you need other calendars in it?", "If your work calendar lives in Google or Outlook and you want it next to the family plan, check whether and how the app connects to it."),
            ("Which language and which devices?", "Will grandparents be comfortable with the language? Does the app run on every phone in the house and on a computer?"),
            ("What happens without signal?", "Shopping in a basement supermarket, or a task in the car. Check which parts work offline."),
            ("What is free and what is paid?", "See what the free version includes, whether the paid plan is per family or per person, and its currency and billing interval."),
        ),
        "apps_title": "The apps at a glance",
        "apps_intro": "Information about the other apps comes from their official websites. Details and sources are in each comparison.",
        "fit_label": "A good fit if",
        "watch_label": "Keep in mind that",
        "apps": {
            "rodinka": ("you want one space for everyday family life in Czech, Slovak or English: a calendar that shows who is taking whom, chores with rewards and pocket money for children, shopping, meals, trips, pets and memories. Grandparents and helpers can take part too.", "it does not connect Google or Outlook calendars yet, and on phones it runs as a web app added to the home screen."),
            "familia": ("you want to add tasks and plans as quickly as possible by voice, text or photo and simply review the result. Familia also has a Czech version.", "the web version needs the paid Smart plan, and we did not find meal planning or children’s profiles on its website."),
            "familywall": ("next to the calendar and lists you also want a family messenger, a photo gallery and location sharing.", "the meal planner and calendar connections are in Premium, and we could not verify Czech or Slovak."),
            "cozi": ("you mainly need a calendar and lists, want to see work and school calendars too, and are happy in English.", "the free version shows ads and, according to Cozi’s FAQ, you cannot limit what each person in the family account sees."),
        },
        "faq": (
            ("Do I need a family calendar or a full family planner?", "If you only care about dates, a shared family calendar is enough. Once chores, shopping and meals come into it, a planner saves you from switching between several apps and chats."),
            ("Isn’t a shared Google Calendar enough?", "For two adults it often is. Family apps add what a general calendar lacks: children’s accounts, family chores, a shopping list, or who is taking a child where."),
            ("Should children use the family app?", "From school age it helps: a child sees their own plans and chores without asking. What matters is that the app lets children see only what is meant for them."),
            ("How much does a family planner cost?", "Every app in this overview has a free version. Paid plans differ in what they include, their currency and how you pay, so we compare them in each comparison."),
        ),
        "cta_title": "Try Rodinka for one week.",
        "cta_text": "Add your activities, a few chores and the shopping, and see whether a shared overview helps. Rodinka Free costs nothing and needs no card.",
    },
}


# ---------------------------------------------------------------------------
# One page per competitor. The table rows live in COMPETITORS; this is the prose.

COMPARISON_PAGES = {
    "familia": {
        "cs": {
            "title": "Rodinka vs Familia: srovnání rodinných plánovačů | Rodinka",
            "description": "Familia vs Rodinka: rychlé zadávání s AI, nebo celý rodinný provoz s dětmi, jídly a výlety? Srovnání funkcí, platforem a cen se zdroji.",
            "og_title": "Rodinka vs Familia",
            "og_description": "Dva rodinné plánovače s češtinou: v čem se liší a pro jakou rodinu se hodí který.",
            "og_alt": "Srovnání aplikací Rodinka a Familia",
            "h1": "Rodinka vs Familia",
            "lead": "Obě aplikace chtějí rodině ulehčit plánování a obě mluví česky. Familia sází na rychlé zachycení úkolů s pomocí AI, Rodinka na společný přehled celé domácnosti včetně dětí, jídel, výletů a vzpomínek.",
            "card": "Rychlé zadávání s AI, nebo společný přehled celé domácnosti.",
            "answer": ("Jaký je hlavní rozdíl mezi Rodinkou a Familií?", "Familia je postavená na rychlém zadávání: hlasem, textem nebo fotkou vytvoříte návrh úkolu či plánu a jen ho potvrdíte; propojí se i s Google Kalendářem. Rodinka pokrývá širší rodinný provoz: kalendář s doprovodem, dětské účty s odměnami a kapesným, plán jídel, nákupy, výlety, mazlíčky a vzpomínky, a funguje v prohlížeči i offline. Propojení s jinými kalendáři zatím nemá."),
            "fit_rodinka": (
                "chcete mít kalendář, úkoly, nákupy, jídla i výlety v jednom rodinném prostoru,",
                "se mají zapojit děti s vlastním přihlášením a odměnami nebo kapesným,",
                "chcete Rodinku používat i na počítači v prohlížeči bez placeného tarifu.",
            ),
            "fit_comp": (
                "zadáváte hodně věcí za pochodu a vyhovuje vám diktovat nebo vyfotit papír,",
                "chcete úkoly a plány propojit s Google Kalendářem,",
                "používáte hlavně mobilní aplikaci pro iPhone nebo Android.",
            ),
            "scenarios": (
                ("Lísteček ze školky", "Ve Familii lísteček vyfotíte a z fotky vznikne návrh, který zkontrolujete. V Rodince termín zapíšete ručně a rovnou určíte, koho se týká a kdo dítě doprovodí."),
                ("Týden vaření", "V Rodince naplánujete jídla na týden, rodina může hlasovat a chybějící suroviny se jedním krokem přesunou do nákupního seznamu. Plánování jídel jsme na webu Familie nenašli."),
                ("Úkoly pro děti", "V Rodince má dítě vlastní přihlášení, odškrtne úkol a po potvrzení dospělým se mu připíše odměna nebo kapesné. U Familie jsme dětské profily ani odměny neověřili."),
            ),
            "rodinka_pros": (
                "Široký rodinný záběr od kalendáře po vzpomínky a mazlíčky",
                "Dětské účty s omezeným pohledem, odměnami a kapesným",
                "Webová verze zdarma, část funkcí i offline",
            ),
            "rodinka_cons": (
                "Zatím bez propojení s Google, Apple nebo Outlook kalendářem",
                "Zadávání s pomocí AI z fotky nebo textu nenabízí",
            ),
            "comp_pros": (
                "Rychlé zachycení úkolů hlasem, textem nebo fotkou",
                "Propojení s Google Kalendářem",
                "Aplikace pro iPhone, iPad a Android s českou verzí",
            ),
            "comp_cons": (
                "Webová verze jen s placeným Smart a spárováním z mobilu",
                "Ve verzi Free 10 AI kreditů měsíčně a jedna příloha k položce",
            ),
            "pricing": (
                "Rodinka běží v prohlížeči na telefonu, tabletu i počítači a na plochu ji přidáte jako aplikaci; ve Windows ji najdete i v Microsoft Store. Rodinka Free je zdarma a bez platební karty. Rodinka Pro pro celou rodinu přidává další nástroje a víc místa na fotky; ceny zatím nezveřejňujeme a případnou nabídku uvidíte v aplikaci.",
                "Familia nabízí aplikace pro iPhone, iPad a Android; webová verze patří k tarifu Smart. Free je zdarma, Smart je měsíční předplatné pro celou rodinu. Web uvádí cenu se symbolem $ bez kódu měny a upozorňuje, že ceny v App Store se liší podle země, proto částku neuvádíme.",
            ),
            "faq": (
                ("Je Rodinka alternativa k Familii?", "Ano, pokud hledáte rodinný plánovač, který pokryje i děti, jídla, výlety a vzpomínky. Pokud je pro vás nejdůležitější zadávání s pomocí AI a propojení s Google Kalendářem, bude vám bližší Familia."),
                ("Umí obě aplikace česky?", "Ano. Rodinka má celé rozhraní česky, slovensky a anglicky. Familia na svém webu uvádí podporu češtiny; slovenštinu se nám ověřit nepodařilo."),
                ("Potřebuji pro používání na počítači platit?", "U Rodinky ne, webová verze je základní způsob používání a je i ve verzi Free. U Familie je webová verze podle jejího ceníku součástí tarifu Smart."),
                ("Mohu v Rodince vidět svůj Google Kalendář?", "Zatím ne. Rodinka nyní nepropojuje externí kalendáře a rodinné termíny zapisujete přímo do ní. Familia propojení s Google Kalendářem nabízí."),
                ("Mají v aplikacích děti vlastní účet?", "V Rodince ano: dítě se přihlásí bez e-mailu a vidí jen svoje úkoly, nákupní seznam a kalendář. U Familie jsme informaci o dětských účtech na webu nenašli."),
            ),
            "verdict": (
                "Pokud chcete hlavně co nejrychleji dostat věci z hlavy do aplikace a máte kalendář v Googlu, vyzkoušejte Familii.",
                "Pokud chcete, aby celá rodina, včetně dětí a prarodičů, viděla stejný plán a zvládala v něm i nákupy, jídla a výlety, vyzkoušejte Rodinku. Obě mají bezplatnou verzi, takže si je můžete projít vedle sebe.",
            ),
            "cta_title": "Projděte si Rodinku na vlastním týdnu.",
            "cta_text": "Založte rodinu zdarma, přidejte první kroužek a úkol a porovnejte sami, co vám sedí víc.",
        },
        "sk": {
            "title": "Rodinka vs Familia: porovnanie rodinných plánovačov | Rodinka",
            "description": "Familia vs Rodinka: rýchle zadávanie s AI, alebo celá rodinná prevádzka s deťmi, jedlami a výletmi? Porovnanie funkcií, platforiem a cien so zdrojmi.",
            "og_title": "Rodinka vs Familia",
            "og_description": "Dva rodinné plánovače s češtinou: v čom sa líšia a pre akú rodinu sa hodí ktorý.",
            "og_alt": "Porovnanie aplikácií Rodinka a Familia",
            "h1": "Rodinka vs Familia",
            "lead": "Obe aplikácie chcú rodine uľahčiť plánovanie. Familia stavia na rýchlom zachytení úloh s pomocou AI, Rodinka na spoločný prehľad celej domácnosti vrátane detí, jedál, výletov a spomienok, a to aj po slovensky.",
            "card": "Rýchle zadávanie s AI, alebo spoločný prehľad celej domácnosti.",
            "answer": ("Aký je hlavný rozdiel medzi Rodinkou a Familiou?", "Familia je postavená na rýchlom zadávaní: hlasom, textom alebo fotkou vytvoríte návrh úlohy či plánu a len ho potvrdíte; prepojí sa aj s Google Kalendárom. Rodinka pokrýva širšiu rodinnú prevádzku: kalendár so sprievodom, detské účty s odmenami a vreckovým, plán jedál, nákupy, výlety, zvieratká a spomienky, a funguje v prehliadači aj offline. Prepojenie s inými kalendármi zatiaľ nemá."),
            "fit_rodinka": (
                "chcete mať kalendár, úlohy, nákupy, jedlá aj výlety v jednom rodinnom priestore,",
                "sa majú zapojiť deti s vlastným prihlásením a odmenami alebo vreckovým,",
                "chcete aplikáciu po slovensky a aj v prehliadači na počítači bez plateného tarifu.",
            ),
            "fit_comp": (
                "zadávate veľa vecí za pochodu a vyhovuje vám diktovať alebo odfotiť papier,",
                "chcete úlohy a plány prepojiť s Google Kalendárom,",
                "používate hlavne mobilnú aplikáciu pre iPhone alebo Android.",
            ),
            "scenarios": (
                ("Lístok zo škôlky", "Vo Familii lístok odfotíte a z fotky vznikne návrh, ktorý skontrolujete. V Rodinke termín zapíšete ručne a rovno určíte, koho sa týka a kto dieťa odprevadí."),
                ("Týždeň varenia", "V Rodinke naplánujete jedlá na týždeň, rodina môže hlasovať a chýbajúce suroviny sa jedným krokom presunú do nákupného zoznamu. Plánovanie jedál sme na webe Familie nenašli."),
                ("Úlohy pre deti", "V Rodinke má dieťa vlastné prihlásenie, odškrtne úlohu a po potvrdení dospelým sa mu pripíše odmena alebo vreckové. Pri Familii sme detské profily ani odmeny neoverili."),
            ),
            "rodinka_pros": (
                "Široký rodinný záber od kalendára po spomienky a zvieratká",
                "Detské účty s obmedzeným pohľadom, odmenami a vreckovým",
                "Webová verzia zadarmo, časť funkcií aj offline",
            ),
            "rodinka_cons": (
                "Zatiaľ bez prepojenia s Google, Apple alebo Outlook kalendárom",
                "Zadávanie s pomocou AI z fotky alebo textu neponúka",
            ),
            "comp_pros": (
                "Rýchle zachytenie úloh hlasom, textom alebo fotkou",
                "Prepojenie s Google Kalendárom",
                "Aplikácia pre iPhone, iPad a Android",
            ),
            "comp_cons": (
                "Webová verzia len s plateným Smart a spárovaním z mobilu",
                "Vo verzii Free 10 AI kreditov mesačne a jedna príloha k položke",
            ),
            "pricing": (
                "Rodinka beží v prehliadači v telefóne, tablete aj počítači a na plochu ju pridáte ako aplikáciu; vo Windows ju nájdete aj v Microsoft Store. Rodinka Free je zadarmo a bez platobnej karty. Rodinka Pro pre celú rodinu pridáva ďalšie nástroje a viac miesta na fotky; ceny zatiaľ nezverejňujeme a prípadnú ponuku uvidíte v aplikácii.",
                "Familia ponúka aplikácie pre iPhone, iPad a Android; webová verzia patrí k tarifu Smart. Free je zadarmo, Smart je mesačné predplatné pre celú rodinu. Web uvádza cenu so symbolom $ bez kódu meny a upozorňuje, že ceny v App Store sa líšia podľa krajiny, preto sumu neuvádzame.",
            ),
            "faq": (
                ("Je Rodinka alternatíva k Familii?", "Áno, ak hľadáte rodinný plánovač, ktorý pokryje aj deti, jedlá, výlety a spomienky. Ak je pre vás najdôležitejšie zadávanie s pomocou AI a prepojenie s Google Kalendárom, bude vám bližšia Familia."),
                ("Vedia obe aplikácie po slovensky?", "Rodinka má celé rozhranie po slovensky, česky a anglicky. Familia na svojom webe uvádza podporu češtiny; slovenčinu sa nám overiť nepodarilo."),
                ("Potrebujem na používanie v počítači platiť?", "Pri Rodinke nie, webová verzia je základný spôsob používania a je aj vo verzii Free. Pri Familii je webová verzia podľa jej cenníka súčasťou tarifu Smart."),
                ("Môžem v Rodinke vidieť svoj Google Kalendár?", "Zatiaľ nie. Rodinka teraz neprepája externé kalendáre a rodinné termíny zapisujete priamo do nej. Familia prepojenie s Google Kalendárom ponúka."),
                ("Majú v aplikáciách deti vlastný účet?", "V Rodinke áno: dieťa sa prihlási bez e-mailu a vidí len svoje úlohy, nákupný zoznam a kalendár. Pri Familii sme informáciu o detských účtoch na webe nenašli."),
            ),
            "verdict": (
                "Ak chcete hlavne čo najrýchlejšie dostať veci z hlavy do aplikácie a máte kalendár v Googli, vyskúšajte Familiu.",
                "Ak chcete, aby celá rodina vrátane detí a starých rodičov videla rovnaký plán a zvládala v ňom aj nákupy, jedlá a výlety, vyskúšajte Rodinku. Obe majú bezplatnú verziu, takže si ich môžete prejsť vedľa seba.",
            ),
            "cta_title": "Prejdite si Rodinku na vlastnom týždni.",
            "cta_text": "Založte rodinu zadarmo, pridajte prvý krúžok a úlohu a porovnajte sami, čo vám sedí viac.",
        },
        "en": {
            "title": "Rodinka vs Familia: family planner comparison | Rodinka",
            "description": "Familia vs Rodinka: quick AI-assisted capture, or the whole of family life with children, meals and trips? Features, platforms and pricing compared, with sources.",
            "og_title": "Rodinka vs Familia",
            "og_description": "Two family planners compared: how they differ and which kind of family each one suits.",
            "og_alt": "Comparison of the Rodinka and Familia apps",
            "h1": "Rodinka vs Familia",
            "lead": "Both apps want to make family planning lighter. Familia is built around capturing tasks quickly with AI help; Rodinka around one shared overview of the whole household, including children, meals, trips and memories.",
            "card": "Quick AI-assisted capture, or one overview of the whole household.",
            "answer": ("What is the main difference between Rodinka and Familia?", "Familia is built for quick capture: voice, text or a photo becomes a draft task or plan that you simply confirm, and it connects to Google Calendar. Rodinka covers more of family life: a calendar that shows who is taking whom, children’s accounts with rewards and pocket money, meal planning, shopping, trips, pets and memories, and it works in a browser and offline. It does not connect to other calendars yet."),
            "fit_rodinka": (
                "you want the calendar, chores, shopping, meals and trips in one family space,",
                "children should take part with their own sign-in and rewards or pocket money,",
                "you want to use it in a browser on a computer without a paid plan.",
            ),
            "fit_comp": (
                "you add a lot on the go and like to dictate or photograph a note,",
                "you want tasks and plans connected to Google Calendar,",
                "you mainly use a phone app on iPhone or Android.",
            ),
            "scenarios": (
                ("A note from nursery", "In Familia you photograph the note and get a draft to review. In Rodinka you type the date yourself and say straight away who it is for and who will take the child."),
                ("A week of cooking", "In Rodinka you plan the week’s meals, the family can vote and missing ingredients move to the shopping list in one step. We did not find meal planning on Familia’s website."),
                ("Chores for children", "In Rodinka a child has their own sign-in, ticks off a chore and, once an adult confirms it, gets the reward or pocket money. For Familia we could not verify children’s profiles or rewards."),
            ),
            "rodinka_pros": (
                "Covers family life from the calendar to memories and pets",
                "Children’s accounts with a limited view, rewards and pocket money",
                "Free web version, with parts working offline",
            ),
            "rodinka_cons": (
                "No Google, Apple or Outlook calendar connection yet",
                "No AI-assisted capture from photos or text",
            ),
            "comp_pros": (
                "Quick capture by voice, text or photo",
                "Google Calendar connection",
                "Apps for iPhone, iPad and Android, with a Czech version",
            ),
            "comp_cons": (
                "Web version only with paid Smart and pairing from the phone",
                "Free includes 10 AI credits a month and one attachment per item",
            ),
            "pricing": (
                "Rodinka runs in the browser on phones, tablets and computers and can be added to the home screen like an app; on Windows it is also in the Microsoft Store. Rodinka Free costs nothing and needs no payment card. Rodinka Pro, for the whole family, adds more tools and photo storage; prices are not published yet, and any offer will be shown in the app.",
                "Familia offers apps for iPhone, iPad and Android; the web version comes with the Smart plan. Free costs nothing and Smart is a monthly subscription for the whole family. The site shows the price with a $ sign and no currency code and notes that App Store prices vary by country, so we do not quote an amount.",
            ),
            "faq": (
                ("Is Rodinka an alternative to Familia?", "Yes, if you want a family planner that also covers children, meals, trips and memories. If AI-assisted capture and a Google Calendar connection matter most, Familia will suit you better."),
                ("Do both apps support Czech?", "Yes. Rodinka’s whole interface is in Czech, Slovak and English. Familia says on its website that it supports Czech; we could not verify Slovak."),
                ("Do I have to pay to use it on a computer?", "Not with Rodinka: the web version is the main way to use it and is part of Rodinka Free. According to Familia’s pricing, its web version is part of the Smart plan."),
                ("Can I see my Google Calendar in Rodinka?", "Not yet. Rodinka does not connect external calendars at the moment; you add family dates directly. Familia does offer a Google Calendar connection."),
                ("Do children get their own account?", "In Rodinka, yes: a child signs in without an email address and sees only their own chores, the shopping list and the calendar. We did not find information about children’s accounts on Familia’s website."),
            ),
            "verdict": (
                "If you mainly want to get things out of your head and into an app as fast as possible, and your calendar lives in Google, try Familia.",
                "If you want the whole family, children and grandparents included, to see the same plan and handle shopping, meals and trips in it too, try Rodinka. Both have a free version, so you can try them side by side.",
            ),
            "cta_title": "Try Rodinka on a real week.",
            "cta_text": "Create your family for free, add the first activity and chore, and see for yourself what suits you better.",
        },
    },
}

COMPARISON_PAGES["familywall"] = {
    "cs": {
        "title": "Alternativa k FamilyWall: Rodinka vs FamilyWall | Rodinka",
        "description": "Hledáte alternativu k FamilyWall? Srovnání Rodinky a FamilyWall: sdílený rodinný kalendář, úkoly, jídla, děti, poloha, platformy a ceny podle oficiálních zdrojů.",
        "og_title": "Rodinka vs FamilyWall",
        "og_description": "Rodinný plánovač v češtině, nebo rodinná síť se zprávami a polohou? Férové srovnání se zdroji.",
        "og_alt": "Srovnání aplikací Rodinka a FamilyWall",
        "h1": "Rodinka vs FamilyWall",
        "lead": "FamilyWall je rodinná aplikace s kalendářem, seznamy, messengerem, galerií a sdílením polohy. Rodinka se soustředí na každodenní plánování domácnosti v češtině a slovenštině, s dětskými účty, jídly, výlety a vzpomínkami.",
        "card": "Rodinný plánovač v češtině, nebo rodinná síť se zprávami a polohou.",
        "answer": ("Jaký je hlavní rozdíl mezi Rodinkou a FamilyWall?", "FamilyWall spojuje sdílený kalendář a seznamy s rodinným messengerem, galerií fotek a sdílením polohy; plánovač jídel, dokumenty a propojení s Google a Outlook kalendářem jsou v Premium. Rodinka nabízí kalendář s doprovodem, úkoly s odměnami a kapesným pro děti, plán jídel, výlety, mazlíčky a společnou kroniku ve verzi zdarma, celé rozhraní česky a slovensky. Polohu nesdílí a jiné kalendáře zatím nepropojí."),
        "fit_rodinka": (
            "chcete mít rodinné plánování v češtině nebo slovenštině, i pro prarodiče,",
            "chcete dětem dát vlastní účet s úkoly, odměnami a kapesným,",
            "plánujete jídla a výlety a nechcete kvůli tomu placený tarif.",
        ),
        "fit_comp": (
            "chcete v rodině sdílet polohu a dostávat upozornění na příchod domů nebo do školy,",
            "rodina si píše a posílá fotky a videa v jedné aplikaci,",
            "potřebujete vidět pracovní kalendář Google nebo Outlook vedle rodinného.",
        ),
        "scenarios": (
            ("Kdo vyzvedne dceru z tréninku", "V Rodince je u tréninku vidět, koho se týká a kdo ho doprovází, a babička může termín potvrdit odkazem bez účtu. Ve FamilyWall najdete termín ve sdíleném kalendáři a podle webu můžete vidět, kde se kdo nachází."),
                ("Plán jídel na týden", "V Rodince je plán jídel s hlasováním a přenosem surovin do nákupu součástí verze zdarma. Ve FamilyWall je plánovač jídel s recepty podle nápovědy součástí Premium."),
            ("Platnost pasů před dovolenou", "Rodinka připomene konec platnosti dokladů s předstihem a doklady vidí jen dospělí. FamilyWall nabízí sdílení dokumentů v Premium; hlídání platnosti jsme na webu nenašli."),
        ),
        "rodinka_pros": (
            "Celé rozhraní česky a slovensky",
            "Dětské účty s odměnami, kapesným a omezeným pohledem",
            "Plán jídel, výlety, mazlíčci a kronika ve verzi zdarma",
        ),
        "rodinka_cons": (
            "Bez sdílení polohy",
            "Zatím bez propojení s Google, Apple nebo Outlook kalendářem",
            "Na telefonu jako webová aplikace přidaná na plochu",
        ),
        "comp_pros": (
            "Rodinný messenger a galerie fotek a videí",
            "Sdílení polohy a upozornění na příchod a odchod",
            "Aplikace pro iPhone, iPad, Android i web, podle webu bez reklam",
        ),
        "comp_cons": (
            "Plánovač jídel, dokumenty a propojení kalendářů jsou v Premium",
            "Češtinu ani slovenštinu se nám ověřit nepodařilo",
        ),
        "pricing": (
            "Rodinka běží v prohlížeči na telefonu, tabletu i počítači a na plochu ji přidáte jako aplikaci; ve Windows ji najdete i v Microsoft Store. Rodinka Free je zdarma a bez platební karty a obsahuje kalendář, úkoly, nákupy, jídla, výlety, vzpomínky i doklady. Rodinka Pro pro celou rodinu přidává další nástroje a víc místa na fotky; ceny zatím nezveřejňujeme.",
            "FamilyWall je dostupná na webu, iPhonu, iPadu a Androidu. Základ je zdarma, Premium platí pro celou rodinu, dá se platit měsíčně nebo ročně a začíná 30denní zkušební verzí. Předplatit lze přes Google Play, App Store nebo web. Cena je na webu uvedena se symbolem $ bez kódu měny, proto ji neuvádíme.",
        ),
        "faq": (
            ("Je Rodinka dobrá alternativa k FamilyWall?", "Pokud hledáte rodinný plánovač v češtině nebo slovenštině s dětskými účty, jídly a výlety ve verzi zdarma, tak ano. Pokud potřebujete sdílení polohy nebo rodinný messenger s videem, Rodinka to nenahradí."),
            ("Má Rodinka sdílení polohy jako FamilyWall?", "Ne. Rodinka polohu členů rodiny nesdílí. Rodinná místa v ní slouží k plánování a otevření navigace na místo konání."),
            ("Je FamilyWall v češtině?", "Češtinu ani slovenštinu se nám na oficiálním webu FamilyWall ověřit nepodařilo. Nápověda je v angličtině, francouzštině, němčině, portugalštině a španělštině."),
            ("Jak přenesu kalendář z FamilyWall do Rodinky?", "Automatický import Rodinka zatím nenabízí. Pravidelné termíny, jako kroužky, stačí zadat jednou s opakováním a jednorázové události průběžně."),
            ("Které funkce jsou u FamilyWall placené?", "Podle nápovědy FamilyWall mimo jiné plánovač jídel, sdílení dokumentů, rozpočet, rozvrhy, propojení s Google a Outlook kalendářem, rozšířená poloha a víc úložiště."),
        ),
        "verdict": (
            "Pokud je pro vás důležité vidět, kde se kdo z rodiny nachází, a chcete si v aplikaci i psát a posílat fotky, je FamilyWall dobrá volba.",
            "Pokud chcete hlavně společně plánovat týden v češtině nebo slovenštině, zapojit děti s jejich vlastními úkoly a mít jídla a výlety bez placeného tarifu, vyzkoušejte Rodinku.",
        ),
        "cta_title": "Zkuste Rodinku jako rodinný plánovač.",
        "cta_text": "Je zdarma a bez karty. Přidejte kroužky, úkoly a nákup a uvidíte, jestli vám společný přehled sedí.",
    },
    "sk": {
        "title": "Alternatíva k FamilyWall: Rodinka vs FamilyWall | Rodinka",
        "description": "Hľadáte alternatívu k FamilyWall? Porovnanie Rodinky a FamilyWall: zdieľaný rodinný kalendár, úlohy, jedlá, deti, poloha, platformy a ceny podľa oficiálnych zdrojov.",
        "og_title": "Rodinka vs FamilyWall",
        "og_description": "Rodinný plánovač po slovensky, alebo rodinná sieť so správami a polohou? Férové porovnanie so zdrojmi.",
        "og_alt": "Porovnanie aplikácií Rodinka a FamilyWall",
        "h1": "Rodinka vs FamilyWall",
        "lead": "FamilyWall je rodinná aplikácia s kalendárom, zoznamami, messengerom, galériou a zdieľaním polohy. Rodinka sa sústreďuje na každodenné plánovanie domácnosti po slovensky a po česky, s detskými účtami, jedlami, výletmi a spomienkami.",
        "card": "Rodinný plánovač po slovensky, alebo rodinná sieť so správami a polohou.",
        "answer": ("Aký je hlavný rozdiel medzi Rodinkou a FamilyWall?", "FamilyWall spája zdieľaný kalendár a zoznamy s rodinným messengerom, galériou fotiek a zdieľaním polohy; plánovač jedál, dokumenty a prepojenie s Google a Outlook kalendárom sú v Premium. Rodinka ponúka kalendár so sprievodom, úlohy s odmenami a vreckovým pre deti, plán jedál, výlety, zvieratká a spoločnú kroniku vo verzii zadarmo, celé rozhranie po slovensky a po česky. Polohu nezdieľa a iné kalendáre zatiaľ neprepojí."),
        "fit_rodinka": (
            "chcete mať rodinné plánovanie po slovensky alebo po česky, aj pre starých rodičov,",
            "chcete deťom dať vlastný účet s úlohami, odmenami a vreckovým,",
            "plánujete jedlá a výlety a nechcete kvôli tomu platený tarif.",
        ),
        "fit_comp": (
            "chcete v rodine zdieľať polohu a dostávať upozornenia na príchod domov alebo do školy,",
            "rodina si píše a posiela fotky a videá v jednej aplikácii,",
            "potrebujete vidieť pracovný kalendár Google alebo Outlook vedľa rodinného.",
        ),
        "scenarios": (
            ("Kto vyzdvihne dcéru z tréningu", "V Rodinke pri tréningu vidno, koho sa týka a kto ho sprevádza, a stará mama môže termín potvrdiť odkazom bez účtu. Vo FamilyWall nájdete termín v zdieľanom kalendári a podľa webu môžete vidieť, kde sa kto nachádza."),
            ("Plán jedál na týždeň", "V Rodinke je plán jedál s hlasovaním a prenosom surovín do nákupu súčasťou verzie zadarmo. Vo FamilyWall je plánovač jedál s receptami podľa nápovedy súčasťou Premium."),
            ("Platnosť pasov pred dovolenkou", "Rodinka pripomenie koniec platnosti dokladov s predstihom a doklady vidia len dospelí. FamilyWall ponúka zdieľanie dokumentov v Premium; stráženie platnosti sme na webe nenašli."),
        ),
        "rodinka_pros": (
            "Celé rozhranie po slovensky a po česky",
            "Detské účty s odmenami, vreckovým a obmedzeným pohľadom",
            "Plán jedál, výlety, zvieratká a kronika vo verzii zadarmo",
        ),
        "rodinka_cons": (
            "Bez zdieľania polohy",
            "Zatiaľ bez prepojenia s Google, Apple alebo Outlook kalendárom",
            "V telefóne ako webová aplikácia pridaná na plochu",
        ),
        "comp_pros": (
            "Rodinný messenger a galéria fotiek a videí",
            "Zdieľanie polohy a upozornenia na príchod a odchod",
            "Aplikácia pre iPhone, iPad, Android aj web, podľa webu bez reklám",
        ),
        "comp_cons": (
            "Plánovač jedál, dokumenty a prepojenie kalendárov sú v Premium",
            "Češtinu ani slovenčinu sa nám overiť nepodarilo",
        ),
        "pricing": (
            "Rodinka beží v prehliadači v telefóne, tablete aj počítači a na plochu ju pridáte ako aplikáciu; vo Windows ju nájdete aj v Microsoft Store. Rodinka Free je zadarmo a bez platobnej karty a obsahuje kalendár, úlohy, nákupy, jedlá, výlety, spomienky aj doklady. Rodinka Pro pre celú rodinu pridáva ďalšie nástroje a viac miesta na fotky; ceny zatiaľ nezverejňujeme.",
            "FamilyWall je dostupná na webe, iPhone, iPade a Androide. Základ je zadarmo, Premium platí pre celú rodinu, dá sa platiť mesačne alebo ročne a začína 30-dňovou skúšobnou verziou. Predplatiť možno cez Google Play, App Store alebo web. Cena je na webe uvedená so symbolom $ bez kódu meny, preto ju neuvádzame.",
        ),
        "faq": (
            ("Je Rodinka dobrá alternatíva k FamilyWall?", "Ak hľadáte rodinný plánovač po slovensky alebo po česky s detskými účtami, jedlami a výletmi vo verzii zadarmo, tak áno. Ak potrebujete zdieľanie polohy alebo rodinný messenger s videom, Rodinka to nenahradí."),
            ("Má Rodinka zdieľanie polohy ako FamilyWall?", "Nie. Rodinka polohu členov rodiny nezdieľa. Rodinné miesta v nej slúžia na plánovanie a otvorenie navigácie na miesto konania."),
            ("Je FamilyWall po slovensky?", "Slovenčinu ani češtinu sa nám na oficiálnom webe FamilyWall overiť nepodarilo. Nápoveda je v angličtine, francúzštine, nemčine, portugalčine a španielčine."),
            ("Ako prenesiem kalendár z FamilyWall do Rodinky?", "Automatický import Rodinka zatiaľ neponúka. Pravidelné termíny, ako krúžky, stačí zadať raz s opakovaním a jednorazové udalosti priebežne."),
            ("Ktoré funkcie sú pri FamilyWall platené?", "Podľa nápovedy FamilyWall okrem iného plánovač jedál, zdieľanie dokumentov, rozpočet, rozvrhy, prepojenie s Google a Outlook kalendárom, rozšírená poloha a viac úložiska."),
        ),
        "verdict": (
            "Ak je pre vás dôležité vidieť, kde sa kto z rodiny nachádza, a chcete si v aplikácii aj písať a posielať fotky, je FamilyWall dobrá voľba.",
            "Ak chcete hlavne spoločne plánovať týždeň po slovensky alebo po česky, zapojiť deti s ich vlastnými úlohami a mať jedlá a výlety bez plateného tarifu, vyskúšajte Rodinku.",
        ),
        "cta_title": "Skúste Rodinku ako rodinný plánovač.",
        "cta_text": "Je zadarmo a bez karty. Pridajte krúžky, úlohy a nákup a uvidíte, či vám spoločný prehľad sedí.",
    },
    "en": {
        "title": "FamilyWall alternative: Rodinka vs FamilyWall | Rodinka",
        "description": "Looking for a FamilyWall alternative? Rodinka and FamilyWall compared: shared family calendar, chores, meals, children, location, platforms and pricing from official sources.",
        "og_title": "Rodinka vs FamilyWall",
        "og_description": "A family planner, or a family network with messaging and location? A fair comparison with sources.",
        "og_alt": "Comparison of the Rodinka and FamilyWall apps",
        "h1": "Rodinka vs FamilyWall",
        "lead": "FamilyWall is a family app with a calendar, lists, a messenger, a gallery and location sharing. Rodinka focuses on everyday household planning in Czech, Slovak and English, with children’s accounts, meals, trips and memories.",
        "card": "A family planner, or a family network with messaging and location.",
        "answer": ("What is the main difference between Rodinka and FamilyWall?", "FamilyWall combines a shared calendar and lists with a family messenger, a photo gallery and location sharing; the meal planner, documents and the Google and Outlook calendar connection are in Premium. Rodinka offers a calendar that shows who is taking whom, chores with rewards and pocket money for children, meal planning, trips, pets and a shared chronicle in its free version, with the whole interface in Czech, Slovak and English. It does not share locations and does not connect other calendars yet."),
        "fit_rodinka": (
            "you want family planning in Czech or Slovak, including for grandparents,",
            "you want to give children their own account with chores, rewards and pocket money,",
            "you plan meals and trips and do not want a paid plan for that.",
        ),
        "fit_comp": (
            "you want to share locations in the family and get arrival alerts for home or school,",
            "your family chats and shares photos and videos in one app,",
            "you need your Google or Outlook work calendar next to the family one.",
        ),
        "scenarios": (
            ("Who picks up from practice", "In Rodinka the practice shows who it is for and who is taking her, and Grandma can confirm by link without an account. In FamilyWall the date is in the shared calendar and, according to the website, you can see where everyone is."),
            ("A week of meals", "In Rodinka the meal plan, with voting and ingredients sent to the shopping list, is part of the free version. In FamilyWall the meal planner with recipes is part of Premium, according to its help center."),
            ("Passports before a holiday", "Rodinka reminds you well before documents expire, and only adults can see them. FamilyWall offers document sharing in Premium; we did not find expiry reminders on its website."),
        ),
        "rodinka_pros": (
            "The whole interface in Czech, Slovak and English",
            "Children’s accounts with rewards, pocket money and a limited view",
            "Meal planning, trips, pets and the chronicle in the free version",
        ),
        "rodinka_cons": (
            "No location sharing",
            "No Google, Apple or Outlook calendar connection yet",
            "On phones it runs as a web app added to the home screen",
        ),
        "comp_pros": (
            "A family messenger and a photo and video gallery",
            "Location sharing with arrival and departure alerts",
            "Apps for iPhone, iPad and Android plus the web, ad-free according to the website",
        ),
        "comp_cons": (
            "Meal planner, documents and calendar connections are in Premium",
            "We could not verify Czech or Slovak",
        ),
        "pricing": (
            "Rodinka runs in the browser on phones, tablets and computers and can be added to the home screen like an app; on Windows it is also in the Microsoft Store. Rodinka Free costs nothing, needs no payment card and includes the calendar, chores, shopping, meals, trips, memories and documents. Rodinka Pro, for the whole family, adds more tools and photo storage; prices are not published yet.",
            "FamilyWall is available on the web, iPhone, iPad and Android. The core is free; Premium covers the whole family, can be paid monthly or yearly and starts with a 30-day trial. You can subscribe through Google Play, the App Store or the website. The site shows the price with a $ sign and no currency code, so we do not quote it.",
        ),
        "faq": (
            ("Is Rodinka a good FamilyWall alternative?", "If you want a family planner with children’s accounts, meals and trips in the free version, and Czech or Slovak matters, yes. If you need location sharing or a family messenger with video, Rodinka does not replace that."),
            ("Does Rodinka share locations like FamilyWall?", "No. Rodinka does not share family members’ locations. Family places are there for planning and opening directions to where something happens."),
            ("Is FamilyWall available in Czech?", "We could not verify Czech or Slovak on FamilyWall’s official website. Its help center is in English, French, German, Portuguese and Spanish."),
            ("How do I move my calendar from FamilyWall to Rodinka?", "Rodinka does not offer automatic import yet. Recurring dates such as activities only need to be added once with a repeat, and one-off events as they come."),
            ("Which FamilyWall features are paid?", "According to FamilyWall’s help center, these include the meal planner, document sharing, the budget tracker, timetables, Google and Outlook calendar connection, enhanced location and extra storage."),
        ),
        "verdict": (
            "If seeing where family members are matters to you and you want to chat and share photos in the same app, FamilyWall is a good choice.",
            "If you mainly want to plan the week together, involve children with chores of their own, and have meals and trips without a paid plan, try Rodinka.",
        ),
        "cta_title": "Try Rodinka as your family planner.",
        "cta_text": "It is free and needs no card. Add your activities, chores and shopping, and see whether a shared overview works for you.",
    },
}

COMPARISON_PAGES["cozi"] = {
    "cs": {
        "title": "Alternativa ke Cozi: Rodinka vs Cozi | Rodinka",
        "description": "Hledáte alternativu ke Cozi v češtině? Srovnání Rodinky a Cozi: sdílený rodinný kalendář, nákupy, jídla, děti, oprávnění, propojení kalendářů a ceny se zdroji.",
        "og_title": "Rodinka vs Cozi",
        "og_description": "Osvědčený rodinný kalendář v angličtině, nebo rodinný plánovač v češtině s dětskými účty? Srovnání se zdroji.",
        "og_alt": "Srovnání aplikací Rodinka a Cozi",
        "h1": "Rodinka vs Cozi",
        "lead": "Cozi je zavedený rodinný organizér s kalendářem, seznamy a receptářem, který umí zobrazit i další kalendáře. Rodinka je rodinný plánovač v češtině a slovenštině, který kromě kalendáře a nákupů řeší i děti, výlety, mazlíčky a vzpomínky.",
        "card": "Rodinný kalendář s propojením jiných kalendářů, nebo plánovač v češtině s dětskými účty.",
        "answer": ("Jaký je hlavní rozdíl mezi Rodinkou a Cozi?", "Cozi nabízí sdílený kalendář až pro 12 členů, nákupní seznamy, povinnosti a receptář a umí zobrazit kalendáře Google, Apple nebo Outlook; verze zdarma má reklamy a podle FAQ v ní každý vidí a upravuje vše. Rodinka má role pro dospělé a děti, dětské účty s odměnami a kapesným, plán jídel, výlety a kroniku, celé rozhraní česky a slovensky a je bez reklam. Jiné kalendáře zatím nepropojí."),
        "fit_rodinka": (
            "chcete aplikaci v češtině nebo slovenštině bez reklam,",
            "chcete dětem ukázat jen to, co je pro ně, a dát jim úkoly s odměnou,",
            "chcete mít v jednom místě i výlety, mazlíčky, doklady a rodinné vzpomínky.",
        ),
        "fit_comp": (
            "potřebujete vidět pracovní, školní nebo sportovní kalendáře vedle rodinného,",
            "vyhovuje vám angličtina a zavedená aplikace s dlouhou historií,",
            "stačí vám, že všichni v účtu mají stejný plný přístup.",
        ),
        "scenarios": (
            ("Rozvrh kroužků na pololetí", "V Cozi zadáte opakovanou událost a do rodinného pohledu přidáte třeba školní kalendář. V Rodince zadáte kroužek s opakováním, určíte dítě a doprovod a změnu jednoho termínu provedete bez zásahu do celé série."),
            ("Dítě s vlastním telefonem", "V Rodince se dítě přihlásí bez e-mailu a vidí jen svoje úkoly, nákup a kalendář, ne doklady ani správu rodiny. Podle FAQ Cozi má každý v účtu plný přístup ke všem údajům."),
            ("Nákup v obchodě bez signálu", "Obě aplikace podle svých informací umožňují odškrtávat nákupní seznam offline. Rodinka offline zvládá i úkoly, kalendář a obrazovku Dnes."),
        ),
        "rodinka_pros": (
            "Celé rozhraní česky a slovensky, bez reklam",
            "Role pro dospělé a děti, dětské účty s odměnami a kapesným",
            "Výlety, mazlíčci, doklady a rodinná kronika na jednom místě",
        ),
        "rodinka_cons": (
            "Zatím bez propojení s Google, Apple nebo Outlook kalendářem",
            "Na telefonu jako webová aplikace přidaná na plochu",
        ),
        "comp_pros": (
            "Zobrazení kalendářů Google, Apple, Outlook a dalších v Cozi",
            "Kalendář, seznamy, povinnosti a receptář ve verzi zdarma",
            "Aplikace pro iPhone a Android i webová verze",
        ),
        "comp_cons": (
            "Verze zdarma obsahuje reklamy",
            "Podle FAQ bez omezeného přístupu pro jednotlivé členy",
            "Češtinu ani slovenštinu se nám ověřit nepodařilo",
        ),
        "pricing": (
            "Rodinka běží v prohlížeči na telefonu, tabletu i počítači a na plochu ji přidáte jako aplikaci; ve Windows ji najdete i v Microsoft Store. Rodinka Free je zdarma, bez reklam a bez platební karty. Rodinka Pro pro celou rodinu přidává další nástroje a víc místa na fotky; ceny zatím nezveřejňujeme.",
            "Cozi je dostupné na webu, iPhonu a Androidu. Verze zdarma je hrazená z reklam. Cozi Gold stojí podle FAQ 39 USD ročně a platí pro všechny v účtu; přidává mimo jiné provoz bez reklam, měsíční pohled v mobilu, hledání a víc připomínek. Dvoutýdenní zkušební verze platí jen při objednání na webu. Vyšší tarif Max přidává AI funkce.",
        ),
        "faq": (
            ("Je Rodinka alternativa ke Cozi?", "Ano, pokud hledáte rodinný plánovač v češtině nebo slovenštině s dětskými účty a bez reklam. Pokud je pro vás klíčové vidět v rodinném kalendáři i pracovní nebo školní kalendáře, Cozi to dnes umí a Rodinka zatím ne."),
            ("Je Cozi v češtině?", "Češtinu ani slovenštinu se nám na oficiálním webu Cozi ověřit nepodařilo. Rodinka má celé rozhraní česky, slovensky a anglicky."),
            ("Mohu v Rodince omezit, co vidí děti?", "Ano. Dětský účet nevidí doklady ani správu rodiny a pomocník, třeba babička, vidí jen termíny, na které ho vyberete jako doprovod. Podle FAQ Cozi taková omezení nenabízí."),
            ("Kolik stojí Cozi Gold?", "Podle FAQ Cozi 39 USD ročně za celý účet (ověřeno 9.\u00a011.\u00a02026). Rodinka Free je zdarma; ceny Rodinky Pro zatím nezveřejňujeme."),
            ("Lze ke vzpomínkám nebo událostem přidat fotku?", "V Rodince ano, vzpomínky a milníky mají fotografie ve společné kronice. Podle FAQ Cozi zatím nepodporuje přikládání obrázků a souborů k událostem a seznamům."),
        ),
        "verdict": (
            "Pokud žijete v angličtině a potřebujete vedle rodinného plánu vidět i pracovní a školní kalendáře, je Cozi osvědčená volba.",
            "Pokud chcete plánovat v češtině nebo slovenštině, zapojit děti s vlastním účtem a mít bez reklam i výlety, mazlíčky a rodinné vzpomínky, vyzkoušejte Rodinku.",
        ),
        "cta_title": "Vyzkoušejte Rodinku bez reklam a bez karty.",
        "cta_text": "Založte rodinu, přidejte první kroužek a nákup a podívejte se, jestli vám Rodinka sedí.",
    },
    "sk": {
        "title": "Alternatíva ku Cozi: Rodinka vs Cozi | Rodinka",
        "description": "Hľadáte alternatívu ku Cozi po slovensky? Porovnanie Rodinky a Cozi: zdieľaný rodinný kalendár, nákupy, jedlá, deti, oprávnenia, prepojenie kalendárov a ceny so zdrojmi.",
        "og_title": "Rodinka vs Cozi",
        "og_description": "Osvedčený rodinný kalendár v angličtine, alebo rodinný plánovač po slovensky s detskými účtami? Porovnanie so zdrojmi.",
        "og_alt": "Porovnanie aplikácií Rodinka a Cozi",
        "h1": "Rodinka vs Cozi",
        "lead": "Cozi je zavedený rodinný organizér s kalendárom, zoznamami a receptárom, ktorý vie zobraziť aj ďalšie kalendáre. Rodinka je rodinný plánovač po slovensky a po česky, ktorý okrem kalendára a nákupov rieši aj deti, výlety, zvieratká a spomienky.",
        "card": "Rodinný kalendár s prepojením iných kalendárov, alebo plánovač po slovensky s detskými účtami.",
        "answer": ("Aký je hlavný rozdiel medzi Rodinkou a Cozi?", "Cozi ponúka zdieľaný kalendár až pre 12 členov, nákupné zoznamy, povinnosti a receptár a vie zobraziť kalendáre Google, Apple alebo Outlook; verzia zadarmo má reklamy a podľa FAQ v nej každý vidí a upravuje všetko. Rodinka má roly pre dospelých a deti, detské účty s odmenami a vreckovým, plán jedál, výlety a kroniku, celé rozhranie po slovensky a po česky a je bez reklám. Iné kalendáre zatiaľ neprepojí."),
        "fit_rodinka": (
            "chcete aplikáciu po slovensky alebo po česky bez reklám,",
            "chcete deťom ukázať len to, čo je pre ne, a dať im úlohy s odmenou,",
            "chcete mať na jednom mieste aj výlety, zvieratká, doklady a rodinné spomienky.",
        ),
        "fit_comp": (
            "potrebujete vidieť pracovné, školské alebo športové kalendáre vedľa rodinného,",
            "vyhovuje vám angličtina a zavedená aplikácia s dlhou históriou,",
            "stačí vám, že všetci v účte majú rovnaký plný prístup.",
        ),
        "scenarios": (
            ("Rozvrh krúžkov na polrok", "V Cozi zadáte opakovanú udalosť a do rodinného pohľadu pridáte napríklad školský kalendár. V Rodinke zadáte krúžok s opakovaním, určíte dieťa a sprievod a zmenu jedného termínu urobíte bez zásahu do celej série."),
            ("Dieťa s vlastným telefónom", "V Rodinke sa dieťa prihlási bez e-mailu a vidí len svoje úlohy, nákup a kalendár, nie doklady ani správu rodiny. Podľa FAQ Cozi má každý v účte plný prístup ku všetkým údajom."),
            ("Nákup v obchode bez signálu", "Obe aplikácie podľa svojich informácií umožňujú odškrtávať nákupný zoznam offline. Rodinka offline zvládne aj úlohy, kalendár a obrazovku Dnes."),
        ),
        "rodinka_pros": (
            "Celé rozhranie po slovensky a po česky, bez reklám",
            "Roly pre dospelých a deti, detské účty s odmenami a vreckovým",
            "Výlety, zvieratká, doklady a rodinná kronika na jednom mieste",
        ),
        "rodinka_cons": (
            "Zatiaľ bez prepojenia s Google, Apple alebo Outlook kalendárom",
            "V telefóne ako webová aplikácia pridaná na plochu",
        ),
        "comp_pros": (
            "Zobrazenie kalendárov Google, Apple, Outlook a ďalších v Cozi",
            "Kalendár, zoznamy, povinnosti a receptár vo verzii zadarmo",
            "Aplikácia pre iPhone a Android aj webová verzia",
        ),
        "comp_cons": (
            "Verzia zadarmo obsahuje reklamy",
            "Podľa FAQ bez obmedzeného prístupu pre jednotlivých členov",
            "Češtinu ani slovenčinu sa nám overiť nepodarilo",
        ),
        "pricing": (
            "Rodinka beží v prehliadači v telefóne, tablete aj počítači a na plochu ju pridáte ako aplikáciu; vo Windows ju nájdete aj v Microsoft Store. Rodinka Free je zadarmo, bez reklám a bez platobnej karty. Rodinka Pro pre celú rodinu pridáva ďalšie nástroje a viac miesta na fotky; ceny zatiaľ nezverejňujeme.",
            "Cozi je dostupné na webe, iPhone a Androide. Verzia zadarmo je hradená z reklám. Cozi Gold stojí podľa FAQ 39 USD ročne a platí pre všetkých v účte; pridáva okrem iného prevádzku bez reklám, mesačný pohľad v mobile, vyhľadávanie a viac pripomienok. Dvojtýždňová skúšobná verzia platí len pri objednaní na webe. Vyšší tarif Max pridáva AI funkcie.",
        ),
        "faq": (
            ("Je Rodinka alternatíva ku Cozi?", "Áno, ak hľadáte rodinný plánovač po slovensky alebo po česky s detskými účtami a bez reklám. Ak je pre vás kľúčové vidieť v rodinnom kalendári aj pracovné alebo školské kalendáre, Cozi to dnes vie a Rodinka zatiaľ nie."),
            ("Je Cozi po slovensky?", "Slovenčinu ani češtinu sa nám na oficiálnom webe Cozi overiť nepodarilo. Rodinka má celé rozhranie po slovensky, česky a anglicky."),
            ("Môžem v Rodinke obmedziť, čo vidia deti?", "Áno. Detský účet nevidí doklady ani správu rodiny a pomocník, napríklad stará mama, vidí len termíny, na ktoré ho vyberiete ako sprievod. Podľa FAQ Cozi takéto obmedzenia neponúka."),
            ("Koľko stojí Cozi Gold?", "Podľa FAQ Cozi 39 USD ročne za celý účet (overené 9.\u00a011.\u00a02026). Rodinka Free je zadarmo; ceny Rodinky Pro zatiaľ nezverejňujeme."),
            ("Dá sa k spomienkam alebo udalostiam pridať fotka?", "V Rodinke áno, spomienky a míľniky majú fotografie v spoločnej kronike. Podľa FAQ Cozi zatiaľ nepodporuje prikladanie obrázkov a súborov k udalostiam a zoznamom."),
        ),
        "verdict": (
            "Ak žijete v angličtine a potrebujete vedľa rodinného plánu vidieť aj pracovné a školské kalendáre, je Cozi osvedčená voľba.",
            "Ak chcete plánovať po slovensky alebo po česky, zapojiť deti s vlastným účtom a mať bez reklám aj výlety, zvieratká a rodinné spomienky, vyskúšajte Rodinku.",
        ),
        "cta_title": "Vyskúšajte Rodinku bez reklám a bez karty.",
        "cta_text": "Založte rodinu, pridajte prvý krúžok a nákup a pozrite sa, či vám Rodinka sedí.",
    },
    "en": {
        "title": "Cozi alternative: Rodinka vs Cozi | Rodinka",
        "description": "Looking for a Cozi alternative? Rodinka and Cozi compared: shared family calendar, shopping, meals, children, permissions, calendar connections and pricing, with sources.",
        "og_title": "Rodinka vs Cozi",
        "og_description": "An established family calendar that connects other calendars, or a family planner with children’s accounts? A comparison with sources.",
        "og_alt": "Comparison of the Rodinka and Cozi apps",
        "h1": "Rodinka vs Cozi",
        "lead": "Cozi is an established family organizer with a calendar, lists and a recipe box that can also show other calendars. Rodinka is a family planner in Czech, Slovak and English that covers children, trips, pets and memories as well as the calendar and shopping.",
        "card": "A family calendar that shows other calendars, or a planner with children’s accounts.",
        "answer": ("What is the main difference between Rodinka and Cozi?", "Cozi offers a shared calendar for up to 12 members, shopping lists, chores and a recipe box, and can show Google, Apple or Outlook calendars; the free version shows ads and, according to its FAQ, everyone sees and edits everything. Rodinka has adult and child roles, children’s accounts with rewards and pocket money, meal planning, trips and a family chronicle, no ads, and Czech and Slovak as well as English. It does not connect other calendars yet."),
        "fit_rodinka": (
            "you want an ad-free app, in Czech or Slovak if that matters to you,",
            "you want children to see only what is meant for them and earn rewards for chores,",
            "you also want trips, pets, documents and family memories in the same place.",
        ),
        "fit_comp": (
            "you need work, school or sports calendars next to the family one,",
            "you are happy in English and like an established app with a long history,",
            "it is fine that everyone in the account has the same full access.",
        ),
        "scenarios": (
            ("A term of activities", "In Cozi you add a recurring event and can bring a school calendar into the family view. In Rodinka you add the activity with a repeat, choose the child and who takes them, and change a single date without touching the series."),
            ("A child with their own phone", "In Rodinka a child signs in without an email address and sees only their chores, the shopping and the calendar, not documents or family settings. According to Cozi’s FAQ, everyone in the account has full access to all data."),
            ("Shopping without signal", "Both apps say the shopping list can be checked off offline. Rodinka also handles chores, the calendar and the Today screen offline."),
        ),
        "rodinka_pros": (
            "No ads, and the whole interface in Czech, Slovak and English",
            "Adult and child roles, children’s accounts with rewards and pocket money",
            "Trips, pets, documents and a family chronicle in one place",
        ),
        "rodinka_cons": (
            "No Google, Apple or Outlook calendar connection yet",
            "On phones it runs as a web app added to the home screen",
        ),
        "comp_pros": (
            "Shows Google, Apple, Outlook and other calendars inside Cozi",
            "Calendar, lists, chores and recipe box in the free version",
            "Apps for iPhone and Android plus a web version",
        ),
        "comp_cons": (
            "The free version shows ads",
            "No restricted access for individual members, according to the FAQ",
            "We could not verify Czech or Slovak",
        ),
        "pricing": (
            "Rodinka runs in the browser on phones, tablets and computers and can be added to the home screen like an app; on Windows it is also in the Microsoft Store. Rodinka Free costs nothing, has no ads and needs no payment card. Rodinka Pro, for the whole family, adds more tools and photo storage; prices are not published yet.",
            "Cozi is available on the web, iPhone and Android. The free version is supported by ads. According to the FAQ, Cozi Gold costs USD 39 a year and covers everyone in the account; it adds no ads, a month view on mobile, search and more reminders, among other things. The two-week trial applies only to subscriptions started on the web. A higher Max plan adds AI features.",
        ),
        "faq": (
            ("Is Rodinka a Cozi alternative?", "Yes, if you want an ad-free family planner with children’s accounts, especially in Czech or Slovak. If seeing work or school calendars inside the family calendar is essential, Cozi does that today and Rodinka does not yet."),
            ("Is Cozi available in Czech?", "We could not verify Czech or Slovak on Cozi’s official website. Rodinka’s whole interface is in Czech, Slovak and English."),
            ("Can I limit what children see in Rodinka?", "Yes. A child account does not see documents or family settings, and a helper such as a grandparent sees only the sessions you pick them for. According to its FAQ, Cozi does not offer restrictions like this."),
            ("How much does Cozi Gold cost?", "According to Cozi’s FAQ, USD 39 a year for the whole account (checked on 9\u00a0November 2026). Rodinka Free costs nothing; Rodinka Pro prices are not published yet."),
            ("Can I add a photo to a memory or an event?", "In Rodinka, yes: memories and milestones carry photos in the shared chronicle. According to Cozi’s FAQ, it does not currently support attaching images or files to events or lists."),
        ),
        "verdict": (
            "If your family works in English and you need work and school calendars next to the family plan, Cozi is a proven choice.",
            "If you want to involve children with their own account, keep the app free of ads and have trips, pets and family memories in it too, try Rodinka.",
        ),
        "cta_title": "Try Rodinka, with no ads and no card.",
        "cta_text": "Create your family, add the first activity and the shopping, and see whether Rodinka suits you.",
    },
}
