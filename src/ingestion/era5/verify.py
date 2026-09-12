from pathlib import Path
import xarray as xr


DATA_FILE = Path("data/raw/era5/era5_weather_2026-08-01.nc")


def verify_era5():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"File not found: {DATA_FILE}")

    ds = xr.open_dataset(DATA_FILE)

    try:
        print("===== ERA5 WEATHER VERIFICATION =====")
        print(f"File: {DATA_FILE}")
        print(f"Dimensions: {dict(ds.sizes)}")
        print(f"Variables: {list(ds.data_vars)}")

        print("\n===== VARIABLE STATISTICS =====")

        for variable in ds.data_vars:
            data = ds[variable]

            print(f"\n{variable}")
            print(f"  Min: {float(data.min())}")
            print(f"  Max: {float(data.max())}")
            print(f"  Mean: {float(data.mean())}")
            print(f"  Missing: {int(data.isnull().sum())}")

        print("\n===== TIME =====")
        print(f"Start: {ds.valid_time.values[0]}")
        print(f"End:   {ds.valid_time.values[-1]}")

        print("\n===== UNITS =====")
        for variable in ds.data_vars:
            print(f"{variable}: {ds[variable].attrs.get('units', 'not specified')}")

    finally:
        ds.close()


if __name__ == "__main__":
    verify_era5()
