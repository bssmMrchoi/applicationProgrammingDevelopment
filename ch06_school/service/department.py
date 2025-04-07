from ch06_school.data import department as department_dao


# 학과 삭제시 소속된 학생이 있는지 확인 후 있다면 삭제 안함.
# 학과의 이름은 중복안됨