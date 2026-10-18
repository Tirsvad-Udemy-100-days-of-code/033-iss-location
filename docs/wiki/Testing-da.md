# Test

🌐 [English](Testing) · **Dansk** · [Bahasa Melayu](Testing-ms)

## Tests

Testene kører offline: API'erne og mailserveren er erstattet af fakes, og intet venter på rigtig tid. Med `.venv` aktivt:

```bash
python -m pytest
```

![pytest result](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/raw/branch/main/docs/images/pytest.png)

## Kvalitetskontrol

```bash
ruff check .
ruff format --check .
mypy
lint-imports
```

## Kildedokumentation

Kilden bruger Doxygen-kommentarer. Byg dem med:

```bash
doxygen Doxyfile
```

Resultatet ligger i `build/doxygen/index.html`.
