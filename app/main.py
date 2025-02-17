from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#coukd get entire item object later and just forward it to prometheus?
@app.post("/items/")
def create_item(item_name: str, item_stock: int):
    return {"item_name": item_name, "item_stock": item_stock}