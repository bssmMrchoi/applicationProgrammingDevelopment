from typing import List

from . import con, cur
from ..model.todo import Todo, TodoInsertRequest, TodoResponse


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


def insert_one(task: TodoInsertRequest) -> TodoResponse:
    query = "insert into todos(task) values(?)"
    cur.execute(query, (str(task.task),))
    con.commit()
    todo_id = cur.lastrowid
    cur.execute("SELECT * FROM todos WHERE task_id = ?", (todo_id,))
    return row_to_model(cur.fetchone())
