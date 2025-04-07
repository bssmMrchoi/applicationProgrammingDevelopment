from typing import List

from ch06_school.model.student import StudentResponse, AssignDepartment

_students = [
    StudentResponse(
        id=2100,
        name='kim',
        score=99.8,
    ),
    StudentResponse(
        id=2200,
        name='jung',
        score=99.9,
    ),
]


def find_all() -> List[StudentResponse]:
    return _students


def find_one(student_id: int) -> StudentResponse:
    _student = next((x for x in _students if x.id == student_id), None)
    if _student is None:
        raise ValueError(f"{student_id} not in")
    return _student


def update(dto: AssignDepartment) -> StudentResponse:
    # _student = next((x for x in _students if x.id == dto.student_id), None)
    # if _student is None:
    #     raise ValueError(f"{dto.student_id} not in")

    _student = find_one(dto.student_id)
    _student.department_id = dto.department_id
    print(_students)

    return _student
