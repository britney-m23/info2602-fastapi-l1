from collections import Counter
from fastapi import FastAPI
import json

app = FastAPI()

with open("./data.json") as f:
    data = json.load(f)

@app.get("/")
async def hello_world():
    return "Hello, World!"

@app.get("/students")
async def get_students(pref: str | None = None):
    if pref:
        return [s for s in data if s.get("pref") == pref]
    return data

@app.get("/students/{id}")
async def get_student(id: str):
    for student in data:
        if student.get("id") == id:
            return student
    return {"error": "Student not found"}

@app.get("/stats")
async def get_stats():
    pref_counts = Counter()
    programme_counts = Counter()

    for student in data:
        pref = student.get("pref")
        programme = student.get("programme")

        if pref:
            pref_counts[pref] += 1
        if programme:
            programme_counts[programme] += 1

    combined = dict(pref_counts)
    combined.update(dict(programme_counts))
    return combined

@app.get("/add/{a}/{b}")
def add(a: float, b: float):
    return a + b

@app.get("/subtract/{a}/{b}")
def subtract(a: float, b: float):
    return a - b

@app.get("/multiply/{a}/{b}")
def multiply(a: float, b: float):
    return a * b

@app.get("/divide/{a}/{b}")
def divide(a: float, b: float):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
