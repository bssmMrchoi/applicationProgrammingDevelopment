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

class AssignDepartmentException(SchoolException):
    def __init__(self, student_name: str):
        super().__init__(
            message=f"학과 정원 초과로 {student_name} 학생 학과 재지정 필요!",
            status_code=status.HTTP_412_PRECONDITION_FAILED
        )


class Missing(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class Duplicate(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg