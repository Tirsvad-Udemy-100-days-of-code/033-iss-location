# Review Record: PP-001 against QC-PP-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-017 |
| CrossReference | [PP-001], [QC-PP-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial review record; verdict Go (autonomous, not independent) | [098f63a] |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001] and [QC-LANG-001]
- Scope: full review
- Language and domain: en / education
- Language reviewer: none (the stand-in reads English and knows the education domain)
- Mode: autonomous, not independent (AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Planning Assumptions give the start date 2026-10-19, the dates of the gateways and the window 2026-11-16 to 2026-11-23 of G5. The Business Case sets no end date; the plan says so and states the effort estimate and the one-pull-request-per-milestone rule as its constraint. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | The Gateway Schedule lists the five gateways once each with document, decision date and owner; every document exists, including MIL-005. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | The decision dates of MIL-001 to MIL-004 equal the Target Dates of their milestone documents (read for this review: 2026-10-19, 2026-10-21, 2026-10-24, 2026-10-28); MIL-005 decides on 2026-11-23, which is its Target Date. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every In Scope item of BC-001 to a gateway; the new baseline item maps to MIL-005. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Dependencies state the chain G1 to G5; it is acyclic and agrees with the order of the dates. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | Dependencies state that a No-Go moves the later dates, that S01 decides the new dates and that a No-Go on G5 leaves the program and the earlier gateways as they are. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owner S01 and reviewer S01 (stand-in for the baseline) are stakeholder IDs of SA-001; no governance document exists, so there is no RACI to contradict. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Each planning assumption names its source or is a decision of S01 (stated in the plan); the added gateways G4 and G5 are recorded with their reason. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Plan Risks give impact and mitigation for each risk; the CI risk of MIL-005 traces to SC9 of BC-001 and the wiki risk to the wiki risk of BC-001 (translations). |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues lists the repository path (closed in its text), the reading of the Python version, the missing user stories, the IP position guess, the earlier lack of a checklist and the domain of the unchanged documents; none contradicts another statement of the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | The main deliverable of MIL-005 names the same items as its Deliverable section; the G4 deliverable now names the IP guess and the User-Agent that MIL-004 delivers; the rows of G1 to G3 match their milestone documents. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | The Stories column of every gateway says none (plain tasks); the milestone tasks show that they are plain technical tasks. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | The Gantt bars use the dates of the schedule table and the dependency line is the same chain as the Dependencies section. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Each gateway links its milestone on the git host (195, 196, 197 and 202 exist and are closed; the milestone of G5 is linked after the sync). |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | PP-001 is the only Project Plan; its Version History records each change in its own row and only the latest row is Accepted. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | The Metadata table has `Language | en` and `Domain | education`; neither is a placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code and `education` is a row of the domain list of docs/artifact-registry.md. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | The prose and the table cells are English; only file names, commands and IDs are code. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | The registry gives the register `IT Executive English` for this type; the text is written for that reader. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | DICT-001 exists. The text added by the baseline uses none of its terms (ISS overhead, night, margin of error, notification, check interval) under a second name, found by reading. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, section headings, IDs and statuses are the framework's English ones. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No file `<name>.<language>.md` exists beside the document. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | The `Domain` row changed from `it` to `education` in this version (the language `en` is unchanged). The Version History row records the change and this review covers it. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The stand-in reads English and knows the education domain and checked the terms; the check is autonomous and not independent. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Fail | Some abbreviations of the earlier text (ISS, API and similar) are not spelled out at first use; CI and the abbreviations added in this change are. Optional, deferred. |

## Overall Verdict

Go — every Mandatory criterion of QC-PP-001 and QC-LANG-001 passes; the domain of the unchanged documents is recorded as an Open Issue. The plan is reviewed against its checklist for the first time. Review of the whole document after the edits of this change.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Criterion LANG 10 (Optional) failed: Abbreviations are spelled out on first use, in the stated language; fix or accept the deferral | S01 | 2026-11-23 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[098f63a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/098f63ab2539f469a56163d3a3c85bbaac7dbc84
