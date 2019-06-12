import json
import requests
import os
from django.http import JsonResponse

def get_json(url):
    body = requests.get(url).content
    return json.loads(body)

def pokemon_show(requests, id):
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
    pokemon = get_json(api_url)
    poke_id = (pokemon["id"])
    poke_name = (pokemon["name"])
    poke_types = (pokemon["types"])
    KEY = os.environ.get("GIPHY_KEY")
    search_results = get_json(f"https://api.giphy.com/v1/gifs/search?api_key={KEY}&q={poke_name}&rating=g")
    url1 = search_results['data'][0]['url']
    poke_type_name = []
    for typ in poke_types:
         poke_type_name.append(typ['type']['name'])
        
    return JsonResponse({'id': poke_id, 'name': poke_name, 'types':poke_type_name, 'gif': url1})