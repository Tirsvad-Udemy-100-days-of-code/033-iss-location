# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [cd21a73] |

---

## Executive Summary

The Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" sets an assignment, the ISS Overhead Notifier. The program checks at a check interval of 60 seconds whether the International Space Station (ISS) is overhead, that is within the margin of error of five degrees of the user's position, while it is night, and then sends a notification by e-mail. This project delivers that program as a small, runnable, documented Python repository. It uses the standard library only, the assignment's function names, a README and a three-language wiki (English, Danish, Bahasa Malaysia) with screenshots. The repository is a learning record for the course participant and a readable reference for other participants and GitHub visitors.

## Methodological and Standards Foundation

- Method: plan first (Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as issues), then code, as `AGENTS.md` and `framework/process/plan-first-gate.md` define it. One branch and one pull request per milestone.
- Quality standards: ISO/IEC 25010:2023 characteristics tag every quality control (QC) criterion; code is reviewed against `qc-programming-python`. The review process is the software quality assurance (SQA) process of the framework.
- Architecture: the `clean-architecture` skill, scaled to a single-purpose script (see Constraints).
- Source documentation: Doxygen comments with a `Doxyfile`.

## Problem Statement

1. The assignment has no repository of its own: the code lives in a lecture folder with no tests, no run instructions and no description.
2. Code shared between course participants is often hard to run: dependencies and the Python version are unstated and credentials are hard-coded.
3. A visitor to the repository cannot tell in a few seconds what the project does, how to run it or what it looks like.

## Business Opportunity

A tested, documented and runnable solution can be reused as a reference by other participants, shows the participant's skill to GitHub visitors and gives the participant a worked example of the project process in `AGENTS.md`.

## Objectives

1. O1: Deliver a program that decides whether the ISS is overhead (within the margin of error of plus or minus 5 degrees of latitude and longitude) and whether it is night at the user's position, and sends a notification by e-mail when both hold.
2. O2: Re-check the conditions in a loop at the check interval of 60 seconds, so the program can run in the background.
3. O3: Keep the assignment's function names so other participants can compare solutions.
4. O4: Cover the logic with pytest tests that need no network and no mail server.
5. O5: Document how to create and use a local `.venv`, upgrade pip, run the program and run the tests.
6. O6: Publish a repository description, topics, a README and a wiki in English, Danish and Bahasa Malaysia, with screenshots.

## Scope

### In Scope

- A Python 3.13 program under `src/`, tests under `tests/`, documents under `docs/`.
- `pyproject.toml`, a Python `.gitignore`, `constants.py`, a `Doxyfile` and Doxygen comments.
- Coordinates and mail settings through environment variables, with no secrets in the repository.
- README from the framework template, wiki pages in `en`, `da` and `ms`, screenshots for both.
- Repository description and topics on the git host.

### Out of Scope

- A graphical user interface, a web service or a database.
- Runtime third-party dependencies, unless a later decision shows one is needed.
- Importing or testing the personal `.env` file; it holds personal tokens for the git host only.
- Mail other than Simple Mail Transfer Protocol (SMTP) with STARTTLS (start Transport Layer Security), push notifications and several locations.
- Packaging for the Python Package Index (PyPI).

## Expected Benefits

### Tangible Benefits

- A repository another participant can clone, run and test in minutes.
- Tests of the decision logic without network access.
- A published description, topics and wiki in three languages.

### Intangible Benefits

- A worked example of plan-first delivery for the course participant.
- A readable reference for the course community.
- A pattern to reuse in the next course assignments.

## Strategic Alignment

The project supports the participant's goal of completing the bootcamp with portfolio-quality results, and the framework's goal of showing the SQA and QC process on a small real project.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| SC1 | Tests pass offline | 100 % of tests pass with no network | `python -m pytest` exit code 0 |
| SC2 | Assignment function names present | `is_iss_overhead` and `is_night` exist; the main loop uses the check interval of 60 seconds | Review of `src/` against the assignment text |
| SC3 | Runtime dependencies | 0 third-party packages in `[project] dependencies` | `pyproject.toml` |
| SC4 | Setup from a clean clone | `.venv` created, pip upgraded and tests run by README steps alone | Fresh-clone walkthrough recorded in the milestone review |
| SC5 | Wiki languages | Same page set in `en`, `da` and `ms` | Page list compared per language |
| SC6 | Screenshots | At least one in the README and one in each wiki language | Image files referenced and present |
| SC7 | Repository metadata | Description and at least 5 topics set | Git host API response |
| SC8 | Source documentation | Every public function has a Doxygen comment; `doxygen Doxyfile` reports no warnings | Doxygen output |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The ISS or sunrise-sunset application programming interface (API) changes or is unavailable | The program cannot decide | Keep API calls in one small client module, handle errors without ending the loop, mock the APIs in tests |
| Mail credentials leak into the repository | Security incident | Read credentials from environment variables only, ignore `.env` in `.gitignore`, never print them |
| Screenshots show personal data (address, coordinates) | Privacy loss | Use placeholder values when taking screenshots |
| The repository named in the request differs from `origin` | Metadata set on the wrong repository | Stop and ask before the first outward-facing action; see Assumptions |
| Translations drift from English | Inconsistent wiki | English is authoritative; same page set per language, checked at the wiki milestone |

## Assumptions

- S01 is the Product Owner (PO) and the reviewer; in autonomous mode the AI acts as stand-in for S01 and records it in each review.
- S02 and S03 cannot be interviewed within this project; their needs are taken from the request.
- The PO language is English and the PO domain is IT.
- "Python greater than 3.13" is read as Python 3.13 or newer (`requires-python = ">=3.13"`); 3.13.14 is installed.
- The `origin` remote (`Tirsvad-Udemy-100-days-of-code/033-iss-location`) is the repository to publish to. The request names `Tirsvad-Udemy-100_days_of_code`, which looks like the organisation; this is raised in the Project Plan's Open Issues.
- The ISS position API (`api.open-notify.org`) and the sunrise-sunset API (`api.sunrise-sunset.org`) are available without a key.

## Constraints

- Python 3.13 or newer, `venv` for the environment, `pytest` for tests (a development dependency only).
- Folders `src/`, `tests/` and `docs/`; constants in `constants.py`; configuration in `pyproject.toml`.
- Standard library only at runtime (`urllib`, `smtplib`, `json`, `datetime`).
- Personal tokens come from `.env`, are used for the git host only and are never printed, tested or imported by the project.
- No commit to `main`; one branch and one pull request per milestone.
- A small script: the Clean Architecture layers are kept as modules (rules, API clients, mail adapter, entry point), not as heavy packages.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About 3 to 5 hours of effort across three milestones | A reusable, tested reference and a complete portfolio repository |
| No licence or hosting cost; the public APIs are free | A worked example of the plan-first process and of a three-language wiki |

Qualitative assessment: the costs are small and the repository already exists, so a quantified return would add no information.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment, owns the scope, writes the code and reviews it |
| S02 | Wants readable, runnable code with the assignment's function names and run instructions |
| S03 | Wants a clear description, topics and README and no runtime dependencies |

## Recommendation

Proceed — the scope is small, the risks have mitigations and the result serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[cd21a73]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/cd21a7366b9c25f09a6ff9c7283f82f8f865d6e5
