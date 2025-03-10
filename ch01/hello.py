import asyncio

from fastapi import FastAPI, Body, Header

app = FastAPI()


# @app.get("/hi")
# def greet():
#     return "Hello? World?"

# @app.get("/hi/{who}")
# def greet(who):
#     return f"Hello? {who}?"


# @app.get("/hi")
# def greet(who):
#     return f"Hello? {who}?"


# @app.post("/hi")
# def greet(who: str = Body(embed=True)):
#     return f"Hello? {who}?"


# @app.get("/hi")
# def greet(who: str = Header()):
#     return f"Hello? {who}?"
#
#
# @app.get("/agent")
# def get_agent(user_agent: str = Header()):
#     return user_agent

@app.get("/hi")
async def greet():
    await asyncio.sleep(1)
    return "Hello? World?"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
