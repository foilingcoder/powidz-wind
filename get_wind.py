import requests
import json
from datetime import datetime

import sys

# Ustawienie kodowania na utf-8 dla konsoli Windows, jeśli to możliwe
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

def get_wind_powidz():
    # Koordynaty Powidza (Wielkopolskie)
    lat = 52.4136
    lon = 17.9193
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "wind_speed_10m,wind_direction_10m,wind_gusts_10m",
        "wind_speed_unit": "kmh"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        current = data.get("current", {})
        wind_speed = current.get("wind_speed_10m")
        wind_dir = current.get("wind_direction_10m")
        wind_gusts = current.get("wind_gusts_10m")
        
        print(f"--- Aktualne warunki wiatrowe w Powidzu ---")
        print(f"Czas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Prędkość wiatru: {wind_speed} km/h")
        print(f"Porywy wiatru: {wind_gusts} km/h")
        print(f"Kierunek wiatru: {wind_dir}° ({get_wind_direction_cardinal(wind_dir)})")
        
    except Exception as e:
        print(f"Wystąpił błąd podczas pobierania danych: {e}")

def get_wind_direction_cardinal(degrees):
    dirs = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    ix = round(degrees / (360. / len(dirs)))
    return dirs[ix % len(dirs)]

if __name__ == "__main__":
    get_wind_powidz()
