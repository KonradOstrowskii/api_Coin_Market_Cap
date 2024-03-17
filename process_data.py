import pandas as pd
import json
import re


def read_and_process_data():
    """Reads data from 'crypto_data.json', converts it to DataFrame, formats supply, and adds market_cap_dominance."""

    # Read data from JSON file
    with open("crypto_data.json", "r") as f:
        data = json.load(f)

    # Process data
    for item in data["data"]:
        item["market_cap_dominance"] = item["quote"]["USD"]["market_cap_dominance"]
        item["price"] = item["quote"]["USD"]["price"]
    df = pd.DataFrame(data["data"])

    # Select desired columns
    df = df[["name", "symbol", "price", "circulating_supply", "total_supply", "max_supply", "market_cap_dominance"]]
    
    def format_supply(value):
        if value >= 1e9:  # Billions
            return f"{value / 1e9:.2f} B"
        elif value >= 1e6:  # Millions
            return f"{value / 1e6:.2f} M"
        else:
            return str(value)
        
    def format_dominance(value):
        if 'market_cap_dominance' in df.columns:
            return f"{value:.2f} %"
    

    def extract_decimal(input_float):
        integer_part, decimal_part = str(input_float).split('.')
        return f"{integer_part}.{decimal_part[:2]}"


    df["circulating_supply"] = df["circulating_supply"].apply(format_supply)
    df["total_supply"] = df["total_supply"].apply(format_supply)
    df["max_supply"] = df["max_supply"].fillna(0)
    df["market_cap_dominance"] = df["market_cap_dominance"].apply(format_dominance)
    df["price"] = df["price"].apply(extract_decimal)
    

    return df


if __name__ == "__main__":
    df = read_and_process_data()
    print(df.head())
