import requests


response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
                       json={
                            "name": "Шпротик",
                            "photo": "https://dolnikov.ru/pokemons/albums/001.png"
                            },
                        headers={'Content-Type': 'application/json', 'trainer_token': 'bb3d2e4d46de603d052506e90c28d9bf'}, timeout=5)


print(f'Message: {response.text} ')

response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
                       json={
                           "pokemon_id": "20929",
                           "name": "Котик",
                           "photo": "https://dolnikov.ru/pokemons/albums/008.png"
                            },
                        headers={'Content-Type': 'application/json', 'trainer_token': 'bb3d2e4d46de603d052506e90c28d9bf'}, timeout=5)


print(f'Message: {response.text} ')


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                       json={
                           "pokemon_id": "20929"
                            },
                        headers={'Content-Type': 'application/json', 'trainer_token': 'bb3d2e4d46de603d052506e90c28d9bf'}, timeout=5)


print(f'Message: {response.text} ')