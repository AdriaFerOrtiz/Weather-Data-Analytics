
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "weather_barcelona.csv"


def extract_weather_data() -> pd.DataFrame:
    """Extract weather observations from the generated CSV."""
    if not CSV_PATH.exists():
        raise FileNotFoundError(
            f"No se encuentra el archivo de datos: {CSV_PATH}"
        )

    df = pd.read_csv(CSV_PATH)

    print(f"Datos extraídos: {len(df)} filas")
    return df
