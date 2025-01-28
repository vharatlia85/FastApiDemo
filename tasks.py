from celery_config import app
import time

@app.task
def long_task(x, y):
    time.sleep(10)  # Simulate a long-running task
    return x + y
