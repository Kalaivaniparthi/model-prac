from pathlib import Path

import pandas as pd


DATA_FILE = Path("data/raw/iceberg/antarctic_icebergs_current.csv")


def verify_iceberg_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"File not found: {DATA_FILE}")

    df = pd.read_csv(DATA_FILE)

    required_columns = {
        "iceberg_id",
        "time",
        "latitude",
        "longitude",
    }

    missing_columns = required_columns - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    print("Dimensions:", df.shape)
    print("Columns:", list(df.columns))

    print("\nTime range:")
    print("Start:", df["time"].min())
    print("End:", df["time"].max())

    print("\nLatitude:")
    print("Min:", df["latitude"].min())
    print("Max:", df["latitude"].max())

    print("\nLongitude:")
    print("Min:", df["longitude"].min())
    print("Max:", df["longitude"].max())

    print("\nMissing values:")
    print(df.isna().sum())

    print("\nNumber of unique icebergs:")
    print(df["iceberg_id"].nunique())

    print("\nSample:")
    print(df.head())

    print("\nVerification successful.")


if __name__ == "__main__":
    verify_iceberg_data()

