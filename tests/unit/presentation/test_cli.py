import logging
from collections.abc import Mapping
from pathlib import Path
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
    GEOLOCATION_URL,
)
from iss_notifier.domain.errors import RemoteRequestError
from iss_notifier.presentation.cli import main

ENVIRON = {
    ENV_LATITUDE: "51.5",
    ENV_LONGITUDE: "-0.1",
    ENV_SMTP_HOST: "smtp.example.test",
    ENV_SMTP_USER: "me@example.test",
    ENV_SMTP_PASSWORD: "s3cret-value",
    ENV_MAIL_TO: "you@example.test",
}


@pytest.fixture(autouse=True)
def empty_working_directory(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep a real config.env of the developer out of the tests."""
    monkeypatch.chdir(tmp_path)


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


def _write_config(
    directory: Path, values: Mapping[str, str], name: str = "config.env"
) -> Path:
    path = directory / name
    path.write_text("".join(f"{k}={v}\n" for k, v in values.items()), encoding="utf-8")
    return path


def _far_away_fetch(urls: list[str]) -> Any:
    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        urls.append(url)
        if url == GEOLOCATION_URL:
            return {"latitude": "55.5", "longitude": "12.5"}
        return {"iss_position": {"latitude": "-80", "longitude": "100"}}

    return fetch


def _run(
    tmp_path: Path,
    environ: Mapping[str, str],
    argv: list[str] | None = None,
    fetch: Any = None,
) -> int:
    return main(
        argv or [],
        environ,
        sleep=lambda _: None,
        fetch=fetch or _far_away_fetch([]),
        max_checks=1,
        cwd=tmp_path,
    )


def test_main_starts_from_the_default_config_file_with_an_empty_environment(
    tmp_path: Path,
) -> None:
    _write_config(tmp_path, ENVIRON)
    assert _run(tmp_path, {}) == EXIT_OK


def test_main_lets_the_environment_win_over_the_config_file(tmp_path: Path) -> None:
    _write_config(tmp_path, {**ENVIRON, ENV_LATITUDE: "999"})
    assert _run(tmp_path, {ENV_LATITUDE: "51.5"}) == EXIT_OK
    assert _run(tmp_path, {}) == EXIT_CONFIG_ERROR


def test_main_accepts_a_missing_default_config_file(tmp_path: Path) -> None:
    assert _run(tmp_path, ENVIRON) == EXIT_OK


def test_main_reads_the_file_named_by_config_option(tmp_path: Path) -> None:
    _write_config(tmp_path, ENVIRON, name="other.env")
    assert _run(tmp_path, {}, ["--config", "other.env"]) == EXIT_OK
    assert _run(tmp_path, {}, ["--config", str(tmp_path / "other.env")]) == EXIT_OK


def test_main_exits_2_naming_a_missing_explicit_config_file(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    with caplog.at_level(logging.INFO):
        code = _run(tmp_path, ENVIRON, ["--config", "nowhere.env"])
    assert code == EXIT_CONFIG_ERROR
    assert "Configuration file not found" in caplog.text
    assert "nowhere.env" in caplog.text
    assert "s3cret-value" not in caplog.text


def test_main_exits_2_naming_the_line_of_a_malformed_config_file(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    (tmp_path / "config.env").write_text("A=1\nleaked-secret\n", encoding="utf-8")
    with caplog.at_level(logging.INFO):
        code = _run(tmp_path, ENVIRON)
    assert code == EXIT_CONFIG_ERROR
    assert "line 2" in caplog.text
    assert "leaked-secret" not in caplog.text


def test_main_guesses_the_home_position_when_no_coordinates_are_set(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    environ = {
        k: v for k, v in ENVIRON.items() if k not in (ENV_LATITUDE, ENV_LONGITUDE)
    }
    urls: list[str] = []
    with caplog.at_level(logging.INFO):
        code = _run(tmp_path, environ, fetch=_far_away_fetch(urls))
    assert code == EXIT_OK
    assert urls[0] == GEOLOCATION_URL
    assert "Home position guessed from the public IP address" in caplog.text
    for hidden in ("55.5", "12.5", GEOLOCATION_URL):
        assert hidden not in caplog.text


def test_main_does_not_guess_when_coordinates_are_set(tmp_path: Path) -> None:
    urls: list[str] = []
    assert _run(tmp_path, ENVIRON, fetch=_far_away_fetch(urls)) == EXIT_OK
    assert GEOLOCATION_URL not in urls


@pytest.mark.parametrize("present", [ENV_LATITUDE, ENV_LONGITUDE])
def test_main_exits_2_when_only_one_coordinate_is_set(
    tmp_path: Path, caplog: pytest.LogCaptureFixture, present: str
) -> None:
    environ = {
        k: v for k, v in ENVIRON.items() if k not in (ENV_LATITUDE, ENV_LONGITUDE)
    }
    environ[present] = "51.5"
    with caplog.at_level(logging.INFO):
        code = _run(tmp_path, environ, fetch=_no_network)
    assert code == EXIT_CONFIG_ERROR
    assert ENV_LATITUDE in caplog.text
    assert ENV_LONGITUDE in caplog.text


@pytest.mark.parametrize(
    "reply",
    [
        RemoteRequestError("request failed: URLError"),
        {"unexpected": "shape"},
        {"latitude": "north", "longitude": "12"},
        {"latitude": "123.75", "longitude": "12"},
    ],
)
def test_main_exits_2_when_the_position_guess_fails(
    tmp_path: Path, caplog: pytest.LogCaptureFixture, reply: object
) -> None:
    environ = {
        k: v for k, v in ENVIRON.items() if k not in (ENV_LATITUDE, ENV_LONGITUDE)
    }

    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        if isinstance(reply, Exception):
            raise reply
        assert isinstance(reply, dict)
        return reply

    with caplog.at_level(logging.INFO):
        code = _run(tmp_path, environ, fetch=fetch)
    assert code == EXIT_CONFIG_ERROR
    assert GEOLOCATION_URL not in caplog.text
    assert "123.75" not in caplog.text
