# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-004], [RC-011], [QC-MIL-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-MIL-001] (`QC-MIL-001`)
- Scope: delta re-review of the amended [MIL-004] (criteria 10 and 11 and task 7 added for the IP position guess); earlier record [RC-011]. The Open Issues change in [PP-001] is accepted with it (the Project Plan has no checklist)
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the AI)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | A concrete deliverable is defined for every gate | Pass | Deliverable names the merged pull request and its concrete content, now including the IP lookup. |
| 2 | Explicit Go/No-Go criteria are stated for each gate | Pass | Eleven objectively checkable Go / No-Go criteria (commands, files, exit codes). |
| 3 | Dependencies on other milestones are explicitly mapped | Pass | Dependencies table names [MIL-002] and [MIL-003] with reasons. |
| 4 | Each milestone is traceable to a Business Case objective or KPI | Pass | Traceability cites Business Case objectives O1, O5, O6 and success criteria SC1, SC4, SC6. |
| 5 | Milestone owner and approving reviewer are identified | Pass | Owner S01; approving reviewer S01 (AI as stand-in). |
| 6 | Milestone has a defined target date consistent with project constraints | Pass | Target date 2026-10-28; the Business Case has no end date and [PP-001] schedules G4 on it. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has Language = en and Domain = it. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose is English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register matches the registry row for MIL. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Uses the PO terms of [DICT-001]; no synonym added. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version of this document; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The reviewer (stand-in for S01) reads English and knows the domain. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (SMTP, API) are not used; config terms are file names. |

## Overall Verdict

Go — every mandatory criterion passes; criteria 10 and 11 are objectively checkable and traced to O1 and O5.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | - | - |

---

[MIL-004]: ../../milestones/mil-004-config-file.md
[RC-011]: ./rc-011-mil-004.md
[QC-MIL-001]: ../../../framework/qc/artifacts/qc-milestones-gateways.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
