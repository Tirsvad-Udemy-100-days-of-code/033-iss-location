# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Purpose

This analysis names the people involved in the ISS (International Space Station) Overhead Notifier project and what each needs, so that owners, reviewers and readers are cited by stable IDs. It follows the Mendelow power/interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen (course participant) | Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the assignment with a clean, tested and documented repository |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and README instructions to run it |
| S03 | GitHub viewers | Repository visitors | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- Manage Closely: S01 decides the scope, writes and reviews the work, and cares about every part of it.
- Keep Informed: S02 cannot change the scope but depends on the quality of the shared code and on its instructions.
- Monitor: S03 browses for ideas; their needs are met by the repository's front page and are not negotiated.

## Primary Concerns and FURPS+ Mapping

FURPS+ stands for Functionality, Usability, Reliability, Performance, Supportability, plus design, implementation, interface and physical constraints.

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Correct decisions on overhead and night; process followed | Functionality, Supportability |
| S01 | Tests run offline and pass | Reliability |
| S02 | Assignment function names kept so solutions can be compared | Functionality |
| S02 | Setup and run steps that work from a clean clone | Usability, Implementation (Python 3.13, venv) |
| S03 | Description, topics, README and screenshots that explain the project quickly | Usability |
| S03 | No runtime dependencies | Implementation, Physical (nothing to install) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat and pull request review | Per milestone | Plan acceptance, pull requests, final summary | All milestones |
| S02 | README and wiki (en, da, ms) | Once per release | Run instructions and screenshots | Documentation milestone |
| S03 | Repository description, topics and README | Once, then on change | Metadata and front page | Foundation and documentation milestones |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Compact code that matches the assignment versus a layered Clean Architecture design | S01, S02 | Keep the assignment's function names in a thin public module and the layers as plain modules behind them |
| Real screenshots versus privacy of coordinates and addresses | S01, S03 | Take screenshots with placeholder values only |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct decisions and process | O1, O2, O4 in [BC-001] |
| S02 | Runnable code, assignment names, instructions | O3, O5 in [BC-001] |
| S03 | Description, topics, README, wiki, screenshots | O6 in [BC-001] |

## Sign-Off

| Stakeholder | Sign-off |
| --- | --- |
| S01 | Pending review (AI as stand-in in autonomous mode) |

---

[BC-001]: ./business-case.md
