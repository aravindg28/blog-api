from pydantic import BaseModel

class BlogBase(BaseModel):
    title : str
    body : str

class BlogCreate(BlogBase):
    pass

class BlogUpdate(BlogBase):
    pass

class Blog(BlogBase):
    id: int

    class Config:
        orm_mode=True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode=True


    