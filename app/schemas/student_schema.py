from pydantic import BaseModel , Field
from typing import Optional

#بررسی و اعتبار سنجی ورودی ها وقتی دانشجو ایجاد میشود
class StudentCreate(BaseModel):
    first_name: str = Field(min_length=2 , max_length=50)
    last_name: str = Field(min_length=2 , max_length=50)
    student_number: str = Field(min_length=3 , max_length=20)
    major: str = Field(min_length=2 , max_length=80)


class StudentUpdate(BaseModel):
    first_name: Optional[str] = Field(default = None , min_length=2 , max_length=50)
    last_name: Optional[str] = Field(default = None , min_length=2 , max_length=50)
    student_number: Optional[str] = Field(default = None , min_length=3 , max_length=20)
    major: Optional[str] = Field(default = None , min_length=2 , max_length=80)

