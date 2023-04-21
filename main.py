from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI(
    title='Rig-line'
)



class Company:
    pass

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# @app.update("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}