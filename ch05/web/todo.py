from fastapi import FastAPI, Request, APIRouter

from ch05.service import todo as service
from ch05.model.todo import Todo, TodoResponse

router = APIRouter(prefix="/todo")


@router.get('/')
def get_all() -> list[TodoResponse]:
    return service.find_all()


@router.post('/')
def insert_one(todo: Todo) -> Todo:
    return service.insert_one(todo)
