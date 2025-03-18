from ch05.data import todo as data
from ch05.model.todo import Todo, TodoInsertRequest, TodoResponse


def find_all() -> list[TodoResponse]:
    return data.find_all()


def insert_one(todo: TodoInsertRequest) -> TodoResponse:
    return data.insert_one(todo)
