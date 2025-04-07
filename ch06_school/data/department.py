from typing import List

from fastapi import HTTPException

from . import con, cur
from ch06_school.model.department import DepartmentResponse

cur.executescript(
    """
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        quota INTEGER NOT NULL DEFAULT 0,
        description TEXT
    );
    INSERT OR IGNORE INTO departments(name, quota) VALUES ('sw', 32);
    INSERT OR IGNORE INTO departments(name, quota) VALUES ('embedded sw', 32);
    """
)


def row_to_model(entity: tuple) -> DepartmentResponse:
    id, name, quota, description = entity
    return DepartmentResponse(
        id=id,
        name=name,
        quota=quota,
        description=description
    )


def find_all() -> List[DepartmentResponse]:
    query = "select * from departments"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]


def find_one(department_id: int) -> DepartmentResponse:
    query = f"select * from departments where id={department_id}"
    cur.execute(query)
    row = cur.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise HTTPException(status_code=404, detail=f'dept id = {department_id} not found')
