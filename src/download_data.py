import copernicusmarine
from pathlib import Path

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

result = copernicusmarine.subset(
    dataset_id="osisaf_obs-si_glo_phy-sic-south_nrt_amsr2_l4_P1D-m",
    variables=["ice_conc"],
    start_datetime="2026-08-01",
    end_datetime="2026-08-10",
    minimum_longitude=20,
    maximum_longitude=25,
    minimum_latitude=-70,
    maximum_latitude=-67,
    output_directory=str(OUTPUT_DIR),
    output_filename="antarctic_sea_ice_2026-08-01_2026-08-10.nc",
)

print("Download completed.")
print(result)
