from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world"}


@app.post("/items")
def create_item(item: str):
    todo_list.append(item)
    return {"message": f"Item {item} added successfully\n"}