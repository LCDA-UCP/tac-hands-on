import json
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the Pydantic model for todo items
class TodoItem(BaseModel):
    description: str
    completed: bool = False

# Initialize the todo list and load existing items if the file exists
todo_list = []

if os.path.exists("todo_list.json"):
    with open("todo_list.json", "r") as file:
        todo_list = [TodoItem(**item) for item in json.load(file)]

# Save todo_list to JSON file
def save_todo_list():
    with open("todo_list.json", "w") as file:
        json.dump([item.dict() for item in todo_list], file)

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items")
def get_items():
    return {"todo_list": todo_list}

# curl -X GET "http://127.0.0.1:8000/items"

# import requests
#
# response = requests.get("http://127.0.0.1:8000/items")
# print(response.json())

@app.post("/items")
def create_item(item: TodoItem):
    todo_list.append(item)
    save_todo_list()
    return {"message": f'Item "{item.description}" added successfully!', "item": item}

# curl -X POST "http://127.0.0.1:8000/items" -H "Content-Type: application/json" -d "{\"description\": \"New task\", \"completed\": false}"

# import requests
#
# new_item = {"description": "New task", "completed": False}
# response = requests.post("http://127.0.0.1:8000/items", json=new_item)
# print(response.json())

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(todo_list):
        return {"item": todo_list[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# curl -X GET "http://127.0.0.1:8000/items/0"

# import requests
#
# item_id = 0
# response = requests.get(f"http://127.0.0.1:8000/items/{item_id}")
# print(response.json())

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(todo_list):
        removed_item = todo_list.pop(item_id)
        save_todo_list()
        return {"message": f'Item "{removed_item.description}" deleted successfully!'}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# curl -X DELETE "http://127.0.0.1:8000/items/0"

# import requests
#
# item_id = 0
# response = requests.delete(f"http://127.0.0.1:8000/items/{item_id}")
# print(response.json())


@app.put("/items/{item_id}")
def update_item(item_id: int, update_data: TodoItem):
    if item_id < len(todo_list):
        old_item = todo_list[item_id]
        todo_list[item_id] = update_data
        save_todo_list()
        return {"message": f'Item "{old_item.description}" updated successfully!', "updated_item": update_data}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# curl -X PUT "http://127.0.0.1:8000/items/0" -H "Content-Type: application/json" -d "{\"description\": \"Updated task\", \"completed\": true}"

# import requests
#
# item_id = 0
# update_data = {"description": "Updated task", "completed": True}
# response = requests.put(f"http://127.0.0.1:8000/items/{item_id}", json=update_data)
# print(response.json())
