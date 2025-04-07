from typing import Optional

from pydantic import BaseModel


class Student(BaseModel):
    name: str


class StudentResponse(Student):
    id: int
    score: float
    department_id: Optional[int] = None


class AssignDepartmentId(BaseModel):
    department_id: int


class AssignDepartment(AssignDepartmentId):
    student_id: int
