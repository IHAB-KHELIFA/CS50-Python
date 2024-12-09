from working import convert
import pytest

def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1 PM to 1 AM") == "13:00 to 01:00"
    assert convert("12:30 AM to 12:45 PM") == "00:30 to 12:45"

def test_invalid_times():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")  # Invalid hour
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")   # Invalid minute
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")            # Missing "to"
    with pytest.raises(ValueError):
        convert("9 AM to")              # Incomplete input
    with pytest.raises(ValueError):
        convert("10 PM - 8 AM")         # Incorrect format

def test_edge_cases():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
