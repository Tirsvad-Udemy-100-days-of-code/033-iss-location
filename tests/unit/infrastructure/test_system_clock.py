from iss_notifier.infrastructure.system_clock import SystemClock


def test_current_hour_is_a_valid_hour() -> None:
    assert 0 <= SystemClock().current_hour() <= 23
