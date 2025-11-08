"""
Custom API Exporter
Пример: сбор данных о погоде в Астане и Алматы (Open-Meteo API)
"""

from prometheus_client import start_http_server, Gauge, Info
import requests
import time

# Метрики погоды
weather_temperature = Gauge(
    'weather_temperature_celsius',
    'Current temperature in city',
    ['city', 'country']
)

weather_windspeed = Gauge(
    'weather_windspeed_kmh',
    'Current wind speed in city',
    ['city', 'country']
)

weather_api_status = Gauge(
    'weather_api_status',
    'Weather API status (1=up, 0=down)'
)

# Информация об экспортере
exporter_info = Info('exporter_info', 'Custom API Exporter metadata')


def fetch_weather_data(city, lat, lon):
    """
    Получить данные о погоде для конкретного города через Open-Meteo API
    """
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            'latitude': lat,
            'longitude': lon,
            'current_weather': 'true',
            'timezone': 'Asia/Almaty'
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        current = data['current_weather']

        weather_temperature.labels(
            city=city,
            country='Kazakhstan'
        ).set(current['temperature'])

        weather_windspeed.labels(
            city=city,
            country='Kazakhstan'
        ).set(current['windspeed'])

        weather_api_status.set(1)
        return True

    except requests.exceptions.RequestException:
        weather_api_status.set(0)
        return False


if __name__ == '__main__':
    exporter_info.info({
        'version': '1.0',
        'author': 'Student',
        'sources': 'weather'
    })

    start_http_server(8000)
    print("✅ Custom weather exporter started on port 8000")

    # Города и координаты
    cities = {
        "Astana": (51.1694, 71.4491),
        "Almaty": (43.2389, 76.8897)
    }

    while True:
        for city, (lat, lon) in cities.items():
            fetch_weather_data(city, lat, lon)

        time.sleep(30)
