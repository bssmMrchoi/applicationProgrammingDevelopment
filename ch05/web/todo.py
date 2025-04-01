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


@router.get('/{todo_id}')
def get_one(todo_id: int) -> TodoResponse:
    try:
        return service.get_one(todo_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


# completed 만 변경
@router.patch('/{todo_id}')
def modify_completed(todo_id: int) -> TodoResponse:
    try:
        return service.modify_completed(todo_id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)


@router.delete("/{todo_id}")
def delete(todo_id: int) -> bool:
    try:
        return service.delete(todo_id)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
