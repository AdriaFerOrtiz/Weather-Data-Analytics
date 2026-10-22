{{ config(materialized='view') }}

SELECT *
FROM read_csv_auto('../weather_barcelona.csv', header = true)