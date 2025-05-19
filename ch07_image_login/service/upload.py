import os
import shutil
from datetime import datetime
from tkinter import Image

from fastapi import UploadFile, File

from ch07_image_login.data import upload as data
from ch07_image_login.error import InvalidImageFormatException, ImageNotFoundException

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise InvalidImageFormatException()

    name, ext = os.path.splitext(file.filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    save_filename = f'{name}_{timestamp}{ext}'

    file_path = os.path.join(UPLOAD_DIR, save_filename)

    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f) #shutil -> 파일의 복사, 이동, 삭제, 압축 등의 기능을 도와줌

    data.save(save_filename, file_path)
    return {"filename": save_filename,
            "filepath": file_path}

def get_image(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)
    if not os.path.exists(file_path):
        raise ImageNotFoundException()
    return file_path