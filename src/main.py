
from extract import extract_weather_data
from transform import transform_weather_data
from load import load_weather_data


def main():
    print("Iniciando pipeline meteorológico...")

    raw_data = extract_weather_data()
    clean_data = transform_weather_data(raw_data)
    load_weather_data(clean_data)

    print("Pipeline completado correctamente.")


if __name__ == "__main__":
    main()
