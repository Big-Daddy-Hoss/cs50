from twttr import shorten
import pytest

def test_one_word():
    assert shorten("poop") == "pp"
    assert shorten("POOp") == "Pp"
    assert shorten("pp") == "pp"

def test_multiple_word():
    assert shorten("Poop Fart") == "Pp Frt"

def test_whitespace():
    assert shorten("I Farted") == "Frtd"