import requests

item = "Buy Groceries"
response = requests.post(f"http://127.0.0.1:8000/items/", params={"item": item})
print(response.text)