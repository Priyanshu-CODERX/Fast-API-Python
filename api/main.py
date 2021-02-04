from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# temp database
db = []

# course model to store courses
class Course(BaseModel):
    id: int
    name: str
    price: float
    isCompleted: Optional[bool] = None

# Home/welcome route
@app.get("/")
def read_root():
    return {"greetings": "Welcome to CodersLane"}

# Get all courses
@app.get("/courses")
def get_courses():
    return db

# get single course
@app.get("/courses/{course_id}")
def get_a_course(course_id: int):
    course = course_id - 1
    return db[course]

# add a new course
@app.post("/courses")
def add_course(course: Course):
    db.append(course.dict())
    return db[-1]

# delete a course
@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    db.pop(course_id-1)
    return {"task": "deletion successful"}
