import logging
import ssl
from collections.abc import Callable, Mapping
from datetime import UTC, datetime
from email.message import EmailMessage
from types import TracebackType
from typing import Any, Self

import pytest

from iss_notifier.constants import (
    CHECK_INTERVAL_SECONDS,
    EMAIL_SUBJECT,
    ENV_LATITUDE,
    ENV_LONGITUDE,
    ENV_MAIL_TO,
    ENV_SMTP_HOST,
    ENV_SMTP_PASSWORD,
    ENV_SMTP_USER,
    EXIT_OK,
    ISS_NOW_URL,
    SUNRISE_SUNSET_URL,
)
from iss_notifier.domain.errors import RemoteRequestError
from iss_notifier.presentation.cli import main

Fetch = Callable[[str, Mapping[str, str] | None], dict[str, Any]]

ENVIRON = {
    ENV_LATITUDE: "51.5",
    ENV_LONGITUDE: "-0.1",
    ENV_SMTP_HOST: "smtp.example.test",
    ENV_SMTP_USER: "me@example.test",
    ENV_SMTP_PASSWORD: "s3cret-value",
    ENV_MAIL_TO: "you@example.test",
}
OVERHEAD = {"iss_position": {"latitude": "53.0", "longitude": "-2.0"}}
FAR_AWAY = {"iss_position": {"latitude": "-40.2", "longitude": "120.9"}}


def _iso(hour: int) -> str:
    return f"2026-10-19T{hour:02d}:07:00+00:00"


def _sun(sunrise_hour: int, sunset_hour: int) -> dict[str, Any]:
    return {
        "results": {"sunrise": _iso(sunrise_hour), "sunset": _iso(sunset_hour)},
        "status": "OK",
    }


def _night_now() -> dict[str, Any]:
    """Daylight data that makes the current UTC hour night."""
    hour = (datetime.now(UTC).hour + 1) % 24
    return _sun(hour, hour)


def _day_now() -> dict[str, Any]:
    """Daylight data that keeps day for hours either side of the current UTC hour."""
    hour = datetime.now(UTC).hour
    return _sun((hour - 3) % 24, (hour + 3) % 24)


class FakeSmtp:
    sent: list[EmailMessage] = []

    def __init__(self, host: str, port: int, timeout: float) -> None:
        pass

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        return None

    def starttls(self, *, context: ssl.SSLContext | None = None) -> object:
        return None

    def login(self, user: str, password: str) -> object:
        return None

    def send_message(self, msg: EmailMessage) -> object:
        FakeSmtp.sent.append(msg)
        return None


@pytest.fixture(autouse=True)
def reset_mailbox() -> None:
    FakeSmtp.sent = []


def _serve(iss: list[dict[str, Any] | Exception], sun: dict[str, Any]) -> Fetch:
    iss_replies = iter(iss)

    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        if url == ISS_NOW_URL:
            reply = next(iss_replies)
            if isinstance(reply, Exception):
                raise reply
            return reply
        assert url == SUNRISE_SUNSET_URL
        assert params is not None
        assert params["formatted"] == "0"
        return sun

    return fetch


def _run(fetch: Fetch, checks: int) -> list[float]:
    sleeps: list[float] = []
    code = main(
        [],
        ENVIRON,
        sleep=sleeps.append,
        smtp_factory=FakeSmtp,
        fetch=fetch,
        max_checks=checks,
    )
    assert code == EXIT_OK
    return sleeps


def test_flow_sends_exactly_one_mail_when_overhead_at_night() -> None:
    sleeps = _run(_serve([OVERHEAD], _night_now()), checks=1)
    assert len(FakeSmtp.sent) == 1
    assert FakeSmtp.sent[0]["Subject"] == EMAIL_SUBJECT
    assert FakeSmtp.sent[0]["To"] == "you@example.test"
    assert sleeps == [CHECK_INTERVAL_SECONDS]


def test_flow_sends_nothing_when_overhead_by_day() -> None:
    _run(_serve([OVERHEAD], _day_now()), checks=1)
    assert FakeSmtp.sent == []


def test_flow_sends_nothing_when_the_iss_is_far_away() -> None:
    _run(_serve([FAR_AWAY], _night_now()), checks=1)
    assert FakeSmtp.sent == []


def test_flow_continues_after_a_failing_fetch(
    caplog: pytest.LogCaptureFixture,
) -> None:
    fetch = _serve([RemoteRequestError("request failed"), OVERHEAD], _night_now())
    with caplog.at_level(logging.INFO):
        sleeps = _run(fetch, checks=2)
    assert len(FakeSmtp.sent) == 1
    assert sleeps == [60, 60]
    assert "Check failed" in caplog.text


def test_flow_logs_neither_secrets_nor_coordinates(
    caplog: pytest.LogCaptureFixture,
) -> None:
    with caplog.at_level(logging.INFO):
        _run(_serve([OVERHEAD], _night_now()), checks=1)
    assert "ISS overhead: yes, night: yes" in caplog.text
    for hidden in ("s3cret-value", "me@example.test", "you@example.test", "51.5"):
        assert hidden not in caplog.text
