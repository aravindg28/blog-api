from blog import schemas
from blog.crud import authentication
from blog.database import get_db
from blog.crud.authentication import get_current_user
from fastapi import  APIRouter, Depends, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/token", status_code=status.HTTP_201_CREATED, response_model=schemas.Token)
def get_token(request:OAuth2PasswordRequestForm = Depends(), 
              db: Session = Depends(get_db)):
    access_token = authentication.get_token(request=request, db=db)

    return access_token
