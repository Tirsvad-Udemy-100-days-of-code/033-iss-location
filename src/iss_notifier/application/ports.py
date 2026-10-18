"""@brief Ports: what the use case needs from the outside world."""

from typing import Protocol

from iss_notifier.domain.models import DaylightHours, GeoPosition


## @brief Source of the current ISS position.
class IssPositionProvider(Protocol):
    """Source of the current ISS position."""

    ## @brief Get the current ISS position.
    #
    # @return The position of the ISS now.
    # @throws PositionUnavailableError when it cannot be obtained.
    def current_position(self) -> GeoPosition:
        """Get the current ISS position."""
        ...


## @brief Source of sunrise and sunset hours.
class DaylightProvider(Protocol):
    """Source of sunrise and sunset hours."""

    ## @brief Get the sunrise and sunset hours of the day.
    #
    # @param home Position of the observer.
    # @return The sunrise and sunset hours in UTC.
    # @throws DaylightUnavailableError when they cannot be obtained.
    def daylight_hours(self, home: GeoPosition) -> DaylightHours:
        """Get the sunrise and sunset hours of the day."""
        ...


## @brief Channel that tells the user something.
class Notifier(Protocol):
    """Channel that tells the user something."""

    ## @brief Send one message.
    #
    # @param subject Subject line.
    # @param body Message text.
    # @return Nothing.
    # @throws NotificationError when the message cannot be sent.
    def send(self, subject: str, body: str) -> None:
        """Send one message."""
        ...


## @brief Source of the current time.
class Clock(Protocol):
    """Source of the current time."""

    ## @brief Get the current hour.
    #
    # @return The hour in UTC, 0 to 23.
    def current_hour(self) -> int:
        """Get the current hour."""
        ...
