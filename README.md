# 🚀 ISS Overhead Notifier

Sends you an e-mail when the International Space Station (ISS) is above your head after dark. It is the day 33 assignment of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp", written in Python 3.13 with no runtime dependencies.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The program checks every 60 seconds whether the ISS is within 5 degrees of your latitude and longitude and whether it is night at your position. When both are true it sends you an e-mail. The assignment's function names `is_iss_overhead` and `is_night` are kept so you can compare your solution with this one.

| Part | What it is for |
| --- | --- |
| `src/iss_notifier/` | The program (domain rules, use case, API clients, mail sender, command line) |
| `tests/` | pytest tests that run offline |
| `docs/` | Business case, plan, milestones, reviews, screenshots and the wiki (`docs/wiki/`, in English, Danish and Bahasa Malaysia) |
| `pyproject.toml` | Project configuration and tool settings |
| `Doxyfile` | Settings for the Doxygen source documentation |

## 📋 Requirements

- Python 3.13 or newer (the standard library is all the program needs at runtime).
- `venv`, which ships with Python, to keep the project's tools out of your system Python.
- An SMTP account (for example a mail provider's app password) to send the e-mail.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation.

## 🛠️ Setup

Create a local virtual environment, upgrade pip and install the project with its development tools.

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

Leave the environment with `deactivate`. The `.venv` folder is ignored by git.

## ▶️ Run

The program reads its settings from environment variables; it loads no `.env` file. Set them in the terminal where you run it (PowerShell shown; use `export NAME="value"` on Linux and macOS):

```powershell
$env:ISS_NOTIFIER_LATITUDE = "<your latitude>"
$env:ISS_NOTIFIER_LONGITUDE = "<your longitude>"
$env:ISS_NOTIFIER_SMTP_HOST = "smtp.example.com"
$env:ISS_NOTIFIER_SMTP_USER = "<your login>"
$env:ISS_NOTIFIER_SMTP_PASSWORD = "<your app password>"
$env:ISS_NOTIFIER_MAIL_TO = "<recipient address>"
```

`ISS_NOTIFIER_SMTP_PORT` is optional (default 587, STARTTLS). Then start the notifier with the `.venv` active:

```bash
python -m iss_notifier
```

![ISS Overhead Notifier running][screenshot-run]

Press Ctrl+C to stop. The screenshot shows the real program running against recorded API responses and placeholder settings. The [wiki][documentation] explains every setting in English, Danish and Bahasa Malaysia.

## 🧪 Tests

With the environment active:

```bash
python -m pytest
```

![pytest result][screenshot-tests]

Quality checks used by the code review:

```bash
ruff check .
ruff format --check .
mypy
lint-imports
```

Build the source documentation (output in `build/doxygen/index.html`):

```bash
doxygen Doxyfile
```

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Domain dictionary][DICT-001] | The PO terms and the IT terms |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/issues
[license]: ./LICENSE
[screenshot-run]: ./docs/images/notifier-run.png
[screenshot-tests]: ./docs/images/pytest.png
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[DICT-001]: ./docs/dictionary.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
