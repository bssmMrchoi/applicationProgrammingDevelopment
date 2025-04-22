from typing import List

from sympy.polys.polyconfig import query

from . import con, cur
from ch06_school.model.student import StudentResponse, AssignDepartment, Student
from ..model.department import Department, DepartmentResponse

cur.executescript(
    """
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score REAL NOT NULL DEFAULT 0,
        department_id INTEGER,
        foreign key(department_id) references department(id)
    );
    INSERT OR IGNORE INTO student(id, name, score, department_id) VALUES (2000, 'choi', 98.5, 1);
    INSERT OR IGNORE INTO student(id, name, score) VALUES (2001,'jung', 99.5);
    PRAGMA foreign_keys = ON;
    """
)


def row_to_model(entity: tuple) -> StudentResponse:
    print(entity)
    id, name, score, d_name = entity
    if d_name is None:
        return StudentResponse(
            id=id,
            name=name,
            score=score
        )
    return StudentResponse(
        id=id,
        name=name,
        score=score,
        department=Department(name=d_name)
    )


def find_all() -> List[StudentResponse]:
    query = ("select s.id, s.name, s.score, d.name "
             "from student s left join department d on d.id = s.department_id order by score")
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]

def find_by_dept_id_score_desc(department_id: int) -> List[StudentResponse]:
    query = ("select s.id, s.name, s.score, d.name "
             f"from student s left join department d on d.id = s.department_id where department_id = {department_id} order by score desc")
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]


def find_by_id(student_id: int) -> StudentResponse:
    query = (f"select s.id, s.name, s.score, d.name "
             f"from student s left join department d on d.id = s.department_id "
             f"where s.id={student_id}")
    cur.execute(query)
    row = cur.fetchone()
    if row is None:
        return None
    return row_to_model(row)


def save(student: Student) -> StudentResponse:
    query = "insert into student(name, score) values (:name, :score)"
    cur.execute(query, student.model_dump())
    con.commit()
    new_id = cur.lastrowid
    return find_by_id(new_id)


def update(dto: AssignDepartment) -> StudentResponse:
    # _student = find_one(dto.student_id)
    # _student.department_id = dto.department_id
    query = "update student set department_id=:department_id where id=:student_id"
    cur.execute(query, dto.model_dump())
    con.commit()

    result = find_by_id(dto.student_id)
    return result
