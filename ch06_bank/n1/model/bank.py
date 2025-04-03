from typing import List

from pydantic import BaseModel


class Bank(BaseModel):
    id: int


class BankResponse(Bank):
    name: str
    min_score: int
    accounts: List[int]
