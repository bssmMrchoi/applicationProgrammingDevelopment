from fastapi import FastAPI, Body, Path

from ch06_department.model.student import StudentResponse, AssignDepartment, AssignDepartmentId
from data import student
from data import department
from service import student as student_service

app = FastAPI()


@app.get("/student")
def find_all_student():
    return student.find_all()


@app.patch("/student/{student_id}")
def update_student(student_id: int = Path(...),
                   dto: AssignDepartmentId = Body(...)) -> StudentResponse:
    _assign = AssignDepartment(student_id=student_id,
                               department_id=dto.department_id)
    _student = student_service.assign_department(_assign)
    return _student


@app.get("/department")
def find_all_department():
    return department.find_all()


if __name__ == "__main__":
    import uvicorn
    # reload=True 부분이 있으면 프로세스가 2개(코드 감지용, 실제 fastapi실행) 실행이 됨
    uvicorn.run("main:app", reload=True)
    # uvicorn.run("main:app", host='0.0.0.0')
