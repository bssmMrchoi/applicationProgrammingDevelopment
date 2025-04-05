from typing import List

from . import con, cur
from ch06_department.model.student import StudentResponse, AssignDepartment

cur.executescript(
    """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        score REAL NOT NULL DEFAULT 0,
        department_id int,
        foreign key(department_id) references departments(id)
    );
    INSERT OR IGNORE INTO students(id, name, score) VALUES (2100, 'choi', 98.5);
    INSERT OR IGNORE INTO students(id, name, score) VALUES (2200, 'jung', 99.5);
    """
)


def row_to_model(entity: tuple) -> StudentResponse:
    id, name, score, department_id = entity
    return StudentResponse(
        id=id,
        name=name,
        score=score,
        department_id=department_id
    )


def find_all() -> List[StudentResponse]:
    query = "select * from students"
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]


def find_one(student_id: int) -> StudentResponse:
    query = f"select * from students where id={student_id}"
    cur.execute(query)
    dto = row_to_model(cur.fetchone())
    return dto


def update(dto: AssignDepartment) -> StudentResponse:
    # _student = find_one(dto.student_id)
    # _student.department_id = dto.department_id
    query = "update students set department_id=:department_id where id=:student_id"
    cur.execute(query, dto.model_dump())
    con.commit()

    result = find_one(dto.student_id)
    return result
