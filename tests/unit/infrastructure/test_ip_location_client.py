from collections.abc import Mapping
from typing import Any

import pytest

from iss_notifier.constants import GEOLOCATION_URL
from iss_notifier.domain.errors import PositionGuessError, RemoteRequestError
from iss_notifier.domain.models import GeoPosition
from iss_notifier.infrastructure.ip_location_client import GeojsIpLocationClient

RECORDED = {
    "ip": "203.0.113.9",
    "country": "Testland",
    "latitude": "55.6759",
    "longitude": "12.5655",
    "accuracy": 20,
}


def test_home_position_parses_the_recorded_response() -> None:
    urls: list[str] = []

    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        urls.append(url)
        return RECORDED

    assert GeojsIpLocationClient(fetch).home_position() == GeoPosition(55.6759, 12.5655)
    assert urls == [GEOLOCATION_URL]


def test_home_position_wraps_a_failed_request() -> None:
    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        raise RemoteRequestError("request failed: URLError")

    with pytest.raises(PositionGuessError) as info:
        GeojsIpLocationClient(fetch).home_position()
    assert isinstance(info.value.__cause__, RemoteRequestError)
    assert GEOLOCATION_URL not in str(info.value)


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"latitude": "1"},
        {"longitude": "1"},
        {"latitude": "x", "longitude": "2"},
        {"latitude": None, "longitude": "2"},
        {"latitude": "95", "longitude": "2"},
        {"latitude": "1", "longitude": "181"},
    ],
)
def test_home_position_rejects_a_malformed_response(payload: dict[str, Any]) -> None:
    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        return payload

    with pytest.raises(PositionGuessError):
        GeojsIpLocationClient(fetch).home_position()
