"""@brief Value objects of the notifier: a position and the daylight hours."""

from dataclasses import dataclass

from iss_notifier.constants import (
    HOURS_PER_DAY,
    MAX_LATITUDE_DEGREES,
    MAX_LONGITUDE_DEGREES,
)


## @brief A point on Earth in degrees.
@dataclass(frozen=True, slots=True)
class GeoPosition:
    """A point on Earth in degrees."""

    ## @brief Latitude in degrees, from -90 to 90.
    latitude: float

    ## @brief Longitude in degrees, from -180 to 180.
    longitude: float

    ## @brief Reject coordinates outside the valid ranges.
    #
    # @return Nothing.
    # @throws ValueError when latitude or longitude is out of range.
    def __post_init__(self) -> None:
        """Reject coordinates outside the valid ranges."""
        latitude = self.latitude
        longitude = self.longitude
        if abs(latitude) > MAX_LATITUDE_DEGREES:
            raise ValueError("latitude out of range")
        if abs(longitude) > MAX_LONGITUDE_DEGREES:
            raise ValueError("longitude out of range")


## @brief The UTC hours of the day at which the sun rises and sets.
@dataclass(frozen=True, slots=True)
class DaylightHours:
    """The UTC hours of the day at which the sun rises and sets."""

    ## @brief UTC hour of sunrise, 0 to 23.
    sunrise_hour: int

    ## @brief UTC hour of sunset, 0 to 23.
    sunset_hour: int

    ## @brief Reject hours outside 0 to 23.
    #
    # @return Nothing.
    # @throws ValueError when an hour is out of range.
    def __post_init__(self) -> None:
        """Reject hours outside 0 to 23."""
        sunrise_hour = self.sunrise_hour
        sunset_hour = self.sunset_hour
        for hour in (sunrise_hour, sunset_hour):
            if not 0 <= hour < HOURS_PER_DAY:
                raise ValueError("hour out of range")
