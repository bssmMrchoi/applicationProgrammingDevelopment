# from ch05.data import todo as data
from ch05.fake import todo as data
from ch05.ml.predictor import predict_category
from ch05.model.todo import Todo, TodoResponse


def find_all() -> list[TodoResponse]:
    return data.find_all()


def insert_one(todo: Todo) -> TodoResponse:
    print(predict_category(todo.task))
    return data.insert_one(todo)


def get_one(todo: Todo) -> TodoResponse:
    return data.get_one(todo)


def modify_completed(todo: Todo) -> TodoResponse:
    return data.modify_completed(todo)


def delete(todo: Todo) -> bool:
    return data.delete(todo)
