import uuid
import asyncio
import httpx
from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class LongTaskRequest(BaseModel):
    callback_url: str

tasks: Dict[str, str] = {}
callbacks: Dict[str, str] = {}
steps =["fetching data","processing data","updating database","done"]

async def long_task(task_id: str, callback_url: str):
    for step in steps:
      tasks[task_id] = step
      await asyncio.sleep(20)
      tasks[task_id] = step
    async with httpx.AsyncClient() as client:
     await client.post(callback_url, json={"task_id": task_id, "status": step})

@app.put("/long_task", status_code=202)
async def start_long_task(task_request: LongTaskRequest, background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    tasks[task_id] = "in_progress"
    callbacks[task_id] = task_request.callback_url
    
    background_tasks.add_task(long_task, task_id, task_request.callback_url)
    
    return JSONResponse(content={"task_id": task_id}, status_code=202)

@app.get("/long_task/{task_id}")
async def get_task_status(task_id: str):
    task_status = tasks.get(task_id, "not_found")
    
    if task_status == "not_found":
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"task_id": task_id, "status": task_status}
