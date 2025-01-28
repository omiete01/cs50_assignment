import pytest
from refuel import convert, gauge

def test_convert():
    assert convert("4/5") == 80

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"

# if user puts 0 as second value, a zerodivisionerror will be raised
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_value_error():
    with pytest.raises(ValueError):
        convert("5/2")
