import pytest
from fuel import convert, gauge

# Test cases for convert function
def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("3/2")  # X > Y should raise ValueError

def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")  # Y = 0 should raise ZeroDivisionError

def test_convert_non_integer():
    with pytest.raises(ValueError):
        convert("a/b")  # Non-integer input should raise ValueError
    with pytest.raises(ValueError):
        convert("1.5/3")  # Non-integer input should raise ValueError

# Test cases for gauge function
def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
