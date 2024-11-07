from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

todo_list = []

class TODOITEM(BaseModel):
    item_id: int
    item: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/items")
def create_item(item: str):
    todo_list.append(item)
    return {"message": f"Item {item} added successfully\n"}

@app.get("/items")
def get_items():
    return {"todo_list": todo_list}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id < len(todo_list):
        return {"item": todo_list[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found!")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < len(todo_list):
        del todo_list[item_id]
        return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found!")

@app.put("/items")
def update_item(item: TODOITEM):
    if item.item_id < len(todo_list):
        todo_list[item.item_id] = item.item
        return {"message": "Item updated"}
    raise HTTPException(status_code=404, detail=f"Item with ID {item.item_id} not found!")