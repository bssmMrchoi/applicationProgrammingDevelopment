from typing import Optional

from pydantic import BaseModel


class Department(BaseModel):
    name: str


class DepartmentResponse(Department):
    id: int
    quota: int
    description: Optional[str] = None
