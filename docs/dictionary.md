# Domain Dictionary (PO and IT terms)

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [cd21a73] |

---

## Purpose and Scope

Maps each Product Owner (PO) term of the ISS Overhead Notifier to its professional IT term. PO language: English (`en`); PO domain: `it`. The dictionary covers the words used in the Business Case, the milestones and the wiki; no Domain Model exists, because the project has no use cases.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| ISS overhead | en | Position match | The International Space Station is within the margin of error of the user's latitude and longitude. | BC, MIL | source code |
| Night | en | Night interval | The time of day before sunrise or after sunset at the user's position. | BC, MIL | source code |
| Margin of error | en | Position tolerance | The plus or minus 5 degrees of latitude and longitude that still count as overhead. | BC, MIL | source code |
| Notification | en | Alert message | The e-mail sent to the user when the ISS is overhead at night. | BC, MIL | source code |
| Check interval | en | Polling interval | The 60 seconds the program waits between two checks. | BC, MIL | source code |

## Rules

- The Business Case, milestones and wiki use the PO term; the source code uses the IT term for identifiers and comments where the two differ. The assignment's function names `is_iss_overhead` and `is_night` are kept as given (a stated exception, [BC-001] objective O3).
- One IT term per PO term and one PO term per IT term; no synonyms.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[cd21a73]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/cd21a7366b9c25f09a6ff9c7283f82f8f865d6e5
