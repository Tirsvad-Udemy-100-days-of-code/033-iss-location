"""@brief ISS Overhead Notifier: e-mails you when the ISS is overhead at night."""

from iss_notifier.domain.rules import is_iss_overhead, is_night

## @brief Package version.
__version__ = "0.1.0"

## @brief Public names of the package.
__all__ = ["__version__", "is_iss_overhead", "is_night"]
