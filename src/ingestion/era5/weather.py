from pathlib import Path
import cdsapi


OUTPUT_DIR = Path("data/raw/era5")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "era5_weather_2026-08-01.nc"


def download_era5():
    client = cdsapi.Client()

    client.retrieve(
        "reanalysis-era5-single-levels",
        {
            "product_type": ["reanalysis"],
            "variable": [
                "10m_u_component_of_wind",
                "10m_v_component_of_wind",
                "2m_temperature",
                "mean_sea_level_pressure",
            ],
            "year": ["2026"],
            "month": ["08"],
            "day": ["01"],
            "time": [
                "00:00",
                "01:00",
                "02:00",
                "03:00",
                "04:00",
                "05:00",
                "06:00",
                "07:00",
                "08:00",
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00",
                "17:00",
                "18:00",
                "19:00",
                "20:00",
                "21:00",
                "22:00",
                "23:00",
            ],
            "area": [-65, 20, -72, 60],
            "format": "netcdf",
        },
        str(OUTPUT_FILE),
    )

    print(f"ERA5 download completed: {OUTPUT_FILE}")


if __name__ == "__main__":
    download_era5()

