from typing import List

from fastapi import FastAPI, Request, APIRouter, HTTPException

from ch05.error import Duplicate, Missing
from ch05.service import todo as service
from ch05.model.todo import Todo, TodoResponse

router = APIRouter(prefix="/todo")


#307 Temporary Redirect는 POST 요청을 유지하면서 리디렉트할 때 발생
# / -> 없앰
# @router.get('/')
@router.get('')
def get_all() -> List[TodoResponse]:
    return service.find_all()


@router.post('')
def insert_one(todo: Todo) -> TodoResponse:
    try:
        return service.insert_one(todo)
    except Duplicate as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.get('/{task}')
def get_one(task: str) -> TodoResponse:
    try:
        return service.get_one(Todo(task=task))
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


# completed 만 변경
@router.patch('/{task}')
def modify_completed(task: str) -> TodoResponse:
    try:
        return service.modify_completed(Todo(task=task))
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete("/{task}")
def delete(task: str) -> bool:
    try:
        return service.delete(Todo(task=task))
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
