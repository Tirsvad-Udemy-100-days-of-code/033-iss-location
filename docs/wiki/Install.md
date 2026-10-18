# Install

🌐 **English** · [Dansk](Install-da) · [Bahasa Melayu](Install-ms)

## Requirements

- Python 3.13 or newer.
- `venv`, which ships with Python.
- Optional: [Doxygen](https://www.doxygen.nl/) for the source documentation.

The program needs no third-party package at runtime; the development tools (pytest, ruff, mypy, import-linter) are installed into the local `.venv` only.

## Create and use a local `.venv`

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The second command line activates the environment, the third upgrades pip. Leave the environment with `deactivate`. The `.venv` folder is ignored by git.

Next: [Usage](Usage).
