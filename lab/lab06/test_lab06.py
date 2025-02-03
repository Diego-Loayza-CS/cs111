# Remember to import from the lab10 file and pytest
import pytest
from lab06 import *


# Write your test code here for Q1

def test_product():
    with pytest.raises(ValueError):
        product(0.1)
    with pytest.raises(ValueError):
        product(-0.1)
    with pytest.raises(ValueError):
        product(-1)
    with pytest.raises(ValueError):
        product("string")
    with pytest.raises(ValueError):
        assert product(0)
    assert product(1) == 1
    assert product(2) == 2
    assert product(3) == 6
    assert product(4) == 24


def test_summation():
    with pytest.raises(ValueError):
        summation(0.1)
    with pytest.raises(ValueError):
        summation(-0.1)
    with pytest.raises(ValueError):
        summation(-1)
    with pytest.raises(ValueError):
        summation("string")
    assert summation(0) == 0
    assert summation(1) == 1
    assert summation(2) == 3
    assert summation(3) == 6
    assert summation(4) == 10


# Q2
#####################################

def test_square():
    assert square(-1) == 1
    assert square(-0.5) == 0.25
    assert square(0) == 0
    assert square(2) == 4
    assert square(4.5) == 20.25


def test_sqrt():
    assert sqrt(0) == 0
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert sqrt(16) == 4


def test_mean():
    with pytest.raises(AssertionError):
        assert mean("hola")
    with pytest.raises(AssertionError):
        assert mean([])
    with pytest.raises(TypeError):
        assert mean(["or", "hi"])
    assert mean([1, 1, 1]) == 1
    assert mean([4]) == 4
    assert mean([5, -1, 3, 3]) == 2.5
    assert mean([9, 9, 9, 9, 9, 9, 9, 9, 9, 10]) == 9.1


def test_median():
    with pytest.raises(AssertionError):
        assert median("hola")
    with pytest.raises(AssertionError):
        assert median([])
    with pytest.raises(TypeError):
        assert median(["or", "hi"])
    assert median([1, 2, 3, 4, 5]) == 3
    assert median([1, 2, 4, 4, 5, 6]) == 4
    assert median([2, 4, 6, 8, 10, 12]) == 7
    assert median([10, 9, 9, 1, 4, 5]) == 7
    assert median([2, 4, 6, 8, 10, 12, 14]) == 8


def test_mode():
    with pytest.raises(AssertionError):
        assert mode("hola")
    with pytest.raises(AssertionError):
        assert mode([])
    assert mode(["or", "hi"]) == "or"
    assert mode([1, 2, 3, 4, 5]) == 1
    assert mode([1, 2, -2, 4, 5, 6, 6]) == 6
    assert mode([-1, -2, 2, -4, -5, -6, -6]) == -6


def test_std_dev():
    with pytest.raises(AssertionError):
        assert std_dev("hola")
    with pytest.raises(AssertionError):
        assert std_dev([])
    with pytest.raises(TypeError):
        assert std_dev(["or", "hi"])
    assert std_dev([0, 1, 13, 17, 19]) == 8


def test_stat_analysis():
    with pytest.raises(AssertionError):
        assert std_dev("hola")
    with pytest.raises(AssertionError):
        assert mode([])
    with pytest.raises(TypeError):
        assert median(["or", "hi"])
    assert mean([5, -1, 3, 3]) == 2.5
    assert mean([9, 9, 9, 9, 9, 9, 9, 9, 9, 10]) == 9.1
    assert square(2) == 4
    assert square(4.5) == 20.25
    assert sqrt(9) == 3
    assert sqrt(16) == 4
    assert median([10, 9, 9, 1, 4, 5]) == 7
    assert median([2, 4, 6, 8, 10, 12, 14]) == 8
    assert mode([1, 2, -2, 4, 5, 6, 6]) == 6
    assert mode([-1, -2, 2, -4, -5, -6, -6]) == -6


# OPTIONAL
#####################################

def test_accumulate():
    assert accumulate(add, 0, 3) == 6
    assert accumulate(add, 2, 3) == 8
    assert accumulate(mul, 2, 4) == 48
    with pytest.raises(ValueError):
        assert accumulate(mul, 5, 0) == 0


def test_product_short():
    with pytest.raises(ValueError):
        product_short(0.1)
    with pytest.raises(ValueError):
        product_short(-0.1)
    with pytest.raises(ValueError):
        product_short(-1)
    with pytest.raises(ValueError):
        product_short("string")
    assert product_short(0) == 1
    assert product_short(1) == 1
    assert product_short(2) == 2
    assert product_short(3) == 6
    assert product_short(4) == 24


def test_summation_short():
    with pytest.raises(ValueError):
        summation_short(0.1)
    with pytest.raises(ValueError):
        summation_short(-0.1)
    with pytest.raises(ValueError):
        summation_short(-1)
    with pytest.raises(ValueError):
        summation_short("string")
    assert summation_short(0) == 0
    assert summation_short(1) == 1
    assert summation_short(2) == 3
    assert summation_short(3) == 6
    assert summation_short(4) == 10


def test_invert():
    assert invert(4, 0.26) == 0.25
    assert invert(4, 0.24) == 0.24
    with pytest.raises(ZeroDivisionError):
        assert invert(0, 0.29)
    assert invert(10, 0.5) == 0.1


def test_change():
    assert change(4, 2, 0.2) == 0.2
    assert change(4, 2, 1) == 0.5
    with pytest.raises(ZeroDivisionError):
        assert change(0, 2, 0.2)
    assert change(5, 10, 2) == 1



def test_invert_short():
    assert invert_short(4, 0.26) == 0.25
    assert invert_short(4, 0.24) == 0.24
    with pytest.raises(ZeroDivisionError):
        assert invert_short(0, 0.29)
    assert invert_short(10, 0.5) == 0.1


def test_change_short():
    assert change_short(4, 2, 0.2) == 0.2
    assert change_short(4, 2, 1) == 0.5
    with pytest.raises(ZeroDivisionError):
        assert change_short(0, 2, 0.2)
    assert change_short(5, 10, 2) == 1