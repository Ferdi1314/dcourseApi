from pydantic import BaseModel
from typing import Optional

class Account(BaseModel):
    fullname: str
    password: str
    email: str

"""
class UpdateAccount(BaseModel):
    username: str
    password: Optional[str]
    email: Optional[str]
    age: Optional[int]
    acctype: Optional[str]
"""
class SEmail(BaseModel):
    email: str

class SPassword(BaseModel):
    password: str

class Course(BaseModel):
    course_name: str
    category: str
    author: str
    information: str

class Content(BaseModel):
    title: str
    course_name: str
    description: str
    video_link: str