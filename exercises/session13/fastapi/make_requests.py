import requests

new_item = {'description': 'Passear o cao', 'is_completed': False}
item_id = 2

# Send a POST request to add the item
response = requests.put(f"http://127.0.0.1:8000/items/{item_id}", json=new_item)
#response = requests.post(f"http://127.0.0.1:8000/items/", json=new_item)
print(response.text)