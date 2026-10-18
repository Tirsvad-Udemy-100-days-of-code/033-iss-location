"""@brief Client of the Open Notify API that reports the ISS position."""

from iss_notifier.constants import ISS_NOW_URL
from iss_notifier.domain.errors import PositionUnavailableError, RemoteRequestError
from iss_notifier.domain.models import GeoPosition
from iss_notifier.infrastructure.http_json import JsonFetcher, fetch_json


## @brief Reads the current ISS position from the Open Notify API.
class OpenNotifyIssClient:
    """Reads the current ISS position from the Open Notify API."""

    ## @brief Create the client.
    #
    # @param fetch Function that fetches JSON; replaced in tests.
    def __init__(self, fetch: JsonFetcher = fetch_json) -> None:
        """Create the client."""
        ## @brief Function that fetches JSON.
        self._fetch = fetch

    ## @brief Get the current ISS position.
    #
    # @return The position of the ISS now.
    # @throws PositionUnavailableError when the call fails or the reply is bad.
    def current_position(self) -> GeoPosition:
        """Get the current ISS position."""
        try:
            data = self._fetch(ISS_NOW_URL, None)
            position = data["iss_position"]
            return GeoPosition(
                latitude=float(position["latitude"]),
                longitude=float(position["longitude"]),
            )
        except RemoteRequestError as error:
            raise PositionUnavailableError(str(error)) from error
        except (KeyError, TypeError, ValueError) as error:
            raise PositionUnavailableError("unexpected ISS response") from error
