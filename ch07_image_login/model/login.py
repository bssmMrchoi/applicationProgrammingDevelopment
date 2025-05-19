from typing import Optional

from pydantic import BaseModel


class LoginUser(BaseModel):
    username: str
    password: str
    admin: bool = False
