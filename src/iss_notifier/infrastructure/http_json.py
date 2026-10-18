"""@brief Small HTTP GET helper that returns decoded JSON."""

import json
import urllib.parse
import urllib.request
from collections.abc import Callable, Mapping
from typing import Any

from iss_notifier.constants import HTTP_TIMEOUT_SECONDS
from iss_notifier.domain.errors import RemoteRequestError

## @brief Signature of a function that fetches a JSON object from a URL.
# Any: the decoded JSON of a remote service has no static shape.
JsonFetcher = Callable[[str, Mapping[str, str] | None], dict[str, Any]]


## @brief Fetch a URL with GET and decode the JSON object in the response.
#
# @param url Address to request.
# @param params Query parameters, or None.
# @param timeout Seconds to wait for the server.
# @param opener Function that opens a URL; replaced in tests.
# @return The decoded JSON object.
# @throws RemoteRequestError when the request fails or the body is not an object.
def fetch_json(
    url: str,
    params: Mapping[str, str] | None = None,
    timeout: float = HTTP_TIMEOUT_SECONDS,
    opener: Callable[..., Any] = urllib.request.urlopen,
) -> dict[str, Any]:
    """Fetch a URL with GET and decode the JSON object in the response."""
    full_url = f"{url}?{urllib.parse.urlencode(params)}" if params else url
    try:
        with opener(full_url, timeout=timeout) as response:
            data = json.loads(response.read())
    except (OSError, ValueError) as error:
        # The URL is left out of the message: it can hold the home position.
        raise RemoteRequestError(f"request failed: {type(error).__name__}") from error
    if not isinstance(data, dict):
        raise RemoteRequestError("response is not a JSON object")
    return data
