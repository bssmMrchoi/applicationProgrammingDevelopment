from datetime import datetime

from pydantic import BaseModel


class Todo(BaseModel):
    task: str
    completed: int
