from fastapi import FastAPI, Cookie
from pydantic import BaseModel
from enum import Enum
from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field
from body import *
import os
os.system('python body.py')

app = FastAPI()

from fastapi import FastAPI, Path, Query, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Image(BaseModel):
    name: str
    desc: str | None = Field(alias="image", min_length=2, default="ok", example="23")

class Item(BaseModel):
    name: str
    age: int
    tax: float | None = None
    desc: str | None = None
    images: list[Image] | None = None


@app.post("/books/{item_id}")
async def find_book(item: Item = Body(embed=True), item_id: int = Cookie(default=1), q: int = Query(gt=2, default="hoangnt")):
    return item.dict()







