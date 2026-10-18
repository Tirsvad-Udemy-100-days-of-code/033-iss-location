"""@brief The monitoring loop: check, survive failures, wait, repeat."""

import logging
from collections.abc import Callable

from iss_notifier.constants import CHECK_INTERVAL_SECONDS
from iss_notifier.domain.errors import IssNotifierError

## @brief Logger of this module.
_LOGGER = logging.getLogger(__name__)


## @brief Run the check repeatedly, waiting between two checks.
#
# A failed check is logged as a warning and the loop goes on.
#
# @param check_once Performs one check.
# @param sleep Waits for the given number of seconds.
# @param interval_seconds Seconds to wait after each check.
# @param max_checks Stop after this many checks; None means run forever.
# @return Nothing.
def run_monitor(
    check_once: Callable[[], bool],
    sleep: Callable[[float], None],
    interval_seconds: float = CHECK_INTERVAL_SECONDS,
    max_checks: int | None = None,
) -> None:
    """Run the check repeatedly, waiting between two checks."""
    checks_done = 0
    while max_checks is None or checks_done < max_checks:
        try:
            check_once()
        except IssNotifierError as error:
            _LOGGER.warning("Check failed (%s): %s", type(error).__name__, error)
        checks_done += 1
        sleep(interval_seconds)
