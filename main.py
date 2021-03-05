from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from tasks import create_todo_item


class Todo(BaseModel):
    title: str
    completed: Optional[bool] = False
    user_id: int


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def ping():
    return {"Status": "Healthy"}


@app.post("/todos/")
def add_todos(todo: Todo):
    todo_item = {
        "userId": todo.user_id,
        "title": todo.title,
        "completed": todo.completed
    }
    create_todo_item.run(todo_details=todo_item)
    return todo
