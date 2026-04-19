import requests


def get_lat_and_long_from_postcode(postcode):
    print("Using postcodes_io_client for coordinates")
    url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == 200:
            result = data["result"]
            return [result["latitude"], result["longitude"]]
    else:
        return [0.0, 0.0]  # Default value if the API call fails or returns an error
