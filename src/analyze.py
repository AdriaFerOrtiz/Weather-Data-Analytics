
from pathlib import Path

import duckdb


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "weather.duckdb"


def main():
    with duckdb.connect(str(DB_PATH), read_only=True) as connection:

        print("\nPrimeras observaciones:")
        print(connection.execute("""
            SELECT *
            FROM weather_observations
            ORDER BY timestamp
            LIMIT 5
        """).df())

        print("\nResumen de temperatura y viento:")
        print(connection.execute("""
            SELECT
                ROUND(AVG(temperature_c), 2) AS avg_temperature_c,
                ROUND(MAX(temperature_c), 2) AS max_temperature_c,
                ROUND(MIN(temperature_c), 2) AS min_temperature_c,
                ROUND(AVG(wind_speed_kmh), 2) AS avg_wind_speed_kmh,
                ROUND(SUM(precipitation_mm), 2) AS total_precipitation_mm
            FROM weather_observations
        """).df())

        print("\nResumen por día:")
        print(connection.execute("""
            SELECT
                CAST(timestamp AS DATE) AS observation_date,
                ROUND(AVG(temperature_c), 2) AS avg_temperature_c,
                ROUND(MAX(temperature_c), 2) AS max_temperature_c,
                ROUND(SUM(precipitation_mm), 2) AS total_precipitation_mm
            FROM weather_observations
            GROUP BY CAST(timestamp AS DATE)
            ORDER BY observation_date
        """).df())


if __name__ == "__main__":
    main()
