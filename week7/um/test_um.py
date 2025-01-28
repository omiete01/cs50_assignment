# testing um.py

import pytest
from um import count

def test_count():
    assert count("um") == 1
    assert count("rum") == 0
    assert count("UM") == 1
    assert count("um, thanks, um...") == 2
    assert count("Hello, um, mummy, um?...") == 2
