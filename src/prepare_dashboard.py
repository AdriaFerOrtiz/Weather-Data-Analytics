
from pathlib import Path

import duckdb

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "weather.duckdb"
OUTPUT_PATH = PROJECT_ROOT / "data" / "daily_weather_summary.csv"


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with duckdb.connect(str(DB_PATH), read_only=True) as connection:
        daily_summary = connection.execute("""
            SELECT
                CAST(timestamp AS DATE) AS observation_date,
                ROUND(AVG(temperature_c), 1) AS avg_temperature_c,
                ROUND(MIN(temperature_c), 1) AS min_temperature_c,
                ROUND(MAX(temperature_c), 1) AS max_temperature_c,
                ROUND(SUM(precipitation_mm), 1) AS total_precipitation_mm,
                ROUND(AVG(wind_speed_kmh), 1) AS avg_wind_speed_kmh,
                ROUND(MAX(wind_speed_kmh), 1) AS max_wind_speed_kmh
            FROM weather_observations
            GROUP BY CAST(timestamp AS DATE)
            ORDER BY observation_date
        """).df()

    daily_summary.to_csv(OUTPUT_PATH, index=False)

    print("Resumen diario generado correctamente.")
    print(f"Archivo: {OUTPUT_PATH}")
    print(f"Días incluidos: {len(daily_summary)}")
    print()
    print(daily_summary.to_string(index=False))


if __name__ == "__main__":
    main()
