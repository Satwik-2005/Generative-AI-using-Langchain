from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Satwik Reddy Kunduru"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default=8.9, description="A decimal value representing the cgpa of the student")

newStudent = {'age': 21, "email": 'satwik@gmail.com'}
student = Student(**newStudent)

print(type(student))
print(student.__dict__)
print(student.model_dump_json())