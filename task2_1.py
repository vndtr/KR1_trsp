from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User
from models import UserAge 
from models import Feedback 

app = FastAPI()

@app.get("/")
async def root():
    return FileResponse("index.html")

user = User(name="Алёна", id=1)

@app.get("/users")
async def get_user():
    return user

@app.post("/user")
async def check_user(user: UserAge):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

feedbacks = []
@app.post("/feedback")
async def create_feedback(fb: Feedback):
    feedbacks.append(fb)
    return {"message": f"Feedback received. Thank you, {fb.name}."}