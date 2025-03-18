from datetime import datetime

from pydantic import BaseModel


class Todo(BaseModel):
    task: str
    completed: int


class TodoResponse(Todo):
    todo_id: int
    created_at: datetime


class TodoInsertRequest(BaseModel):
    task: str


class TodoRequest(BaseModel):
    completed: int