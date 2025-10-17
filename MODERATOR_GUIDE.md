# Moderator-Anleitung: Geschichten prüfen und veröffentlichen

## Willkommen als Moderator!

Diese Anleitung zeigt Ihnen Schritt für Schritt, wie Sie eingereichte Geschichten prüfen und veröffentlichen können.

## Übersicht

Als Moderator haben Sie Zugriff auf ein Google Sheets-Dokument, in dem alle Einreichungen gesammelt werden. Ihre Aufgabe ist es, diese zu prüfen und zu entscheiden, ob sie veröffentlicht werden sollen.

**Keine Sorge:** Der Prozess ist sehr einfach und erfordert keine technischen Kenntnisse!

---

## Schritt-für-Schritt Anleitung

### 1. Neue Einreichung erhalten

Sie erhalten eine E-Mail-Benachrichtigung (falls aktiviert), wenn jemand eine Geschichte eingereicht hat.

**Tipp:** Prüfen Sie regelmäßig (z.B. wöchentlich) das Spreadsheet, auch wenn Sie keine Benachrichtigung erhalten haben.

### 2. Google Sheets öffnen

1. Öffnen Sie das Moderations-Spreadsheet: **[LINK HIER EINFÜGEN]**
2. Melden Sie sich mit Ihrem Uni-Freiburg Google-Account an
3. Sie sehen eine Tabelle mit allen Einreichungen

### 3. Übersicht der Spalten

| Spalte | Bedeutung |
|--------|-----------|
| **A: Timestamp** | Wann wurde die Geschichte eingereicht |
| **B: Ihr Name** | Name des Einreichenden (kann Pseudonym oder "Anonym" sein) |
| **C: E-Mail** | Optional, nur für Rückfragen |
| **D: Abschlussjahr** | Optional, Studienabschluss-Jahr |
| **E: Titel** | Überschrift der Geschichte |
| **F: Ihre Geschichte** | Der eigentliche Inhalt |
| **G: Art** | Erinnerung, Erfolgsgeschichte, oder Beides |
| **H: Status** | **WICHTIG** – Hier treffen Sie Ihre Entscheidung |
| **I: Moderation Notes** | Interne Notizen (nicht öffentlich) |
| **J: Moderated By** | Wer hat moderiert |
| **K: Moderation Date** | Wann wurde moderiert |

### 4. Geschichte prüfen

Neue Einreichungen sind **gelb** markiert und haben den Status "Pending".

**Lesen Sie die Geschichte und prüfen Sie:**

✓ **Ist der Inhalt angemessen?**
- Keine beleidigenden oder unangemessenen Inhalte
- Keine Werbung oder Spam
- Kein persönlicher Angriff auf andere Personen

✓ **Bezieht sich die Geschichte auf Kognitionswissenschaft?**
- Muss sich auf das Studium in Freiburg beziehen
- Kann Erinnerung oder Erfolgsgeschichte sein
- Thematischer Bezug sollte erkennbar sein

✓ **Ist die Länge ausreichend?**
- Mindestens 50 Zeichen (normalerweise automatisch geprüft)
- Sollte eine zusammenhängende Geschichte sein

✓ **Ist der Ton angemessen?**
- Respektvoll gegenüber anderen
- Authentisch und persönlich
- Keine reinen Beschwerden oder Kritik

### 5. Entscheidung treffen

#### ✅ **Zum Genehmigen:**

1. Klicken Sie auf die Zelle in Spalte **H (Status)** in der Zeile der Geschichte
2. Öffnen Sie das Dropdown-Menü (kleiner Pfeil)
3. Wählen Sie **"Approve"**
4. Die Zeile wird automatisch **grün**
5. Optional: Fügen Sie eine Notiz in Spalte **I** hinzu (z.B. "Sehr schöne Erinnerung!")
6. Optional: Tragen Sie Ihren Namen in Spalte **J** ein
7. Optional: Tragen Sie das heutige Datum in Spalte **K** ein (Format: TT.MM.JJJJ)

**Das war's!** Die Geschichte wird automatisch auf der Website veröffentlicht.

#### ❌ **Zum Ablehnen:**

1. Klicken Sie auf die Zelle in Spalte **H (Status)**
2. Wählen Sie **"Reject"** aus dem Dropdown
3. Die Zeile wird automatisch **rot**
4. **Wichtig:** Tragen Sie in Spalte **I** den Grund für die Ablehnung ein
   - Beispiel: "Nicht themenbezogen", "Unangemessener Inhalt", "Spam"
5. Optional: Tragen Sie Ihren Namen und Datum ein (Spalten J und K)

**Abgelehnte Geschichten werden niemals veröffentlicht.**

### 6. Automatische Veröffentlichung

- **Täglich um 9:00 Uhr** prüft ein automatisches System das Spreadsheet
- Alle Geschichten mit Status "Approve" werden auf die Website übertragen
- **Sie müssen nichts weiter tun!**
- Nach maximal 24 Stunden ist die Geschichte online

### 7. Sofortige Veröffentlichung (optional)

Wenn Sie möchten, dass eine Geschichte **sofort** erscheint (z.B. für wichtige Einreichungen):

1. Öffnen Sie: [https://github.com/YOUR_USERNAME/kogni-memorial/actions](https://github.com/YOUR_USERNAME/kogni-memorial/actions)
2. Klicken Sie auf "Sync Stories from Google Sheets"
3. Klicken Sie auf den grünen Button **"Run workflow"**
4. Bestätigen Sie mit **"Run workflow"**
5. Nach 1-2 Minuten ist die Geschichte online

**Hinweis:** Dies erfordert einen GitHub-Account. Normalerweise ist die automatische tägliche Synchronisation ausreichend.

---

## Häufige Fragen (FAQ)

### Kann ich eine Entscheidung rückgängig machen?

**Ja!** Ändern Sie einfach den Status zurück:
- Von "Approve" → "Pending" (Geschichte verschwindet beim nächsten Sync)
- Von "Reject" → "Approve" (Geschichte wird veröffentlicht)

### Was passiert mit abgelehnten Geschichten?

- Sie werden niemals öffentlich angezeigt
- Sie bleiben im Spreadsheet sichtbar (für Dokumentation)
- Nach 90 Tagen werden sie automatisch aus dem System gelöscht

### Können mehrere Personen gleichzeitig moderieren?

**Ja!** Google Sheets unterstützt gleichzeitiges Bearbeiten.
- Sie sehen in Echtzeit, was andere Moderatoren tun
- Kein Risiko von Konflikten oder Überschneidungen

### Wie lange dauert es, bis Änderungen sichtbar sind?

- **Automatisch:** Bis zu 24 Stunden (täglicher Sync um 9 Uhr)
- **Manuell:** 1-2 Minuten (wenn Sie den Workflow manuell starten)

### Was ist, wenn jemand eine unpassende Geschichte einreicht?

1. Setzen Sie den Status auf "Reject"
2. Dokumentieren Sie den Grund in Spalte "Moderation Notes"
3. Die Geschichte wird niemals öffentlich angezeigt
4. Falls nötig, können Sie den Einreichenden per E-Mail kontaktieren (falls angegeben)

### Kann ich eine veröffentlichte Geschichte nachträglich bearbeiten?

- **Titel/Inhalt ändern:** Ja, direkt im Spreadsheet in der entsprechenden Zelle
- **Geschichte entfernen:** Status von "Approve" auf "Reject" ändern
- Änderungen werden beim nächsten Sync (täglich 9 Uhr) übernommen

### Was bedeuten die Farben der Zeilen?

- **Gelb:** Pending (noch nicht geprüft)
- **Grün:** Approved (wird veröffentlicht)
- **Rot:** Rejected (wird nicht veröffentlicht)
- **Weiß:** Noch keine Einreichung oder gelöscht

### Muss ich alle Spalten ausfüllen?

**Nein!** Nur Spalte **H (Status)** ist wichtig.
- Spalten I, J, K sind optional und dienen Ihrer eigenen Dokumentation
- Sie können auch leer bleiben

---

## Moderations-Richtlinien

### ✅ **Sollte veröffentlicht werden:**

- Authentische Erinnerungen an das Studium
- Erfolgsgeschichten über den Werdegang nach dem Studium
- Anekdoten über Dozenten, Seminare, Projekte (positiv oder neutral)
- Beschreibungen des interdisziplinären Charakters des Studiengangs
- Persönliche Reflexionen über die Studienzeit
- Dankbarkeit oder Wertschätzung gegenüber dem Studiengang

### ❌ **Sollte abgelehnt werden:**

- Beleidigende oder unangemessene Inhalte
- Persönliche Angriffe auf andere Personen
- Werbung oder kommerzielle Inhalte
- Spam oder offensichtlich gefälschte Einreichungen
- Inhalte ohne Bezug zur Kognitionswissenschaft Freiburg
- Reine Beschwerden ohne konstruktiven Inhalt
- Sehr kurze, nichtssagende Texte (unter 50 Zeichen)

### 🤔 **Grenzfälle:**

- **Kritik am Studiengang:** OK, wenn konstruktiv und respektvoll
- **Lustige/ironische Geschichten:** OK, wenn nicht beleidigend
- **Anonyme Einreichungen:** OK, solange Inhalt angemessen
- **Englischsprachige Einreichungen:** OK (internationale Alumni)
- **Sehr persönliche Geschichten:** OK, wenn nicht zu intim

**Im Zweifelsfall:** Diskutieren Sie mit anderen Moderatoren oder genehmigen Sie die Geschichte (Sie können sie später immer noch entfernen).

---

## Kontakt bei Problemen

### Technische Probleme:
- GitHub Actions funktioniert nicht
- Spreadsheet ist beschädigt
- Sync-Fehler

**Kontakt:** [TECHNISCHER KONTAKT HIER]

### Inhaltliche Fragen:
- Unsicherheit bei Moderation
- Umgang mit schwierigen Einreichungen
- Allgemeine Fragen zum Projekt

**Kontakt:** kogni@psychologie.uni-freiburg.de

---

## Vielen Dank!

Ihre Arbeit als Moderator hilft dabei, die Erinnerungen an den Studiengang Kognitionswissenschaft zu bewahren. Jede veröffentlichte Geschichte ist ein wertvoller Beitrag zur Geschichte dieses einzigartigen Studiengangs.

**Bei Fragen oder Unsicherheiten:** Zögern Sie nicht, nachzufragen!

---

*Letzte Aktualisierung: Oktober 2025*
