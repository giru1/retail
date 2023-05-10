from typing import Union, List
from pydantic import BaseModel
from fastapi import FastAPI
from dao.model.company import Company

app = FastAPI(
    title='Rig-line'
)


@app.get("/", response_model=List[Company])
def read_root():
    return {"Hello": "World"}


@app.post("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# @app.update("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
