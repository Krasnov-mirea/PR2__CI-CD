from calculator import add, sub
import pytest


def test_add():
    assert add(10, 24) == 34

def test_sub():
    assert sub(30, 21) == 9
