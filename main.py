from fastapi import FastAPI,HTTPException,BackgroundTasks
from typing import List
from fruitDB import fruits

app = FastAPI()

#Get root
@app.get("/")
async def root():
    return {"Message": "Hello World"}

#get all fruits
@app.get("/fruits")
async def get_fruits():
    return {"fruits":fruits}

#get fruit by id
@app.get("/fruits/{fruit_id}")
async def get_fruit(fruit_id: int):
    try:
        return {"fruit":fruits[fruit_id]}
    except:
        raise HTTPException(status_code=404, detail="Fruit not found")
    
#Add fruit
@app.post("/fruits")
async def add_fruit(fruit: str):
    fruits.append(fruit)
    return {"fruits":fruits}

#insert fruit on specific index
@app.post("/fruits/{fruit_id}")
async def insert_fruit(fruit_id: int, fruit: str):
    try:
        fruits.insert(fruit_id, fruit)
        return {"fruits":fruits}
    except:
        raise HTTPException(status_code=404, detail="Fruit not found")

#Delete fruit 
@app.delete("/fruits/{fruit_id}")
async def delete_fruit(fruit_id: int):
    try:
        fruits.pop(fruit_id)
        return {"fruits":fruits}
    except:
        raise HTTPException(status_code=404, detail="Fruit not found")
    

#update fruit 
@app.put("/fruits/{fruit_id}")
async def update_fruit(fruit_id: int, fruit: str):
    try:
        fruits[fruit_id] = fruit
        return {"fruits":fruits}
    except:
        raise HTTPException(status_code=404, detail="Fruit not found")

