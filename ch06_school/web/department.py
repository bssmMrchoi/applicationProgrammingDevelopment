from fastapi import APIRouter, Path, Body, HTTPException, status

from ch06_school.data import department as data
from ch06_school.error import Duplicate, Missing
from ch06_school.service import department as service
from ch06_school.model.department import DepartmentRequest

router = APIRouter(prefix="/departments")


@router.get("")
def get_all():
    return data.find_all()


@router.get("/{dept_id}")
def get_by_id(dept_id: int = Path(...)):
    try:
        return data.find_by_id(dept_id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.post("", status_code=status.HTTP_201_CREATED)
def create(department: DepartmentRequest = Body()):
    try:
        data.save(department)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


@router.patch("/{dept_id}")
def update(dept_id: int = Path(...), request_dto: DepartmentRequest = Body()):
    return data.update(dept_id, request_dto)



@router.delete("/{dept_id}")
def delete(dept_id: int = Path(...)) -> bool:
    try:
        return data.delete(dept_id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
