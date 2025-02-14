import requests
import requests.auth

url = 'http://127.0.0.1:5000/cotacao/'

payload = {
    "tamanho": 120,
    "ano": 2001,
    "garagem": 2
}

auth = requests.auth.HTTPBasicAuth(username='gabriel', password='nichio')

response = requests.post(url, json=payload, auth=auth)

print(response.json())