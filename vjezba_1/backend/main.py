
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Moj prvi FastAPI poslužitelj!"}

@app.get("/tasks")
def get_tasks():
    return [
        {"id": 1, "title": "Naučiti HTTP"},
        {"id": 2, "title": "Napraviti REST API"}
    ]
