from fastapi import FastAPI, Cookie
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field
from enum import Enum

class Item(BaseModel):
    name: str
    age: int
    tax: float | None = None
    desc: str | None = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World 2"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


class NameModel(str, Enum):
    en="en"
    vn="vn"


@app.get("/{model_name}")
async def root2(model_name : NameModel):
    if (model_name == NameModel.en):  return {"model_name": model_name, "message": "Excellent"}
    if (model_name == NameModel.vn):  return {"model_name": model_name, "message": "ExcellentVN"}


@app.get("/book/{item_id}")
async def read_book(item_id: int):
    return {"item_id": item_id}


@app.post("/books/{item_id}")
async def create_book(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name}


@app.put("/books/{item_id}")
async def update_book(item_id: int, item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.age + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict