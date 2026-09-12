from pathlib import Path
import io

import pandas as pd
import requests


URL = "https://usicecenter.gov/File/DownloadCurrent?pId=134"

OUTPUT_DIR = Path("data/raw/iceberg")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

RAW_FILE = OUTPUT_DIR / "usnic_current_icebergs.csv"
PROCESSED_FILE = OUTPUT_DIR / "antarctic_icebergs_current.csv"


def download_iceberg_data():
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    RAW_FILE.write_bytes(response.content)

    print("Download successful.")
    print(f"Raw file: {RAW_FILE}")
    print(f"Size: {len(response.content)} bytes")


def process_iceberg_data():
    df = pd.read_csv(
        io.BytesIO(RAW_FILE.read_bytes()),
        encoding="utf-8-sig",
    )

    # Keep only the fields required by our project
    df = df.rename(
        columns={
            "Iceberg": "iceberg_id",
            "Latitude": "latitude",
            "Longitude": "longitude",
            "Last Update": "time",
        }
    )

    df = df[
        [
            "iceberg_id",
            "time",
            "latitude",
            "longitude",
        ]
    ]

    df["time"] = pd.to_datetime(
        df["time"],
        format="%m/%d/%Y",
        errors="coerce",
    )

    df = df.dropna(
        subset=["iceberg_id", "time", "latitude", "longitude"]
    )

    df.to_csv(PROCESSED_FILE, index=False)

    print("Processing successful.")
    print(f"Processed file: {PROCESSED_FILE}")
    print(f"Number of iceberg records: {len(df)}")

    print("\nSample:")
    print(df.head())


if __name__ == "__main__":
    download_iceberg_data()
    process_iceberg_data()

