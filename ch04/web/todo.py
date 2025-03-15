from fastapi import FastAPI, Request

from ch04.service import todo as service
from ch04.model.todo import Todo, TodoInsertRequest, TodoResponse

app = FastAPI()


@app.get('/')
def get_all() -> list[TodoResponse]:
    return service.find_all()


@app.post('/')
def insert_one(todo: TodoInsertRequest) -> TodoResponse:
    return service.insert_one(todo)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("todo:app", reload=True)
