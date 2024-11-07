<<<<<<< HEAD
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world"}
=======
import json
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class TodoItem(BaseModel):
    description: str
    is_completed: bool = False

app = FastAPI()

todo_list = []

# Load todo_list from file if it exists
if os.path.exists("todo_list.json"):
    with open("todo_list.json", "r") as file:
        todo_list = json.load(file)

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/items")
def get_items():
    return {"todo_list": todo_list}
>>>>>>> e5e2fd81cb8bf0ada66c5a53f7c56b55c8c44025


@app.post("/items")
def create_item(item: str):
    todo_list.append(item)
<<<<<<< HEAD
    return {"message": f"Item {item} added successfully\n"}
=======
    # Save the updated list to the file
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)
    return {"message": f'Item "{item}" added successfully!'}

@app.get("/items/{item_id}")
def get_itemv1(item_id: int):
    if item_id < len(todo_list):
        return {"item": todo_list[item_id]}
    else:
        return {"message": "Item not found"}

@app.get("/items/{item}")
def get_item(item: int): # -> TodoItem:
    if len(todo_list) < item:
        raise HTTPException(status_code=404, detail=f'Item with index {item} not found!')
    return {"item": todo_list[item]}

@app.delete("/items/{item}")
def delete_item(item: int):
    if len(todo_list) < item:
        raise HTTPException(status_code=404, detail=f'Item with index {item} not found!')
    todo_list.pop(item)
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)
    return {"message": f'Item "{item}" deleted successfully!'}

# curl -X DELETE 'http://127.0.0.1:8000/items/0'

# import requests
#
# item_id = 0
# response = requests.delete(f"http://127.0.0.1:8000/items/{item_id}")
# print(response.json())

@app.put("/items/{item_id}")
def update_item(item_id: int, update_item: str):
    if item_id < len(todo_list):
        old_item = todo_list[item_id]
        todo_list[item_id] = update_item
        with open("todo_list.json", "w") as file:
            json.dump(todo_list, file)
        return {"message": f'Item "{old_item}" updated to "{update_item}" successfully!'}
    else:
        raise HTTPException(status_code=404, detail="Item not found")

# curl -X PUT 'http://127.0.0.1:8000/items/0?update_item=Updated%20task'

# import requests
#
# item_id = 0
# update_text = "Updated task"
#
# # Send a PUT request with the update_item as a query parameter
# response = requests.put(f"http://127.0.0.1:8000/items/{item_id}", params={"update_item": update_text})
#
# # Print the response from the server
# print(response.json())

>>>>>>> e5e2fd81cb8bf0ada66c5a53f7c56b55c8c44025
