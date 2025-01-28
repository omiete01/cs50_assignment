# code to test twttr.py

from twttr import shorten


def test_shorten():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_error():
    assert shorten("tw1tter") == "tw1ttr"
    assert shorten("twitter!") == "twttr!"

