"""
TDD-Template für Weather-API Service
====================================

TODO: Team A - Implementiert get_weather_category() testgetrieben!

Aufgabe:
- Funktion ruft Weather-API auf (mocken!)
- Extrahiert Temperatur aus JSON
- Gibt Kategorie zurück basierend auf Temperatur

Temperatur-Kategorien:
- < 0°C:      "frostgefahr"
- 0-10°C:     "kalt"
- 11-15°C:    "kühl"
- 16-24°C:    "angenehm"
- 25-30°C:    "warm"
- > 30°C:     "heiß"

TDD-Prozess: RED → GREEN → REFACTOR → wiederholen!

Dokumentiert eure Autorschaft: Wer hat welchen TDD-Schritt gemacht?
"""

import pytest
from unittest.mock import patch

# TODO: Team A - Import nach erster Implementierung:
from Uebung4.Code.weather_service import get_weather_category as weather


class TestWeatherService:
    """
    Tests für Weather-API Service

    TDD-Vorgehen:
    1. Test schreiben (RED)
    2. Minimale Implementierung (GREEN)
    3. Refactoring
    """

    @pytest.mark.parametrize("city,temp,expected", [
        ("Berlin", 20, "angenehm"),
        ("Warschau", -5, "frostgefahr"),
        ("Kiew", 5, "kalt"),
        ("Wien", 13, "kühl"),
        ("Rom", 28, "warm"),
        ("Barcelona", 35, "heiß"),
    ])
    def test_weather_categories(self, city, temp, expected):
        """Parametrisierter Test: mocked API-Response liefert verschiedene Temperaturen
        Erwartet: korrekte Kategorie als String und korrekter API-Aufruf mit Timeout
        """
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {"temperature": temp}

            result = weather(city)
            assert result == expected

            # Prüfe, dass die API mit URL und Timeout aufgerufen wurde
            mock_get.assert_called_once_with(
                f"https://api.weather.com/current?city={city}", timeout=5)

    def test_missing_temperature_raises(self):
        """Wenn die API keine 'temperature' liefert, wird ein ValueError ausgelöst."""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = {}

            with pytest.raises(ValueError):
                weather("Berlin")

            mock_get.assert_called_once_with(
                "https://api.weather.com/current?city=Berlin", timeout=5)
