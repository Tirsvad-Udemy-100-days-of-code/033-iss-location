# Pemasangan

🌐 [English](Install) · [Dansk](Install-da) · **Bahasa Melayu**

## Keperluan

- Python 3.13 atau lebih baharu.
- `venv`, yang disertakan dengan Python.
- Pilihan: [Doxygen](https://www.doxygen.nl/) untuk dokumentasi sumber.

Program tidak memerlukan pakej pihak ketiga semasa dijalankan; alat pembangunan (pytest, ruff, mypy, import-linter) dipasang dalam `.venv` setempat sahaja.

## Cipta dan gunakan `.venv` setempat

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux dan macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Baris arahan kedua mengaktifkan persekitaran, yang ketiga menaik taraf pip. Keluar daripada persekitaran dengan `deactivate`. Folder `.venv` diabaikan oleh git.

Seterusnya: [Penggunaan](Usage-ms).
