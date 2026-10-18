# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-003], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [7e33d80] |

---

## Artifact Under Review

- Instance reviewed: `.gitea/workflows/publish-wiki.yml` on branch `ci-publish-wiki` (a workflow file, not a registered artifact; it implements the wiki publishing of [MIL-003] criterion 3, requested by S01 in chat)
- Checklist used: [QC-WF-001] (`QC-WF-001`)
- Scope: full review of the files changed by the branch
- Language and domain: n/a (source code is professional IT English)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the author is the AI)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | QC-YML-001 checked: PyYAML 1.x SafeLoader with a duplicate-key check parses it; 2-space indent, LF, one final newline; `yamllint` 1.38.0 passes with the committed `.yamllint.yml`; `prune` is quoted; the key `on` is the documented workflow key; no tags, anchors or secrets; header comment present. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | Only `.gitea/workflows/publish-wiki.yml`; no copy in `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name`, `on` (push, branch `main`, two paths) and `jobs` are present. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | Header states purpose, trigger, inputs, secret, what changes outside the repository (the wiki only), host, and the origin template. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | The only job has a descriptive name; the steps are inside the reusable workflow. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | `actionlint` 1.7.12 reports nothing for the file. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | The job declares `permissions: contents: read`. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | The called workflow is `TirSystem/github-action` at the moving major tag `v2`, the same organisation as the framework and the release policy in its CHANGELOG; `tools-ref` is the same tag. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | The secret is read as `secrets.TOKEN_FOR_GITEA_WIKI` and passed to the reusable workflow; it exists as an organisation secret; the name does not start with `GITEA_` or `GITHUB_`. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No `inputs.*` or event text is interpolated; the inputs are literals. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | Trigger is `push` to `main`; no fork-triggered event. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | The only trigger is a push to the protected `main` branch; there is no manual trigger, so no manual run can skip a dry run (the framework template also offers `workflow_dispatch`, which was left out for this reason). |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | Pass | Needs `write:repository` for the wiki, which the organisation token has; the built-in token cannot write the wiki. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | `runs-on` and `timeout-minutes: 10` are set in the reusable workflow (`publish-wiki-pages.yml` at v2). |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` group `publish-wiki` with `cancel-in-progress: false`, so publishing queues. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Filtered by branch and by the paths `docs/wiki/**` and this file. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | No tools are installed by this file; the script comes from `tools-ref: v2`. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | Nothing is installed, so there is nothing to cache. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | N-A | The steps and their logging are in the reusable workflow. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | No `run:` block; the logic is `tools/publish_wiki.py` in the shared repository. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | The logic is the reusable workflow `publish-wiki-pages.yml`; this file only calls it. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | Gitea 1.27.3; the provider repository runs the same caller pattern on this instance with success (`publish-own-wiki.yml`, runs of release 2.1.1). The first run of this file is checked after the merge. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | N-A | The header names the tag; pinning is the provider's responsibility (optional). |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | N-A | The repository has no static test of workflows yet (optional); `actionlint` and `yamllint` were run by hand. |

## Overall Verdict

Go — all mandatory criteria pass. One thing is open: no run of this file exists yet; the first run after the merge is recorded in the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | - | - |

---

[MIL-003]: ../../milestones/mil-003-docs-wiki.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[7e33d80]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/7e33d80b6515e32cf520545805c1673d183cbdf9
