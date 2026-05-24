from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Temporary in-memory storage for now
tasks = []
counter = {"id": 1}

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

@app.get("/")
def home():
    return {"message": "Task Manager API is live!"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(task: Task):
    new_task = task.dict()
    new_task["id"] = counter["id"]
    counter["id"] += 1
    tasks.append(new_task)
    return {"message": "Task created", "task": new_task}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")
