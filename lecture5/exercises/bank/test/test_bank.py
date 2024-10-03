from bank import value
import pytest

def test_0():
    assert value("hello") == 0
    assert value("hello,") == 0

    
def test_20():
    assert value("hi") == 20

def test_100():
    assert value("I Farted") == 100