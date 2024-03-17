import requests
import json
import os

# API Settings
api_key = "1e4c09c2-3be3-4abc-949d-fb9eb5900456"

# API URL with parameters
url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
params = {
    "limit": 100,  # Get the top 100 cryptocurrencies
}

# Request Headers
headers = {
    "X-CMC_PRO_API_KEY": api_key,
}


def fetch_crypto_data():
    """Fetches data from CoinMarketCap API and returns it as a dictionary."""

    # Make the request
    response = requests.get(url, headers=headers, params=params)

    # Check for errors
    if response.status_code != 200:
        print("Error:", response.status_code)
        exit()

    # Get data
    data = json.loads(response.content)
    return data


if __name__ == "__main__":
    crypto_data = fetch_crypto_data()

    # Save data to JSON file (optional)
    with open("crypto_data.json", "w") as f:
        json.dump(crypto_data, f)

    print("Data fetched and saved to crypto_data.json")
