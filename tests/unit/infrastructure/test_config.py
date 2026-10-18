import pytest

from iss_notifier.constants import (
    ENV_LATITUDE,
    ENV_LONGITUDE,
    ENV_MAIL_TO,
    ENV_SMTP_HOST,
    ENV_SMTP_PASSWORD,
    ENV_SMTP_PORT,
    ENV_SMTP_USER,
    SMTP_DEFAULT_PORT,
)
from iss_notifier.domain.errors import ConfigError
from iss_notifier.infrastructure.config import load_settings

ENVIRON = {
    ENV_LATITUDE: "51.5",
    ENV_LONGITUDE: "-0.1",
    ENV_SMTP_HOST: "smtp.example.test",
    ENV_SMTP_PORT: "2525",
    ENV_SMTP_USER: "me@example.test",
    ENV_SMTP_PASSWORD: "s3cret-value",
    ENV_MAIL_TO: "you@example.test",
}


COORDINATES = (ENV_LATITUDE, ENV_LONGITUDE)


def test_load_settings_reads_every_variable() -> None:
    settings = load_settings(ENVIRON)
    assert settings.home is not None
    assert settings.home.latitude == 51.5
    assert settings.home.longitude == -0.1
    assert settings.smtp_host == "smtp.example.test"
    assert settings.smtp_port == 2525
    assert settings.smtp_user == "me@example.test"
    assert settings.smtp_password == "s3cret-value"
    assert settings.mail_to == "you@example.test"


def test_load_settings_uses_default_port_when_unset() -> None:
    environ = {k: v for k, v in ENVIRON.items() if k != ENV_SMTP_PORT}
    assert load_settings(environ).smtp_port == SMTP_DEFAULT_PORT


def test_load_settings_leaves_home_unset_when_both_coordinates_are_absent() -> None:
    environ = {k: v for k, v in ENVIRON.items() if k not in COORDINATES}
    assert load_settings(environ).home is None


def test_load_settings_treats_two_blank_coordinates_as_absent() -> None:
    environ = {**ENVIRON, ENV_LATITUDE: "", ENV_LONGITUDE: "  "}
    assert load_settings(environ).home is None


@pytest.mark.parametrize("present", COORDINATES)
@pytest.mark.parametrize("blank", [False, True])
def test_load_settings_rejects_a_single_coordinate_naming_both(
    present: str, blank: bool
) -> None:
    environ = {k: v for k, v in ENVIRON.items() if k not in COORDINATES}
    environ[present] = "12.5"
    for name in COORDINATES:
        if blank and name != present:
            environ[name] = " "
    with pytest.raises(ConfigError) as info:
        load_settings(environ)
    assert ENV_LATITUDE in str(info.value)
    assert ENV_LONGITUDE in str(info.value)
    assert "12.5" not in str(info.value)


@pytest.mark.parametrize(
    "name",
    [
        ENV_SMTP_HOST,
        ENV_SMTP_USER,
        ENV_SMTP_PASSWORD,
        ENV_MAIL_TO,
    ],
)
def test_load_settings_names_the_missing_variable(name: str) -> None:
    environ = {k: v for k, v in ENVIRON.items() if k != name}
    with pytest.raises(ConfigError, match=name):
        load_settings(environ)


def test_load_settings_treats_a_blank_value_as_missing() -> None:
    with pytest.raises(ConfigError, match=ENV_SMTP_HOST):
        load_settings({**ENVIRON, ENV_SMTP_HOST: "  "})


def test_load_settings_rejects_a_non_numeric_value_without_echoing_it() -> None:
    with pytest.raises(ConfigError) as info:
        load_settings({**ENVIRON, ENV_LATITUDE: "north-ish"})
    assert ENV_LATITUDE in str(info.value)
    assert "north-ish" not in str(info.value)


def test_load_settings_rejects_a_non_numeric_port() -> None:
    with pytest.raises(ConfigError, match=ENV_SMTP_PORT):
        load_settings({**ENVIRON, ENV_SMTP_PORT: "abc"})


def test_load_settings_rejects_coordinates_out_of_range() -> None:
    with pytest.raises(ConfigError, match="out of range"):
        load_settings({**ENVIRON, ENV_LATITUDE: "123"})


def test_settings_repr_hides_secrets_and_position() -> None:
    text = repr(load_settings(ENVIRON))
    for hidden in ("s3cret-value", "me@example.test", "you@example.test", "51.5"):
        assert hidden not in text
