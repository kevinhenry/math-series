from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == "0.1.0"


def test_one():
    actual = fibonacci(4)
    expected = 2
    assert actual == expected


def test_two():
    actual = fibonacci(8)
    expected = 13
    assert actual == expected


def test_three():
    actual = lucas(4)
    expected = 4
    assert actual == expected


def test_four():
    actual = lucas(8)
    expected = 29
    assert actual == expected


def test_five():
    actual = sum_series(4)
    expected = 2
    assert actual == expected


def test_six():
    actual = sum_series(8)
    expected = 13
    assert actual == expected
