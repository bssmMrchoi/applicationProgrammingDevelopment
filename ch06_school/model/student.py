from typing import Optional

from pydantic import BaseModel

from ch06_school.model.department import Department


class Student(BaseModel):
    name: str
    score: float


class StudentResponse(Student):
    id: int
    department: Department = None


class AssignDepartmentId(BaseModel):
    department_id: int


class AssignDepartment(AssignDepartmentId):
    student_id: int
