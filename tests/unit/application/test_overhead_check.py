from iss_notifier.application.overhead_check import IssOverheadCheck
from iss_notifier.constants import EMAIL_BODY, EMAIL_SUBJECT
from iss_notifier.domain.models import DaylightHours, GeoPosition

HOME = GeoPosition(50.0, 10.0)


class FakePositions:
    def __init__(self, position: GeoPosition) -> None:
        self.position = position

    def current_position(self) -> GeoPosition:
        return self.position


class FakeDaylight:
    def __init__(self, daylight: DaylightHours) -> None:
        self.daylight = daylight
        self.calls = 0

    def daylight_hours(self, home: GeoPosition) -> DaylightHours:
        self.calls += 1
        return self.daylight


class FakeNotifier:
    def __init__(self) -> None:
        self.sent: list[tuple[str, str]] = []

    def send(self, subject: str, body: str) -> None:
        self.sent.append((subject, body))


class FakeClock:
    def __init__(self, hour: int) -> None:
        self.hour = hour

    def current_hour(self) -> int:
        return self.hour


def _check(
    iss: GeoPosition, hour: int
) -> tuple[IssOverheadCheck, FakeNotifier, FakeDaylight]:
    notifier = FakeNotifier()
    daylight = FakeDaylight(DaylightHours(6, 18))
    check = IssOverheadCheck(
        FakePositions(iss), daylight, notifier, FakeClock(hour), HOME
    )
    return check, notifier, daylight


def test_run_once_sends_one_message_when_overhead_at_night() -> None:
    check, notifier, _ = _check(GeoPosition(52.0, 12.0), hour=23)
    assert check.run_once() is True
    assert notifier.sent == [(EMAIL_SUBJECT, EMAIL_BODY)]


def test_run_once_sends_nothing_when_overhead_by_day() -> None:
    check, notifier, _ = _check(GeoPosition(52.0, 12.0), hour=12)
    assert check.run_once() is False
    assert notifier.sent == []


def test_run_once_sends_nothing_when_far_away_at_night() -> None:
    check, notifier, daylight = _check(GeoPosition(-30.0, 100.0), hour=23)
    assert check.run_once() is False
    assert notifier.sent == []
    assert daylight.calls == 0
