from fastapi import FastAPI

app = FastAPI()

todo_list =[]

@app.get("/")
def root():
    return {"message": "Hello world"}

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
        return {"message": "Item not found"}