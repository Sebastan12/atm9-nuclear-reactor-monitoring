from typing import Union
from prometheus_client import Counter, Gauge, make_asgi_app
from fastapi import FastAPI

app = FastAPI()
metric_app = make_asgi_app()
app.mount("/metrics", metric_app)

URANIUM_INGOT_GAUGE = Gauge(
    "ae2_uranium_ingot_quantity",
    "Current quantity of uranium ingots in the AE2 storage system"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/uranium-ingot-stock/")
def create_item(item_stock: int):
    URANIUM_INGOT_GAUGE.set(item_stock)
    return {"item_stock": item_stock}