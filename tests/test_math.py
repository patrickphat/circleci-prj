import pytest
from my_math import add, minus

def test_add():
    assert add(3,4) == 7, "wrong answer"
    assert add(7,12) == 19, "wrong answer"

def test_minus():
    assert(minus(3,4)) == -1, "wrong answer"
    assert(minus(5,1)) == 4, "wrong answer"
