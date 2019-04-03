import pytest

# Testing travis

def add(x, y):
    return x + y


def test1():
    x = 1
    y = 2
    assert add(x, y) == x + y


def t():
    with pytest.raises(TypeError):
        pass
