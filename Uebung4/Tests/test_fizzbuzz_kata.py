"""
TDD-Template für FizzBuzz Kata
==============================

TODO: Team A - Entwickelt FizzBuzz mit TDD!

FizzBuzz-Regeln:
- Zahl durch 3 teilbar → "Fizz"  
- Zahl durch 5 teilbar → "Buzz"
- Zahl durch 3 UND 5 teilbar → "FizzBuzz"
- Sonst → Zahl als String

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Autorschaft dokumentieren: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest

# TODO: Team A - Import nach erster Implementierung:
# from ..Code.fizzbuzz_kata import fizzbuzz
from Uebung4.Code.fizzbuzz_kata import fizzbuzz as fizzbuzz


class TestFizzBuzzTDD:
    """
    TODO: Team A - Entwickelt FizzBuzz mit TDD!

    Tipps:
    - Startet mit dem einfachsten Test
    - Schreibt minimalen Code zum Bestehen
    - Refaktoriert wenn nötig
    - Ein Test nach dem anderen!
    """

    def test_fizzbuzz_1_returns_1(self):
        # Testet: fizzbuzz(1) soll den String "1" zurückgeben
        assert fizzbuzz(1) == "1"

    def test_fizzbuzz_2_returns_2(self):
        # Testet: fizzbuzz(2) soll den String "2" zurückgeben
        assert fizzbuzz(2) == "2"

    def test_fizzbuzz_3_returns_Fizz(self):
        # Testet: durch 3 teilbare Zahl -> "Fizz"
        assert fizzbuzz(3) == "Fizz"

    def test_fizzbuzz_5_returns_Buzz(self):
        # Testet: durch 5 teilbare Zahl -> "Buzz"
        assert fizzbuzz(5) == "Buzz"

    def test_fizzbuzz_15_returns_FizzBuzz(self):
        # Testet: durch 3 und 5 teilbar -> "FizzBuzz"
        assert fizzbuzz(15) == "FizzBuzz"


class TestFizzBuzzErweitert:
    """
    TODO: Team A - Erweiterte Tests, wenn Basis funktioniert
    """

    def test_return0String(self):
        testArray = [0]
        # Edge-Case-Test: 0 sollte als String zurückgegeben werden
        for test in testArray:
            assert fizzbuzz(test) == str(test)

    def test_returnString(self):
        testArray = [0, 1, 2]
        # Testet mehrere Werte: nicht durch 3 oder 5 teilbar -> Rückgabe als String
        for test in testArray:
            assert fizzbuzz(test) == str(test)

    def test_returnFizz(self):
        testArray = [3, 6, 9]
        # Testet mehrere Werte: alle durch 3 teilbar -> "Fizz"
        for test in testArray:
            assert fizzbuzz(test) == "Fizz"

    def test_returnBuzz(self):
        testArray = [5, 10, 20]
        # Testet mehrere Werte: alle durch 5 teilbar -> "Buzz"
        for test in testArray:
            assert fizzbuzz(test) == "Buzz"

    def test_returnFizzBuzz(self):
        testArray = [15, 30, 45]
        # Testet mehrere Werte: alle durch 3 und 5 teilbar -> "FizzBuzz"
        for test in testArray:
            assert fizzbuzz(test) == "FizzBuzz"

    def test_returnFizz_negativ(self):
        testArray = [-3, -6, -9]
        # Erweiterter Test: auch negative Vielfache von 3 sollen "Fizz" liefern
        for test in testArray:
            assert fizzbuzz(test) == "Fizz"

    def test_returnBuzz_negativ(self):
        testArray = [-5, -10, -20]
        # Erweiterter Test: auch negative Vielfache von 5 sollen "Buzz" liefern
        for test in testArray:
            assert fizzbuzz(test) == "Buzz"

    def test_returnFizzBuzz_negativ(self):
        testArray = [-15, -30, -45]
        # Erweiterter Test: Vielfache von 3 und 5 (auch negativ) -> "FizzBuzz"
        for test in testArray:
            assert fizzbuzz(test) == "FizzBuzz"

    def test_negativeValues_string(self):
        # Edge-Case-Test: negative Zahlen und 0 sollten als String zurückgegeben werden
        assert fizzbuzz(-4) == str(-4)

    def test_große_Zahlen(self):
        # Weitere Edge-Cases: große Zahlen und negative Werte -> String zurückgeben
        assert fizzbuzz(8096) == str(8096)

    def test_canonicallyAll(self):
        testArray = [0, 1, 2, 3, 5, 15, -3]
        # Kanonischer Test: iteriert über typische Fälle und prüft die erwartete Rückgabe
        for test in testArray:
            def fizzbuzzreturn(test):
                # Erwartung: je nach Teilbarkeit -> "Fizz"/"Buzz"/"FizzBuzz" oder Zahl als String
                if ((test % 3) and (test % 5)):
                    assert fizzbuzz(test) == "FizzBuzz"
                elif (test % 3):
                    assert fizzbuzz(test) == "Fizz"
                elif (test % 5):
                    assert fizzbuzz(test) == "Buzz"
                else:
                    assert fizzbuzz(test) == str(test)

 # Parametrisierte, erweiterte Tests für FizzBuzz
    @pytest.mark.parametrize("value,expected", [
        (0, "0"), (1, "1"), (2, "2")
    ])
    def test_param_return_string(self, value, expected):
        """Prüft, dass für nicht-Fizz/Buzz-Werte der String der Zahl zurückgegeben wird."""
        assert fizzbuzz(value) == expected

    @pytest.mark.parametrize("value", [3, 6, 9, -3])
    def test_param_return_fizz(self, value):
        """Prüft, dass Vielfache von 3 'Fizz' liefern."""
        assert fizzbuzz(value) == "Fizz"

    @pytest.mark.parametrize("value", [5, 10, 20, -5])
    def test_param_return_buzz(self, value):
        """Prüft, dass Vielfache von 5 'Buzz' liefern."""
        assert fizzbuzz(value) == "Buzz"

    @pytest.mark.parametrize("value", [15, 30, 45, -15])
    def test_param_return_fizzbuzz(self, value):
        """Prüft, dass Vielfache von 3 und 5 'FizzBuzz' liefern."""
        assert fizzbuzz(value) == "FizzBuzz"

    @pytest.mark.parametrize("value", [-4, -7, 8096])
    def test_param_edge_cases_return_string(self, value):
        """Prüft Edge-Cases: negative und große Zahlen -> String."""
        assert fizzbuzz(value) == str(value)


# TODO: Team A - Optional: TDD-Protokoll
"""
TDD-Fortschritt dokumentieren:

Alle Tests und Implementierungen wurden von Team A (FALR und CNSK) gemeinsam entwickelt.

Erkenntnisse:
- Was war überraschend?
- Wo musstet ihr refaktorieren?
- Welche Tests brachten neue Herausforderungen?
"""
