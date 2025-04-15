from typing import List

from fastapi import APIRouter, Path, Body

from ch06_school.model.student import AssignDepartmentId, StudentResponse, AssignDepartment, Student
from ch06_school.service import student as service

router = APIRouter(prefix="/students")


@router.get("")
def find_all() -> List[StudentResponse]:
    return service.find_all()


@router.get("/{student_id}")
def get_by_id(student_id: int) -> StudentResponse:
    return service.get_by_id(student_id)

@router.post("")
def create(student: Student) -> StudentResponse:
    return service.save(student)



@router.patch("/{student_id}")
def update_student(student_id: int = Path(...),
                   dto: AssignDepartmentId = Body(...)) -> StudentResponse:
    _assign = AssignDepartment(student_id=student_id,
                               department_id=dto.department_id)
    _student = service.assign_department(_assign)
    return _student
