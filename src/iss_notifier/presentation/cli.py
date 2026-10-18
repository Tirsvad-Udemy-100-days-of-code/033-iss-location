"""@brief Command line entry point and composition root."""

import argparse
import logging
import os
import smtplib
import time
from collections.abc import Callable, Mapping, Sequence
from contextlib import AbstractContextManager
from pathlib import Path

from iss_notifier.application.monitor import run_monitor
from iss_notifier.application.overhead_check import IssOverheadCheck
from iss_notifier.constants import (
    CHECK_INTERVAL_SECONDS,
    DEFAULT_CONFIG_FILE,
    EXIT_CONFIG_ERROR,
    EXIT_OK,
    LOG_FORMAT,
)
from iss_notifier.domain.errors import ConfigError, PositionGuessError
from iss_notifier.infrastructure.config import load_settings
from iss_notifier.infrastructure.env_file import read_env_file
from iss_notifier.infrastructure.http_json import JsonFetcher, fetch_json
from iss_notifier.infrastructure.ip_location_client import GeojsIpLocationClient
from iss_notifier.infrastructure.iss_client import OpenNotifyIssClient
from iss_notifier.infrastructure.smtp_notifier import SmtpNotifier, SmtpSession
from iss_notifier.infrastructure.sun_client import SunriseSunsetClient
from iss_notifier.infrastructure.system_clock import SystemClock

## @brief Logger of this module.
_LOGGER = logging.getLogger(__name__)


## @brief Parse the command line.
#
# @param argv Command line arguments, or None for sys.argv.
# @return The parsed arguments.
def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="iss-notifier",
        description=(
            "E-mail me when the ISS is overhead at night. "
            f"Checks every {CHECK_INTERVAL_SECONDS} seconds. "
            f"Configure through environment variables or a {DEFAULT_CONFIG_FILE} file."
        ),
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        metavar="PATH",
        help=f"configuration file to read (default: {DEFAULT_CONFIG_FILE} in the "
        "current directory, if it exists)",
    )
    return parser.parse_args(argv)


## @brief Read the configuration file, if there is one.
#
# @param config Path given with --config, or None for the default file.
# @param base Directory against which a relative path is resolved.
# @return Values of the file; empty when the default file does not exist.
# @throws ConfigError when the explicit file is missing or a file is invalid.
def _read_config_file(config: Path | None, base: Path) -> dict[str, str]:
    path = base / (DEFAULT_CONFIG_FILE if config is None else config)
    if not path.is_file():
        if config is None:
            return {}
        raise ConfigError(f"Configuration file not found: {path}")
    return read_env_file(path)


## @brief Build the notifier from the config file and environment and run it.
#
# @param argv Command line arguments, or None for sys.argv.
# @param environ Environment variables, or None for os.environ; they win over the
#     configuration file.
# @param sleep Waits between two checks; replaced in tests.
# @param smtp_factory Creates SMTP connections; replaced in tests.
# @param fetch Fetches JSON over HTTP; replaced in tests.
# @param max_checks Stop after this many checks; None means run until Ctrl+C.
# @param cwd Directory of the default and relative config file; None for the
#     current directory.
# @return Process exit code: 0 after a clean stop, 2 for a configuration error.
def main(
    argv: Sequence[str] | None = None,
    environ: Mapping[str, str] | None = None,
    *,
    sleep: Callable[[float], None] = time.sleep,
    smtp_factory: Callable[..., AbstractContextManager[SmtpSession]] = smtplib.SMTP,
    fetch: JsonFetcher = fetch_json,
    max_checks: int | None = None,
    cwd: Path | None = None,
) -> int:
    """Build the notifier from the config file and environment and run it."""
    args = _parse_args(argv)
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    try:
        values = {
            **_read_config_file(args.config, Path.cwd() if cwd is None else cwd),
            **(os.environ if environ is None else environ),
        }
        settings = load_settings(values)
    except ConfigError as error:
        _LOGGER.error("Configuration error: %s", error)
        return EXIT_CONFIG_ERROR
    home = settings.home
    if home is None:
        try:
            home = GeojsIpLocationClient(fetch).home_position()
        except PositionGuessError as error:
            _LOGGER.error("Configuration error: %s", error)
            return EXIT_CONFIG_ERROR
        _LOGGER.info("Home position guessed from the public IP address")
    check = IssOverheadCheck(
        position_provider=OpenNotifyIssClient(fetch),
        daylight_provider=SunriseSunsetClient(fetch),
        notifier=SmtpNotifier(settings, smtp_factory),
        clock=SystemClock(),
        home=home,
    )
    try:
        run_monitor(check.run_once, sleep, max_checks=max_checks)
    except KeyboardInterrupt:
        _LOGGER.info("Notifier stopped")
    return EXIT_OK
