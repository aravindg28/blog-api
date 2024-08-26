from pydantic import BaseModel
from typing import List, Union

class BlogBase(BaseModel):
    title : str
    body : str

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BlogBase):
    pass

class BlogShow(BlogBase):
    id: int

    class Config:
        orm_mode=True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserShow(UserBase):
    id: int
    email: str

    class Config:
        orm_mode=True

class Blog(BlogBase):
    id: int
    creator: UserShow

    class Config:
        orm_mode=True

class User(UserBase):
    id: int
    blogs: List[BlogShow] = []

    class Config:
        orm_mode=True

class UserLogin(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None
