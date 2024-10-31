import requests

url = 'http://127.0.0.1:8000/items'
data = {'item': 'Buy groceries'}

response = requests.post(url, data=data)
print(response.json())