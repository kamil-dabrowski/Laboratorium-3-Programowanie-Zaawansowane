==================
Kalkulator klasowy
==================

Kalkulator klasowy służy do obsługi prostych operacji arytmetycznych.

Oto jego funkcjonalności:

* Dodawanie
* Odejmowanie
* Mnożenie
* Dzielenie (uwzględnia dzielenie przez zero)
* testy

Przykładowe użycie klasy Calculator

.. code-block:: python

    from calculator import Calculator

    calc = Calculator()

    wynik_dodawania = calc.dodawanie(10, 5)
    print(f"Wynik dodawania to {wynik_dodawania}")

    wynik_odejmowania = calc.odejmowanie(10, 5)
    print(f"Wynik odejmowania to {wynik_odejmowania}")

Link do dokumentacji Python: `https://docs.python.org/ <https://docs.python.org/>`_

.. image:: https://img.shields.io/badge/python-%3E%3D3.10-blue
.. image:: https://img.shields.io/badge/testing-pytest-green
