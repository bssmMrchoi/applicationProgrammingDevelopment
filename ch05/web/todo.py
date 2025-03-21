from fastapi import FastAPI, Request, APIRouter, HTTPException

from ch05.service import todo as service
from ch05.model.todo import Todo, TodoResponse

router = APIRouter(prefix="/todo")


#307 Temporary Redirect는 POST 요청을 유지하면서 리디렉트할 때 발생
# / -> 없앰
# @router.get('/')
@router.get('')
def get_all() -> list[TodoResponse]:
    return service.find_all()


@router.post('')
def insert_one(todo: Todo) -> Todo:
    return service.insert_one(todo)


@router.get('/{task}')
def get_one(task: str) -> TodoResponse:
    try:
        return service.get_one(Todo(task=task))

    # 모든 예외를 처리하기 때문에 좋진 않다.
    except Exception as e:
        raise HTTPException(status_code=404, detail="Invalid task")
