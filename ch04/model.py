from datetime import datetime

from pydantic import BaseModel


class Todo(BaseModel):
    task: str


class TodoResponse(Todo):
    task_id: int
    completed: int
    created_at: str