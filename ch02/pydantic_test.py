from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str


class Product(BaseModel):
    name: str = Field(..., min_length=4, max_length=10)
    price: float = Field(..., gt=10000, le=100000)  # 가격은 10000보다 커야 함
    stock: Optional[int] = 10  # 기본 재고값 10


class Event(BaseModel):
    name: str
    start_time: datetime


class AdminUser(User):
    role: str = "admin"


if __name__ == "__main__":
    user = User(id=1, name="choi", age=25, email="teacher009@bssm.hs.kr")
    user2 = User(id="2", name="kim", age=31, email="teacher099@bssm.hs.kr")
    print(user)
    print(user2)

    p1 = Product(name="맥북프로", price=30000.0)
    print(p1)

    e1 = Event(name="Algorithm Competition", start_time="2025-06-25")
    print(e1)

    admin = AdminUser(id=3, name="jung", age=42, email="teacher999@bssm.hs.kr")
    print(admin)

    print(admin.json())
