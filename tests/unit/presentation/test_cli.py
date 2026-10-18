import logging
from collections.abc import Mapping
from typing import Any

import pytest

from iss_notifier.constants import (
    ENV_LATITUDE,
    ENV_LONGITUDE,
    ENV_MAIL_TO,
    ENV_SMTP_HOST,
    ENV_SMTP_PASSWORD,
    ENV_SMTP_USER,
    EXIT_CONFIG_ERROR,
    EXIT_OK,
)
from iss_notifier.presentation.cli import main

ENVIRON = {
    ENV_LATITUDE: "51.5",
    ENV_LONGITUDE: "-0.1",
    ENV_SMTP_HOST: "smtp.example.test",
    ENV_SMTP_USER: "me@example.test",
    ENV_SMTP_PASSWORD: "s3cret-value",
    ENV_MAIL_TO: "you@example.test",
}


def _no_network(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
    raise AssertionError("no request expected")


def test_main_returns_config_exit_code_when_a_variable_is_missing(
    caplog: pytest.LogCaptureFixture,
) -> None:
    environ = {k: v for k, v in ENVIRON.items() if k != ENV_SMTP_HOST}
    with caplog.at_level(logging.INFO):
        code = main([], environ, sleep=lambda _: None, fetch=_no_network)
    assert code == EXIT_CONFIG_ERROR
    assert ENV_SMTP_HOST in caplog.text


def test_main_returns_ok_and_logs_stop_on_ctrl_c(
    caplog: pytest.LogCaptureFixture,
) -> None:
    def interrupted(seconds: float) -> None:
        raise KeyboardInterrupt

    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        return {"iss_position": {"latitude": "-80", "longitude": "100"}}

    with caplog.at_level(logging.INFO):
        code = main([], ENVIRON, sleep=interrupted, fetch=fetch)
    assert code == EXIT_OK
    assert "stopped" in caplog.text
    assert "s3cret-value" not in caplog.text
