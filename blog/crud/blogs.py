from blog import models
from blog.util import check_resource_exists

def create_blog(request, db, user_id):
    check_resource_exists(user_id, db, models.User)
    new_blog = models.Blog(title=request.title, body=request.body, creator_id=user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog

def list_blogs(db, limit, offset):
    return db.query(models.Blog).offset(offset).limit(limit).all()

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
