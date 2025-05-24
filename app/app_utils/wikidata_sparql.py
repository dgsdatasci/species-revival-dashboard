import requests

def get_iucn_status_from_wikidata(scientific_name):
    endpoint = "https://query.wikidata.org/sparql"
    headers = {"Accept": "application/json"}
    query = f"""
    SELECT ?statusLabel WHERE {{
      ?species wdt:P225 "{scientific_name}".
      ?species wdt:P141 ?status.
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }}
    }}
    """

    r = requests.get(endpoint, params={"query": query}, headers=headers)
    if r.status_code == 200:
        results = r.json()
        bindings = results["results"]["bindings"]
        if bindings:
            return bindings[0]["statusLabel"]["value"]
    return "No conservation status found"
