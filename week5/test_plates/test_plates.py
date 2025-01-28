from plates import is_valid
import pytest

def test_length():
    assert is_valid("he") == True
    assert is_valid("IKJ98764") == False

def test_number():
    assert is_valid("as099") == False

def test_letter():
    assert is_valid("y7900") == False

def test_digit():
    assert is_valid("cs50p2") == False

def test_alnum():
    assert is_valid("hello!") == False


