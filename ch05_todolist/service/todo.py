# from ch05_todolist.data import todo as data
from ch05_todolist.fake import todo as data
from ch05_todolist.ml.predictor import predict_category
from ch05_todolist.model.todo import Todo, TodoResponse


def find_all() -> list[TodoResponse]:
    return data.find_all()


def insert_one(todo: Todo) -> TodoResponse:
    print(predict_category(todo.task))
    return data.insert_one(todo)


def get_one(todo_id: int) -> TodoResponse:
    return data.get_one(todo_id)


def modify_completed(todo_id: int) -> TodoResponse:
    return data.modify_completed(todo_id)


def delete(todo_id: int) -> bool:
    return data.delete(todo_id)
