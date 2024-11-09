from src.maths_operations import add, sub


def test_add():
    assert add(3, 4) == 7
    assert add(0, 0) == 0
    assert add(-1, 1) == 0


def test_sub():
    assert sub(3, 4) == -1
    assert sub(0, 0) == 0
    assert sub(-1, 1) == -2