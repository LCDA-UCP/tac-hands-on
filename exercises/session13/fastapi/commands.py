import requests

item = {"description": "Lavar a loica", "is_completed": False}

response = requests.post(f'http://127.0.0.1:8000/items/', json=item)
print(response.json())

