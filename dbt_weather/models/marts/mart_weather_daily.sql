{{ config(materialized='table') }}

SELECT
    CAST(timestamp AS DATE) AS weather_date,

    COUNT(*) AS observations_count,

    ROUND(AVG(temperature_c), 2) AS avg_temperature_c,
    ROUND(MIN(temperature_c), 2) AS min_temperature_c,
    ROUND(MAX(temperature_c), 2) AS max_temperature_c,

    ROUND(
        SUM(COALESCE(precipitation_mm, 0)),
        2
    ) AS total_precipitation_mm,

    ROUND(AVG(wind_speed_kmh), 2) AS avg_wind_speed_kmh,
    ROUND(MAX(wind_speed_kmh), 2) AS max_wind_speed_kmh,

    SUM(
        CASE
            WHEN COALESCE(precipitation_mm, 0) > 0
            THEN 1
            ELSE 0
        END
    ) AS hours_with_precipitation

FROM {{ ref('stg_weather') }}

GROUP BY CAST(timestamp AS DATE)

ORDER BY weather_date