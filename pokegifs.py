import json
import requests
import os

# Equivalent to: curl -X GET "http://pokeapi.co/api/v2/pokemon/pikachu/"
# res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
# Parsing the content (string) to JSON (Dict)
# body = json.loads(res.content)

# Helper method for convenience
def get_json(url):
    body = requests.get(url).content
    return json.loads(body)

####################################################################################

pokemon = get_json("http://pokeapi.co/api/v2/pokemon/pikachu/")
print(pokemon["name"]) # should be "pikachu"

poke_id = (pokemon["id"])
poke_name = (pokemon["name"])
poke_types = (pokemon["types"])

####################################################################################

KEY = os.environ.get("GIPHY_KEY")
search_results = get_json(f"https://api.giphy.com/v1/gifs/search?api_key={KEY}&q=pikachu&rating=g")

for key in search_results['data']:
    print(key['url'])

url1 = search_results['data'][0]['url']