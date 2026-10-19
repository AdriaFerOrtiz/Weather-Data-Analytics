
import logging

import pandas as pd
import requests


logger = logging.getLogger(__name__)

API_URL = "https://api.open-meteo.com/v1/forecast"

PARAMS = {
    "latitude": 41.3874,
    "longitude": 2.1686,
    "hourly": "temperature_2m,precipitation,wind_speed_10m",
    "forecast_days": 3,
    "timezone": "Europe/Madrid",
}


def extract_weather_data() -> pd.DataFrame:
    """Extract hourly weather forecasts from Open-Meteo."""
    logger.info("Solicitando datos a Open-Meteo")

    response = requests.get(
        API_URL,
        params=PARAMS,
        timeout=30,
    )
    response.raise_for_status()

    data = response.json()

    if "hourly" not in data:
        raise ValueError("La respuesta de la API no contiene datos horarios")

    hourly = data["hourly"]

    df = pd.DataFrame({
        "timestamp": hourly["time"],
        "temperature_c": hourly["temperature_2m"],
        "precipitation_mm": hourly["precipitation"],
        "wind_speed_kmh": hourly["wind_speed_10m"],
    })

    logger.info("Extraídas %s observaciones", len(df))
    return df
