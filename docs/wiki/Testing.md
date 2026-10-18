# Testing

🌐 **English** · [Dansk](Testing-da) · [Bahasa Melayu](Testing-ms)

## Tests

The tests run offline: the APIs and the mail server are replaced by fakes, and nothing waits for real time. With the `.venv` active:

```bash
python -m pytest
```

![pytest result](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/raw/branch/main/docs/images/pytest.png)

## Quality checks

```bash
ruff check .
ruff format --check .
mypy
lint-imports
```

## Source documentation

The source uses Doxygen comments. Build them with:

```bash
doxygen Doxyfile
```

The output is in `build/doxygen/index.html`.
