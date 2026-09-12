from pathlib import Path

import requests


STAC_URL = "https://stac.dataspace.copernicus.eu/v1/search"

# Same project region used for our other datasets
BBOX = [20, -72, 60, -65]

# One-day search
DATE = "2026-08-01"

OUTPUT_DIR = Path("data/raw/sar")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

RESULT_FILE = OUTPUT_DIR / "sentinel1_search_results.json"


def search_sentinel1():
    payload = {
        "collections": ["sentinel-1-grd"],
        "bbox": BBOX,
        "datetime": f"{DATE}T00:00:00Z/{DATE}T23:59:59Z",
        "limit": 20,
    }

    response = requests.post(
        STAC_URL,
        json=payload,
        timeout=60,
    )

    response.raise_for_status()

    data = response.json()

    RESULT_FILE.write_text(
        response.text,
        encoding="utf-8",
    )

    features = data.get("features", [])

    print("Sentinel-1 search successful.")
    print(f"Date: {DATE}")
    print(f"BBox: {BBOX}")
    print(f"Products found: {len(features)}")
    print(f"Search result: {RESULT_FILE}")

    for i, item in enumerate(features, start=1):
        properties = item.get("properties", {})

        print(f"\nProduct {i}")
        print("ID:", item.get("id"))
        print("Datetime:", properties.get("datetime"))
        print("Platform:", properties.get("platform"))
        print("Instrument mode:", properties.get("sar:instrument_mode"))
        print("Polarization:", properties.get("sar:polarizations"))


if __name__ == "__main__":
    search_sentinel1()

