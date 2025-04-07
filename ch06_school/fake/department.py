from typing import List

from ch06_school.model.department import DepartmentResponse

_departments = [
    DepartmentResponse(
        id=1,
        name='sw',
        quota=32,
        description="Web app developer training"
    ),
    # DepartmentResponse(
    #     id=2,
    #     name='embeded sw',
    #     quota=32,
    #     description="embeded developer training"
    # ),
]

id = 1


def find_all() -> List[DepartmentResponse]:
    """할일 목록을 반환한다."""
    return _departments


def find_one(department_id: int) -> DepartmentResponse:
    _department = next((x for x in _departments if x.id == department_id), None)
    if _department is None:
        raise ValueError(f"{department_id} not in")
    return _department