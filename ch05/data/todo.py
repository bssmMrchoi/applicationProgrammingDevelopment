from typing import List

from ch05.data import cur, con
from ch05.model.todo import TodoResponse, Todo

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
    index, task, completed, created_at = entity
    return TodoResponse(
        todo_id=index,
        task=task,
        completed=completed,
        created_at=created_at
    )


def find_all() -> List[TodoResponse]:
    query = "select * from todos"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]


def insert_one(task: Todo) -> Todo:
    query = "insert into todos(task) values(:task)"
    param = task.model_dump()
    cur.execute(query, param)
    con.commit()

    todo_id = cur.lastrowid # excute 한 테이블의 마지막 행 id 값을 가져와주는데
    cur.execute(f"SELECT * FROM todos WHERE task_id = {todo_id}")
    return row_to_model(cur.fetchone())
