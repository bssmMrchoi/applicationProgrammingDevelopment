import sqlite3
from typing import List

from fastapi import HTTPException

from . import con, cur
from ch06_school.model.department import DepartmentResponse, DepartmentRequest
from ..error import Missing, Duplicate

cur.executescript(
    """
    CREATE TABLE IF NOT EXISTS department (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        quota INTEGER NOT NULL DEFAULT 0,
        description TEXT
    );
    INSERT OR IGNORE INTO department(name, quota) VALUES ('sw', 32);
    INSERT OR IGNORE INTO department(name, quota) VALUES ('embedded sw', 32);
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
    query = "select * from department"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]


def find_by_id(department_id: int) -> DepartmentResponse:
    query = f"select * from department where id={department_id}"
    cur.execute(query)
    row = cur.fetchone()
    if row:
        return row_to_model(row)
    else:
        # raise HTTPException(status_code=404, detail=f'dept id = {department_id} not found')
        raise Missing(msg=f"{department_id} not found")


def save(department: DepartmentRequest):
    query = "insert into department(name, quota, description) values(:name, :quota, :description)"
    try:
        cur.execute(query, department.model_dump())
        con.commit()
    except sqlite3.IntegrityError:
        raise Duplicate(msg=f"{department.name} is duplicate")

def update(department_id: int, request_dto: DepartmentRequest):
    query = f"update department set quota=:quota where id={department_id}"
    cur.execute(query, request_dto.model_dump())
    con.commit()
    print(cur.fetchone())

def delete(department_id: int) -> bool:
    query = f"delete from department where id={department_id}"
    cur.execute(query)
    con.commit()
    if cur.rowcount == 0:
        raise Missing(msg=f"{department_id} already delete")
    return True
