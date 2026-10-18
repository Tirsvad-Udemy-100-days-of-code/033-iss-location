# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-003] (README, screenshots and wiki of branch `mil-003-docs-wiki`)
- Checklist used: none exists for a README or a wiki; the Go / No-Go criteria of [MIL-003] are used as the checklist, in their order
- Scope: full review of the files changed by the branch
- Language and domain: n/a (a technical delivery check; the wiki is en, da and ms)
- Language reviewer: none; the Danish and Bahasa Malaysia pages were translated by the AI and no native reader has checked them (see Action Items)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the AI)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | README follows the framework template sections and its commands work from a clean clone | Pass | A clone of the branch into a temporary folder, then the README steps (`python -m venv .venv`, pip upgrade, `pip install -e ".[dev]"`), gave 88 passed, ruff, mypy and lint-imports clean. |
| 2 | `bash framework/scripts/check-readme.sh` passes | Pass | Exit code 0. |
| 3 | Every wiki page exists in `en`, `da` and `ms` with the same page set | Pass | Home, Install, Usage, Configuration, Testing: 5 pages x 3 languages in `docs/wiki/`. |
| 4 | Every wiki page starts with the language line and `_Sidebar.md` lists all three languages | Pass | Each page has the language line under its heading; the sidebar has a Languages block. |
| 5 | The README and each wiki language reference at least one screenshot that exists in the repository | Pass | `docs/images/notifier-run.png` and `docs/images/pytest.png` are referenced by the README and by every wiki page set. |
| 6 | Screenshots show placeholder values only | Pass | Settings are shown as `<your latitude>` and similar; the log lines contain no coordinates, address or password. |
| 7 | Code blocks, commands, file names and IDs are identical across languages | Pass | The wiki pages are generated from shared code blocks; only prose and table cells differ. |

## Overall Verdict

Go — all seven criteria pass. The translations are unreviewed by a native speaker, which is recorded as an action item, not a condition of this gate.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Have a Danish and a Bahasa Malaysia reader check the translated wiki pages | S01 | 2026-11-01 |

---

[MIL-003]: ../../milestones/mil-003-docs-wiki.md
