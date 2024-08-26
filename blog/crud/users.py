from blog import models
from blog.auth.hash import hash_password
from blog.crud.util import check_resource_exists

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
