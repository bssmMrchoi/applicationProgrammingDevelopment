import json
from uuid import uuid4

import redis
from fastapi import APIRouter, Body
from starlette.requests import Request
from starlette.responses import Response

from ch07_image_login.error import InvalidUserException, UserNotFoundException
from ch07_image_login.model.login import LoginUser

router = APIRouter(prefix="/session")
redis_client = redis.Redis(host="localhost", port=6379, db=0)

SESSION_COOKIE_NAME = "session_id"
SESSION_TTL_SECONDS = 3600  # 세션 만료 시간

fake_users = list()
fake_users.append(LoginUser(username="user", password="user"))
fake_users.append(LoginUser(username="admin", password="admin", admin=True))

@router.post("/login")
def login(response: Response, login_user: LoginUser = Body()):
    find_user = next((user for user in fake_users if user.username == login_user.username), None)
    if not find_user or find_user.password != login_user.password:
        raise InvalidUserException()

    session_id = str(uuid4())
    redis_client.setex(session_id, SESSION_TTL_SECONDS, json.dumps(find_user.dict()))  # 세션 저장


    response.set_cookie(
        key=SESSION_COOKIE_NAME,
        value=session_id,
        httponly=True,
        max_age=SESSION_TTL_SECONDS
    )
    response.body = b"session login ok"
    response.status_code = 200

    return response

@router.get("/page")
def page(request: Request):
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    if not session_id:
        raise UserNotFoundException()

    get_user = redis_client.get(session_id)
    get_user = json.loads(get_user)

    if not get_user:
        raise UserNotFoundException()
    if str(get_user["admin"]) == "True":
        return Response(status_code=200, content="admin page")
    return Response(status_code=200, content="user page")


@router.post("/logout")
def logout(request: Request, response: Response):
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    if session_id:
        redis_client.delete(session_id)
        response.delete_cookie(SESSION_COOKIE_NAME)
        response.body = b"session logout ok"
        response.status_code = 200
    return response