
import logging

import pandas as pd


logger = logging.getLogger(__name__)

REQUIRED_COLUMNS = [
    "timestamp",
    "temperature_c",
    "precipitation_mm",
    "wind_speed_kmh",
]


def transform_weather_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and validate weather observations."""
    logger.info("Iniciando transformación de datos")

    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Faltan columnas obligatorias: {missing_columns}"
        )

    df = df[REQUIRED_COLUMNS].copy()

    df["timestamp"] = pd.to_datetime(
        df["timestamp"], errors="coerce"
    )

    numeric_columns = [
        "temperature_c",
        "precipitation_mm",
        "wind_speed_kmh",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

    initial_rows = len(df)

    df = df.dropna(subset=REQUIRED_COLUMNS)
    df = df.drop_duplicates(subset=["timestamp"])
    df = df.sort_values("timestamp").reset_index(drop=True)

    discarded_rows = initial_rows - len(df)

    logger.info(
        "Filas iniciales: %s; filas descartadas: %s",
        initial_rows,
        discarded_rows,
    )

    if df.empty:
        raise ValueError(
            "No quedan datos válidos tras la transformación"
        )

    if (df["precipitation_mm"] < 0).any():
        raise ValueError("Se han encontrado precipitaciones negativas")

    if (df["wind_speed_kmh"] < 0).any():
        raise ValueError("Se han encontrado velocidades negativas")

    logger.info("Transformación completada: %s filas", len(df))
    return df
