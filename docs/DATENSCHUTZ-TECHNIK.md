# Technische Datenschutzdokumentation – iPhone-User-or-Not

Stand: 18. November 2026 · Öffentliche Erklärung: [`datenschutz.html`](../datenschutz.html) (live: https://iphone-user-or-not.by0.link/datenschutz.html, GitHub Pages liefert auch `/datenschutz` aus)

Hinweis: Diese Datei liegt unter `docs/` und wird von GitHub Pages (Quelle: Branch `main`, Root) mit ausgeliefert. Sie enthält nichts Vertrauliches.

## Architektur

- Rein statische Seite (HTML/CSS/Inline-JS), kein Build, keine Abhängigkeiten, kein Server-Code.
- Hosting: GitHub Pages mit Custom Domain `iphone-user-or-not.by0.link` (`CNAME:1`; DNS zeigt auf `einfachruwen.github.io`, Response-Header `server: GitHub.com`, geprüft 18.11.2026). Repo-Feld „homepage“: `https://iphone-user-or-not.by0.link/`.
- Keine `vercel.json`, kein Dockerfile, keine `.env`, kein `package.json`, nur Branch `main`.
- `create-json.py` ist ein lokales Pflege-Skript (CLI), läuft nur lokal beim Pflegen; es schreibt nur die lokale JSON-Datei.

## Verarbeitungen

| # | Verarbeitung | Fundstelle | Datenkategorien | Empfänger / Ort | Speicherdauer | Rechtsgrundlage | Status |
|---|---|---|---|---|---|---|---|
| 1 | Auslieferung aller Seiten, Server-Logs | `CNAME:1`, DNS/Header | IP, Zeitpunkt, URL inkl. Query (`group`, `mode`, `game.html:161-163`, `index.html:190`), Referrer, User-Agent | GitHub, Inc. (USA, DPF aktiv bis 08/2027) | durch GitHub festgelegt („logged and stored for security purposes“, docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) | Art. 6 Abs. 1 lit. f | belegt; Aufbewahrungsdauer offen |
| 2 | Laden der Gruppendaten | `game.html:166-178` (XHR `GET <group>.json`, gleiche Origin) | wie 1 | GitHub | wie 1 | Art. 6 Abs. 1 lit. f | belegt |
| 3 | Spielbilder (lokal) | `img/FemboyTrain.png`, `img/milestone_lars.png`, `img/TimatixEU.png`; referenziert in `bahnbubble.json:185,209,215`, eingebunden über `game.html:205-215` (`showProfile()`) | wie 1 | GitHub (gleiche Origin) | wie 1 | Art. 6 Abs. 1 lit. f | belegt; am 18.11.2026 von i.imgur.com ins Repo übernommen – **keine Anfrage an Imgur mehr** |
| 4 | Einträge ohne Bild (35 von 38) | `bahnbubble.json` (`"picture": ""`), Platzhalter `#profile-placeholder` in `game.html` | – (nur Handle aus der JSON, kein Request) | – | – | – | belegt; die bisherigen URLs auf `ruwen.is-from.space` (nest.rip/Cloudflare) lieferten am 18.11.2026 alle HTTP 404 und wurden entfernt – **keine Anfrage an nest.rip/Cloudflare mehr**. `create-json.py` nimmt nur noch lokale Pfade unter `img/` an (externe URLs werden abgewiesen). |
| 5 | Daten Dritter im Spiel (Art. 14) | `bahnbubble.json` (38 Einträge: `name` = X-Handle, `picture` = lokaler Profil-Screenshot unter `img/` bei 3 Einträgen bzw. leer, `isiPhoneUser`) | Benutzername, Profilbild/-screenshot, abgeleitete Angabe zum Endgerät | öffentlich (alle Besucher), Repo öffentlich auf GitHub | bis Widerspruch / Offline-Gang | Art. 6 Abs. 1 lit. f | belegt; Abwägung/Einwilligung offen |
| 6 | „Report a problem“ | `report.html:58-101` | Name, E-Mail, Kategorie, Nachricht | **nicht** von der Seite gesendet: `mailto:` → Mailprogramm des Nutzers → `byzero@duck.com` (DuckDuckGo Email Protection, USA, Weiterleitung ohne Speicherung laut DDG) → Postfach des Verantwortlichen | bis Anfrage erledigt (aus bisheriger Erklärung, Abschnitt 6) | Art. 6 Abs. 1 lit. f | belegt; DPF-Status DDG nicht verifiziert; Ziel-Postfach unbekannt |
| 7 | Ergebnis teilen | `game.html:312-318` (`window.open` auf `twitter.com/intent/tweet` nur bei Klick) | Punktestand, Gruppe, Modus im vorbefüllten Text; ab Klick Daten bei X | X / Twitter International Unlimited Company (IE) | durch X | Nutzerhandlung, keine Verarbeitung durch Verantwortlichen vor Klick | belegt |
| 8 | Externe Links | `index.html` (Source Code → GitHub), `about.html:57-60` (by0.link, twitter.com, github.com) | – (erst bei Klick) | jeweilige Anbieter | – | – | belegt |
| 9 | Popups About/Report | `index.html:221-239` (`window.open` gleiche Origin) | – | GitHub | – | – | belegt |

## Was es nicht gibt (geprüft)

- Keine Cookies (`document.cookie` nicht verwendet), kein `localStorage`/`sessionStorage`/IndexedDB, kein Service Worker, kein Cache-API.
- Keine Analytics (kein Umami, kein Vercel Analytics, kein Google), keine externen Skripte, keine CDNs.
- Keine externen Bilder: seit 18.11.2026 werden alle Spielbilder vom eigenen Origin geladen; per Netzwerkmitschnitt (Startseite, Spiel mit mehreren Runden inkl. Einträgen ohne Bild, About, Report, Datenschutz) wurden nur Requests an den eigenen Host festgestellt.
- Keine externen Fonts (nur `Arial`/`monospace`, `index.html:9`, `game.html:9`, `report.html:7`, `about.html:7`).
- Keine Formular-Übertragung an einen Server, keine fetch/WebSocket-Aufrufe außer XHR aus Zeile 2.
- Vor dieser Änderung gab es **keinen** Datenschutz- und **keinen** Impressum-Link im Repo (auch nicht auf focusonruwen.com/datenschutz); die bisherige Erklärung (focusonruwen.com/datenschutz, Stand 15.11.2026) nennt dieses Projekt nicht im Geltungsbereich.

## Aus der bisherigen Erklärung übernommen

- Verantwortlicher, Anschrift, E-Mail, Aufsichtsbehörde (Niedersachsen), Rechte-Abschnitt, Löschregel für Kontakt-E-Mails, Stil.

## Offene Punkte

1. ~~Imgur ohne DPF~~ – erledigt 18.11.2026 (Bilder lokal unter `img/`).
2. ~~35 Bilder auf `ruwen.is-from.space` (404)~~ – erledigt 18.11.2026 (URLs entfernt, Platzhalter mit Handle). Falls die Originalbilder wieder auftauchen: als Datei unter `img/` ablegen, nicht extern verlinken.
3. Abwägung / Einwilligung der 38 gezeigten X-Nutzer (Nr. 5).
4. Impressum-Link fehlt (ggf. auf zentrales Impressum verlinken).
5. Report-Adresse `byzero@duck.com` vs. Kontaktadresse `info@focusonruwen.com` – bewusst so?
6. Log-Aufbewahrungsdauer bei GitHub Pages nicht öffentlich beziffert.
