# Sea-Ice Concentration Data Verification

## Source

Copernicus Marine / OSI SAF sea-ice concentration product.

## File

`data/raw/antarctic_sea_ice_2026-08-01_2026-08-10.nc`

## Dataset Structure

- Time points: 10 daily observations
- Latitude points: 30
- Longitude points: 50
- Variable: `ice_conc`
- Format: NetCDF

## Observed Values

- Minimum SIC: 79.33%
- Maximum SIC: 100%
- Mean SIC: 98.06%
- Missing values: 90
- Data shape: `(10, 30, 50)`

## Time Range

2026-08-01 to 2026-08-10

## Interpretation

The selected Antarctic region has very high sea-ice concentration during
the inspected period.

Missing values are present in 90 grid cells. These should not be
automatically converted to 0%, because 0% represents open water and may
not represent missing observations.

## Metadata Note

The NetCDF metadata contains `start_date` and `stop_date` values that do
not match the actual `time` coordinate. The processing pipeline should use
the dataset time coordinate for temporal alignment and flag the metadata
inconsistency.

## Status

SIC data successfully loaded and verified using Python and Xarray.
