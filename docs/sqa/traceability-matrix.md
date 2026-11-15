# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [DICT-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added RC-014, the re-review of MIL-004 for the User-Agent fix | [8defb7f] |
| 2026-10-28 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added RC-015, the code review of the User-Agent fix | [6998b0b] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Added MIL-005, the review records RC-016 to RC-019 and the wiki; set the reviewed rows of BC-001 and PP-001 and the domain of the changed rows to education; recorded the removed wiki workflow (autonomous, not independent) | [098f63a] |

---

## Purpose

Tracks backward and forward links between artifact instances so that the Business Case's cross-artifact traceability is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | education | - | [SA-001], [DICT-001], [PP-001], [MIL-005] | [RC-016], [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | [RC-002] |
| [DICT-001] | DICT | en | it | [BC-001] | - | [RC-003] |
| [PP-001] | PP | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-017] |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-004], [RC-007] |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | [MIL-003] | [RC-005], [RC-008] |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | - | [RC-006], [RC-009] |
| [MIL-004] | MIL | en | it | [BC-001], [PP-001], [MIL-003] | [MIL-005] | [RC-011], [RC-012], [RC-013], [RC-014], [RC-015] |
| [MIL-005] | MIL | en | education | [BC-001], [PP-001], [MIL-004] | - | [RC-018] |
| `.gitea/workflows/publish-wiki.yml` (removed, see the Coverage Notes) | CI workflow | - | - | [MIL-003] | - | [RC-010] |
| Wiki | Wiki | en, da, ms | education | [BC-001], [MIL-005] | - | [RC-019] |

## Coverage Notes

- [PP-001] was accepted without a QC checklist; it is reviewed against `QC-PP-001` for the first time in [RC-017].
- The wiki (`docs/wiki/`) is documentation, not an artifact with an ID or a Language and Domain row; it has its own review record, [RC-019].
- The project workflow `.gitea/workflows/publish-wiki.yml` was removed when the repository moved to the shared workflows of the git host (pull request #37); [RC-010] reviewed it while it existed.
- The domain of [BC-001], [PP-001], [MIL-005] and the wiki is `education` since [MIL-005]. The other documents keep the domain `it` they were accepted with; a change of their domain would need a new review of each (see the Open Issues of [PP-001]).
- [MIL-005] changes no source file, so the source code is not reviewed again.
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
[RC-008]: ./reviews/rc-008-mil-002-code.md
[RC-009]: ./reviews/rc-009-mil-003-docs.md
[RC-010]: ./reviews/rc-010-publish-wiki-workflow.md
[RC-011]: ./reviews/rc-011-mil-004.md
[RC-012]: ./reviews/rc-012-mil-004-ip-guess.md
[RC-013]: ./reviews/rc-013-mil-004-code.md
[RC-014]: ./reviews/rc-014-mil-004-user-agent.md
[RC-015]: ./reviews/rc-015-mil-004-user-agent-code.md
[MIL-004]: ../milestones/mil-004-config-file.md
[8defb7f]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/8defb7f0440d375136e4d200a3d0f08081cfbdf7
[6998b0b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/6998b0b260cae75083d035358c41dfd438090890
[MIL-005]: ../milestones/mil-005-framework-baseline.md
[RC-016]: ./reviews/rc-016-business-case-baseline.md
[RC-017]: ./reviews/rc-017-project-plan-baseline.md
[RC-018]: ./reviews/rc-018-milestone-005.md
[RC-019]: ./reviews/rc-019-wiki.md
[098f63a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/098f63ab2539f469a56163d3a3c85bbaac7dbc84
