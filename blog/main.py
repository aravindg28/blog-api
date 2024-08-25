from fastapi import FastAPI, Depends, status
from . import schemas, models, crud
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog", status_code=status.HTTP_201_CREATED, response_model=schemas.Blog, 
          tags=["blog"])
def create_blog(user_id, request: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = crud.create_blog(request=request, db=db, user_id=user_id)

    return new_blog

@app.get("/blog", tags=["blog"])
def list_blogs(db: Session = Depends(get_db), limit:int=100, offset:int=0):
    return crud.list_blogs(db=db, limit=limit, offset=offset)

@app.get("/blog/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def get_blog(id: int, db : Session = Depends(get_db)):
    return crud.get_blog(id=id, db=db)
          
@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blog"])
def delete_blog(id: int, db: Session = Depends(get_db)):
    crud.delete_blog(id=id, db=db)

@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blog"])
def update_blog(id: int, request:schemas.BlogUpdate, db: Session = Depends(get_db)):
    result = crud.update_blog(id=id, db=db, request=request)
    if result:
        return {"detail": f"Blog with id {id} has been updated"}
    
@app.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.User,
          tags=["user"])
def create_user(request:schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = crud.create_user(request=request, db=db)

    return new_user

@app.get("/user/{id}", status_code=status.HTTP_200_OK, response_model=schemas.User,
         tags=["user"])
def get_user(id: int, db : Session = Depends(get_db)):
    return crud.get_user(id=id, db=db)
