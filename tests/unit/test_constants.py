from iss_notifier import constants


def test_check_interval_is_sixty_seconds() -> None:
    assert constants.CHECK_INTERVAL_SECONDS == 60


def test_position_margin_is_five_degrees() -> None:
    assert constants.POSITION_MARGIN_DEGREES == 5.0


def test_env_names_share_the_notifier_prefix() -> None:
    names = [v for k, v in vars(constants).items() if k.startswith("ENV_")]
    assert names
    assert all(name.startswith("ISS_NOTIFIER_") for name in names)
