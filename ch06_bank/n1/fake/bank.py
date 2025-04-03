from typing import List

from ch06_bank.n1.model.bank import BankResponse

_banks = [
    BankResponse(
        id=1,
        name='woori',
        min_score=70,
        accounts=[]
    ),
    BankResponse(
        id=2,
        name='kb',
        min_score=65,
        accounts=[]
    )
]
id = 2
account = 1000


def find_all() -> List[BankResponse]:
    """할일 목록을 반환한다."""
    return _banks