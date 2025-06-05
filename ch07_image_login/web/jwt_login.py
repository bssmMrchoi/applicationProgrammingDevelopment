from fastapi import APIRouter, Body, HTTPException, Header
from starlette.requests import Request
from starlette.responses import Response

from ch07_image_login.model.login import LoginUser, fake_users
from ch07_image_login.web.jwt_util import create_access_token, decode_access_token

router = APIRouter(prefix="/jwt")

@router.post("/login")
def login_jwt(response: Response, login_user: LoginUser = Body()):
    find_user = next((user for user in fake_users if user.username == login_user.username), None)
    if not find_user or find_user.password != login_user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token_data = {"username": find_user.username, "admin": find_user.admin}
    access_token = create_access_token(data=token_data)

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/page")
def page(auth_header: str = Header(..., alias="Authorization")):
    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="토큰이 없습니다")

    token = auth_header[7:]  # 'Bearer ' 이후 문자열만 추출
    claims = decode_access_token(token)

    username = claims.get("username")  # 사용자 이름 또는 아이디
    is_admin = claims.get("admin", False)

    if is_admin:
        return "admin page"
    else:
        return f"{username} user page"

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    response.status_code = 200
    response.body = b"jwt cookie logout ok"
    return response