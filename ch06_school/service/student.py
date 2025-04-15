from typing import List

from ch06_school.error import StudentNotFoundException
from ch06_school.model.student import StudentResponse, AssignDepartment, Student
from ch06_school.data import student as student_dao
from ch06_school.data import department as department_dao


def find_all() -> List[StudentResponse]:
    return student_dao.find_all()

def get_by_id(student_id: int) -> StudentResponse:
    _student = student_dao.find_by_id(student_id)
    if _student is None:
        raise StudentNotFoundException(student_id)
    return _student

def save(student: Student) -> StudentResponse:
    return student_dao.save(student)

def assign_department(assign_dto: AssignDepartment) -> StudentResponse:
    department = department_dao.find_one(assign_dto.department_id)



    if department.quota <= 0:
        raise ValueError("Department is full")

    student = student_dao.update(assign_dto)

    return student
