from typing import List

from ch07_bank.n1.model.customer import CustomerResponse, EmploymentStatus

_customer = [
    CustomerResponse(
        id=1,
        name="choi",
        employment_status=EmploymentStatus.FULL_TIME,
        monthly_income=2500000,
        overdue_count=1
    ),
    CustomerResponse(
        id=2,
        name="jung",
        employment_status=EmploymentStatus.FREELANCER,
        monthly_income=3000000,
        overdue_count=0
    )
]
id = 2


def find_all() -> List[CustomerResponse]:
    """할일 목록을 반환한다."""
    return _customer