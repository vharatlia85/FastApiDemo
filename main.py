from fastapi import FastAPI,HTTPException
from typing import List


app = FastAPI()

items = ["apple", "banana", "cherry"]

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}

@app.get("/items")
def read_all_items():
    return {"items": items}

@app.post("/items")
def add_item(item:str):
    items.append(item)
    return {"message": "Item added successfully", "items": items}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    removed_item = items.pop(item_id)
    return {"message": f"Item '{removed_item}' deleted successfully", "items": items}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: str):
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"message": "Item updated successfully", "items": items}
