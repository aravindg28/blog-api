from blog import schemas
from blog.crud import users
from blog.database import get_db
from blog.crud.authentication import get_current_user
from fastapi import  APIRouter, Depends, status
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(request:schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = users.create_user(request=request, db=db)

    return new_user

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.User)
def get_user(id: int, db : Session = Depends(get_db), current_user = Depends(get_current_user)):
    return users.get_user(id=id, db=db)
