from blog import schemas
from blog.crud import blogs
from blog.database import get_db
from blog.crud.authentication import get_current_user
from fastapi import  APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Blog)
def create_blog(user_id, request: schemas.BlogCreate, db: Session = Depends(get_db), 
                current_user = Depends(get_current_user)):
    new_blog = blogs.create_blog(request=request, db=db, user_id=user_id)

    return new_blog

@router.get("/")
def list_blogs(db: Session = Depends(get_db), limit:int=100, offset:int=0, 
               current_user = Depends(get_current_user)):
    return blogs.list_blogs(db=db, limit=limit, offset=offset)

@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, db : Session = Depends(get_db)):
    return blogs.get_blog(id=id, db=db)
          
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db), 
                current_user = Depends(get_current_user)):
    blogs.delete_blog(id=id, db=db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request:schemas.BlogUpdate, db: Session = Depends(get_db), 
                current_user = Depends(get_current_user)):
    result = blogs.update_blog(id=id, db=db, request=request)
    if result:
        return {"detail": f"Blog with id {id} has been updated"}
