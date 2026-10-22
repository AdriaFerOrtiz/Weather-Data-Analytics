SELECT
    timestamp,
    precipitation_mm
FROM {{ ref('stg_weather') }}
WHERE precipitation_mm < 0