from fastapi import FastAPI, Body, Path, Request
from fastapi.responses import JSONResponse
from ch06_school.error import SchoolException
from web import student as student_web
from web import department as department_web

app = FastAPI()
app.include_router(student_web.router)
app.include_router(department_web.router)


@app.exception_handler(SchoolException)
def app_exception_handler(request: Request, exc: SchoolException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message
        }
    )

if __name__ == "__main__":
    import uvicorn
    # reload=True 부분이 있으면 프로세스가 2개(코드 감지용, 실제 fastapi실행) 실행이 됨
    uvicorn.run("main:app", reload=True)
    # uvicorn.run("main:app", host='0.0.0.0')
