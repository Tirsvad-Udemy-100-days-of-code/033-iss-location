import dataclasses

import pytest

from iss_notifier.domain.models import DaylightHours, GeoPosition


@pytest.mark.parametrize("latitude", [-90.1, 91.0])
def test_geo_position_rejects_latitude_out_of_range(latitude: float) -> None:
    with pytest.raises(ValueError, match="latitude"):
        GeoPosition(latitude, 0.0)


@pytest.mark.parametrize("longitude", [-180.1, 181.0])
def test_geo_position_rejects_longitude_out_of_range(longitude: float) -> None:
    with pytest.raises(ValueError, match="longitude"):
        GeoPosition(0.0, longitude)


def test_geo_position_accepts_the_extremes() -> None:
    assert GeoPosition(-90.0, 180.0).longitude == 180.0


def test_geo_position_is_immutable() -> None:
    position = GeoPosition(1.0, 2.0)
    with pytest.raises(dataclasses.FrozenInstanceError):
        position.latitude = 3.0  # type: ignore[misc]


@pytest.mark.parametrize("hours", [(-1, 5), (5, 24)])
def test_daylight_hours_rejects_hour_out_of_range(hours: tuple[int, int]) -> None:
    with pytest.raises(ValueError, match="hour"):
        DaylightHours(*hours)
