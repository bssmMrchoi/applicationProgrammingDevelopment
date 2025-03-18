from fastapi import FastAPI, Query, Depends, HTTPException

app = FastAPI()


# 1. 유저 조회 후 리턴 의존성
def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "gender": gender}


@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user


# 2. 토큰 확인 후 권한 부여
def check_admin(token: str = Query(...)):
    if token != "secure_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"role": "admin"}


@app.get("/check_admin")
def check_admin(user: dict = Depends(check_admin)):
    return {"message": "Welcome!", "user": user}


# 3. 데이터베이스 연결을 의존성으로 사용하기
class Database:
    def __init__(self):
        self.connection = "데이터베이스 연결"

    def get_connect(self):
        return self.connection


def get_db():
    db = Database()
    return db.get_connect()


@app.get("/db")
async def read_db(connection: str = Depends(get_db)):
    return {"db_connect": connection}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("depends:app", reload=True)


# 4. 전체 라우터 수준에서 의존성 주입

async def verify_token(token: str = Query(...)):
    if token != "secure":
        raise HTTPException(status_code=401, detail="Invalid token")

app_dep = FastAPI(dependencies=[Depends(verify_token)])


@app_dep.get("/public")
async def public_endpoint():
    return {"message": "public endpoint!"}


@app_dep.get("/private")
async def private_endpoint():
    return {"message": "private endpoint!"}


# 5. 특정 라우터 하위에 의존성 주입
async def check_admin(role: str = Query(...)):
    if role != "admin":
        raise HTTPException(status_code=401, detail="Invalid role")


@app_dep.get("/admin", dependencies=[Depends(check_admin)])
async def check_admin():
    return {"message": "admin ok!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("depends:app_dep", reload=True)
