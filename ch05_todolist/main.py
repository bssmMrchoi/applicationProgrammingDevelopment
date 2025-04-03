from fastapi import FastAPI
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from web import todo

app = FastAPI()
app.include_router(todo.router)
templates = Jinja2Templates(directory="templates/")
@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todo.get_all()})


if __name__ == "__main__":
    import uvicorn
    # reload=True 부분이 있으면 프로세스가 2개(코드 감지용, 실제 fastapi실행) 실행이 됨
    # uvicorn.run("main:app", reload=True)
    uvicorn.run("main:app", host='0.0.0.0')
