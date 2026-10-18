# G2 Notifier

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-18 | Deprecated | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [cd21a73] |
| 2026-10-27 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Fixed a duplicated link block; no change of content | pending |

---

## Purpose

Decide whether the notifier works: the decisions whether the International Space Station (ISS) is overhead and whether it is night are correct, a notification is sent by e-mail when both hold, and the loop checks every 60 seconds without crashing on a failed call.

## Deliverable

A merged pull request with `src/iss_notifier/` containing the ISS client, the sunrise-sunset client, the rules `is_iss_overhead` and `is_night`, the Simple Mail Transfer Protocol (SMTP) mailer, environment-variable configuration and a main loop; plus pytest tests for all of them using fakes instead of the network and a mail server; with Doxygen comments on every public function.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `is_iss_overhead` is true for positions within plus or minus 5 degrees of the configured latitude and longitude and false outside, including the wrap-around at plus or minus 180 degrees longitude | Yes | No |
| 2 | `is_night` is true before sunrise and after sunset and false between, using the hour taken from the time string of the application programming interface (API) response | Yes | No |
| 3 | The mailer sends one message when both conditions hold and none otherwise | Yes | No |
| 4 | A failed network call is logged and the loop continues | Yes | No |
| 5 | The loop waits 60 seconds (a constant) between checks | Yes | No |
| 6 | `python -m pytest` exits 0 with no network access | Yes | No |
| 7 | Review against `qc-programming-python` is a Go; no credential in the diff | Yes | No |
| 8 | `pyproject.toml` still lists no runtime dependency | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Project configuration, constants and test runner |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O3, O4 | [BC-001] |
| SC1, SC2, SC3, SC8 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-10-21 — within the plan window in [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add configuration from environment | Read latitude, longitude and the SMTP settings (host, port, user, password, recipient) from environment variables into a frozen dataclass; fail with a clear message when one is missing. The project loads no `.env` file. | No | BC-001 O1 |
| 2 | Add ISS position client | Call the ISS position API with `urllib`, parse the JavaScript Object Notation (JSON) response into latitude and longitude floats and raise a typed error on failure. The fetch function is injectable for tests. | No | BC-001 O1 |
| 3 | Add sunrise-sunset client | Call the sunrise-sunset API with the configured coordinates and `formatted=0`, and return sunrise and sunset hours in 24-hour format taken from the time strings. | No | BC-001 O1 |
| 4 | Implement is_iss_overhead | Return true when the ISS latitude and longitude are within plus or minus 5 degrees of the configured position, handling longitude wrap-around. Keep the assignment's function name. | No | BC-001 O1, O3 |
| 5 | Implement is_night | Return true when the current hour is before sunrise or after sunset, with the clock injectable for tests. Keep the assignment's function name. | No | BC-001 O1, O3 |
| 6 | Add SMTP mailer | Send the notification e-mail with `smtplib` and STARTTLS (start Transport Layer Security) using the configured settings; the SMTP class is injectable so tests need no server. | No | BC-001 O1 |
| 7 | Add main loop | Check both conditions every 60 seconds (a constant), send mail when both hold, log and survive network errors, and stop cleanly on Ctrl+C. Entry point `python -m iss_notifier`. | No | BC-001 O2 |
| 8 | Write pytest tests | Test the rules, clients (with fake fetchers), mailer (with a fake SMTP) and the loop (with a fake clock and sleeper); all run offline. Supports SC1. | No | BC-001 O4 |
| 9 | Add Doxygen comments | Document every public module, class and function with Doxygen comments and run `doxygen Doxyfile` clean. Supports SC8. | No | BC-001 SC8 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ./mil-001-foundation.md
[cd21a73]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location/commit/cd21a7366b9c25f09a6ff9c7283f82f8f865d6e5
