import os

from fastapi import APIRouter, UploadFile, File
from scipy._lib.cobyqa import settings
from starlette.responses import FileResponse

from ch07_image_login.service import upload as service

router = APIRouter(prefix="/uploads")

@router.post("")
def upload_file(file: UploadFile = File(...)):
    return service.save_image(file)

@router.get("/images/{filename}")
def get_image(filename: str):
    file_path = service.get_image(filename)
    return FileResponse(file_path, media_type="image/jpeg")