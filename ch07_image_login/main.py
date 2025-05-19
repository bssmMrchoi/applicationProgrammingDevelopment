from fastapi import FastAPI, Body, Path, Request
from fastapi.responses import JSONResponse
from ch07_image_login.error import UploadException
from ch07_image_login.web import upload

app = FastAPI()
app.include_router(upload.router)


@app.exception_handler(UploadException)
def app_exception_handler(request: Request, exc: UploadException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)
    # uvicorn.run("main:app", host='0.0.0.0')
