# G1 Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [cd21a73] |
| 2026-10-27 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Fixed a duplicated link block; no change of content | [c6b02ef] |

---

## Purpose

Decide whether the repository is ready to receive code: project configuration, ignore rules, environment instructions, constants, documentation tooling, the package skeleton and public metadata are in place.

## Deliverable

A merged pull request containing `pyproject.toml` (Python 3.13 or newer, `pytest` as an optional development dependency, no runtime dependencies), a Python `.gitignore` that also ignores `.env` and `.venv`, `Doxyfile`, a package skeleton under `src/` with `constants.py`, a `tests/` folder with a passing smoke test, a short `README.md` section on the local `.venv`, and the repository description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` has `requires-python = ">=3.13"` and an empty `dependencies` list | Yes | No |
| 2 | `.gitignore` ignores `.venv/`, `.env`, `__pycache__/`, `.pytest_cache/` and Doxygen output | Yes | No |
| 3 | Following the README, `python -m venv .venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` succeed | Yes | No |
| 4 | `python -m pytest` exits 0 | Yes | No |
| 5 | `doxygen Doxyfile` runs without warnings, or Doxygen is documented as not installed | Yes | No |
| 6 | The git host shows a description and at least 5 topics | Yes | No |
| 7 | No token or credential appears in the diff | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [BC-001], [SA-001], [PP-001] accepted | The plan-first gate |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O5 and O6 (metadata part) | [BC-001] |
| SC3, SC4, SC7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-10-19 — within the plan window in [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml | Configure the project for Python 3.13 or newer with no runtime dependencies, pytest as an optional `dev` dependency, the `src/` layout and pytest settings (`testpaths = ["tests"]`). Supports SC3. | No | BC-001 O5 |
| 2 | Add Python .gitignore | Ignore virtual environments, caches, build output, Doxygen output and the personal `.env` so that no token is ever committed. | No | BC-001 Constraints |
| 3 | Add package skeleton and constants.py | Create `src/iss_notifier/` with `__init__.py` and `constants.py` (API URLs, 60-second interval, 5-degree margin, timeouts) and a smoke test in `tests/` so that the test runner has something to run. | No | BC-001 O3, O4 |
| 4 | Add Doxyfile | Add a Doxyfile that reads `src/` and writes to `build/doxygen`, so Doxygen comments in source can be rendered. Supports SC8. | No | BC-001 SC8 |
| 5 | Document local .venv | Add README instructions to create `.venv`, activate it on Windows and POSIX, upgrade pip with `python -m pip install --upgrade pip` and install the project. Supports SC4. | No | BC-001 O5 |
| 6 | Set repository description and topics | Set the description and topics on the git host through its application programming interface (API) with the token in the personal `.env` (read in the shell, never printed or stored in the project). Supports SC7. | No | BC-001 O6 |

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[cd21a73]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/cd21a7366b9c25f09a6ff9c7283f82f8f865d6e5
[c6b02ef]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/c6b02ef5942d486bc8f5a86a4a733d3ba76c1dc5
