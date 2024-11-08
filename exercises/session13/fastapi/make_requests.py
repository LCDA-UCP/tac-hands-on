import requests

new_item = {'description': 'Lavar as loiça', 'is_completed': False}

#Send a Post to add the item
response = requests.post(f"http://127.0.0.1:8000/items", json=new_item)
print(response.text)
