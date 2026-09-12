from pathlib import Path
import xarray as xr

DATA_FILE = Path("data/raw/cmems/cmems_ocean_2026-06-23.nc")


def verify_cmems():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"CMEMS file not found: {DATA_FILE}")

    ds = xr.open_dataset(DATA_FILE)

    try:
        print("=== CMEMS Ocean Data Verification ===")
        print(f"File: {DATA_FILE}")
        print(f"Dimensions: {dict(ds.sizes)}")
        print(f"Variables: {list(ds.data_vars)}")
        print(f"Coordinates: {list(ds.coords)}")

        print("\n=== Depth ===")
        print(f"Minimum depth: {float(ds.depth.min()):.6f} m")
        print(f"Maximum downloaded depth: {float(ds.depth.max()):.6f} m")
        print(f"Depth levels: {ds.depth.values}")

        print("\n=== Variable Statistics ===")

        for variable in ["uo", "vo", "thetao"]:
            data = ds[variable]

            print(f"\n{variable}")
            print(f"  Shape: {data.shape}")
            print(f"  Units: {data.attrs.get('units', 'not specified')}")
            print(f"  Minimum: {float(data.min(skipna=True)):.6f}")
            print(f"  Maximum: {float(data.max(skipna=True)):.6f}")
            print(f"  Mean: {float(data.mean(skipna=True)):.6f}")
            print(f"  Missing values: {int(data.isnull().sum())}")

        print("\n=== Time ===")
        print(f"Start: {ds.time.min().values}")
        print(f"End: {ds.time.max().values}")

        print("\n=== Spatial Coverage ===")
        print(f"Latitude: {float(ds.latitude.min())} to {float(ds.latitude.max())}")
        print(f"Longitude: {float(ds.longitude.min())} to {float(ds.longitude.max())}")

        print("\nVerification successful.")

    finally:
        ds.close()


if __name__ == "__main__":
    verify_cmems()

