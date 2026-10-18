# Konfiguration

🌐 [English](Configuration) · **Dansk** · [Bahasa Melayu](Configuration-ms)

## Miljøvariabler

| Variabel | Påkrævet | Betydning |
| --- | --- | --- |
| `ISS_NOTIFIER_LATITUDE` | ja | Din breddegrad i grader, -90 til 90 |
| `ISS_NOTIFIER_LONGITUDE` | ja | Din længdegrad i grader, -180 til 180 |
| `ISS_NOTIFIER_SMTP_HOST` | ja | Værtsnavn på din SMTP-server |
| `ISS_NOTIFIER_SMTP_PORT` | nej | SMTP-port, standard 587 (STARTTLS) |
| `ISS_NOTIFIER_SMTP_USER` | ja | Login til SMTP-serveren |
| `ISS_NOTIFIER_SMTP_PASSWORD` | ja | Adgangskode eller app-adgangskode |
| `ISS_NOTIFIER_MAIL_TO` | ja | Adressen, der modtager e-mailen |

En manglende variabel stopper programmet med en besked, der nævner variablens navn, aldrig dens værdi. Programmet indlæser ikke en `.env`-fil.

## Konstanter

Faste værdier (de to API-adresser, kontrolintervallet på 60 sekunder, marginen på 5 grader, timeouts og e-mailteksten) er defineret ét sted i `src/iss_notifier/constants.py`.
