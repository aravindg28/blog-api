from . import schemas, models
from fastapi import HTTPException, status
from .util import hash_password

def create_blog(request, db, user_id):
    check_resource_exists(user_id, db, models.User)
    new_blog = models.Blog(title=request.title, body=request.body, creator_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

def list_blogs(db, limit, offset):
    return db.query(models.Blog).offset(offset).limit(limit).all()

def check_resource_exists(id, db, model):
    resource = db.query(model).filter(model.id == id)
    if resource.first():
        return
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Resource of type {model} with id {id} is not found")
    
def get_blog(id, db):
    check_resource_exists(id, db, models.Blog)
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    return blog

def delete_blog(id, db):
    check_resource_exists(id, db, models.Blog)
    db.query(models.Blog).filter(models.Blog.id == id).delete()
    db.commit()

def update_blog(id, request, db):
    check_resource_exists(id, db, models.Blog)
    db.query(models.Blog).filter(models.Blog.id == id).update(request.model_dump())
    db.commit()
    return True

def create_user(request, db):
    new_user = models.User(email=request.email, password=hash_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user(id, db):
    check_resource_exists(id, db, models.User)
    user = db.query(models.User).filter(models.User.id == id).first()
    
    return user
