import logging

import pytest

from iss_notifier.application.monitor import run_monitor
from iss_notifier.domain.errors import PositionUnavailableError


def test_run_monitor_checks_and_sleeps_for_each_round() -> None:
    sleeps: list[float] = []
    calls: list[int] = []

    def check() -> bool:
        calls.append(1)
        return False

    run_monitor(check, sleeps.append, max_checks=3)
    assert len(calls) == 3
    assert sleeps == [60, 60, 60]


def test_run_monitor_uses_the_given_interval() -> None:
    sleeps: list[float] = []
    run_monitor(lambda: False, sleeps.append, interval_seconds=5, max_checks=1)
    assert sleeps == [5]


def test_run_monitor_continues_after_a_failed_check(
    caplog: pytest.LogCaptureFixture,
) -> None:
    results: list[bool | Exception] = [PositionUnavailableError("down"), True]
    calls: list[int] = []

    def check() -> bool:
        calls.append(1)
        outcome = results[len(calls) - 1]
        if isinstance(outcome, Exception):
            raise outcome
        return outcome

    with caplog.at_level(logging.WARNING):
        run_monitor(check, lambda _: None, max_checks=2)
    assert len(calls) == 2
    assert "PositionUnavailableError" in caplog.text


def test_run_monitor_does_not_swallow_unexpected_errors() -> None:
    def check() -> bool:
        raise RuntimeError("bug")

    with pytest.raises(RuntimeError):
        run_monitor(check, lambda _: None, max_checks=1)
