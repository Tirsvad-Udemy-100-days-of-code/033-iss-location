# G3 Docs and wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Purpose

Decide whether the repository can be understood and used by S02 and S03 without help: README, screenshots and a three-language wiki are complete and accurate.

## Deliverable

A merged pull request with `README.md` built from the framework template (setup, run, tests, screenshot), screenshots under `docs/images/`, and the wiki in `docs/wiki/` as English pages plus Danish (`-da`) and Bahasa Malaysia (`-ms`) translations with the same page set, a language line on every page and a `_Sidebar.md`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `README.md` follows the framework template sections and its commands work from a clean clone | Yes | No |
| 2 | `bash framework/scripts/check-readme.sh` passes | Yes | No |
| 3 | Every wiki page exists in `en`, `da` and `ms` with the same page set | Yes | No |
| 4 | Every wiki page starts with the language line and `_Sidebar.md` lists all three languages | Yes | No |
| 5 | The README and each wiki language reference at least one screenshot that exists in the repository | Yes | No |
| 6 | Screenshots show placeholder values only (no real address, coordinates or credentials) | Yes | No |
| 7 | Code blocks, commands, file names and IDs are identical across languages | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The documented behaviour and commands must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O5, O6 | [BC-001] |
| SC4, SC5, SC6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-10-24 — within the plan window in [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture screenshots | Run the notifier against recorded responses with placeholder coordinates and capture the console output as Portable Network Graphics (PNG) images in `docs/images/` for the README and the wiki. Supports SC6. | No | BC-001 O6 |
| 2 | Write README from the framework template | Fill the template sections (overview, requirements, `.venv` setup, run, tests, license, links, appendix of documents) and embed a screenshot. Supports SC4. | No | BC-001 O5 |
| 3 | Write English wiki pages | Create Home, Install, Usage, Configuration, Testing and the sidebar in `docs/wiki/` following `framework/process/wiki.md`. English is the authoritative text. | No | BC-001 O6 |
| 4 | Translate wiki to Danish | Translate every English page to Danish (`-da`) with the same page set and the language line. Supports SC5. | No | BC-001 O6 |
| 5 | Translate wiki to Bahasa Malaysia | Translate every English page to Bahasa Malaysia (`-ms`) with the same page set and the language line. Supports SC5. | No | BC-001 O6 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-notifier.md

---

[BC-001]: ../business-case.md
