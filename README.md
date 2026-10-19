# Weather Data Analytics

Proyecto de portfolio de Data Engineering y Business Intelligence para recopilar, transformar, almacenar y analizar datos meteorológicos.

## Objetivos

- Obtener datos de una API meteorológica pública.
- Procesar y validar datos con Python y Pandas.
- Almacenar información en DuckDB y consultarla mediante SQL.
- Crear un dashboard interactivo con Power BI Desktop.
- Incorporar controles de calidad de datos, logs y documentación.

## Tecnologías

- Python
- Requests
- Pandas
- DuckDB
- SQL
- Power BI Desktop
- Git y GitHub

## Arquitectura

Open-Meteo API → Python / Pandas → DuckDB → Power BI

## Estado del proyecto

En desarrollo. Actualmente se está preparando el entorno y la primera extracción de datos meteorológicos.

## Pipeline de datos

1. **Extract:** consulta la API de previsión meteorológica de Open-Meteo.
2. **Transform:** convierte tipos, elimina filas incompletas y duplicadas y valida las mediciones.
3. **Load:** carga las observaciones en DuckDB y actualiza los registros existentes.
4. **Analyze:** ejecuta consultas SQL para obtener estadísticas meteorológicas.
5. **Quality checks:** comprueba valores nulos, marcas de tiempo duplicadas y mediciones negativas.
6. **Logging:** registra las etapas del pipeline, el número de observaciones procesadas y los errores.

## Ejecución

Instala las dependencias:

```bash
python -m pip install requests pandas duckdb
```

Ejecuta el pipeline desde la raíz del proyecto:

```bash
python src/main.py
```

Consulta los resultados:

```bash
python src/analyze.py
```

Ejecuta los controles de calidad:

```bash
python src/quality_checks.py
```

## Almacenamiento y logs

La base de datos se almacena localmente en `data/weather.duckdb`.

Los registros de ejecución se guardan en
`logs/weather_pipeline.log`.

Los archivos generados localmente no se versionan en Git.