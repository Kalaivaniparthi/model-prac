from pathlib import Path
import xarray as xr


DATA_FILE = Path(
    "data/raw/antarctic_sea_ice_2026-08-01_2026-08-10.nc"
)


def inspect_sea_ice():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"File not found: {DATA_FILE}")

    ds = xr.open_dataset(DATA_FILE)

    try:
        if "ice_conc" not in ds:
            raise ValueError("Variable 'ice_conc' not found")

        sic = ds["ice_conc"]

        result = {
            "file": str(DATA_FILE),
            "dimensions": dict(ds.sizes),
            "variable": "ice_conc",
            "min": float(sic.min()),
            "max": float(sic.max()),
            "mean": float(sic.mean()),
            "missing_values": int(sic.isnull().sum()),
            "shape": tuple(sic.shape),
            "time_start": str(ds.time.values[0]),
            "time_end": str(ds.time.values[-1]),
        }

        return result

    finally:
        ds.close()


if __name__ == "__main__":
    result = inspect_sea_ice()

    print("===== SEA ICE VERIFICATION =====")

    for key, value in result.items():
        print(f"{key}: {value}")
