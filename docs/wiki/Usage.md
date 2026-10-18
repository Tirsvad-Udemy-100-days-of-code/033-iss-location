# Usage

🌐 **English** · [Dansk](Usage-da) · [Bahasa Melayu](Usage-ms)

## 1. Configure

The program reads its settings from a file named `config.env` in the folder where you run it. Copy the example and edit the copy. Windows (PowerShell):

```powershell
Copy-Item config.env.example config.env
```

Linux and macOS:

```bash
cp config.env.example config.env
```

Replace every placeholder in `config.env`. The file is ignored by git, so your values are never committed. Use an app password from your mail provider, not your normal password.

A variable that is also set in the real environment overrides the file, and `--config <path>` reads another file. If you leave out both `ISS_NOTIFIER_LATITUDE` and `ISS_NOTIFIER_LONGITUDE`, the program guesses your position from your public IP address (see [Configuration](Configuration)). All settings are listed there.

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
