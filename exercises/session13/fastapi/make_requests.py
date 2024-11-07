import requests

item = "Buy Groceries"
item2 = "Ir ás compras"
item_id = 1
new_item = "Ir ao cinema"

# Send a POST request to add the item
post = requests.post("http://127.0.0.1:8000/items/", params={"item": item})
post2 = requests.post("http://127.0.0.1:8000/items/", params={"item": item2})

# Send a DELETE request to delete the item
delete = requests.delete(f"http://127.0.0.1:8000/items/{item_id}")

# Send a GUET request to get the items
get = requests.get("http://127.0.0.1:8000/items/")
print(get.json())

# Send a PUT request to update the item
put = requests.put(f"http://127.0.0.1:8000/items/{item_id}", params={"update_item": item})
put.json()
