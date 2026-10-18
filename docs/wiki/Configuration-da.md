# Konfiguration

🌐 [English](Configuration) · **Dansk** · [Bahasa Melayu](Configuration-ms)

## Filen `config.env`

Indstillingerne er linjer af typen `NAVN=værdi` i `config.env`, i den mappe, hvor du kører programmet. Linjer, der starter med `#`, og tomme linjer ignoreres; et `export `-præfiks og citationstegn om en værdi er tilladt. Start fra `config.env.example`:

```text
ISS_NOTIFIER_LATITUDE=<your latitude>
ISS_NOTIFIER_LONGITUDE=<your longitude>
ISS_NOTIFIER_SMTP_HOST=smtp.example.com
ISS_NOTIFIER_SMTP_PORT=587
ISS_NOTIFIER_SMTP_USER=<your login>
ISS_NOTIFIER_SMTP_PASSWORD=<your app password>
ISS_NOTIFIER_MAIL_TO=<recipient address>
```

En variabel sat i det rigtige miljø tilsidesætter filen; `--config <sti>` læser en anden fil. En manglende `config.env` er i orden, når miljøet indeholder indstillingerne; en manglende fil angivet med `--config` stopper programmet.

## Indstillinger

| Variabel | Påkrævet | Betydning |
| --- | --- | --- |
| `ISS_NOTIFIER_LATITUDE` | sammen med længdegraden | Din breddegrad i grader, -90 til 90 |
| `ISS_NOTIFIER_LONGITUDE` | sammen med breddegraden | Din længdegrad i grader, -180 til 180 |
| `ISS_NOTIFIER_SMTP_HOST` | ja | Værtsnavn på din SMTP-server |
| `ISS_NOTIFIER_SMTP_PORT` | nej | SMTP-port, standard 587 (STARTTLS) |
| `ISS_NOTIFIER_SMTP_USER` | ja | Login til SMTP-serveren |
| `ISS_NOTIFIER_SMTP_PASSWORD` | ja | Adgangskode eller app-adgangskode |
| `ISS_NOTIFIER_MAIL_TO` | ja | Adressen, der modtager e-mailen |

En manglende variabel stopper programmet med en besked, der nævner variablens navn, aldrig dens værdi. Programmet læser kun `config.env`; det læser aldrig en fil med navnet `.env`.

## Positionsgæt

Udelades både `ISS_NOTIFIER_LATITUDE` og `ISS_NOTIFIER_LONGITUDE`, spørger programmet `get.geojs.io`, hvor din offentlige IP-adresse befinder sig, og bruger den position. Det sender din offentlige IP-adresse til den tredjepartstjeneste, det er kun præcist til byniveau (nok til marginen på 5 grader), og loggen siger, at positionen er gættet, uden at udskrive den. Sætter du begge variabler, slås gættet fra. Sætter du kun den ene, er det en fejl.

## Konstanter

Faste værdier (de to API-adresser, kontrolintervallet på 60 sekunder, marginen på 5 grader, timeouts og e-mailteksten) er defineret ét sted i `src/iss_notifier/constants.py`.
