# CMEMS Ocean Data Verification

## Dataset

- Product ID: GLOBAL_MULTIYEAR_PHY_001_030
- Dataset ID: cmems_mod_glo_phy_my_0.083deg_P1D-m
- Source: CMEMS / MERCATOR GLORYS12V1
- Date: 2026-06-23
- Temporal resolution: Daily

## Spatial Coverage

- Longitude: 20.0°E to 60.0°E
- Latitude: 72.0°S to 65.0°S
- Latitude points: 85
- Longitude points: 481

## Variables

| Variable | Meaning | Units |
|---|---|---|
| uo | East-west ocean current | m s-1 |
| vo | North-south ocean current | m s-1 |
| thetao | Ocean temperature | degrees_C |

## Dimensions

- Time: 1
- Depth: 8
- Latitude: 85
- Longitude: 481

Data shape for each variable:

`(time, depth, latitude, longitude)`

## Depth

Downloaded depth range:

- Minimum: 0.494025 m
- Maximum: 9.572997 m

Depth levels:

`0.494025, 1.541375, 2.645669, 3.819495, 5.078224, 6.440614, 7.929560, 9.572997 m`

The shallowest physical depth is automatically identified as the minimum available depth rather than assuming depth index 0.

## Data Statistics

### uo

- Minimum: -0.627461 m s-1
- Maximum: 0.368664 m s-1
- Mean: -0.061857 m s-1
- Missing values: 169576

### vo

- Minimum: -0.427870 m s-1
- Maximum: 0.252083 m s-1
- Mean: -0.030055 m s-1
- Missing values: 169576

### thetao

- Minimum: -2.003876 °C
- Maximum: -0.566088 °C
- Mean: -1.745678 °C
- Missing values: 169544

## Time

- Start: 2026-06-23 00:00:00
- End: 2026-06-23 00:00:00

## Verification Status

SUCCESS

The CMEMS ocean dataset was successfully downloaded and verified.

The data contains near-surface ocean currents (`uo`, `vo`) and ocean temperature (`thetao`) for the Antarctic study region.

## Intended Use

The data will be used as environmental input for the Antarctic navigation system, particularly:

- Iceberg trajectory prediction
- Ocean-current influence modelling
- Sea-ice/environment interaction
- Navigation risk and route analysis

SSH (`zos`) is not used in the current prototype.
