import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'a260f4fdd3102c87548aa1526ed492f9'
HEADER =  {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_pokemons = {
    "name": "bulba",
    "photo_id": 7
}

new_name = {
    "pokemon_id": "70514",
    "name": "bulbazavr",
    "photo_id": 2
}

add_pokeball = {
    "pokemon_id": "70514"
}


'''response_pokemons = requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_pokemons)
print(response_pokemons.text)'''

'''response_name = requests.put(url=f'{URL}/pokemons', headers=HEADER, json=new_name)
print(response_name.text)'''

response_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=new_name)
print(response_pokeball.text)