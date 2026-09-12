# ERA5 Weather Data Verification

## Source

Copernicus Climate Data Store (CDS) — ERA5 hourly single-level reanalysis.

## File

`data/raw/era5/era5_weather_2026-08-01.nc`

## Coverage

- Date: 2026-08-01
- Time points: 24 hourly observations
- Latitude: -65° to -72°
- Longitude: 20°E to 60°E

## Variables

- `u10` — 10 m eastward wind component
- `v10` — 10 m northward wind component
- `t2m` — 2 m air temperature
- `msl` — mean sea-level pressure

## Validation

- Missing values: 0 for all variables
- Data format: NetCDF
- All four required variables are present.

## Observed Ranges

| Variable | Minimum | Maximum | Mean |
|---|---:|---:|---:|
| u10 | -26.74 m/s | 17.35 m/s | -4.27 m/s |
| v10 | -16.04 m/s | 16.53 m/s | 2.05 m/s |
| t2m | 213.46 K | 269.96 K | 249.44 K |
| msl | 95269.94 Pa | 101132.94 Pa | 98010.39 Pa |

## Preprocessing Note

`t2m` is stored in Kelvin and will be converted to Celsius during
preprocessing. The raw NetCDF file will remain unchanged.

## Status

ERA5 real data successfully downloaded and verified.
