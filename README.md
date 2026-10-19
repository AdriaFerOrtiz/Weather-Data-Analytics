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

1. **Extract:** lectura de las observaciones meteorológicas desde un CSV.
2. **Transform:** conversión de tipos, eliminación de registros incompletos y duplicados, y validación de mediciones.
3. **Load:** almacenamiento en DuckDB mediante una carga que actualiza las observaciones existentes.
4. **Analyze:** consultas SQL para calcular estadísticas generales y agregaciones diarias.
5. **Quality checks:** comprobación de valores nulos, marcas de tiempo duplicadas y mediciones negativas.

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

## Almacenamiento

La base de datos se genera localmente en `data/weather.duckdb`.
Los archivos de datos generados no se versionan en Git.