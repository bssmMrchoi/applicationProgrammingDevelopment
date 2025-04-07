from fastapi import APIRouter, Path, Body

from ch06_school.model.student import AssignDepartmentId, StudentResponse, AssignDepartment
from ch06_school.service import student as service

router = APIRouter(prefix="/students")


@router.get("")
def find_all():
    return service.find_all()


@router.patch("/{student_id}")
def update_student(student_id: int = Path(...),
                   dto: AssignDepartmentId = Body(...)) -> StudentResponse:
    _assign = AssignDepartment(student_id=student_id,
                               department_id=dto.department_id)
    _student = service.assign_department(_assign)
    return _student
