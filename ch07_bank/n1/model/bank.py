from typing import List

from pydantic import BaseModel


class Bank(BaseModel):
    name: str


class BankResponse(Bank):
    id: int
    min_score: int
    accounts: List[int]
