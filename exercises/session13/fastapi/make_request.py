import requests

new_item = {'description': 'Lavar a loiça', 'is_completed': False}

response = requests.post(f'http://127.0.0.1:8000/items', json = new_item)
print(response.json())
