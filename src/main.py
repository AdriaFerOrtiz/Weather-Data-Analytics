
import logging
from pathlib import Path

from extract import extract_weather_data
from transform import transform_weather_data
from load import load_weather_data


PROJECT_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIR / "weather_pipeline.log"


def configure_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
        ],
        force=True,
    )


def main():
    configure_logging()
    logger = logging.getLogger(__name__)

    logger.info("========== INICIO DEL PIPELINE ==========")

    try:
        raw_data = extract_weather_data()
        clean_data = transform_weather_data(raw_data)
        load_weather_data(clean_data)

        logger.info("Pipeline completado correctamente")

    except Exception:
        logger.exception("El pipeline ha fallado")
        raise

    finally:
        logger.info("========== FIN DEL PIPELINE ==========")


if __name__ == "__main__":
    main()
