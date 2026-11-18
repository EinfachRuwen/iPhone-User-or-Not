# Hinweise für KI-Assistenten und Mitwirkende

Statische Seite (GitHub Pages, Custom Domain `iphone-user-or-not.by0.link`), kein Build.

## Datenschutz (verbindlich)

Bei jeder datenschutzrelevanten Codeänderung – neue Dienste oder Bildhoster, neue Requests (fetch/XHR/WebSocket, eingebundene Bilder/Skripte/Fonts), Cookies oder Browserspeicher, Analytics, neue Datenfelder (z. B. in `report.html` oder den Gruppen-JSONs), Änderungen am Hosting – müssen geprüft und im selben Commit aktualisiert werden:

1. `datenschutz.html` (öffentliche Datenschutzerklärung) inkl. **Stand-Datum**,
2. `docs/DATENSCHUTZ-TECHNIK.md` (Tabelle mit Fundstellen, Empfängern, Speicherdauer, Rechtsgrundlage, Status) inkl. Stand-Datum.

Neue Seiten verlinken die Datenschutzerklärung intern (`datenschutz.html`), nicht extern.
