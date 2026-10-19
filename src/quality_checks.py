
from pathlib import Path

import duckdb


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "weather.duckdb"


def main():
    with duckdb.connect(str(DB_PATH), read_only=True) as connection:

        total_rows = connection.execute("""
            SELECT COUNT(*)
            FROM weather_observations
        """).fetchone()[0]

        null_rows = connection.execute("""
            SELECT COUNT(*)
            FROM weather_observations
            WHERE timestamp IS NULL
               OR temperature_c IS NULL
               OR precipitation_mm IS NULL
               OR wind_speed_kmh IS NULL
        """).fetchone()[0]

        duplicate_timestamps = connection.execute("""
            SELECT COUNT(*)
            FROM (
                SELECT timestamp
                FROM weather_observations
                GROUP BY timestamp
                HAVING COUNT(*) > 1
            )
        """).fetchone()[0]

        invalid_measurements = connection.execute("""
            SELECT COUNT(*)
            FROM weather_observations
            WHERE precipitation_mm < 0
               OR wind_speed_kmh < 0
        """).fetchone()[0]

        print(f"Total de registros: {total_rows}")
        print(f"Registros con nulos: {null_rows}")
        print(f"Marcas de tiempo duplicadas: {duplicate_timestamps}")
        print(f"Registros con mediciones negativas: {invalid_measurements}")

        if null_rows or duplicate_timestamps or invalid_measurements:
            raise ValueError("Han fallado uno o más controles de calidad")

        print("Todos los controles de calidad han pasado.")


if __name__ == "__main__":
    main()
