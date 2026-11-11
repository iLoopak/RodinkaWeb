"""German copy for the Rodinka marketing site.

Every structure mirrors the English entry of the same name in generate_site.py
(or comparisons.py); install_locale() there merges it in as the "de" locale.
Feature names follow the app's own German catalogue (Heute, Planen, Rodinka
Heute, Moment des Tages, Familienwoche, Familienjahrbuch …), so the website and
the product read the same. Informal "du"/"ihr", like the app.
"""

LOCALE = {
    "lang": "de",
    "og_locale": "de_DE",
    "home_path": "/de/",
    "site_description": "Rodinka ist ein Familienplaner für einen gemeinsamen Kalender, Aufgaben, Einkäufe, Essen, Ausflüge und Familienerinnerungen – für Eltern, Kinder und alle, die der Familie helfen.",
    "claim": "Damit zu Hause alles läuft.",
    "skip": "Zum Inhalt springen",
    "menu": "Menü",
    "nav": {"calendar": "Kalender", "chores": "Aufgaben", "shopping": "Einkauf", "meals": "Essen", "trips": "Ausflüge", "memories": "Erinnerungen"},
    "open_app": "App öffnen",
    "start": "Kostenlos starten",
    "home": "Startseite",
    "features": "Funktionen",
    "primary_nav": "Hauptnavigation",
    "breadcrumb": "Navigationspfad",
    "about": "Rodinka",
    "learn_more": "Mehr erfahren",
    "related": "Verwandte Themen",
    "related_kicker": "WEITERLESEN",
    "language_label": "Sprache der Website",
    "theme_light_label": "Zum hellen Modus wechseln",
    "theme_dark_label": "Zum dunklen Modus wechseln",
    "footer_text": "Ein Familienplaner für Kalender, Aufgaben, Einkäufe, Ausflüge und Erinnerungen – für die ganze Familie und alle, die ihr helfen. Auf Tschechisch, Slowakisch, Englisch, Deutsch und Polnisch.",
    "cta_note": "Rodinka öffnet sich im Browser. Ohne Zahlungskarte und ohne Installation.",
    "social_heading": "Rodinka folgen",
    "new_tab": "öffnet sich in einem neuen Tab",
    "copyright": "© 2026 Rodinka",
    "app_label": "Über die App Rodinka",
    "cookie_settings": "Cookie-Einstellungen",
    "consent_title": "Website-Analyse",
    "consent_text": "Wir nutzen Analysen, um zu verstehen, wie die Website von Rodinka genutzt wird, und sie zu verbessern. Sie starten erst nach deiner Einwilligung.",
    "consent_allow": "Analyse erlauben",
    "consent_reject": "Ablehnen",
}

DIRECT_ANSWER_LABEL = "KURZE ANTWORT"
SUPPORT_LABEL = "Rodinka-Support"
CANONICAL_LABEL = "Aktuelles Dokument in der App Rodinka"
LANGUAGE_SWITCH = ("DE", "Deutsch")

DIRECT_ANSWERS = {
    "home": (
        "Was ist Rodinka und wie hilft es, das Familienleben zu organisieren?",
        "Rodinka ist ein Familienplaner mit gemeinsamem Kalender, Aufgaben, Einkaufsliste und Essensplan – dazu Ausflüge, Familienerinnerungen und die Überwachung von Ablaufdaten wichtiger Dokumente. Die Erwachsenen arbeiten mit derselben aktuellen Übersicht, und Kinder können eine eigene Anmeldung mit ihren eigenen Aufgaben haben. Auch Oma oder eine Babysitterin können mitmachen: Sie sehen nur die Termine, für die ihr sie als Begleitung auswählt.",
    ),
    "planner": (
        "Wie funktioniert ein Familienplaner?",
        "Ein Familienplaner bündelt gemeinsame Termine, Zuständigkeiten und praktische Listen in einem Bereich für den ganzen Haushalt. In Rodinka siehst du schnell, wer heute abholt, was zu Hause zu erledigen ist und was die Familie einkaufen muss. Alle arbeiten mit denselben aktuellen Informationen, sodass die Organisation nicht an einer Person hängen bleibt.",
    ),
    "calendar": (
        "Wie können Eltern einen Familienkalender teilen?",
        "Die Erwachsenen nutzen in Rodinka einen gemeinsamen Familienbereich und tragen Termine in denselben Kalender ein. Bei einer Aktivität, einem Arzttermin oder einem Ausflug bleiben Datum, Beteiligte und Begleitung zusammen. Beide Eltern sehen Änderungen, ohne sie zwischen getrennten Kalendern abzuschreiben, und Geburtstage oder Jahrestage erscheinen als ruhige Ebene, die keine Zeit blockiert.",
    ),
    "shopping": (
        "Wie führt man eine gemeinsame Einkaufsliste für den ganzen Haushalt?",
        "Rodinka gibt dem Haushalt eine gemeinsame Einkaufsliste, die alle ergänzen, sobald etwas ausgeht. Beim Einkaufen wird in derselben Liste abgehakt, sodass alle den aktuellen Stand sehen. Vor jedem Einkauf muss niemand eine neue Version verschicken.",
    ),
    "chores": (
        "Wie verteilt man Haushaltsaufgaben in der Familie?",
        "Beginne mit konkreten Zuständigkeiten und gib jeder eine verantwortliche Person und ein realistisches Fälligkeitsdatum. Rodinka hält diese Absprache für den ganzen Haushalt sichtbar, sodass die Liste nicht nur im Kopf eines Elternteils lebt. Kinder können einfache Aufgaben übernehmen, die zu ihrem Alter passen.",
    ),
    "meals": (
        "Wie plant man das Essen für eine Familie eine Woche im Voraus?",
        "Geh vom Familienkalender aus und plane die Mahlzeiten nach der Zeit, die an jedem Tag zur Verfügung steht. Rodinka hält den Wochenplan für das Essen neben dem restlichen Familienplan, und fehlende Zutaten landen auf der gemeinsamen Einkaufsliste. Ein flexibler Abend lässt Platz für Reste oder spontane Änderungen.",
    ),
    "app": (
        "Welche App hilft, das Familienleben zu organisieren?",
        "Ein nützlicher Familienorganizer beantwortet Alltagsfragen schnell: Was steht heute an, wer kümmert sich um etwas und was muss gekauft werden? Rodinka verbindet Familienkalender, Aufgaben, Einkaufsliste und Essensplan und ergänzt Ausflüge, Erinnerungen, Wunschlisten, Dokumente, Gesundheitstermine und einen Familienchat. Auch Großeltern und helfende Personen können dabei sein. Rodinka läuft im Browser auf Handy und Computer, eine Installation ist optional.",
    ),
    "memories": (
        "Wo kann eine Familie Meilensteine und Erinnerungen der Kinder aufbewahren?",
        "Rodinka bewahrt Familienerinnerungen als gemeinsame Chronik auf: Meilensteine der Kinder, Familienschätze, Kindersprüche und gemeinsame Erlebnisse mit Fotos liegen auf einer Zeitleiste, und jede Erinnerung kann einem bestimmten Familienmitglied gehören. Die Ansicht Heute holt ab und zu hervor, was am selben Tag in früheren Jahren passiert ist, und aus einem Meilenstein wird eine Karte zum Ausdrucken.",
    ),
    "documents": (
        "Wie behält eine Familie die Ablaufdaten von Reisepass und Personalausweis im Blick?",
        "Trage ein, wem ein Dokument gehört und wann es abläuft. Rodinka erinnert dann standardmäßig 180, 90, 30 und 7 Tage vor dem Ablauf, damit ein abgelaufener Reisepass oder Ausweis nicht erst eine Woche vor dem Urlaub auffällt. Dokumente sehen nur Erwachsene, und Erinnerungen halten die Ruhezeiten ein, die ihr festlegt.",
    ),
    "baby": (
        "Wie können sich Partner gemeinsam auf ein Baby vorbereiten?",
        "Rodinka verbindet einen leichten Weg Woche für Woche, praktische Vorbereitungen und die Namenswahl in einem gemeinsamen Familienbereich. Beide Eltern sehen, was schon bereit ist, was sie noch erledigen möchten und welche Namen sie in Betracht ziehen. Es ist kein medizinischer Schwangerschaftstracker; es hilft der Familie, sich vor der Ankunft des Babys gemeinsam zu organisieren.",
    ),
    "circle": (
        "Wie können Großeltern oder eine Babysitterin in den Familienplan eingebunden werden?",
        "Oma oder eine Babysitterin müssen in Rodinka nicht den ganzen Familienkalender sehen. Schick ihnen einen Link zu einem Termin: Sie sehen Zeit, Ort und deine Hinweise und bestätigen, ob sie gehen können – ganz ohne Konto. Wer regelmäßig hilft, kann sich als helfende Person anmelden und sieht nur die Termine, für die ihr sie als Begleitung auswählt.",
    ),
    "trips": (
        "Wie plant eine Familie einen Ausflug, bei dem alle mitreden?",
        "In Rodinka sammelt die Familie Ideen für Ausflüge und Urlaube, sobald sie auftauchen – ein eingefügter Link genügt. Aus ein paar Ideen wird ein Reiseplan, alle in der Familie stimmen über jede Idee ab, und ein Erwachsener macht aus der gewählten Idee mit einem Schritt einen Kalendertermin. Nach dem Ausflug kann daraus eine Familienerinnerung werden.",
    ),
}

PRODUCT_PROOFS = {
    "home": (
        "Die Ansicht Heute in Rodinka mit der Tageslinie der Familie und dem heutigen Programm aus Aktivitäten und Aufgaben",
        "Auf einem Bildschirm siehst du, wer wann etwas vorhat, und unter der Tageslinie das ganze heutige Programm aus Aktivitäten und Aufgaben.",
    ),
    "planner": (
        "Die Ansicht Planen in Rodinka mit Haushaltsaufgaben, Aktivitäten, Gesundheit, Essen und Dokumenten",
        "Die Übersicht Planen bündelt die Bereiche, die eine Familie immer wieder beschäftigen, und zeigt bei jedem das Nächste und wer sich darum kümmert.",
    ),
    "calendar": (
        "Monatsansicht des gemeinsamen Familienkalenders in Rodinka, in dem jedes Familienmitglied seine eigene Farbe hat",
        "In der Monatsansicht zeigen farbige Punkte, wer an welchem Tag etwas vorhat, und unter dem Raster steht das Programm des gewählten Tages.",
    ),
    "shopping": (
        "Gemeinsame Einkaufsliste in Rodinka mit Artikeln nach Kategorien, Mengen sowie wer sie hinzugefügt hat und wer sie kauft",
        "Die Liste ist synchronisiert und in Kategorien geordnet; bei jedem Artikel siehst du die Menge, wer ihn hinzugefügt hat und wer ihn kauft.",
    ),
    "chores": (
        "Die Ansicht Aufgaben in Rodinka mit schnellen Aufgaben und Aufgaben für Kinder, inklusive Wiederholung und Belohnung",
        "Eine Aufgabe hat eine Person, eine Wiederholung und auf Wunsch eine Belohnung. Das Kind hakt sie ab, ein Elternteil bestätigt, und der Betrag wird gutgeschrieben.",
    ),
    "app": (
        "Die Ansicht Heute in Rodinka mit dem gemeinsamen Programm der ganzen Familie, Aktivitäten und Aufgaben an einem Ort",
        "Die Ansicht Heute beantwortet die Alltagsfragen: wer wann etwas vorhat, was zu tun ist und was die Familie noch erwartet.",
    ),
    "memories": (
        "Die Ansicht Erinnerungen in Rodinka mit der Zeitleiste der Familie, einem Foto vom Herbstspaziergang und Filtern für Meilensteine und Schätze",
        "Erlebnisse mit Foto, Meilensteine der Kinder und Familienschätze liegen auf einer gemeinsamen Zeitleiste, die sich filtern lässt.",
    ),
    "baby": (
        "Zwei Handys mit der Funktion für ein erwartetes Kind in Rodinka, der Übersicht der Vorbereitungen und der gemeinsamen Namenswahl",
        "Rodinka verbindet einen leichten Weg Woche für Woche, praktische Vorbereitungen und die gemeinsame Namenswahl.",
    ),
}

HOME_MEMORY_STORY = {
    "kicker": "MEHR ALS ORGANISATION",
    "title": "Nicht nur, was erledigt werden muss. Auch, was ihr behalten wollt.",
    "text": "Meilensteine der Kinder, Familienschätze, Kindersprüche und gemeinsame Erlebnisse mit Foto liegen in Rodinka auf einer gemeinsamen Zeitleiste. Jede Erinnerung kann der Person gehören, um die es geht, die Ansicht Heute holt ab und zu hervor, was am selben Tag in früheren Jahren passiert ist, und aus einem Meilenstein wird eine Karte zum Ausdrucken.",
    "link": "Familienerinnerungen",
    "alt": "Die Ansicht Erinnerungen in Rodinka mit der Zeitleiste der Familie und einem Foto von einem Herbstspaziergang im Wald",
    "caption": "Erinnerungen mit Foto, Meilensteine der Kinder und Familienschätze auf einer gemeinsamen Zeitleiste der Familie.",
}

HOME_BABY_STORY = {
    "kicker": "EIN NEUES KAPITEL FÜR EURE FAMILIE",
    "title": "Ein Baby unterwegs? Bereitet euch gemeinsam vor.",
    "text": "Vom leichten Weg Woche für Woche über praktische Vorbereitungen bis zu Namen, die euch beiden gefallen: Rodinka hilft Eltern, das nächste Kapitel an einem gemeinsamen Ort zu haben.",
    "link": "Vorbereitung auf ein Baby",
    "alt": "Zwei Handys mit dem Weg zum erwarteten Kind in Rodinka, praktischen Vorbereitungen und der gemeinsamen Namenswahl",
    "caption": "Die Funktion für ein erwartetes Kind gibt den Erwachsenen eine gemeinsame Übersicht über die Vorbereitungen der Familie vor der Ankunft des Babys.",
}

HOME_PHONE = {
    "family": "Novák",
    "greeting": "Willkommen, Klára.",
    "date": "Dienstag, 6. Oktober",
    "summary": "Du hast heute 3 Sachen vor.",
    "program": "Tagesplan",
    "rows": (
        ("7:45", "Kita", "Tobiáš · Begleitung Martin"),
        ("15:00", "Schwimmen", "Ema · Begleitung Klára"),
        ("18:30", "Abendessen: Risotto", "Kocht Martin"),
    ),
    "dinner": "Abendessen",
    "daily_title": "Rodinka Heute",
    "daily_eyebrow": "Heutige Abstimmung",
    "question": "Wohin fahren wir am Samstag?",
    "options": (("Zur Burg", "2 Stimmen"), ("In den Zoo", "1 Stimme"), ("Zu Oma", "0 Stimmen")),
    "voted": "3 von 4 haben abgestimmt",
    "nav": ("Heute", "Kalender", "Erinnerungen", "Planen", "Familie"),
}

HOME_FOCUS = {
    "kicker": "WOMIT ANFANGEN",
    "title": "Wobei soll dir Rodinka am meisten helfen?",
    "lead": "Das fragt Rodinka direkt nach dem Anlegen eurer Familie. Sieben Bereiche, ein gemeinsamer Haushalt – fang mit dem an, der bei euch zu Hause das meiste Hin und Her verursacht.",
    "cards": (
        ("calendar", "calendar", "Familienzeit und Kalender", "Ein Kalender für die ganze Familie in Monats-, Wochen- und Listenansicht. Bei jedem Eintrag siehst du, um wen es geht und wer sich kümmert. Geburtstage und Feiertage erscheinen von selbst.", ("Wiederholung", "Begleitung", "Besondere Tage"), (("calendar", "Familienkalender"),)),
        ("tasks", "chores", "Zuhause und Aufgaben", "Aufgaben mit Person und Fälligkeit, einmalig oder wiederkehrend. Ein Kind hakt ab, ein Erwachsener bestätigt, und die Belohnung oder das Taschengeld wird gutgeschrieben.", ("Taschengeld", "Bestätigung", "Diktieren"), (("chores", "Aufgaben für die Familie"),)),
        ("family", "shopping", "Einkaufen", "Eine Liste, die alle ergänzen, auch per Stimme. Im Laden funktioniert sie ohne Netz, und Zutaten aus dem Essensplan landen mit einem Schritt darauf.", ("Offline", "Kategorien", "Essensplan"), (("shopping", "Einkaufsliste"), ("meals", "Essensplanung"))),
        ("activities", "school", "Schule und Freizeit", "Eine Aktivität trägst du einmal ein, mit Ort und Zahlung. Fährt diese Woche jemand anderes, änderst du nur diesen einen Termin. Rodinka warnt, wenn eine Person zwei Verpflichtungen gleichzeitig hat.", ("Zahlungen", "Familienorte", "Konfliktwarnungen"), (("planner", "Familienplaner"),)),
        ("travel", "trips", "Ausflüge und Urlaub", "Ideen für Orte, an die ihr wollt, speicherst du, sobald sie auftauchen – ein eingefügter Link genügt. Daraus wird ein Reiseplan, die Familie stimmt ab, und die gewählte Idee landet im Kalender.", ("Abstimmung", "Ideenkarte", "Reisepläne"), (("trips", "Familienausflüge"),)),
        ("memories", "memories", "Familienerinnerungen", "Eine Familienchronik: Meilensteine der Kinder, Schätze und gemeinsame Erlebnisse auf einer Zeitleiste. Aus einem Meilenstein wird eine Karte zum Ausdrucken.", ("Meilensteine", "Schätze", "Druckbare Karten"), (("memories", "Familienerinnerungen"),)),
        ("documents", "documents", "Dokumente und Wichtiges", "Reisepässe, Ausweise, Führerscheine und Versicherungen mit ihren Ablaufdaten. Erinnerungen kommen rechtzeitig, und Dokumente sehen nur Erwachsene.", ("180 · 90 · 30 · 7 Tage", "Nur Erwachsene", "Ruhezeiten"), (("documents", "Ablaufdaten von Dokumenten"),)),
    ),
    "cta": ("Wähle so viele, wie du willst.", "Deine Antwort in der App sperrt oder versteckt nichts. Rodinka ordnet danach nur die ersten Vorschläge in der Ansicht Heute."),
}

HOME_START = {
    "kicker": "DER START DAUERT NUR MINUTEN",
    "title": "Zwei Fragen und Rodinka weiß, wer ihr seid",
    "lead": "Der Einstieg fragt nur, was die App nicht selbst herausfinden kann. Der erste Eintrag, Einladungen und alles andere warten, bis du sie wirklich brauchst.",
    "steps": (
        ("Wer gehört zu eurer Rodinka?", "Füge Kinder, ein Haustier und auch ein Baby hinzu, das noch unterwegs ist. Den zweiten Erwachsenen lädst du per Link ein – den eigenen Namen trägt er selbst ein."),
        ("Wobei soll dir Rodinka am meisten helfen?", "Wähle die Bereiche, die euch zu Hause am meisten beschäftigen. Gesperrt wird dadurch nichts; es entscheidet nur, welche Vorschläge zuerst kommen."),
        ("Das ist eure Rodinka", "Das eigene Zeichen eurer Familie entsteht aus ihren Mitgliedern. In der Ansicht Heute wartet eine kurze Liste mit höchstens drei nächsten Schritten."),
    ),
    "kit": ("Fertige Pakete statt eines leeren Bildschirms", "Schule, Zuhause, Auto oder Dokumente: Ein Paket zeigt, was es in Rodinka anlegen würde, und lässt dich vorher alles ändern. Gespeichert wird erst nach deiner Bestätigung."),
    "family": "Nováks",
    "pet": "Bady",
    "caption": "Das Familienzeichen besteht aus ihren Mitgliedern. Alle haben ihre eigene Farbe, Erwachsene sind etwas größer, und ein Haustier ist ein kleineres Blatt am Ende der Reihe.",
}

HOME_FAMILY_LAYER = {
    "kicker": "FAMILIE IST MEHR ALS LOGISTIK",
    "title": "Mehr als nur das, was erledigt werden muss",
    "lead": "Kalender, Aufgaben und Einkauf halten einen Haushalt am Laufen. Rodinka ergänzt die Dinge, für die ihr die App gern öffnet – und ein paar, die man sonst leicht vergisst.",
    "cards": (
        ("memories", "sparkle", "Ein kleiner Grund, jeden Tag zusammenzukommen", "Rodinka Heute bietet eine Frage für die ganze Familie, eine kurze Abstimmung, ein Rätsel oder eine Erinnerung aus früheren Jahren. Es ist keine Pflicht: keine Serien, Punkte oder Ranglisten.", "memories"),
        ("tasks", "child", "Kinder bekommen ihre eigene Rodinka", "Eine Anmeldung ohne E-Mail-Adresse, eigene Aufgaben, die Einkaufsliste und der Kalender. Belohnung oder Taschengeld für erledigte Aufgaben und fünf Familienspiele, die auch offline funktionieren. Wenn ein Kind ein eigenes Konto möchte, übergebt ihr ihm sein Profil samt Geschichte.", "chores"),
        ("family", "gift", "Wünsche, die nie doppelt gekauft werden", "Alle in der Familie führen eine Liste mit Dingen und Erlebnissen, die sie sich wünschen. Erwachsene können einen Wunsch still mit „Ich besorge das“ markieren, und wer ihn geäußert hat, erfährt es nie.", "app"),
        ("calendar", "chat", "Reden, wo es hingehört", "Ein Familienchat und Direktnachrichten. Teile eine bestimmte Aufgabe, einen Einkaufsartikel oder einen Termin im Gespräch und mach aus einer Nachricht mit einem Schritt eine Aufgabe.", "app"),
        ("health", "health", "Gesundheit und Haustiere", "Vorsorgeuntersuchungen, Impfungen und nächste Dosen für die ganze Familie mit rechtzeitiger Erinnerung. Ein Haustier bekommt ein eigenes Profil, Pflegeroutinen und eine Tierarzthistorie. Es dient der Planung, nicht als medizinische Akte.", "app"),
    ),
}

TRIP_MOCK = {
    "kicker": "Reiseplan",
    "title": "Herbstwochenende",
    "pills": ("17.–18. Okt.", "Vysočina", "An Heute angeheftet"),
    "note": "Nehmen wir Bady mit?",
    "tips": (
        ("Burg Pernštejn", "Nedvědice", (3, 1, 0)),
        ("Aussichtsturm Harusův kopec", "Nové Město na Moravě", (2, 1, 1)),
        ("Zoo Jihlava", "Jihlava", (1, 2, 1)),
    ),
    "selected": "Gewählt",
    "caption": "Ein Reiseplan: Termin, Gegend, Ideen und die Stimmen der ganzen Familie. Die gewählte Idee wird zum Termin im Familienkalender.",
}

HOME_TRIPS_STORY = {
    "kicker": "AUSFLÜGE UND URLAUB",
    "title": "Wohin fahren wir? Das entscheidet die ganze Familie.",
    "text": "Speichere Ausflugsideen, sobald sie auftauchen – füge einen Link ein, und Rodinka übernimmt Titel und Vorschau. Wenn ein freies Wochenende kommt, wird aus ein paar Ideen ein Reiseplan, alle stimmen ab, und die gewählte Idee landet im Kalender.",
    "points": (
        "Ein Ideenvorrat als Karten oder auf der Landkarte.",
        "Den Reiseplan an die Ansicht Heute anheften.",
        "Zurück zu Hause tippst du auf Besucht, und der Ausflug wird zur Erinnerung.",
        "Und vor der Abfahrt können die Kinder Kofferraum packen spielen.",
    ),
    "link": "Familienausflüge",
}

HOME_CIRCLE = {
    "kicker": "DIE GROSSE FAMILIE",
    "title": "Familie ist mehr als ein Haushalt",
    "lead": "Oma holt aus der Kita ab, die Tante bringt die Kinder zum Schwimmen, und der Älteste hat schon ein eigenes Konto. Rodinka macht Platz für alle, die helfen – und alle sehen nur, was sie betrifft.",
    "cards": (
        ("calendar", "confirm", "Oma weiß, wann sie abholt. Du weißt, dass sie da ist.", "Schick ihr einen Link zu einem bestimmten Termin. Sie sieht Zeit, Ort und deine Hinweise und bestätigt mit einem Tippen – ganz ohne Rodinka-Konto."),
        ("activities", "people", "Holt die Menschen dazu, die helfen", "Eine Babysitterin, Opa oder eine Nachbarin können sich als helfende Person anmelden. Sie sehen nur die Termine, für die ihr sie als Begleitung auswählt – nicht den Familienkalender, Einkäufe oder Nachrichten."),
        ("family", "homes", "Eine App, mehr als eine Familie", "Du gehörst zu deinem eigenen Haushalt und auch zur Familie deiner Eltern? Ein Konto reicht. Zwischen den Familien wechselst du in der Kopfzeile, und ihre Informationen vermischen sich nie."),
        ("memories", "sprout", "Kinder werden groß. Ihre Geschichte geht weiter.", "Wenn ein Kind eine eigene Anmeldung möchte, übergebt ihm sein Profil. Erinnerungen, Meilensteine und Aufgaben bleiben, wo sie waren."),
    ),
    "link": "Wie Rodinka für die große Familie funktioniert",
}

INVITE_MOCK = {
    "kicker": "Einladung zur Begleitung",
    "greeting": "Hallo Jana",
    "invited_by": "Klára bittet dich um Begleitung.",
    "title": "Schwimmen",
    "rows": (
        ("Wann", "Dienstag, 6. Oktober · 15:00"),
        ("Wo", "Schwimmbad Lužánky, Brno"),
        ("Du begleitest", "Ema"),
        ("Hinweise", "Badeanzug und Handtuch sind im blauen Rucksack."),
    ),
    "confirm": "Ja, ich gehe",
    "decline": "Ich kann nicht",
    "privacy": "Diese Seite sieht nur, wer den Link hat. Ein Rodinka-Konto brauchst du nicht.",
    "echo_label": "In Kláras Kalender",
    "echo": ("15:00", "Schwimmen", "Ema · Begleitung Jana", "bestätigt"),
    "caption": "Oma öffnet den Link auf ihrem Handy und antwortet mit einem Tippen. Die Eltern sehen sofort, dass der Termin bestätigt ist.",
}

HOME_TRUST = {
    "kicker": "PRIVATSPHÄRE UND ZUVERLÄSSIGKEIT",
    "title": "Familiensachen bleiben in der Familie",
    "lead": "Rodinka ist für echte Haushalte gemacht: mit Kindern, wechselndem Empfang und Details, die niemanden sonst etwas angehen.",
    "items": (
        ("lock", "Jede Familie hat ihren eigenen geschlossenen Bereich", "Die Daten jeder Familie sind direkt in der Datenbank getrennt. Gehörst du zu mehreren Familien, vermischen sich ihre Informationen nie, und eine helfende Person sieht nur ihre eigenen Termine."),
        ("shield", "Kinder sehen nur, was ihnen gehört", "Ein Kinderkonto sieht keine Dokumente und keine Familienverwaltung – weder in der Oberfläche noch in der Datenbank."),
        ("image", "Fotos in privatem Speicher", "Fotos und Scans werden Familienmitgliedern nur über zeitlich begrenzte, gesicherte Links angezeigt."),
        ("offline", "Funktioniert ohne Netz", "Heute, Kalender, Aufgaben und Einkauf lassen sich offline ändern und gleichen sich nach der Verbindung ab. Essensplan, Erinnerungen und Ausflugsideen bleiben ohne Verbindung lesbar."),
        ("bell", "Erinnerungen, die die Nacht respektieren", "Alle stellen ihre eigenen Ruhezeiten, Erinnerungskategorien und eine tägliche oder wöchentliche Übersicht ein."),
        ("languages", "Fünf Sprachen", "Die Oberfläche gibt es auf Tschechisch, Slowakisch, Englisch, Deutsch und Polnisch, im hellen und dunklen Design, auf Handy, Tablet und Computer."),
    ),
}

HOME_PRO = {
    "title": "Noch ein bisschen mehr für eure Rodinka",
    "text": "Rodinka funktioniert kostenlos hervorragend. Rodinka Pro ergänzt Helfer, die euch Planungsarbeit abnehmen: die Familienwoche, wiederverwendbare Vorbereitungen für Reisen und Ereignisse, vorgeschlagene Einkäufe und Essenspläne aus euren eigenen Familiendaten und das Familienjahrbuch. Dazu mehr Platz für Fotos, den Moment des Tages und euer eigenes Aussehen.",
    "benefits": (
        "Familienwoche: alles, was noch zu klären ist, an einem Ort",
        "Familienszenarien und Vorbereitungen für Reisen, Ausflüge und Feiern",
        "Vorgeschlagene Artikel und Essenspläne nach dem, was ihr wirklich kauft und kocht",
        "Familienjahrbuch als druckfertiges PDF",
        "5 GiB für Familienfotos und den Moment des Tages",
        "Eigene Farben für Mitglieder und Akzentfarbe der App",
    ),
    "summary": "Pro gilt für eine bestimmte Familie. Neue Käufe werden vorbereitet; einen Preis siehst du bei einem verfügbaren Angebot in der App.",
    "cta": "Free und Pro vergleichen",
}

HOME = {
    "title": "Rodinka – Familienplaner, Kalender, Aufgaben und Einkauf",
    "description": "Ein Familienplaner für die ganze Familie: gemeinsamer Kalender, Aufgaben, Einkauf und Essen, dazu Ausflüge und Erinnerungen. Auch Oma oder eine Babysitterin können mitmachen. Auf Handy und Computer.",
    "og_title": "Rodinka: weniger Hin und Her, mehr Zeit füreinander",
    "og_description": "Gemeinsamer Kalender, Aufgaben, Einkauf, Essen, Ausflüge und Erinnerungen – für Eltern, Kinder und alle, die helfen.",
    "og_alt": "Familienorganizer Rodinka mit Kalender, Aufgaben, Einkaufsliste und Essen",
    "eyebrow": "Ein Familienplaner für die ganze Familie",
    "h1": "Weniger Hin und Her. Mehr Zeit füreinander.",
    "lead": "Rodinka hält Kalender, Aufgaben, Einkäufe und Essen des Haushalts zusammen – dazu die Ausflüge und Erinnerungen, zu denen ihr gern zurückkehrt. Auch Oma, die abholt, oder eine Babysitterin können mitmachen. Alle sehen, was sie betrifft.",
    "how_link": "So fängst du an",
    "proof": ("Ohne Zahlungskarte", "Handy und Computer", "Einkaufen ohne Netz"),
    "trust_title": "Eine Familie, eine gemeinsame Übersicht.",
    "trust_text": "Leg eure Familie an, lade den zweiten Erwachsenen ein und später auch die Menschen, die euch helfen.",
    "directory_kicker": "ALLE THEMEN",
    "directory_title": "Ein Wegweiser durch das, was euer Haushalt regelt",
    "directory_lead": "Jede Seite behandelt einen Bereich von Rodinka: wie er funktioniert, wem er hilft und was Familien am häufigsten fragen.",
    "quote": "Bei Rodinka geht es nicht um ein perfekt organisiertes Leben. Es geht darum, dass die Organisation nicht an einer einzigen Person hängen bleibt.",
    "quote_by": "Gemacht für echte Haushalte",
    "cta_kicker": "DU KANNST SOFORT LOSLEGEN",
    "cta_title": "Gebt dem Familienchaos ein gemeinsames Zuhause.",
    "cta_text": "Rodinka öffnet sich im Browser. Sag, wer zu eurer Familie gehört und wobei sie helfen soll, und schon seid ihr startklar. Nichts zu installieren.",
    "login": "Ich habe schon ein Konto",
    "journey": (("1. Wer gehört zu eurer Rodinka", "Kinder, der zweite Erwachsene, ein Haustier."), ("2. Wobei sie helfen soll", "Danach ordnen wir die ersten Schritte."), ("3. Das ist eure Rodinka", "Euer Familienzeichen und ein paar Ideen für Heute.")),
    "install_title": "Möchtest du Rodinka als Windows-App?",
    "install_text": "Der Microsoft Store ist eine weitere Möglichkeit, Rodinka zu installieren. Auf dem Handy fügst du die Webversion wie eine App zum Startbildschirm hinzu.",
    "store": "Microsoft Store öffnen",
    "fine_print": "Ohne Zahlungskarte. Funktioniert auf Handy und Computer.",
}


TOPICS = {
    "planner": {
        "title": "Ein praktischer Familienplaner für den Alltag | Rodinka",
        "description": "Familienkalender, Aufgaben, Einkauf und Essen in einem gemeinsamen Planer. Organisiert den Alltag zu Hause, ohne daraus ein weiteres Projekt zu machen.",
        "og_title": "Ein Familienplaner, der nicht zum nächsten Haushaltsprojekt wird",
        "og_description": "Ein praktischer Ort für Termine, Zuständigkeiten, Einkäufe und Essen, geteilt von allen, die den Haushalt am Laufen halten.",
        "og_alt": "Familienplaner Rodinka mit einer gemeinsamen Übersicht über den Familienalltag",
        "eyebrow": "EINE GEMEINSAME FAMILIENÜBERSICHT",
        "h1": "Ein Familienplaner für alles, woran der Alltag euch erinnern lässt",
        "lead": "Aktivitäten, Abholungen, Einkäufe, Abendessen und Aufgaben verteilen sich schnell auf Kalender, Chats und Zettel am Kühlschrank. Ein gemeinsamer Familienplaner gibt allen einen verlässlichen Ort zum Nachschauen.",
        "problem_title": "Das Familienleben zu organisieren sollte nicht die unsichtbare Arbeit einer einzigen Person sein",
        "problem": (
            "In vielen Haushalten trägt ein Elternteil den Terminplan und die gedankliche Liste aller Erledigungen. Alle anderen fragen nach, und die Antwort wird wieder in Nachrichten gesucht. Selten fehlt es am guten Willen; die Informationen haben einfach kein gemeinsames Zuhause.",
            "Ein nützlicher Planer soll Verwaltung reduzieren, nicht erzeugen. In wenigen Sekunden soll er beantworten, wer heute abholt, wann das Training beginnt, was im Haushalt fehlt und welche Abendessen diese Woche geplant sind.",
        ),
        "scenarios": (
            ("Morgens ohne Detektivarbeit", "Bevor alle aus dem Haus gehen, sind Termine, Abholungen und wichtige Aufgaben des Tages klar."),
            ("Änderungen bleiben sichtbar", "Ein verschobenes Training oder ein neu ergänzter Einkauf erscheint in der gemeinsamen Übersicht."),
            ("Weniger Mental Load", "Eine Person muss nicht mehr den ganzen Plan überwachen; Informationen und Verantwortung werden wirklich geteilt."),
        ),
        "help_title": "Wie Rodinka hilft, das Familienleben zu organisieren",
        "help_intro": "Fang mit einem Bereich an und nimm weitere erst dazu, wenn sie nützlich werden. Alles bleibt im selben Familienbereich verbunden.",
        "steps": (
            ("Denselben Terminplan teilen", "Der Familienkalender bringt gemeinsame und einzelne Termine zusammen und zeigt, wer sich um die praktischen Details kümmert."),
            ("Aus vagen Vorsätzen klare Aufgaben machen", "Gib einer Aufgabe eine verantwortliche Person und eine Fälligkeit, damit aus „das sollten wir mal machen“ eine verständliche Absprache wird."),
            ("Die Haushaltsbasics in der Nähe haben", "Einkaufsliste und Essensplan liegen neben dem Terminplan – für die Dinge, die eure Familie jede Woche regelt."),
        ),
        "answers_title": "Häufige Fragen zu Familienplanern",
        "answers": (
            ("Was sollte ein guter Familienplaner enthalten?", "Er sollte schnell den gemeinsamen Kalender, verteilte Aufgaben und praktische Listen zeigen. Außerdem muss er so einfach sein, dass alle Erwachsenen im Haushalt ihn nutzen – und Kinder, wenn es zu ihrem Alter passt."),
            ("Wie fangen wir an, wenn niemand noch eine App will?", "Wählt eine wiederkehrende Reibungsquelle, etwa Aktivitäten oder Einkäufe. Sobald die gemeinsame Übersicht ein paar Nachrichten spart, nehmt ihr den nächsten Bereich dazu. Ihr müsst nicht am ersten Tag alles umziehen."),
            ("Wie kann sich eine Familie weniger auf den Gruppenchat verlassen?", "Lasst das Gespräch im Chat, aber legt Termine, Aufgaben und Einkäufe dort ab, wo man sie später wiederfindet. Wichtige Details verschwinden dann nicht mehr zwischen anderen Nachrichten."),
            ("Wie können Großeltern oder eine Babysitterin Teil des Plans sein?", "Sie müssen nicht alles sehen. Schickt ihnen einen Link, mit dem sie einen Termin bestätigen, an dem sie die Kinder begleiten, oder ladet sie als helfende Personen ein. In beiden Fällen sehen sie nur ihre eigenen Termine und sonst nichts aus der Familie."),
            ("Kann Rodinka uns helfen, die ganze Woche vorauszuplanen?", "Mit Rodinka Pro ja. Die Familienwoche zeigt an einem Ort, was in dieser Woche noch zu klären ist: Termine ohne erwachsene Begleitung, Vorbereitungen für Ereignisse, Aufgaben, Zahlungstermine und auf Wunsch noch nicht geplante Abendessen. Sie legt nichts selbst an; sie führt euch dorthin, wo die Sache erledigt wird. Für wiederkehrende Situationen wie ein Wochenende weg, einen Tagesausflug oder eine Feier speichert ihr ein Familienszenario und macht daraus jedes Mal eine neue Vorbereitung, die die Erwachsenen gemeinsam abhaken."),
        ),
        "card": "Eine gemeinsame Übersicht für Termine, Aufgaben, Einkäufe und Essen.",
        "cta_title": "Fangt mit dem an, worüber ihr zu Hause am meisten redet.",
        "cta_text": "Leg eure Rodinka an und füge den ersten Termin, die erste Aufgabe oder den ersten Einkauf hinzu. Alles andere kann nach und nach folgen.",
    },
    "calendar": {
        "title": "Gemeinsamer Familienkalender für Eltern und Kinder | Rodinka",
        "description": "Ein gemeinsamer Familienkalender für Schule, Aktivitäten, Arzttermine und Abholungen. Alle sehen, was ansteht und wer sich kümmert.",
        "og_title": "Ein Familienkalender, der die Frage „Wer holt ab?“ beantwortet",
        "og_description": "Schule, Aktivitäten, Arzttermine, Besuche und Begleitung in einem Kalender für den ganzen Haushalt.",
        "og_alt": "Gemeinsamer Familienkalender in Rodinka mit Terminen und Abholdetails",
        "eyebrow": "EIN TERMINPLAN FÜR DEN GANZEN HAUSHALT",
        "h1": "Ein gemeinsamer Familienkalender mit allen praktischen Details",
        "lead": "Wann ist das Schulkonzert, wer fährt zum Schwimmen, und ist der Besuch am Samstag bestätigt? Ein Familienkalender hält Termine und Übergaben zusammen, damit alle selbst nachschauen können.",
        "problem_title": "Datum und Uhrzeit sind oft nur der halbe Plan",
        "problem": (
            "Ein Familienterminplan ist nicht nur eine Liste von Terminen. Aktivitäten der Kinder brauchen auch einen Ort, das richtige Kind und einen klaren Erwachsenen, der begleitet. Bleibt die Hälfte davon im Chat, kann der Kalender seine Aufgabe nicht ganz erfüllen.",
            "Die gemeinsame Ansicht muss für den schnellen Blick am Morgen genauso funktionieren wie für die Wochenplanung. Regelmäßige Aktivitäten werden einmal eingetragen, Ausnahmen sehen alle, und niemand pflegt eine eigene Version des Familienplans.",
        ),
        "scenarios": (
            ("Aktivitäten der Kinder", "Schwimmen, Musikunterricht und Training mit Uhrzeit, Ort, Kind und Begleitung."),
            ("Schule und Arzttermine", "Elternabende, Vorsorgetermine und schulfreie Tage liegen nicht mehr nur im Posteingang eines Elternteils."),
            ("Wochenenden und Besuche", "Geburtstage und Zeit bei den Großeltern sind sichtbar, bevor etwas anderes geplant wird."),
        ),
        "help_title": "So funktioniert der gemeinsame Familienkalender in Rodinka",
        "help_intro": "Termine liegen im selben Familienbereich, sodass alle eingeladenen Erwachsenen den aktuellen Plan sehen, statt auf einen Screenshot oder eine weitergeleitete Nachricht zu warten.",
        "steps": (
            ("Den ganzen Termin eintragen", "Erfasse Uhrzeit, Ort und das betroffene Familienmitglied. Regelmäßige Aktivitäten stellst du auf Wiederholung, damit sie nicht jede Woche neu eingetragen werden müssen."),
            ("Trennen, um wen es geht und wer sich kümmert", "Ein Termin zeigt die teilnehmende Person – das Kind, das zum Schwimmen geht – getrennt vom Erwachsenen, der es hinbringt. Das sind zwei verschiedene Fakten, und Rodinka vermischt sie nicht."),
            ("Eine Familienwoche überblicken", "Wechsle zwischen Monat, Woche und einer nach Dringlichkeit gruppierten Liste. Wenn ein Erwachsener etwas plant, sehen alle dieselben Familienverpflichtungen."),
            ("Wichtige Tage kommen von selbst", "Geburtstage in der Familie, Jahrestage und eure eigenen besonderen Tage erscheinen im Kalender als ruhige Ebene, die keine Zeit blockiert, und Rodinka kann vorher an die wichtigen erinnern."),
        ),
        "answers_title": "Was Familien zu gemeinsamen Kalendern fragen",
        "answers": (
            ("Wie teilen Eltern einen Familienkalender?", "Legt einen Familienbereich an und ladet den zweiten Erwachsenen ein. Tragt gemeinsame Termine dort ein und gebt an, wer die Kinder begleitet, wann immer das den Plan beeinflusst."),
            ("Wie organisieren wir die Aktivitäten der Kinder?", "Erfasst bei jeder Aktivität Tag, Uhrzeit, Ort, Kind und Begleitung. Regelmäßige Termine wiederholt ihr, Ausnahmen bearbeitet ihr einzeln, damit die Wochenansicht stimmt."),
            ("Was, wenn nur eine Woche lang jemand anderes fährt?", "Ändere die Begleitung bei genau diesem einen Termin. Die wiederkehrende Aktivität bleibt unberührt, sodass eine Ausnahme nicht bedeutet, die Serie aufzuteilen oder neu anzulegen."),
            ("Gehören Aufgaben in den Familienkalender?", "Nutze einen Termin für etwas, das zu einer bestimmten Zeit stattfindet. Vorbereitungen wie ein Geschenk kaufen oder ein Formular abgeben funktionieren besser als eigene Aufgabe mit verantwortlicher Person und Fälligkeit."),
            ("Warnt der Kalender vor Überschneidungen?", "Ja, wenn ein Familienmitglied zwei Verpflichtungen zur selben Zeit hätte – etwa eine Aktivität und einen Arzttermin. Zwei Kinder gleichzeitig bei zwei Aktivitäten sind kein Konflikt, solange jedes von jemand anderem begleitet wird. Die Warnung hindert dich nie am Speichern."),
            ("Kann Oma eine Abholung ohne Konto bestätigen?", "Ja. Für einen Termin, bei dem jemand außerhalb der Familie die Kinder begleitet, erstellst du einen Link und schickst ihn. Die Person sieht Zeit, Ort und deine Hinweise, antwortet mit einem Tippen, und am Termin siehst du, dass er bestätigt ist."),
        ),
        "card": "Schule, Aktivitäten, Besuche und Abholungen in einem gemeinsamen Kalender.",
        "cta_title": "Macht den Plan zugänglich, ohne noch eine Nachricht zu schreiben.",
        "cta_text": "Trag in Rodinka den ersten Familientermin ein und gib an, wer sich um die praktische Seite kümmert.",
    },
    "circle": {
        "title": "Großeltern, helfende Personen und die große Familie | Rodinka",
        "description": "Bindet Großeltern, eine Babysitterin oder andere nahe Menschen ein – nur für die Termine, die sie betreffen. Begleitung per Link bestätigen, helfende Personen und mehrere Familien in einem Konto.",
        "og_title": "Oma weiß, wann sie abholt. Du weißt, dass sie da ist.",
        "og_description": "Rodinka für Eltern, Kinder und alle, die der Familie nahestehen – jede Person sieht nur, was sie betrifft.",
        "og_alt": "Eine Einladung zur Begleitung in Rodinka, die Oma ohne Konto bestätigt",
        "eyebrow": "GROSSE FAMILIE UND HELFENDE",
        "h1": "Für Eltern, Kinder und alle, die der Familie nahestehen",
        "lead": "Oma holt mittwochs ab, Opa fährt zum Training, und freitags hilft eine Babysitterin. Rodinka gibt ihnen genau das, was sie wissen müssen – wann, wo und mit wem – und dir die Gewissheit, dass es geregelt ist. Den Rest des Familienlebens müssen sie nicht sehen.",
        "problem_title": "Hilfe aus der Familie wird immer noch am Telefon geregelt",
        "problem": (
            "Mit deinem Partner teilst du einen Kalender, aber Oma erfährt von einer Änderung am Telefon und die Babysitterin aus einer Nachricht, die untergeht. Wenn ein Elternteil die Arbeit verlässt, weiß er oft nicht, ob die Abholung wirklich steht.",
            "Den Großeltern den ganzen Familienkalender zu geben, ist auch keine Lösung. Sie wollen nicht durch Einkäufe, Aufgaben und Nachrichten scrollen, und ihr wollt nicht alles teilen. Sie müssen ihre eigenen Termine sehen und sagen können, ob sie es schaffen.",
        ),
        "scenarios": (
            ("Mittwochs bei Oma", "Oma bekommt einen Link für die Abholung, bestätigt ihn, und du siehst ihre Antwort direkt am Termin."),
            ("Eine Babysitterin für den ganzen Monat", "Die Babysitterin meldet sich als helfende Person an und sieht alle ihre Termine zusammen, mit Orten und den Namen der Kinder."),
            ("Zwei Familien, eine Anmeldung", "Eine erwachsene Tochter hat ihren eigenen Haushalt und bleibt auch in der Familie ihrer Eltern. Sie wechselt mit einem Tippen zwischen beiden."),
        ),
        "help_title": "Wie Rodinka die große Familie einbindet",
        "help_intro": "Vier Möglichkeiten, die ihr einzeln nutzen könnt. Keine davon gibt jemandem Zugang zu eurer ganzen Familie, solange ihr die Person nicht als Mitglied einladet.",
        "steps": (
            ("Begleitung per Link bestätigen", "Für einen Termin, bei dem jemand außerhalb der Familie die Kinder begleitet, erstellst du einen Link und schickst ihn auf dem üblichen Weg. Die Person sieht Titel, Zeit, Ort, deine Hinweise und, wenn du es erlaubst, die Namen der Kinder. Sie antwortet „Ja, ich gehe“ oder „Ich kann nicht“, auf Wunsch mit kurzer Notiz, und du siehst die Antwort am Termin."),
            ("Helfende Personen mit eigener Anmeldung", "Wer regelmäßig hilft, kann ein eigenes Konto haben. Du lädst die Person per E-Mail ein, und in Rodinka sieht sie nur die Termine, für die ihr sie als Begleitung auswählt, und bestätigt jeden einzelnen. Den Zugang kannst du jederzeit entfernen."),
            ("Ein Konto in mehreren Familien", "Ein Konto kann zu mehr als einer Familie gehören – etwa zu deinem eigenen Haushalt und zur Familie deiner Eltern. Jede behält ihre eigenen Informationen und Einstellungen, und du wechselst in der Kopfzeile der App zwischen ihnen."),
            ("Ein Profil an ein Kind übergeben", "Wenn ein Kind eine eigene E-Mail-Adresse und ein eigenes Passwort nutzt, übergebt ihr ihm sein Profil. Erinnerungen, Meilensteine, Aufgaben und Taschengeld bleiben, und das Passwort, das ihr kanntet, funktioniert nicht mehr. Das Profil bleibt ein Kinderprofil mit denselben Regeln wie bisher."),
        ),
        "answers_title": "Fragen zur großen Familie und zu helfenden Personen",
        "answers": (
            ("Braucht Oma ein Rodinka-Konto?", "Nein. Für die Bestätigung eines Termins reicht ein Link, der sich auf ihrem Handy ohne Anmeldung öffnet. Hilft sie regelmäßig, kann sie ein eigenes Konto anlegen und alle ihre Termine zusammen sehen."),
            ("Kann jemand außerhalb unserer Familie mit den Kindern helfen?", "Ja. Speichere eine Babysitterin, eine Nachbarin oder die Eltern eines Freundes unter euren weiteren Personen und wähle sie als Begleitung. Sie werden kein Mitglied eurer Familie: Sie bekommen entweder einen Link oder Zugang als helfende Person zu ihren eigenen Terminen."),
            ("Was sieht eine helfende Person?", "Nur die Termine, für die ihr sie als Begleitung auswählt: Titel, Datum und Uhrzeit, Ort, die Namen der begleiteten Kinder und ob der Termin bestätigt ist. Familienkalender, Aufgaben, Einkäufe, Nachrichten, Notizen oder Dokumente sieht sie nie. Entfernst du den Zugang, verschwinden die Termine für sie sofort."),
            ("Wer kann einen Einladungslink zur Begleitung sehen?", "Jede Person, der du ihn schickst – schick ihn also nur an die Person, für die er gedacht ist. Die Seite zeigt Titel, Datum und Uhrzeit, den Ort mit Adresse, eure beiden Namen und deine Hinweise; die Namen der Kinder nur, wenn du es erlaubst. Der Link gilt höchstens bis eine Woche nach dem Termin, und du kannst ihn jederzeit widerrufen."),
            ("Kann ich zu mehr als einer Familie gehören?", "Ja. Ein Konto kann zu mehreren Familien gehören. In einer bist du vielleicht Elternteil, in einer anderen Kind oder ein weiterer Erwachsener. Die Informationen der Familien vermischen sich nie, und du wechselst in der Kopfzeile. Benachrichtigungen kommen auf einem Gerät vorerst aus der Familie, für die du sie eingeschaltet hast."),
            ("Was passiert, wenn ein Kind ein eigenes Konto nutzt?", "Ihr übergebt das Profil mit einem Link, der nur mit seiner bestätigten E-Mail-Adresse funktioniert. Die ganze Geschichte bleibt beim selben Profil, und die verwaltete Kinderanmeldung, die ihr betreut habt, funktioniert nicht mehr. Das Profil wird kein Erwachsenenprofil: Die Familienregeln bleiben, und Eltern sehen, was sie vorher gesehen haben. Einen selbstständigeren Modus für erwachsene Kinder hat Rodinka noch nicht."),
            ("Gehört das zu Rodinka Pro?", "Nein. Begleitung per Link, helfende Personen, mehrere Familien und die Übergabe eines Profils funktionieren alle ohne Rodinka Pro."),
        ),
        "card": "Großeltern, eine Babysitterin und andere nahe Menschen sehen nur die Termine, die sie betreffen.",
        "cta_title": "Ladet Oma zu ihrem ersten Termin ein.",
        "cta_text": "Öffne in Rodinka einen Termin, bei dem jemand außerhalb der Familie die Kinder begleitet, und schick der Person einen Link zur Bestätigung.",
    },
    "chores": {
        "title": "Aufgaben für die Familie und Zuständigkeiten im Haushalt | Rodinka",
        "description": "Verteilt Aufgaben in der Familie, gebt ihnen eine Fälligkeit und macht klar, wer sich um was kümmert. Eine praktische gemeinsame Übersicht für Eltern und Kinder.",
        "og_title": "Haushaltsaufgaben ohne endlose Erinnerungen",
        "og_description": "Klare Familienaufgaben, sichtbare Verantwortung und eine gemeinsame Übersicht, was erledigt ist.",
        "og_alt": "Familienaufgaben und Zuständigkeiten im Haushalt, verteilt in Rodinka",
        "eyebrow": "WER SICH ZU HAUSE UM WAS KÜMMERT",
        "h1": "Familienaufgaben, die nicht nur im Kopf eines Elternteils leben",
        "lead": "Den Zahnarzt buchen, Bücher in die Bibliothek bringen, den Müll rausbringen oder für einen Ausflug packen. Wenn eine Aufgabe eine Person und eine Fälligkeit hat, muss der Haushalt nicht auf ständigen Erinnerungen laufen.",
        "problem_title": "„Das müssten wir mal machen“ ist keine verteilte Aufgabe",
        "problem": (
            "Hausarbeit wird oft erst sichtbar, wenn sie liegen bleibt. Organisationsarbeit übersieht man noch leichter: eine Anmeldefrist fürs Ferienlager, ein Geburtstagsgeschenk oder der Anruf beim Handwerker. Hält eine Person all diese Details, trägt sie auch den größten Teil des Mental Load.",
            "Eine Familienaufgabenliste ist keine Leistungsbewertung des Haushalts. Sie ist eine einfache Absprache, was zu tun ist, wer es übernommen hat und bis wann es wichtig ist. Ist die Aufgabe erledigt, braucht es keine weitere Nachfrage.",
        ),
        "scenarios": (
            ("Kleine tägliche Pflichten", "Müll trennen, Geschirr oder den Schulranzen packen – alles mit einer kurzen, klaren Vorstellung davon, wann es erledigt ist."),
            ("Unsichtbare Organisationsarbeit", "Ein Anruf beim Arzt, die Zahlung für eine Aktivität oder ein Geschenkkauf bekommt eine Person und eine Fälligkeit."),
            ("Aufgaben für Kinder", "Ein Kind kann eine eigene Anmeldung haben, die nur seine Aufgaben zeigt. Eine Aufgabe kann eine Belohnung oder Taschengeld bringen, und ein Erwachsener bestätigt die Erledigung."),
        ),
        "help_title": "So verteilt ihr Haushaltsaufgaben in der Familie",
        "help_intro": "Rodinka macht aus vagen Vorhaben im Haushalt kleine, konkrete Schritte, die alle in der gemeinsamen Übersicht sehen.",
        "steps": (
            ("Das Ergebnis benennen", "Ersetze „Schule regeln“ durch „Formular für den Ausflug abschicken“. Eine konkrete Aufgabe macht klar, was erledigt bedeutet."),
            ("Person und Datum wählen", "Lasst nicht jede Aufgabe gemeinsam liegen, bis die aufmerksamste Person sie erledigt. Klärt die Zuständigkeit, solange der Bedarf klar ist."),
            ("Wiederkehrendes wiederholt sich selbst", "Den Müll jeden Dienstag rausbringen stellst du einmal ein. Eine einmalige Notiz ohne Fälligkeit und eine feste wöchentliche Pflicht sind hier dieselbe Art von Aufgabe."),
            ("Erledigtes darf aus dem Kopf", "Alle sehen, dass die Aufgabe erledigt ist, und wo eine Belohnung dranhängt, bestätigt ein Erwachsener und der Betrag wird gutgeschrieben."),
        ),
        "answers_title": "Fragen zu Familienaufgaben und Zuständigkeiten",
        "answers": (
            ("Wie verteilen wir die Hausarbeit fair?", "Rechnet Planung, Anrufe und das Im-Blick-Behalten von Fristen genauso mit wie sichtbares Putzen. Berücksichtigt dann Zeit und gedanklichen Aufwand, nicht nur die Zahl der Punkte pro Person."),
            ("Wie geben wir Kindern Aufgaben?", "Wählt etwas Altersgerechtes, Konkretes und bis zu einer klaren Zeit Machbares. Es geht um Beteiligung und die Gewohnheit zu helfen, nicht um ein perfektes Ergebnis."),
            ("Wie erinnern wir uns gegenseitig, ohne zu streiten?", "Einigt euch auf die verantwortliche Person und legt die Aufgabe an einen gemeinsamen Ort. Eine Erinnerung bezieht sich dann auf dieselbe sichtbare Absprache, statt dass eine Person die andere managt."),
            ("Wie funktionieren Belohnungen und Taschengeld?", "Eine Aufgabe kann eine Belohnung tragen und eine Bestätigung durch einen Erwachsenen verlangen. Das Kind hakt sie ab, ein Elternteil bestätigt, und der Betrag wird gutgeschrieben. Regelmäßiges Taschengeld kann davon abhängen, dass die vereinbarten Aufgaben erledigt sind."),
            ("Lässt sich eine schnelle Aufgabe diktieren?", "Auf unterstützten Geräten ja – direkt aus der Ansicht Heute. Du sagst, was zu tun ist, Rodinka macht daraus Aufgabenentwürfe und zeigt sie dir zum Bearbeiten. Angelegt wird nichts, bevor du bestätigst."),
        ),
        "card": "Konkrete Zuständigkeiten, eine klare verantwortliche Person und eine Fälligkeit für Erwachsene und Kinder.",
        "cta_title": "Verteilt eine Aufgabe, bevor sie in einer gedanklichen Liste verschwindet.",
        "cta_text": "Füge in Rodinka eine konkrete Aufgabe im Haushalt hinzu und klärt, wer sie übernimmt.",
    },
    "shopping": {
        "title": "Gemeinsame Einkaufsliste für die Familie, immer aktuell | Rodinka",
        "description": "Eine gemeinsame Einkaufsliste, die alle ergänzen und im Laden abhaken. Schluss mit verstreuten Nachrichten und vergessenen Zetteln.",
        "og_title": "Eine Einkaufsliste für den Haushalt, immer griffbereit",
        "og_description": "Ergänze, was zu Hause ausgeht, und kauf nach derselben aktuellen Liste ein.",
        "og_alt": "Gemeinsame Einkaufsliste der Familie in Rodinka für Lebensmittel und Haushaltsartikel",
        "eyebrow": "EINKAUFEN OHNE VERLORENE NACHRICHTEN",
        "h1": "Eine gemeinsame Einkaufsliste, die die ganze Familie ergänzt",
        "lead": "Die Milch ist heute Morgen ausgegangen, jemand hat im Chat Brot erwähnt, und der Zettel vom Kühlschrank ist zu Hause geblieben. Eine gemeinsame Liste hält einen Artikel fest, sobald jemand daran denkt – und ist auch im Laden aktuell.",
        "problem_title": "Die Liste zusammenzubekommen ist oft schwieriger als das Einkaufen",
        "problem": (
            "Lebensmittel einzukaufen ist einfach. Herauszufinden, was wirklich fehlt, ob es schon jemand eingetragen hat und wer einkaufen geht, ist der chaotische Teil. Papier funktioniert nur dort, wo es liegt, und eine Chatnachricht verschwindet schnell.",
            "Mit einer Liste für den Haushalt ist es weniger wichtig, wer am Ende einkauft. Alle können Artikel ergänzen, gekaufte werden abgehakt, und was übrig bleibt, wartet auf das nächste Mal.",
        ),
        "scenarios": (
            ("Gerade ist etwas ausgegangen", "Die letzte Milch oder das Waschmittel kommt sofort auf die Liste, nicht erst bei einem hektischen Gedächtnistest später."),
            ("Im Laden ohne Netz", "Die Liste funktioniert auch, wenn das Handy keinen Empfang hat. Abgehakte Artikel gleichen sich ab, sobald die Verbindung zurück ist."),
            ("Jemand anderes kauft ein", "Der Partner, der auf dem Heimweg einkauft, öffnet dieselbe Liste, ohne um eine aktuelle Nachricht zu bitten."),
        ),
        "help_title": "So führt ihr eine gemeinsame Einkaufsliste in Rodinka",
        "help_intro": "Die Liste gehört zu eurem Familienbereich, sodass eingeladene Haushaltsmitglieder sie auf Handy oder Computer öffnen und ergänzen können.",
        "steps": (
            ("Artikel tippen oder sprechen", "Halte einen Artikel fest, sobald du ihn bemerkst. Auf unterstützten Geräten musst du nicht tippen: Sag, was ausgegangen ist, und Rodinka macht daraus Artikel, die du prüfst, bearbeitest und bestätigst, bevor etwas hinzugefügt wird."),
            ("Nach derselben Version einkaufen, mit oder ohne Netz", "Hake im Laden ab. Alle anderen sehen, was erledigt ist, und kaufen nichts doppelt, und die Liste funktioniert offline, bis die Verbindung zurück ist."),
            ("Einkauf mit Essen verbinden", "Wenn ihr die Abendessen der Woche wählt, ergänzt die nötigen Zutaten, damit der Essensplan praktisch umsetzbar ist."),
        ),
        "answers_title": "Praktische Fragen zu gemeinsamen Einkaufslisten",
        "answers": (
            ("Wie teile ich eine Einkaufsliste mit meinem Partner?", "Nutzt eine Liste in einem gemeinsamen Familienbereich. Beide können Artikel ergänzen und abhaken, sodass ihr nicht vor jedem Einkauf eine neue Version schicken müsst."),
            ("Ist eine App besser als ein Einkaufszettel?", "Papier ist neben dem Kühlschrank schnell. Eine gemeinsame digitale Liste ist auch unterwegs verfügbar und lässt sich von mehreren Personen ergänzen – praktisch, wenn verschiedene Familienmitglieder einkaufen."),
            ("Kann ich die Einkaufsliste diktieren?", "Auf unterstützten Geräten ja. Du sagst, was fehlt, Rodinka macht daraus einzelne Artikel und zeigt sie zur Bestätigung – erst dann werden sie hinzugefügt. Was falsch erkannt wurde, kannst du vorher bearbeiten oder entfernen, und keine Aufnahme oder Abschrift wird gespeichert."),
            ("Funktioniert die Liste ohne Netz?", "Ja. Die Einkaufsliste ist für die Offline-Nutzung gebaut: Du kannst im Laden weiter Artikel ergänzen und abhaken, und die Änderungen gleichen sich ab, sobald das Handy wieder verbunden ist."),
            ("Kann Rodinka vorschlagen, was wir kaufen sollen?", "Mit Rodinka Pro ja. Artikel vorschlagen schaut, was ihr in den letzten 30 Tagen mindestens zweimal gekauft habt, und bietet Dinge an, die ihr nach eurem eigenen Rhythmus wieder brauchen könntet. Was schon auf der Liste steht oder gerade erst gekauft wurde, lässt es weg. Hinzugefügt wird nichts, bevor du bestätigst, und Mengen kannst du vorher anpassen."),
        ),
        "card": "Eine aktuelle Liste zu Hause und im Laden, ergänzt von der ganzen Familie.",
        "cta_title": "Der nächste Einkauf kann ohne Suche im Chat beginnen.",
        "cta_text": "Öffne die gemeinsame Liste in Rodinka und ergänze das Erste, was bei euch zur Neige geht.",
    },
