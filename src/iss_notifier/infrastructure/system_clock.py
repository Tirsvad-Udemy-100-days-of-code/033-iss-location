"""@brief Clock backed by the operating system."""

from datetime import UTC, datetime


## @brief Tells the current UTC hour from the system time.
class SystemClock:
    """Tells the current UTC hour from the system time."""

    ## @brief Get the current hour.
    #
    # @return The hour in UTC, 0 to 23.
    def current_hour(self) -> int:
        """Get the current hour."""
        return datetime.now(UTC).hour
