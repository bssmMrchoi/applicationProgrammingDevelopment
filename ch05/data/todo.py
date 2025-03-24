from sqlite3 import IntegrityError
from typing import List

from ch05.data import cur, con
from ch05.error import Duplicate, Missing
from ch05.model.todo import TodoResponse, Todo

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS todos (
        todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL UNIQUE,
        completed INTEGER NOT NULL DEFAULT 0,
        created_at TEXT NOT NULL DEFAULT (datetime('now', 'localtime'))
    )
    """
)


def row_to_model(entity: tuple) -> TodoResponse:
    todo_id, task, completed, created_at = entity
    return TodoResponse(
        todo_id=todo_id,
        task=task,
        completed=completed,
        created_at=created_at
    )


def find_all() -> List[TodoResponse]:
    query = "select * from todos"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]


def insert_one(todo: Todo) -> TodoResponse:
    query = "insert into todos(task) values(:task)"
    param = todo.model_dump()
    try:
        cur.execute(query, param)
        con.commit()
    except IntegrityError as e:
        print(e)
        raise Duplicate(msg=f"{todo.task} already exists")

    todo_id = cur.lastrowid # excute 한 테이블의 마지막 행 id 값을 가져와주는데
    cur.execute(f"SELECT * FROM todos WHERE todo_id = {todo_id}")
    return row_to_model(cur.fetchone())


def get_one(todo: Todo) -> TodoResponse:
    cur.execute("SELECT * FROM todos WHERE task = :task", todo.model_dump())
    row = cur.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"{todo.task} not found")


def modify_completed(todo: Todo) -> TodoResponse:
    query = "update todos set completed = not completed where task=:task"
    param = todo.model_dump()
    cur.execute(query, param)
    con.commit()

    if cur.rowcount == 1:
        return get_one(todo)
    else:
        raise Missing(msg=f"{todo.task} not found")


def delete(todo: Todo) -> bool:
    """할일을 삭제한다. 만약 대상이 없다면 None을 반환한다."""
    query = "delete from todos where task = :task"
    param = todo.model_dump()
    cur.execute(query, param)
    con.commit()

    if cur.rowcount != 1:
        raise Missing(msg=f"{todo.task} not found")

    return True
