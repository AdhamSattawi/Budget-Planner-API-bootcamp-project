from fastapi import FastAPI
import uvicorn
app = FastAPI(Port=3000)

@app.get("/hello")
async def hello():
    return{"hello": "world"} 

@app.get("/add/{x}/{y}")
async def add(x: int, y:int):
    return {"sum": x + y} 

@app.get("/multiply/")
async def multiply(x: int, y:int):
    return {"sum": x * y} 

@app.get("/users")
async def get_users():
    pass

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    pass

