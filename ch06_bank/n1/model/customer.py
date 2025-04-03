from enum import Enum
from typing import Optional

from pydantic import BaseModel


# str을 함께 상속하면: FastAPI에서 요청/응답으로 들어오는 문자열과 자동 매핑이 잘 됩니다
class EmploymentStatus(str, Enum):
    FULL_TIME = "정규직"
    CONTRACT = "계약직"
    FREELANCER = "프리랜서"
    UNEMPLOYED = "무직"


class Customer(BaseModel):
    id: int


class CustomerResponse(Customer):
    name: str
    employment_status: EmploymentStatus
    monthly_income: int
    account: Optional[int] = None
    overdue_count: int
    bank_id: Optional[int] = None
