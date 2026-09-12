# Iceberg Data Verification

## Source

US National Ice Center (USNIC) Antarctic Iceberg Product.

## Data Access

The data was downloaded programmatically using Python `requests` from the USNIC current Antarctic iceberg CSV endpoint.

## Dataset

- Records: 33
- Unique icebergs: 33
- Observation date: 2026-09-10
- Missing values: 0

## Required Fields

- `iceberg_id`
- `time`
- `latitude`
- `longitude`

## Spatial Coverage

- Latitude: -74.25 to -53.94
- Longitude: -176.55 to 164.79

## Example Icebergs

| Iceberg | Date | Latitude | Longitude |
|---|---|---:|---:|
| A76C | 2026-09-10 | -53.94 | -26.43 |
| A81 | 2026-09-10 | -57.36 | -47.22 |
| A83 | 2026-09-10 | -61.07 | -50.61 |
| A84 | 2026-09-10 | -71.19 | -101.65 |
| A85 | 2026-09-10 | -61.72 | -53.02 |

## Verification

All required columns were present and no missing values were detected.

## Project Use

The dataset provides real iceberg positions that can be used as observations for the iceberg trajectory component. Historical position data will be required later to train and validate a trajectory model.

## Important Limitation

This USNIC product provides current iceberg positions and update dates. It is not a continuous hourly or daily trajectory dataset. Therefore, it is used here for real iceberg-position ingestion; historical tracking data will be needed for trajectory-learning and validation.

## Status

Verification successful.
