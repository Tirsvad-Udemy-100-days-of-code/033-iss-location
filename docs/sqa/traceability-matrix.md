# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [DICT-001], [PP-001], [MIL-001], [MIL-002], [MIL-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [cd21a73] |
| 2026-10-19 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added RC-007, the code review of MIL-001 | [f906248] |

---

## Purpose

Tracks backward and forward links between artifact instances so that the Business Case's cross-artifact traceability is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [DICT-001], [PP-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [DICT-001] | DICT | en | it | [BC-001] | - | [RC-003] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | - |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-004], [RC-007] |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | - | [RC-006] |

## Coverage Notes

- `PP` has no QC checklist yet, so it has no review record; the Product Owner accepts it (stand-in in autonomous mode).
- No use cases, user stories or Domain Model exist: every task is a plain technical task ([PP-001] Open Issues).
- `-` in Upstream means foundational; in Downstream it means nothing is built on it yet; in Last Reviewed it means no `RC-*` exists.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[DICT-001]: ../dictionary.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-foundation.md
[MIL-002]: ../milestones/mil-002-notifier.md
[MIL-003]: ../milestones/mil-003-docs-wiki.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-dictionary.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-001-code.md
[cd21a73]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/cd21a7366b9c25f09a6ff9c7283f82f8f865d6e5
[f906248]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/f906248afdd210283469ba31c11f034a7c477bad
