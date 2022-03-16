from fastapi import FastAPI, Path
from pydantic import BaseModel  # to use Request Body and The Post Method
from typing import Optional

app = FastAPI()

students = {
    1: {
        "name": "Zezinho",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "Pedrinho",
        "age": 16,
        "year": "year 12"
    }
}


class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="Retrive the student ID", gt=0)):
    return students[student_id]


@app.get("/get-by-name")
def get_student_name(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "Not found"}

# combine path and query parameters the same logi that i used in fumction/ end-point in
# get_data_by_name_or_age


@app.get("/get-by-name-id/{student_id}")
def get_studant_with_id(*, student_id: int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"data": "Not found"}


# Recommended pattern for queries on non-mandatory fields
# Combining riquired field with non-mandatory field in the query
# @app.get("/get-by-name-optional")
# def get_student_name_optional(*, name: Optional[str] = None, age: int):
#     return get_data_by_name_or_age(name, age, students)


# def get_data_by_name_or_age(name: str, age: int, data) -> dict:
#     for student_id in data:
#         if students[student_id]["name"] == name or students[student_id]["age"] == age:
#             return students[student_id]
#         if students[student_id]["name"] == name and students[student_id]["age"] == age:
#             return students[student_id]
#     return {"data": "Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return{"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student:UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]
