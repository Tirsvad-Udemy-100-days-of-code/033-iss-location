"""@brief Errors raised by the notifier. None of their messages holds a secret."""


## @brief Base class of every error the notifier raises on purpose.
class IssNotifierError(Exception):
    """Base class of every error the notifier raises on purpose."""


## @brief A request to a remote HTTP service failed or returned bad data.
class RemoteRequestError(IssNotifierError):
    """A request to a remote HTTP service failed or returned bad data."""


## @brief The current ISS position could not be obtained.
class PositionUnavailableError(IssNotifierError):
    """The current ISS position could not be obtained."""


## @brief The home position could not be guessed from the public IP address.
class PositionGuessError(IssNotifierError):
    """The home position could not be guessed from the public IP address."""


## @brief The sunrise and sunset hours could not be obtained.
class DaylightUnavailableError(IssNotifierError):
    """The sunrise and sunset hours could not be obtained."""


## @brief The notification e-mail could not be sent.
class NotificationError(IssNotifierError):
    """The notification e-mail could not be sent."""


## @brief The configuration is missing or invalid.
class ConfigError(IssNotifierError):
    """The configuration is missing or invalid."""
