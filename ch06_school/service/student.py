from ch06_school.model.student import StudentResponse, AssignDepartment
from ch06_school.data import student as student_dao
from ch06_school.data import department as department_dao


def assign_department(assign_dto: AssignDepartment) -> StudentResponse:
    department = department_dao.find_one(assign_dto.department_id)



    if department.quota <= 0:
        raise ValueError("Department is full")

    student = student_dao.update(assign_dto)

    return student
