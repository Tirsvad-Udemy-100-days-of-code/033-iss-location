# Ujian

🌐 [English](Testing) · [Dansk](Testing-da) · **Bahasa Melayu**

## Ujian

Ujian berjalan di luar talian: API dan pelayan mel digantikan dengan palsu, dan tiada apa menunggu masa sebenar. Dengan `.venv` aktif:

```bash
python -m pytest
```

![pytest result](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/raw/branch/main/docs/images/pytest.png)

## Semakan kualiti

```bash
ruff check .
ruff format --check .
mypy
lint-imports
```

## Dokumentasi sumber

Sumber menggunakan ulasan Doxygen. Bina dengan:

```bash
doxygen Doxyfile
```

Hasilnya ada di `build/doxygen/index.html`.
