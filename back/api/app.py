from fastapi import FastAPI

app = FastAPI

@app.get("/student/login/")
async def authenticate_user()