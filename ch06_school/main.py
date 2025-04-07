from fastapi import FastAPI, Body, Path

from web import student as student_web
from web import department as department_web

app = FastAPI()
app.include_router(student_web.router)
app.include_router(department_web.router)


if __name__ == "__main__":
    import uvicorn
    # reload=True 부분이 있으면 프로세스가 2개(코드 감지용, 실제 fastapi실행) 실행이 됨
    uvicorn.run("main:app", reload=True)
    # uvicorn.run("main:app", host='0.0.0.0')
