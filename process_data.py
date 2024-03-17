import pandas as pd
import json

def read_and_process_data():
    """Reads data from 'crypto_data.json', converts it to DataFrame, and formats circulating supply."""

    # Read data from JSON file
    with open("crypto_data.json", "r") as f:
        data = json.load(f)

    # Process data
    df = pd.DataFrame(data["data"])

    # Select desired columns (ID renamed to cmc_id for clarity)
    df = df[["id", "name", "symbol", "slug", "circulating_supply"]]
    df.rename(columns={"id": "cmc_id"}, inplace=True)

    # Convert circulating supply to human-readable format (millions/billions)
    def format_supply(value):
        if value >= 1e9:  # Billions
            return f"{value / 1e9:.2f} B"
        elif value >= 1e6:  # Millions
            return f"{value / 1e6:.2f} M"
        else:
            return str(value)

    df["circulating_supply"] = df["circulating_supply"].apply(format_supply)

    return df


if __name__ == "__main__":
    df = read_and_process_data()

    # Display Data (showing the first 5 rows by default)
    print(df.head())
