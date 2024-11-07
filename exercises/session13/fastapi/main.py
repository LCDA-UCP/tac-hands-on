from fastapi import FastAPI


app = FastAPI()


todo_list = []
def root():
    return {"message": "Hello World"}

@app.get("/items")
def create_item(item: str):
    todo_list.append(item)
    return {"message": f"Item {item} added successfully\n"}






