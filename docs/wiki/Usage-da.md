# Brug

🌐 [English](Usage) · **Dansk** · [Bahasa Melayu](Usage-ms)

## 1. Konfigurer

Programmet læser sine indstillinger fra miljøvariabler, aldrig fra en fil. Sæt dem i den terminal, hvor du kører programmet. Windows (PowerShell):

```powershell
$env:ISS_NOTIFIER_LATITUDE = "<your latitude>"
$env:ISS_NOTIFIER_LONGITUDE = "<your longitude>"
$env:ISS_NOTIFIER_SMTP_HOST = "smtp.example.com"
$env:ISS_NOTIFIER_SMTP_USER = "<your login>"
$env:ISS_NOTIFIER_SMTP_PASSWORD = "<your app password>"
$env:ISS_NOTIFIER_MAIL_TO = "<recipient address>"
```

Linux og macOS:

```bash
export ISS_NOTIFIER_LATITUDE="<your latitude>"
export ISS_NOTIFIER_LONGITUDE="<your longitude>"
export ISS_NOTIFIER_SMTP_HOST="smtp.example.com"
export ISS_NOTIFIER_SMTP_USER="<your login>"
export ISS_NOTIFIER_SMTP_PASSWORD="<your app password>"
export ISS_NOTIFIER_MAIL_TO="<recipient address>"
```

Brug en app-adgangskode fra din mailudbyder, ikke din almindelige adgangskode. Alle indstillinger står på siden [Konfiguration](Configuration-da).

## 2. Kør

Med `.venv` aktivt:

```bash
python -m iss_notifier
```

![ISS Overhead Notifier running](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/raw/branch/main/docs/images/notifier-run.png)

Tryk Ctrl+C for at stoppe. Et mislykket netværkskald logges, og løkken fortsætter med næste kontrol. Loggen indeholder aldrig dine koordinater, din adresse eller din adgangskode.

## Hvad det afgør

- `is_iss_overhead` er sand, når ISS er inden for plus/minus 5 grader af din breddegrad og din længdegrad (længdegraden løber rundt ved 180 grader).
- `is_night` er sand før solopgang og fra solnedgang, målt i UTC-timer.
- Begge funktioner bevarer opgavens navne, så du kan sammenligne din løsning:

```python
from iss_notifier import is_iss_overhead, is_night
```
