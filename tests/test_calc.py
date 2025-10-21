from calculator import add, sub, mul, div
import pytest

def test_add():
    assert add(10, 24) == 34

def test_sub():
    assert sub(30, 21) == 9

def test_mul():
    assert mul(5, 5) == 25

def test_div():
    assert div(100, 5) == 20
