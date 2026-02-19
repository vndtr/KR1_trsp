from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")

user = User(name="Алёна", id=1)

@app.get("/users")
async def get_user():
    return user