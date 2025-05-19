from fastapi import status

class UploadException(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code


class InvalidImageFormatException(UploadException):
    def __init__(self):
        super().__init__(
            message=f"only image uploads allowed"
        )

class ImageNotFoundException(UploadException):
    def __init__(self):
        super().__init__(
            message=f"Image not found",
            status_code=status.HTTP_404_NOT_FOUND
        )