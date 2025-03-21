from fastapi import FastAPI

from web import todo

app = FastAPI()
app.include_router(todo.router)


if __name__ == "__main__":
    import uvicorn
    # reload=True 부분이 있으면 프로세스가 2개(코드 감지용, 실제 fastapi실행) 실행이 됨
    # uvicorn.run("main:app", reload=True)
    uvicorn.run("main:app")
