import pytest


def add_numbers(x, y):
    return x + y


def test_add_numbers():
    assert add_numbers(3, 5) == 8
    assert add_numbers(0, 10) == 10
    assert add_numbers(-2, -5) == -7
