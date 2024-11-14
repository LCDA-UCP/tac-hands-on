import requests

task = "Buy groceries"

reponse = requests.get('127.0.0.1:8000/items')
print(response.text)
