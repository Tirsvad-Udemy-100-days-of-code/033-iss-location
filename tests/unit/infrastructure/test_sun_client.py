from collections.abc import Mapping
from typing import Any

import pytest

from iss_notifier.constants import SUNRISE_SUNSET_URL
from iss_notifier.domain.errors import DaylightUnavailableError, RemoteRequestError
from iss_notifier.domain.models import DaylightHours, GeoPosition
from iss_notifier.infrastructure.sun_client import SunriseSunsetClient

HOME = GeoPosition(51.5, -0.25)
RECORDED = {
    "results": {
        "sunrise": "2026-10-19T05:12:33+00:00",
        "sunset": "2026-10-19T16:48:01+00:00",
        "day_length": 41728,
    },
    "status": "OK",
}


def test_daylight_hours_parses_utc_hours_and_sends_the_query() -> None:
    calls: list[tuple[str, Mapping[str, str] | None]] = []

    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        calls.append((url, params))
        return RECORDED

    assert SunriseSunsetClient(fetch).daylight_hours(HOME) == DaylightHours(5, 16)
    assert calls == [
        (SUNRISE_SUNSET_URL, {"lat": "51.5", "lng": "-0.25", "formatted": "0"})
    ]


def test_daylight_hours_converts_other_offsets_to_utc() -> None:
    payload = {
        "results": {
            "sunrise": "2026-10-19T23:30:00+02:00",
            "sunset": "2026-10-19T01:00:00-03:00",
        }
    }

    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        return payload

    assert SunriseSunsetClient(fetch).daylight_hours(HOME) == DaylightHours(21, 4)


def test_daylight_hours_wraps_a_failed_request() -> None:
    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        raise RemoteRequestError("request failed")

    with pytest.raises(DaylightUnavailableError):
        SunriseSunsetClient(fetch).daylight_hours(HOME)


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"results": {"sunrise": "2026-10-19T05:12:33+00:00"}},
        {"results": {"sunrise": "garbage", "sunset": "garbage"}},
        {"results": None},
    ],
)
def test_daylight_hours_rejects_a_malformed_response(payload: dict[str, Any]) -> None:
    def fetch(url: str, params: Mapping[str, str] | None) -> dict[str, Any]:
        return payload

    with pytest.raises(DaylightUnavailableError):
        SunriseSunsetClient(fetch).daylight_hours(HOME)
