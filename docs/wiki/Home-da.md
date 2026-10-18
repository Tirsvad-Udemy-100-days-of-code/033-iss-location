# ISS Overhead Notifier

🌐 [English](Home) · **Dansk** · [Bahasa Melayu](Home-ms)

Sender dig en e-mail, når den Internationale Rumstation (ISS) er over dig efter mørkets frembrud. Det er opgaven fra dag 33 i Udemys "100 Days of Code: The Complete Python Pro Bootcamp", skrevet i Python 3.13 uden runtime-afhængigheder.

![ISS Overhead Notifier running](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/raw/branch/main/docs/images/notifier-run.png)

_Skærmbilledet viser det rigtige program, der kører mod optagede API-svar og pladsholder-indstillinger._

| Side | Læs den, når du vil |
| --- | --- |
| [Installation](Install-da) | Oprette det lokale `.venv` og installere projektet |
| [Brug](Usage-da) | Indstille programmet, køre det og forstå, hvad det gør |
| [Konfiguration](Configuration-da) | Slå hver indstilling op |
| [Test](Testing-da) | Køre testene, kvalitetskontrollerne og kildedokumentationen |

## Sådan virker det

1. Hvert 60. sekund spørger programmet ISS-positions-API'et, hvor stationen er.
2. Det spørger solopgang-solnedgang-API'et, hvornår solen står op og går ned hos dig.
3. Hvis ISS er inden for 5 grader af din breddegrad og længdegrad, og det er nat, sender det dig en e-mail.

Repositoriet findes [her](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location).
