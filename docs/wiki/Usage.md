# Usage

🌐 **English** · [Dansk](Usage-da) · [Bahasa Melayu](Usage-ms)

## 1. Configure

The program reads its settings from environment variables, never from a file. Set them in the terminal where you run the program. Windows (PowerShell):

```powershell
$env:ISS_NOTIFIER_LATITUDE = "<your latitude>"
$env:ISS_NOTIFIER_LONGITUDE = "<your longitude>"
$env:ISS_NOTIFIER_SMTP_HOST = "smtp.example.com"
$env:ISS_NOTIFIER_SMTP_USER = "<your login>"
$env:ISS_NOTIFIER_SMTP_PASSWORD = "<your app password>"
$env:ISS_NOTIFIER_MAIL_TO = "<recipient address>"
```

Linux and macOS:

```bash
export ISS_NOTIFIER_LATITUDE="<your latitude>"
export ISS_NOTIFIER_LONGITUDE="<your longitude>"
export ISS_NOTIFIER_SMTP_HOST="smtp.example.com"
export ISS_NOTIFIER_SMTP_USER="<your login>"
export ISS_NOTIFIER_SMTP_PASSWORD="<your app password>"
export ISS_NOTIFIER_MAIL_TO="<recipient address>"
```

Use an app password from your mail provider, not your normal password. All settings are listed on [Configuration](Configuration).

## 2. Run

With the `.venv` active:

```bash
python -m iss_notifier
```

![ISS Overhead Notifier running](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/raw/branch/main/docs/images/notifier-run.png)

Press Ctrl+C to stop. A failed network call is logged and the loop carries on with the next check. The log never contains your coordinates, address or password.

## What it decides

- `is_iss_overhead` is true when the ISS is within plus or minus 5 degrees of your latitude and your longitude (the longitude wraps around at 180 degrees).
- `is_night` is true before sunrise and from sunset, using UTC hours.
- Both functions keep the names of the assignment, so you can compare your solution:

```python
from iss_notifier import is_iss_overhead, is_night
```
