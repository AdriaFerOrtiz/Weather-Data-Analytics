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

1. **Extract:** consulta la API de Open-Meteo.
2. **Transform:** valida, limpia y ordena los datos.
3. **Load:** almacena los registros en DuckDB.
4. **Analyze:** ejecuta consultas SQL de análisis.
5. **Dashboard preparation:** genera un resumen diario en CSV
   para utilizarlo en Power BI Desktop.

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

Para generar el resumen diario destinado a Business Intelligence:

```bash
python src/prepare_dashboard.py
```

### Fiabilidad y calidad

- Registro de eventos y errores mediante logging.
- Reintentos HTTP para determinados fallos temporales.
- Validación de columnas, tipos, valores nulos y duplicados.
- Carga idempotente por timestamp mediante actualización
  de los registros que ya existen.


## Almacenamiento y logs

La base de datos se almacena localmente en `data/weather.duckdb`.

Los registros de ejecución se guardan en
`logs/weather_pipeline.log`.

Los archivos generados localmente no se versionan en Git.

### Limitaciones

- Los datos proceden de una API de previsiones, no de una
  estación meteorológica que mida el tiempo real.
- Los timestamps antiguos se conservan en la base de datos.
- Las previsiones de una misma fecha pueden cambiar entre
  ejecuciones.
- La base de datos y los CSV generados se almacenan localmente.