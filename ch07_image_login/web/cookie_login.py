from fastapi import APIRouter, Body
from starlette.requests import Request
from starlette.responses import Response

from ch07_image_login.error import InvalidUserException, UserNotFoundException
from ch07_image_login.model.login import LoginUser

router = APIRouter(prefix="/cookie")

fake_users = list()
fake_users.append(LoginUser(username="user", password="user"))
fake_users.append(LoginUser(username="admin", password="admin", admin=True))

@router.post("/login")
def login_cookie(response: Response, login_user: LoginUser = Body()):
    find_user = next((user for user in fake_users if user.username == login_user.username), None)
    if not find_user or find_user.password != login_user.password:
        raise InvalidUserException()

    response.set_cookie("username", find_user.username)
    response.set_cookie("admin", str(find_user.admin))
    response.body = b"cookie login ok"
    response.status_code = 200

    return response


@router.get("/page")
def page(request: Request):
    find_user = next((user for user in fake_users if user.username == request.cookies.get("username")), None)
    if not find_user:
        raise UserNotFoundException()
    if find_user.admin and request.cookies.get("admin") == "True":
        return Response(status_code=200, content="admin page")
    return Response(status_code=200, content="user page")

@router.post("/logout")
def logout(response: Response):
    response.set_cookie("username", "", max_age=0)
    response.set_cookie("admin", "", max_age=0)
    response.body = b"cookie logout ok"
    response.status_code = 200
    return response