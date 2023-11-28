import requests
import json

response_API = requests.get('https://swapi.dev/api/')

data = response_API.text

parse_json = json.loads(data)

for key, value in parse_json.items():
    res = requests.get(value)
    data = res.text
    array = json.loads(data)
    for key, value in array.items():
        print(key, value)