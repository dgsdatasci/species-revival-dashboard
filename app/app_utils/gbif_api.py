import requests

def get_species_occurrences(species_name):
    url = f"https://api.gbif.org/v1/occurrence/search?scientificName={species_name}&limit=100"
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None
