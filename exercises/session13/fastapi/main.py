import json
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
class TodoItem(BaseModel):
    description: str
    is_completed: bool = False
def root():
    return {"message": "Hello World"}
todo_list = []

@app.post("/items")
def create_item(item: TodoItem):
    todo_list.append(item.dict())
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)
    return {"message": f"Item {item.description} added successfully\n"}
@app.get("/items")
def get_items():
    return {"todo_list": todo_list}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(todo_list):
        return {"item": todo_list[item_id]}
    else:
        return {"message": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(todo_list):
        del todo_list[item_id]
        return {"message": "Item deleted"}
    raise HTTPException(status_code=400, detail="Item not found")