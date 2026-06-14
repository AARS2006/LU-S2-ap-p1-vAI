from pydantic import BaseModel, Field
from typing import Optional

#بررسی و اعتبار سنجی وقتی درس ایجاد میشود
class CourseCreate(BaseModel):
    major: str = Field(min_length=2, max_length=80)
    title: str = Field(min_length=2, max_length=100)
    code: str = Field(min_length=2, max_length=20)
    unit: int = Field(ge=1, le=5)
    capacity: int = Field(ge=1, le=200)


class CourseUpdate(BaseModel):
    major: Optional[str] = Field(default=None, min_length=2, max_length=80)
    title: Optional[str] = Field(default=None, min_length=2, max_length=100)
    code: Optional[str] = Field(default=None, min_length=2, max_length=20)
    unit: Optional[int] = Field(default=None, ge=1, le=5)
    capacity: Optional[int] = Field(default=None, ge=1, le=200)