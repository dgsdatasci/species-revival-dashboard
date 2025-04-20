import requests

API_TOKEN = "p7RzHA8uG89cBhPFeEc8DJ4igu7D6bL6A8oJ"
BASE_URL = "https://apiv3.iucnredlist.org/api/v3"

def get_species_status(species_name):
    url = f"{BASE_URL}/species/{species_name}?token={API_TOKEN}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None
