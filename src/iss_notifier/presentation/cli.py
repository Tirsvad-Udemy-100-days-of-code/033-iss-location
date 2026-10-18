"""@brief Command line entry point and composition root."""

import argparse
import logging
import os
import smtplib
import time
from collections.abc import Callable, Mapping, Sequence
from contextlib import AbstractContextManager

from iss_notifier.application.monitor import run_monitor
from iss_notifier.application.overhead_check import IssOverheadCheck
from iss_notifier.constants import (
    CHECK_INTERVAL_SECONDS,
    EXIT_CONFIG_ERROR,
    EXIT_OK,
    LOG_FORMAT,
)
from iss_notifier.domain.errors import ConfigError
from iss_notifier.infrastructure.config import load_settings
from iss_notifier.infrastructure.http_json import JsonFetcher, fetch_json
from iss_notifier.infrastructure.iss_client import OpenNotifyIssClient
from iss_notifier.infrastructure.smtp_notifier import SmtpNotifier, SmtpSession
from iss_notifier.infrastructure.sun_client import SunriseSunsetClient
from iss_notifier.infrastructure.system_clock import SystemClock

## @brief Logger of this module.
_LOGGER = logging.getLogger(__name__)


## @brief Build the notifier from the environment and run it.
#
# @param argv Command line arguments, or None for sys.argv.
# @param environ Environment variables, or None for os.environ.
# @param sleep Waits between two checks; replaced in tests.
# @param smtp_factory Creates SMTP connections; replaced in tests.
# @param fetch Fetches JSON over HTTP; replaced in tests.
# @param max_checks Stop after this many checks; None means run until Ctrl+C.
# @return Process exit code: 0 after a clean stop, 2 for a configuration error.
def main(
    argv: Sequence[str] | None = None,
    environ: Mapping[str, str] | None = None,
    *,
    sleep: Callable[[float], None] = time.sleep,
    smtp_factory: Callable[..., AbstractContextManager[SmtpSession]] = smtplib.SMTP,
    fetch: JsonFetcher = fetch_json,
    max_checks: int | None = None,
) -> int:
    """Build the notifier from the environment and run it."""
    argparse.ArgumentParser(
        prog="iss-notifier",
        description=(
            "E-mail me when the ISS is overhead at night. "
            f"Checks every {CHECK_INTERVAL_SECONDS} seconds. "
            "Configure through environment variables."
        ),
    ).parse_args(argv)
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
    try:
        settings = load_settings(os.environ if environ is None else environ)
    except ConfigError as error:
        _LOGGER.error("Configuration error: %s", error)
        return EXIT_CONFIG_ERROR
    check = IssOverheadCheck(
        position_provider=OpenNotifyIssClient(fetch),
        daylight_provider=SunriseSunsetClient(fetch),
        notifier=SmtpNotifier(settings, smtp_factory),
        clock=SystemClock(),
        home=settings.home,
    )
    try:
        run_monitor(check.run_once, sleep, max_checks=max_checks)
    except KeyboardInterrupt:
        _LOGGER.info("Notifier stopped")
    return EXIT_OK
