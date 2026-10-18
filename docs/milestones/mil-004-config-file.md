# G4 Config file

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [f2afaf8] |
| 2026-10-27 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added task 7 and criteria 10 and 11: guess the position from the IP address | pending |

---

## Purpose

Decide whether the settings can be kept in a `config.env` file next to the program, with a committed `config.env.example` of placeholders, instead of being typed as environment variables in every terminal, and whether the program can guess the position from the public IP address when no latitude and longitude are set. S01 asked for both after G3.

## Deliverable

A merged pull request in which the program reads its settings from `config.env` (key=value lines, standard library only), `config.env.example` lists every setting with placeholders, `config.env` is ignored by git, the tests cover the file reader, the position is looked up from the public IP address through `https://get.geojs.io/v1/ip/geo.json` when neither latitude nor longitude is set, and the README, the wiki in English, Danish and Bahasa Malaysia and the run screenshot describe the file and the lookup instead of the `$env:` commands.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `config.env.example` contains every `ISS_NOTIFIER_*` name from `constants.py` with a placeholder value and no real value | Yes | No |
| 2 | `.gitignore` ignores `config.env`; `git check-ignore config.env` prints the file | Yes | No |
| 3 | With a `config.env` in the working directory and an empty environment, `python -m iss_notifier` starts; a value set in the real environment overrides the file | Yes | No |
| 4 | A missing default `config.env` is not an error (the environment is used); a missing file named by `--config` exits with code 2 and a message that names the file, never a value | Yes | No |
| 5 | Comments, blank lines, `export ` prefixes and single or double quotes around values are handled; a malformed line gives a `ConfigError` naming the line number only | Yes | No |
| 6 | `python -m pytest`, `ruff`, `mypy`, `lint-imports` and `doxygen Doxyfile` pass; `pyproject.toml` still lists no runtime dependency | Yes | No |
| 7 | The README and the wiki pages of all three languages describe `config.env`; no `$env:` setup block remains; `check-readme.sh` passes | Yes | No |
| 8 | The run screenshot is regenerated and shows no real value; no secret appears in the diff | Yes | No |
| 9 | The personal `.env` is neither read, tested nor imported by the project | Yes | No |
| 10 | With neither `ISS_NOTIFIER_LATITUDE` nor `ISS_NOTIFIER_LONGITUDE` set, the home position comes from the IP lookup; with only one of them set the program exits with code 2 naming both variables; a failed or malformed lookup exits with code 2; the log says that the position was guessed but never prints it | Yes | No |
| 11 | The README and the wiki (all three languages) say that the guess sends the public IP address to `get.geojs.io`, is only city accurate and can be replaced by setting the two variables | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The settings loader and the command line |
| [MIL-003] | The README, wiki and screenshots that are updated |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O5, O6 | [BC-001] |
| SC1, SC4, SC6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-10-28 — a change requested after the plan window of [PP-001]; the Business Case has no end date.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add config.env file reader | Parse a `config.env` file with the standard library: `KEY=value` lines, `#` comments, blank lines, an optional `export ` prefix and single or double quotes. A malformed line raises `ConfigError` that names the line number and never a value. Lives in the infrastructure layer. | No | BC-001 O1 |
| 2 | Load settings from config.env | `main` reads `config.env` from the working directory (or the path given with a new `--config` option), merges it under the real environment (the environment wins) and passes the result to `load_settings`. A missing default file is fine; a missing explicit file exits with code 2. | No | BC-001 O1 |
| 3 | Add config.env.example and ignore config.env | Add `config.env.example` with every setting, a comment per setting and placeholder values; add `config.env` to `.gitignore` so that real values are never committed. | No | BC-001 O5 |
| 4 | Test the config file | Unit tests for the reader (comments, quotes, `export`, malformed line, empty file) and for precedence and the missing-file cases, plus the integration test using a temporary `config.env`; all offline. Supports SC1. | No | BC-001 O4 |
| 5 | Update README and wiki for config.env | Replace the `$env:` blocks in the README and in Usage and Configuration of the wiki (English, Danish, Bahasa Malaysia) with the copy-and-edit steps for `config.env`; keep the same page set. | No | BC-001 O5, O6 |
| 6 | Regenerate the run screenshot | Re-render `docs/images/notifier-run.png` so that it shows the `config.env` step with placeholders. Supports SC6. | No | BC-001 O6 |
| 7 | Guess the position from the IP address | When neither latitude nor longitude is set, ask `https://get.geojs.io/v1/ip/geo.json` (standard library, timeout from constants) for the position of the public IP address and use it as the home position. Only one of the two set is a `ConfigError`; a failed or malformed answer raises a domain error and the program exits with code 2. The log says the position was guessed, never the values. The lookup is behind a port so tests use a fake. | No | BC-001 O1 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-notifier.md
[MIL-003]: ./mil-003-docs-wiki.md
[f2afaf8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/f2afaf8f9d93fa95691f273b3fd3a658804eddee
