from typing import List

from ch06_school.error import StudentNotFoundException, AssignDepartmentException
from ch06_school.model.student import StudentResponse, AssignDepartment, Student
from ch06_school.data import student as student_dao
from ch06_school.data import department as department_dao


def find_all() -> List[StudentResponse]:
    return student_dao.find_all()

def get_by_id(student_id: int) -> StudentResponse:
    _student = student_dao.find_by_id(student_id)
    if _student is None:
        raise StudentNotFoundException(student_id)
    return _student

def save(student: Student) -> StudentResponse:
    return student_dao.save(student)

# 학생의 학과 등록
# 학생들의 희망 조사 후 전체 학생 성적순으로 나열
# 상위부터 학과의 정원 수 까지 희망순으로 배정
# ==> 모든 학생의 희망조사부터 받아 일괄 업데이트
def assign_department(assign_dto: AssignDepartment) -> StudentResponse:
    # 학생의 희망에따라 학과를 배정하고 학과 정원에 벗어나는 하위 학생들은 자동 적으로 다른 과로 배정
    # 1. 희망 학과 배정
    assign_ok = student_dao.update(assign_dto)
    # 2. 학과가 배정된 학생 중 학생의 점수로 내림차순 조회
    _students = student_dao.find_by_dept_id_score_desc(assign_dto.department_id)
    _department = department_dao.find_by_id(assign_dto.department_id)
    if len(_students) > _department.quota:
        sorry_student = student_dao.update(AssignDepartment(student_id=_students[-1].id,
                                            department_id=None))
        raise AssignDepartmentException(sorry_student.name)
    return assign_ok