# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-015 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-004] (source code and tests of branch `mil-004-config-file`)
- Checklist used: [QC-PY-001] (`QC-PY-001`)
- Scope: full review of the files changed by the branch
- Language and domain: n/a (source code is professional IT English)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the code was written by the python-developer agent and reviewed by the main AI, so the review is not independent)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules and functions `snake_case`, classes `PascalCase`, constants `UPPER_SNAKE`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`IssOverheadCheck`, `run_monitor`, `load_settings`); the assignment names `is_iss_overhead` and `is_night` are kept on purpose ([DICT-001] Rules). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check .` and `ruff format --check .` pass; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `mypy` strict passes on 37 files; every signature including tests is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | Specific `IssNotifierError` subclasses ; `raise ... from` keeps the cause in `fetch_json`; no bare `except`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; no builtins shadowed. |
| 7 | Files, locks and connections are managed with context managers | Pass | `urlopen`, the SMTP connection and `Path.read_text` are used safely (context managers or the file API). |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public item has a one-line docstring and a Doxygen block; `doxygen Doxyfile` has no warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | Only `logging`; tests assert that logs contain no secret, coordinate or URL, also for the guessed position and the config errors, which name a line number or a path only. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists; the project has no use cases ([PP-001] Open Issues). The design is recorded in [MIL-002] tasks 1 to 9. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 136 tests named for behaviour; no network and no real sleeping; the User-Agent header and the HTTP status in the error message are covered with a fake opener. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Strict mypy passes; `Any` appears only for decoded JSON values. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; dev tools declared with lower bounds, none unused. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Constants, URLs (`GEOLOCATION_URL`), the default file name and the variable names are defined once in `constants.py`. The brief of each item appears in a Doxygen block and a docstring because Doxygen 1.15 does not read docstring commands and ruff requires docstrings; accepted as a tool constraint. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `lint-imports` contract "Layers point inward" kept; no import cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Ports are narrow `Protocol`s (`HomePositionProvider` added); the use case receives its providers; the composition root is `presentation/cli.py`; each class has one reason to change. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Packages `domain`, `application`, `infrastructure`, `presentation`; tests under `tests/unit` and `tests/integration`. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All names are English, lower case, no spaces. |

## Overall Verdict

Go — all applicable mandatory criteria pass. Verified live without sending mail: the IP lookup, the ISS position and the sunrise-sunset calls succeed with the new User-Agent. Not verified: a real mail server.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | - | - |

---

[MIL-004]: ../../milestones/mil-004-config-file.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
