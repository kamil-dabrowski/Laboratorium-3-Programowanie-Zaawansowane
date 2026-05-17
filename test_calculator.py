import pytest
from calculator import Calculator

def test_dodawanie():
    calc = Calculator()
    assert calc.dodawanie(21, 37) == 58

def test_odejmowanie():
    calc = Calculator()
    assert calc.odejmowanie(10, 4) == 6

def test_mnozenie():
    calc = Calculator()
    assert calc.mnozenie(6, 7) == 42

def test_dzielenie():
    calc = Calculator()
    assert calc.dzielenie(100, 2) == 50.0

def test_dzielenie_przez_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Nie można dzielić przez zero."):
        calc.dzielenie(67, 0)