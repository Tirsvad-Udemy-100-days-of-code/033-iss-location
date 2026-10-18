"""@brief Fixed values shared by the notifier: URLs, limits, names and texts."""

from typing import Final

## @brief Endpoint that returns the current ISS position.
ISS_NOW_URL: Final[str] = "http://api.open-notify.org/iss-now.json"

## @brief Endpoint that returns sunrise and sunset for a position.
SUNRISE_SUNSET_URL: Final[str] = "https://api.sunrise-sunset.org/json"

## @brief Endpoint that returns the position of the caller's public IP address.
GEOLOCATION_URL: Final[str] = "https://get.geojs.io/v1/ip/geo.json"

## @brief User-Agent sent with every HTTP request.
# Some services (get.geojs.io) answer 403 to urllib's default agent. The version
# is written here and not read from the package, to avoid an import cycle.
USER_AGENT: Final[str] = (
    "iss-overhead-notifier/0.1.0 "
    "(+https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/033-iss-location)"
)

## @brief Name of the configuration file read when --config is not given.
DEFAULT_CONFIG_FILE: Final[str] = "config.env"

## @brief Seconds between two checks.
CHECK_INTERVAL_SECONDS: Final[int] = 60

## @brief Degrees of latitude and longitude within which the ISS counts as overhead.
POSITION_MARGIN_DEGREES: Final[float] = 5.0

## @brief Timeout in seconds for every HTTP request.
HTTP_TIMEOUT_SECONDS: Final[int] = 10

## @brief SMTP port used when none is configured.
SMTP_DEFAULT_PORT: Final[int] = 587

## @brief Environment variable holding the observer latitude.
ENV_LATITUDE: Final[str] = "ISS_NOTIFIER_LATITUDE"

## @brief Environment variable holding the observer longitude.
ENV_LONGITUDE: Final[str] = "ISS_NOTIFIER_LONGITUDE"

## @brief Environment variable holding the SMTP host.
ENV_SMTP_HOST: Final[str] = "ISS_NOTIFIER_SMTP_HOST"

## @brief Environment variable holding the SMTP port.
ENV_SMTP_PORT: Final[str] = "ISS_NOTIFIER_SMTP_PORT"

## @brief Environment variable holding the SMTP user.
ENV_SMTP_USER: Final[str] = "ISS_NOTIFIER_SMTP_USER"

## @brief Environment variable holding the SMTP password.
ENV_SMTP_PASSWORD: Final[str] = "ISS_NOTIFIER_SMTP_PASSWORD"

## @brief Environment variable holding the recipient address.
ENV_MAIL_TO: Final[str] = "ISS_NOTIFIER_MAIL_TO"

## @brief Largest absolute latitude in degrees.
MAX_LATITUDE_DEGREES: Final[float] = 90.0

## @brief Largest absolute longitude in degrees.
MAX_LONGITUDE_DEGREES: Final[float] = 180.0

## @brief Degrees in a full circle, used to wrap longitude differences.
FULL_CIRCLE_DEGREES: Final[float] = 360.0

## @brief Number of hours in a day; valid hours are 0 to this value minus one.
HOURS_PER_DAY: Final[int] = 24

## @brief Timeout in seconds for the SMTP connection.
SMTP_TIMEOUT_SECONDS: Final[int] = 30

## @brief Format of every log line.
LOG_FORMAT: Final[str] = "%(asctime)s %(levelname)s %(name)s: %(message)s"

## @brief Process exit code for a clean run.
EXIT_OK: Final[int] = 0

## @brief Process exit code when the configuration is missing or invalid.
EXIT_CONFIG_ERROR: Final[int] = 2

## @brief Subject line of the notification e-mail.
EMAIL_SUBJECT: Final[str] = "Look up! The ISS is overhead"

## @brief Body of the notification e-mail.
EMAIL_BODY: Final[str] = (
    "The International Space Station is above you right now and it is dark. Look up!"
)
