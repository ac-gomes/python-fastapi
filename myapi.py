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
