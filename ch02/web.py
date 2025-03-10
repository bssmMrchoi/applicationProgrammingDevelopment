from fastapi import FastAPI, Body, Header

from ch02.model import Champion

app = FastAPI()

@app.get("/champions")
def get_all() -> list[Champion]:
    from data import get_champion
    return get_champion()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("web:app", reload=True)
