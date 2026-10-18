import pytest

from iss_notifier import is_iss_overhead, is_night
from iss_notifier.domain.models import DaylightHours, GeoPosition

HOME = GeoPosition(51.5, -0.1)


def test_is_iss_overhead_true_when_within_margin() -> None:
    assert is_iss_overhead(GeoPosition(54.0, 3.0), HOME)


def test_is_iss_overhead_true_on_the_margin_edge() -> None:
    assert is_iss_overhead(GeoPosition(56.5, 4.9), HOME)


@pytest.mark.parametrize(
    "iss",
    [GeoPosition(56.6, -0.1), GeoPosition(51.5, 5.0), GeoPosition(-40.0, 100.0)],
)
def test_is_iss_overhead_false_when_outside_margin(iss: GeoPosition) -> None:
    assert not is_iss_overhead(iss, HOME)


def test_is_iss_overhead_true_across_the_date_line() -> None:
    home = GeoPosition(10.0, 179.0)
    assert is_iss_overhead(GeoPosition(10.0, -178.0), home)
    assert is_iss_overhead(home, GeoPosition(10.0, -178.0))


def test_is_iss_overhead_false_across_the_date_line_when_far() -> None:
    assert not is_iss_overhead(GeoPosition(10.0, -170.0), GeoPosition(10.0, 179.0))


def test_is_iss_overhead_uses_custom_margin() -> None:
    assert not is_iss_overhead(GeoPosition(54.0, 0.0), HOME, margin=1.0)


@pytest.mark.parametrize("hour", [0, 4, 5])
def test_is_night_true_before_sunrise(hour: int) -> None:
    assert is_night(DaylightHours(6, 18), hour)


@pytest.mark.parametrize("hour", [18, 19, 23])
def test_is_night_true_from_sunset(hour: int) -> None:
    assert is_night(DaylightHours(6, 18), hour)


@pytest.mark.parametrize("hour", [6, 12, 17])
def test_is_night_false_between_sunrise_and_sunset(hour: int) -> None:
    assert not is_night(DaylightHours(6, 18), hour)


@pytest.mark.parametrize("hour", [2, 10, 20])
def test_is_night_true_when_sunrise_after_sunset_in_utc(hour: int) -> None:
    assert is_night(DaylightHours(21, 2), hour)


@pytest.mark.parametrize("hour", [21, 23, 0, 1])
def test_is_night_false_in_the_day_when_sunrise_after_sunset_in_utc(
    hour: int,
) -> None:
    assert not is_night(DaylightHours(21, 2), hour)
