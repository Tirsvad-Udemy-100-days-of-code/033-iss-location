"""@brief Client of the geojs.io API that guesses a position from the public IP."""

from iss_notifier.constants import GEOLOCATION_URL
from iss_notifier.domain.errors import PositionGuessError, RemoteRequestError
from iss_notifier.domain.models import GeoPosition
from iss_notifier.infrastructure.http_json import JsonFetcher, fetch_json


## @brief Guesses the observer position from the public IP address via geojs.io.
class GeojsIpLocationClient:
    """Guesses the observer position from the public IP address via geojs.io."""

    ## @brief Create the client.
    #
    # @param fetch Function that fetches JSON; replaced in tests.
    def __init__(self, fetch: JsonFetcher = fetch_json) -> None:
        """Create the client."""
        ## @brief Function that fetches JSON.
        self._fetch = fetch

    ## @brief Get the position of the public IP address.
    #
    # @return The guessed position.
    # @throws PositionGuessError when the call fails or the reply is bad.
    def home_position(self) -> GeoPosition:
        """Get the position of the public IP address."""
        try:
            data = self._fetch(GEOLOCATION_URL, None)
            return GeoPosition(
                latitude=float(data["latitude"]),
                longitude=float(data["longitude"]),
            )
        except RemoteRequestError as error:
            raise PositionGuessError(str(error)) from error
        except (KeyError, TypeError, ValueError) as error:
            raise PositionGuessError("unexpected geolocation response") from error
