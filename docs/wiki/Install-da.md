# Installation

🌐 [English](Install) · **Dansk** · [Bahasa Melayu](Install-ms)

## Krav

- Python 3.13 eller nyere.
- `venv`, som følger med Python.
- Valgfrit: [Doxygen](https://www.doxygen.nl/) til kildedokumentationen.

Programmet behøver ingen tredjepartspakke ved kørsel; udviklingsværktøjerne (pytest, ruff, mypy, import-linter) installeres kun i det lokale `.venv`.

## Opret og brug et lokalt `.venv`

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux og macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Den anden kommandolinje aktiverer miljøet, den tredje opgraderer pip. Forlad miljøet med `deactivate`. Mappen `.venv` ignoreres af git.

Næste: [Brug](Usage-da).
