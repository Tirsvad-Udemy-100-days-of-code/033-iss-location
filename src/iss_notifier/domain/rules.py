"""@brief Business rules: is the ISS overhead, and is it night."""

from iss_notifier.constants import FULL_CIRCLE_DEGREES, POSITION_MARGIN_DEGREES
from iss_notifier.domain.models import DaylightHours, GeoPosition


## @brief Shortest distance in degrees between two longitudes, across the date line.
#
# @param first First longitude.
# @param second Second longitude.
# @return The distance, 0 to 180.
def _longitude_distance(first: float, second: float) -> float:
    difference = abs(first - second)
    return min(difference, FULL_CIRCLE_DEGREES - difference)


## @brief Tell whether the ISS is within a margin of the home position.
#
# Longitude differences wrap around the date line at 180 degrees.
#
# @param iss Current position of the ISS.
# @param home Position of the observer.
# @param margin Largest accepted difference in degrees, per axis.
# @return True when latitude and longitude both differ by at most the margin.
def is_iss_overhead(
    iss: GeoPosition,
    home: GeoPosition,
    margin: float = POSITION_MARGIN_DEGREES,
) -> bool:
    """Tell whether the ISS is within a margin of the home position."""
    latitude_close = abs(iss.latitude - home.latitude) <= margin
    longitude_close = _longitude_distance(iss.longitude, home.longitude) <= margin
    return latitude_close and longitude_close


## @brief Tell whether it is night at the given UTC hour.
#
# It is night from the sunset hour up to the sunrise hour. When the sunrise
# hour is after the sunset hour (possible in UTC) the night does not cross
# midnight.
#
# @param daylight Sunrise and sunset hours in UTC.
# @param current_hour Current hour in UTC, 0 to 23.
# @return True when the sun is down.
def is_night(daylight: DaylightHours, current_hour: int) -> bool:
    """Tell whether it is night at the given UTC hour."""
    if daylight.sunrise_hour > daylight.sunset_hour:
        return daylight.sunset_hour <= current_hour < daylight.sunrise_hour
    return current_hour < daylight.sunrise_hour or current_hour >= daylight.sunset_hour
