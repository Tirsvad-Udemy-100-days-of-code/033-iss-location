"""@brief Use case: notify when the ISS is overhead at night."""

import logging

from iss_notifier.application.ports import (
    Clock,
    DaylightProvider,
    IssPositionProvider,
    Notifier,
)
from iss_notifier.constants import EMAIL_BODY, EMAIL_SUBJECT
from iss_notifier.domain.models import GeoPosition
from iss_notifier.domain.rules import is_iss_overhead, is_night

## @brief Logger of this module.
_LOGGER = logging.getLogger(__name__)


## @brief Checks once whether to tell the user to look up.
class IssOverheadCheck:
    """Checks once whether to tell the user to look up."""

    ## @brief Create the use case.
    #
    # @param position_provider Source of the ISS position.
    # @param daylight_provider Source of sunrise and sunset hours.
    # @param notifier Channel used to send the message.
    # @param clock Source of the current hour.
    # @param home Position of the observer.
    def __init__(
        self,
        position_provider: IssPositionProvider,
        daylight_provider: DaylightProvider,
        notifier: Notifier,
        clock: Clock,
        home: GeoPosition,
    ) -> None:
        """Create the use case."""
        ## @brief Source of the ISS position.
        self._position_provider = position_provider
        ## @brief Source of sunrise and sunset hours.
        self._daylight_provider = daylight_provider
        ## @brief Channel used to send the message.
        self._notifier = notifier
        ## @brief Source of the current hour.
        self._clock = clock
        ## @brief Position of the observer.
        self._home = home

    ## @brief Check the ISS and notify when it is overhead at night.
    #
    # @return True when a notification was sent.
    # @throws IssNotifierError when a provider or the notifier fails.
    def run_once(self) -> bool:
        """Check the ISS and notify when it is overhead at night."""
        iss = self._position_provider.current_position()
        if not is_iss_overhead(iss, self._home):
            _LOGGER.info("ISS overhead: no")
            return False
        daylight = self._daylight_provider.daylight_hours(self._home)
        if not is_night(daylight, self._clock.current_hour()):
            _LOGGER.info("ISS overhead: yes, night: no")
            return False
        _LOGGER.info("ISS overhead: yes, night: yes")
        self._notifier.send(EMAIL_SUBJECT, EMAIL_BODY)
        return True
