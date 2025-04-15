from fastapi import status

class SchoolException(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code


class StudentNotFoundException(SchoolException):
    def __init__(self, student_id: int):
        super().__init__(
            message=f"학생 ID {student_id}를 찾을 수 없습니다.",
            status_code=status.HTTP_404_NOT_FOUND
        )


class Missing(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class Duplicate(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg