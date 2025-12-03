"""
Implementierung: Weather-API Service
====================================
Bearbeiter: FALR

TODO: Team A - Implementiert get_weather_category() hier!

Die Funktion soll:
1. Weather-API aufrufen (in Tests gemockt)
2. Temperatur extrahieren
3. Kategorie zurückgeben

Hinweise:
- Nutzt requests.get() für API-Aufrufe
- API-URL: https://api.weather.com/current?city={city}
- Response-Format: {"temperature": 20}
- Startet mit minimalster Implementierung!
"""

import requests


def get_weather_category(city: str) -> str:
    """
    Ruft Weather-API auf und gibt Temperatur-Kategorie zurück

    Args:
        city: Stadt, für die das Wetter abgefragt wird

    Returns:
        Temperatur-Kategorie als String:
        - "frostgefahr" (< 0°C)
        - "kalt" (0-10°C)
        - "kühl" (11-15°C)
        - "angenehm" (16-24°C)
        - "warm" (25-30°C)
        - "heiß" (> 30°C)
    """
    # Baut die URL für den API-Aufruf. In Tests wird `requests.get` gemockt.
    url = f"https://api.weather.com/current?city={city}"

    # API-Aufruf mit Timeout; Fehler werden an den Aufrufer weitergegeben (Tests können patchen)
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()

    # Temperatur aus der Antwort extrahieren
    temperature = data.get("temperature")
    if temperature is None:
        # Keine Temperatur im Payload -> Fehler, damit Tests/Caller das merken
        raise ValueError(
            "API-Response enthält keine 'temperature'-Information")

    # Kategorisierung gemäß Aufgabenstellung
    # < 0: frostgefahr
    # 0-10: kalt
    # 11-15: kühl
    # 16-24: angenehm
    # 25-30: warm
    # > 30: heiß
    if temperature < 0:
        return "frostgefahr"
    if 0 <= temperature <= 10:
        return "kalt"
    if 11 <= temperature <= 15:
        return "kühl"
    if 16 <= temperature <= 24:
        return "angenehm"
    if 25 <= temperature <= 30:
        return "warm"
    return "heiß"
