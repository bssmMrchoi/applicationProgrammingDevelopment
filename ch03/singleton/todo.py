from ch03.model import Todo
from . import db, con, cur


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


def row_to_model(entity: tuple) -> Todo:
    index, task, completed, created_at = entity
    return Todo(
        task=task,
        completed=completed
    )


def find_all():
    query = "select * from todos"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]


def insert_one(task: str):
    con1 = db.get_connection()
    cur1 = con1.cursor()
    query = f"insert into todos(task) values('{task}')"
    cur1.execute(query)
    con1.commit()
