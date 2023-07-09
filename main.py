from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from model import Student
from config import conn
import json

app = FastAPI()


@app.post("/insertStudent", response_class=HTMLResponse)
async def find_one(student: Student):
    try:
        doc = await conn.LibraryManagementSystem.students.insert_one(student.dict())
        return json.dumps({"inserted_id": str(doc.inserted_id)})
    except Exception as e:
        print(e)
