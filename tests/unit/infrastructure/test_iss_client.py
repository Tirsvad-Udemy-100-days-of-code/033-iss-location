from collections.abc import Mapping
from typing import Any

import pytest

from iss_notifier.constants import ISS_NOW_URL
from iss_notifier.domain.errors import PositionUnavailableError, RemoteRequestError
from iss_notifier.domain.models import GeoPosition
from iss_notifier.infrastructure.iss_client import OpenNotifyIssClient

RECORDED = {
    "message": "success",
    "timestamp": 1760000000,
    "iss_position": {"latitude": "-12.3456", "longitude": "170.5"},
}


def test_current_position_parses_the_recorded_response() -> None:
    urls: list[str] = []

    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        urls.append(url)
        return RECORDED

    position = OpenNotifyIssClient(fetch).current_position()
    assert position == GeoPosition(-12.3456, 170.5)
    assert urls == [ISS_NOW_URL]


def test_current_position_wraps_a_failed_request() -> None:
    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        raise RemoteRequestError("request failed")

    with pytest.raises(PositionUnavailableError) as info:
        OpenNotifyIssClient(fetch).current_position()
    assert isinstance(info.value.__cause__, RemoteRequestError)


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"iss_position": {"latitude": "1"}},
        {"iss_position": {"latitude": "x", "longitude": "2"}},
        {"iss_position": {"latitude": "95", "longitude": "2"}},
        {"iss_position": None},
    ],
)
def test_current_position_rejects_a_malformed_response(
    payload: dict[str, Any],
) -> None:
    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        return payload

    with pytest.raises(PositionUnavailableError):
        OpenNotifyIssClient(fetch).current_position()
