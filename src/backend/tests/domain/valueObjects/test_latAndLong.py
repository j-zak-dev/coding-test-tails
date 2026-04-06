import domain.valueObjects.latAndLong as latAndLong
import pytest


def test_valid_lat_and_long():
    valid_lat = 40.7128
    valid_long = -74.0060
    lat_long = latAndLong.LatAndLong(valid_lat, valid_long)

    assert lat_long.latitude == valid_lat
    assert lat_long.longitude == valid_long


def test_invalid_lat_and_long():
    with pytest.raises(ValueError) as excinfo:
        latAndLong.LatAndLong(None, None)
    assert str(excinfo.value) == "Latitude or Longitude cannot be empty."

    with pytest.raises(ValueError) as excinfo:
        latAndLong.LatAndLong(100.0, 43.0)  # Invalid latitude
    assert str(excinfo.value) == "Latitude must be between -90 and 90 degrees."

    with pytest.raises(ValueError) as excinfo:
        latAndLong.LatAndLong(40.0, 200.0)  # Invalid longitude
    assert str(excinfo.value) == "Longitude must be between -180 and 180 degrees."


def test_lat_and_long_values():
    valid_lat = 40.7128
    valid_long = -74.0060
    lat_long = latAndLong.LatAndLong(valid_lat, valid_long)

    assert lat_long.values() == [valid_lat, valid_long]
