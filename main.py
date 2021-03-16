import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from tasks import create_todo_item

logger = logging.getLogger(__name__)

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
    logger.info(f"Received request: {todo_item}")
    create_todo_item.run(todo_details=todo_item)
    return todo
