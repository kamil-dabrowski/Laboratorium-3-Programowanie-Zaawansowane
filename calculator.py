class Calculator:
    """Klasa kalkulatora, która wykonuje operacje matematyczne."""

    def dodawanie(self, a, b):
        """
        Dodawanie dwóch podanych liczb.

        Parameters
        ----------
        a : float
            Pierwsza liczba dodawana.
        b : float
            Druga liczba dodawana.

        Returns
        -------
        float
            Suma liczb.
        """
        return a + b

    def odejmowanie(self, a, b):
        """
        Odejmowanie drugiej liczby od pierwszej.

        Parameters
        ----------
        a : float
            Liczba, od której odejmujemy.
        b : float
            Liczba odejmowana.

        Returns
        -------
        float
            Różnica liczb.
        """
        return a - b

    def mnozenie(self, a, b):
        """
        Mnożenie dwóch liczb.

        Parameters
        ----------
        a : float
            Pierwszy czynnik.
        b : float
            Drugi czynnik.

        Returns
        -------
        float
            Iloczyn liczb.
        """
        return a * b

    def dzielenie(self, a, b):
        """
        Dzielenie pierwszej liczby przez drugą.

        Parameters
        ----------
        a : float
            Dzielna.
        b : float
            Dzielnik.

        Returns
        -------
        float
            Iloraz liczb.

        Raises
        ------
        ValueError
            Błąd zgłaszany w przypadku próby dzielenia przez zero.
        """
        if b == 0:
            raise ValueError("Nie można dzielić przez zero.")
        return a / b