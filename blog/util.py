from passlib.context import CryptContext
from fastapi import HTTPException, status

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def check_resource_exists(id, db, model):
    resource = db.query(model).filter(model.id == id)
    if resource.first():
        return
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Resource of type {model} with id {id} is not found")
    