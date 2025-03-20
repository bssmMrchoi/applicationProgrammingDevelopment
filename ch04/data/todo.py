from typing import List

from . import con, cur
from ..model import Todo, TodoResponse

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS todos (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL UNIQUE,
        completed INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
    )
    """
)


def row_to_model(entity: tuple) -> TodoResponse:
    task_id, task, completed, created_at = entity
    return TodoResponse(
        task_id=task_id,
        task=task,
        completed=completed,
        created_at=created_at
    )


def find_all() -> List[TodoResponse]:
    query = "select * from todos"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]


def insert_one(task: Todo):
    query = "insert into todos(task) values(:task)"
    cur.execute(query, task.model_dump())
    con.commit()
