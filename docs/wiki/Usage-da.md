# Brug

🌐 [English](Usage) · **Dansk** · [Bahasa Melayu](Usage-ms)

## 1. Konfigurer

Programmet læser sine indstillinger fra filen `config.env` i den mappe, hvor du kører det. Kopiér eksemplet og redigér kopien. Windows (PowerShell):

```powershell
Copy-Item config.env.example config.env
```

Linux og macOS:

```bash
cp config.env.example config.env
```

Erstat hver pladsholder i `config.env`. Filen ignoreres af git, så dine værdier bliver aldrig committet. Brug en app-adgangskode fra din mailudbyder, ikke din almindelige adgangskode.

En variabel, der også er sat i det rigtige miljø, tilsidesætter filen, og `--config <sti>` læser en anden fil. Udelader du både `ISS_NOTIFIER_LATITUDE` og `ISS_NOTIFIER_LONGITUDE`, gætter programmet din position ud fra din offentlige IP-adresse (se [Konfiguration](Configuration-da)). Alle indstillinger står der.

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
