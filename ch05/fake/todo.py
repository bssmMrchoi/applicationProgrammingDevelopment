from datetime import datetime

from ch05.error import Missing, Duplicate
from ch05.model.todo import TodoResponse, Todo

_todos = [
    TodoResponse(
        todo_id=0,
        task="study fastapi",
        completed=1,
        created_at="2025-03-01"
    ),
    TodoResponse(
        todo_id=1,
        task="study springboot",
        completed=0,
        created_at="2025-03-01"
    ),
]

task_id=1


def find_all() -> list[TodoResponse]:
    """할일 목록을 반환한다."""
    return _todos


def get_one(todo_id: int) -> TodoResponse:
    """검색한 할일을 반환한다."""
    _todo = next((x for x in _todos if x.todo_id == todo_id), None)
    if _todo is None:
        raise Missing(msg=f"{todo_id} not found")
    return _todo


def insert_one(todo: Todo) -> TodoResponse:
    """할일을 추가한다."""
    global task_id
    if next((x for x in _todos if x.task == todo.task), None):
        raise Duplicate(msg=f"{todo.task} already exists")

    task_id = task_id + 1
    _todos.append(TodoResponse(todo_id=task_id, task=todo.task, completed=0, created_at=datetime.now()))
    return _todos[task_id]


def modify_completed(todo_id: int) -> TodoResponse:
    _todo = next((x for x in _todos if x.todo_id == todo_id), None)
    if _todo is None:
        raise Missing(msg=f"{todo_id} not found")
    _todo.completed = not _todo.completed
    return _todo


def delete(todo_id: int) -> bool:
    """할일을 삭제한다. 만약 대상이 없다면 None을 반환한다."""
    _todo = next((x for x in _todos if x.todo_id == todo_id), None)
    if _todo is None:
        raise Missing(msg=f"{todo_id} not found")

    _todos.remove(_todo)
    return True