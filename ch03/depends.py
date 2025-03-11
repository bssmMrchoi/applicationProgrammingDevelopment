from fastapi import FastAPI, Query, Depends

app = FastAPI()


def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "valid": True}


@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("depends:app", reload=True)