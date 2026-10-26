from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",
        "https://rs-vjezba1-frontend.onrender.com",
    ],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PATCH", "DELETE"],
    allow_headers=["Content-Type"],
)

# Privremena pohrana zadataka u memoriji
tasks = [
    {"id": 1, "title": "Naučiti HTTP", "completed": False},
    {"id": 2, "title": "Napraviti REST API", "completed": False}
]


# Model za dodavanje novog zadatka
class TaskCreate(BaseModel):
    title: str


# Model za ažuriranje statusa zadatka
class TaskUpdate(BaseModel):
    completed: bool


# Početna ruta
@app.get("/")
def home():
    return {"message": "Moj prvi FastAPI poslužitelj!"}


# Dohvaćanje svih zadataka
@app.get("/tasks")
def get_tasks():
    return tasks


# Dodavanje novog zadatka
@app.post("/tasks", status_code=201)
def add_task(task: TaskCreate):
    new_task = {
        "id": max((t["id"] for t in tasks), default=0) + 1,
        "title": task.title,
        "completed": False
    }

    tasks.append(new_task)
    return new_task


# Brisanje zadatka
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Zadatak uspješno obrisan"}

    raise HTTPException(
        status_code=404,
        detail="Zadatak nije pronađen"
    )


# Ažuriranje statusa zadatka
@app.patch("/tasks/{task_id}")
def update_task(task_id: int, update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = update.completed
            return task

    raise HTTPException(
        status_code=404,
        detail="Zadatak nije pronađen"
    )
