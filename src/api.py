from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Meraki Cache API", description="API for caching Meraki data", version="1.0.0")


# Define a data schema for request/response validation
class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None


# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Endpoint with path and optional query parameters
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

# Endpoint accepting a JSON request body
@app.post("/items/")
def create_item(item: Item):
    return {"item_name": item.name, "price": item.price}
