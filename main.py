from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import platform

app = FastAPI()


class Item(BaseModel):
    text: str = None
    is_done: bool = False


items = []


@app.get("/")
def root():
    print("This request is being served by server: " + platform.node())

    return {"Hello": "World"}


@app.post("/items")
def create_item(item: Item):
    print("This request is being served by server: " + platform.node())

    items.append(item)
    return items


@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    print("This request is being served by server: " + platform.node())

    return items[0:limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    print("This request is being served by server: " + platform.node())

    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
        
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int) -> Item:
    print("This request is being served by server: " + platform.node())

    if item_id < len(items):
        item = items.pop()
        return item
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")
