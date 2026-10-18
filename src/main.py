
import requests
import pandas as pd

# 1. Configurar la consulta
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 41.3874,
    "longitude": 2.1686,
    "hourly": [
        "temperature_2m",
        "precipitation",
        "wind_speed_10m",
    ],
    "forecast_days": 3,
    "timezone": "Europe/Madrid",
}

# 2. Extraer los datos de la API
response = requests.get(url, params=params, timeout=30)

# 3. Comprobar que la petición ha funcionado
response.raise_for_status()

# 4. Convertir el JSON a un diccionario de Python
data = response.json()

# 5. Mostrar información básica
print("Petición completada correctamente")
print("Latitud:", data["latitude"])
print("Longitud:", data["longitude"])

hourly = data["hourly"]

df = pd.DataFrame({
    "timestamp": hourly["time"],
    "temperature_c": hourly["temperature_2m"],
    "precipitation_mm": hourly["precipitation"],
    "wind_speed_kmh": hourly["wind_speed_10m"],
})

# Mostrar una muestra de la tabla
print(df.head())

# Revisar estructura y valores ausentes
print("\nInformación del DataFrame:")
df.info()

print("\nValores ausentes por columna:")
print(df.isna().sum())

# Guardar una copia local
df.to_csv("weather_barcelona.csv", index=False)

print("\nArchivo CSV guardado correctamente")
