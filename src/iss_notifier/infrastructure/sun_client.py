"""@brief Client of the Sunrise-Sunset API."""

from datetime import UTC, datetime

from iss_notifier.constants import SUNRISE_SUNSET_URL
from iss_notifier.domain.errors import DaylightUnavailableError, RemoteRequestError
from iss_notifier.domain.models import DaylightHours, GeoPosition
from iss_notifier.infrastructure.http_json import JsonFetcher, fetch_json


## @brief Hour in UTC of an ISO 8601 timestamp.
#
# @param timestamp Timestamp with an offset, such as 2026-10-19T05:12:33+00:00.
# @return The hour, 0 to 23.
def _utc_hour(timestamp: str) -> int:
    return datetime.fromisoformat(timestamp).astimezone(UTC).hour


## @brief Reads sunrise and sunset hours from the Sunrise-Sunset API.
class SunriseSunsetClient:
    """Reads sunrise and sunset hours from the Sunrise-Sunset API."""

    ## @brief Create the client.
    #
    # @param fetch Function that fetches JSON; replaced in tests.
    def __init__(self, fetch: JsonFetcher = fetch_json) -> None:
        """Create the client."""
        ## @brief Function that fetches JSON.
        self._fetch = fetch

    ## @brief Get the sunrise and sunset hours of the day.
    #
    # @param home Position of the observer.
    # @return The sunrise and sunset hours in UTC.
    # @throws DaylightUnavailableError when the call fails or the reply is bad.
    def daylight_hours(self, home: GeoPosition) -> DaylightHours:
        """Get the sunrise and sunset hours of the day."""
        params = {
            "lat": str(home.latitude),
            "lng": str(home.longitude),
            "formatted": "0",
        }
        try:
            results = self._fetch(SUNRISE_SUNSET_URL, params)["results"]
            return DaylightHours(
                sunrise_hour=_utc_hour(results["sunrise"]),
                sunset_hour=_utc_hour(results["sunset"]),
            )
        except RemoteRequestError as error:
            raise DaylightUnavailableError(str(error)) from error
        except (KeyError, TypeError, ValueError) as error:
            raise DaylightUnavailableError("unexpected sunrise response") from error
