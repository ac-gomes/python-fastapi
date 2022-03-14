from typing import Optional
from fastapi import FastAPI, Path

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
        "class": "year 12"
    }
}


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

# Recommended pattern for queries on non-mandatory fields
# Combining riquired field with non-mandatory field in the query
@app.get("/get-by-name-optional")
def get_student_name_optional(*,name: Optional[str] = None, age: int):
     return get_data_by_name_or_age(name, age, students)

def get_data_by_name_or_age(name: str, age: int, data) -> dict:
    for student_id in data:
        if students[student_id]["name"] == name or students[student_id]["age"] == age:
            return students[student_id]
        if students[student_id]["name"] == name and students[student_id]["age"] == age:
            return students[student_id]
    return {"data": "Not found"}




