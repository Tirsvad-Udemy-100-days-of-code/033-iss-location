"""@brief Fixed values shared by the notifier: URLs, limits, names and texts."""

from typing import Final

## @brief Endpoint that returns the current ISS position.
ISS_NOW_URL: Final[str] = "http://api.open-notify.org/iss-now.json"

## @brief Endpoint that returns sunrise and sunset for a position.
SUNRISE_SUNSET_URL: Final[str] = "https://api.sunrise-sunset.org/json"

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

## @brief Subject line of the notification e-mail.
EMAIL_SUBJECT: Final[str] = "Look up! The ISS is overhead"

## @brief Body of the notification e-mail.
EMAIL_BODY: Final[str] = (
    "The International Space Station is above you right now and it is dark. Look up!"
)
