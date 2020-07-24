from basic_fastapi import app
from fastapi import Request


@app.get("/")
async def index(request:Request):
   return {"some":"string"}

@app.get("/test")
async def test():
    return {"messge":"Hello World"}