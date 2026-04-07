import requests


def get_lat_and_long_from_postcode(postcode):
    url = f"https://api.postcodes.io/postcodes/{postcode}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == 200:
            result = data["result"]
            return [result["latitude"], result["longitude"]]

    raise ValueError(f"Could not retrieve latitude and longitude for postcode: {postcode}")
