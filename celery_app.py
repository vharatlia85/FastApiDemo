# celery.py
from celery import Celery
from fruitDB import fruits

app = Celery('tasks', broker='memory://', backend='cache+memory://')

@app.task
def long_task(data):
    # Simulate long processing task
    import time
    time.sleep(10)
    return {"status": "Task completed", "data": data}

