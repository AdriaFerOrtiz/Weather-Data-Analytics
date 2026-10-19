
from pathlib import Path

import duckdb
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
DB_PATH = DATA_DIR / "weather.duckdb"


def load_weather_data(df: pd.DataFrame) -> None:
    """Load weather observations into DuckDB."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with duckdb.connect(str(DB_PATH)) as connection:
        connection.register("weather_df", df)

        connection.execute("""
            CREATE TABLE IF NOT EXISTS weather_observations (
                timestamp TIMESTAMP PRIMARY KEY,
                temperature_c DOUBLE NOT NULL,
                precipitation_mm DOUBLE NOT NULL,
                wind_speed_kmh DOUBLE NOT NULL
            )
        """)

        connection.execute("""
            INSERT INTO weather_observations
            SELECT
                timestamp,
                temperature_c,
                precipitation_mm,
                wind_speed_kmh
            FROM weather_df
            ON CONFLICT (timestamp) DO UPDATE SET
                temperature_c = EXCLUDED.temperature_c,
                precipitation_mm = EXCLUDED.precipitation_mm,
                wind_speed_kmh = EXCLUDED.wind_speed_kmh
        """)

        total_rows = connection.execute("""
            SELECT COUNT(*)
            FROM weather_observations
        """).fetchone()[0]

        print(f"Registros almacenados en DuckDB: {total_rows}")
        print(f"Base de datos: {DB_PATH}")
