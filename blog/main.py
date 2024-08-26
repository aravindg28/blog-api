from blog import models
from blog.database import engine
from blog.routers import blogs, users, authentication

from fastapi import FastAPI

app = FastAPI()
app.include_router(users.router)
app.include_router(blogs.router)
app.include_router(authentication.router)

models.Base.metadata.create_all(bind=engine)
