# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001] (`QC-DICT-001`)
- Scope: full review
- Language and domain: en / it (the artifact's Metadata rows)
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is also the AI, so this is a self-review that the user can challenge in the run summary)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | All five rows have PO term, language, IT term and definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Each PO term maps to one IT term and the reverse. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | N-A | No Domain Model exists; the project has no use cases. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | N-A | No Operation Contract, Sequence Diagram, Design Class Diagram or ERD exists. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Definitions are English, one sentence each. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | The artifact types named (BC, MIL, source code) exist or are planned in [PP-001]. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | Metadata and every row are en / it, matching the registry. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language` = en and `Domain` = it, no placeholder. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English; identifiers and commands stay as written. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register matches the registry row for this type. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | This document is the dictionary; its terms are consistent with themselves. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists beside the file (`docs/` listing). |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no earlier accepted version, so no language change to record. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The reviewer (stand-in for S01) reads English and knows the domain. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations are spelled out on first use after the review round. |

## Overall Verdict

Go — every applicable mandatory criterion passes; two criteria are not applicable until a Domain Model exists.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | - | - |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
