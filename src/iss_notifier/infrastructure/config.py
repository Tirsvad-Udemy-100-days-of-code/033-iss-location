"""@brief Settings read from environment variables. No .env file is loaded."""

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field

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
from iss_notifier.domain.models import GeoPosition


## @brief Configuration of the notifier. Private fields are kept out of repr.
@dataclass(frozen=True, slots=True)
class Settings:
    """Configuration of the notifier. Private fields are kept out of repr."""

    ## @brief Position of the observer.
    home: GeoPosition = field(repr=False)

    ## @brief SMTP server host name.
    smtp_host: str

    ## @brief SMTP server port.
    smtp_port: int

    ## @brief SMTP account name, also used as the sender address.
    smtp_user: str = field(repr=False)

    ## @brief SMTP account password.
    smtp_password: str = field(repr=False)

    ## @brief Recipient address of the notification.
    mail_to: str = field(repr=False)


## @brief Read a variable that must be set and not blank.
#
# @param environ Mapping of variable names to values.
# @param name Name of the variable.
# @return The stripped value.
# @throws ConfigError when the variable is missing or blank.
def _require(environ: Mapping[str, str], name: str) -> str:
    value = environ.get(name, "").strip()
    if not value:
        raise ConfigError(f"missing environment variable {name}")
    return value


## @brief Read a required numeric variable.
#
# @param environ Mapping of variable names to values.
# @param name Name of the variable.
# @param convert Conversion of the text to a number, such as int or float.
# @return The converted value.
# @throws ConfigError when the variable is missing or not a number.
def _number(
    environ: Mapping[str, str], name: str, convert: Callable[[str], float]
) -> float:
    try:
        return convert(_require(environ, name))
    except ValueError:
        raise ConfigError(f"invalid value in environment variable {name}") from None


## @brief Read the settings from environment variables.
#
# @param environ Mapping of variable names to values, such as os.environ.
# @return The validated settings.
# @throws ConfigError when a variable is missing or invalid. The message names
#     the variable and never echoes a value.
def load_settings(environ: Mapping[str, str]) -> Settings:
    """Read the settings from environment variables."""
    latitude = _number(environ, ENV_LATITUDE, float)
    longitude = _number(environ, ENV_LONGITUDE, float)
    try:
        home = GeoPosition(latitude, longitude)
    except ValueError:
        raise ConfigError(
            f"{ENV_LATITUDE} or {ENV_LONGITUDE} is out of range"
        ) from None
    port = (
        int(_number(environ, ENV_SMTP_PORT, int))
        if environ.get(ENV_SMTP_PORT, "").strip()
        else SMTP_DEFAULT_PORT
    )
    return Settings(
        home=home,
        smtp_host=_require(environ, ENV_SMTP_HOST),
        smtp_port=port,
        smtp_user=_require(environ, ENV_SMTP_USER),
        smtp_password=_require(environ, ENV_SMTP_PASSWORD),
        mail_to=_require(environ, ENV_MAIL_TO),
    )
