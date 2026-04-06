import domain.valueObjects.postcode as postcode
import pytest


def test_valid_postcode():
    valid_postcode = "12345"
    pc = postcode.Postcode(valid_postcode)

    assert pc.postcode == valid_postcode


def test_empty_postcode():
    with pytest.raises(ValueError) as excinfo:
        postcode.Postcode("")
    assert str(excinfo.value) == "Postcode cannot be empty."


def test_exceeding_length_postcode():
    with pytest.raises(ValueError) as excinfo:
        long_postcode = "a" * 9  # 9 characters, exceeding the limit of 8
        postcode.Postcode(long_postcode)
    assert str(excinfo.value) == "Postcode cannot exceed 8 characters."
