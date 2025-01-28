import uuid
import asyncio
from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

tasks = {}

async def long_task(task_id: str):
    # Simulate a long-running task
    await asyncio.sleep(30)
    tasks[task_id] = "completed"

@app.put("/long_task", status_code=202)
async def start_long_task(background_tasks: BackgroundTasks):
    task_id = str(uuid.uuid4())
    tasks[task_id] = "in_progress"
    
    background_tasks.add_task(long_task, task_id)
    
    return JSONResponse(content={"task_id": task_id}, status_code=202)

@app.get("/long_task/{task_id}")
async def get_task_status(task_id: str):
    task_status = tasks.get(task_id, "not_found")
    
    if task_status == "not_found":
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"task_id": task_id, "status": task_status}
