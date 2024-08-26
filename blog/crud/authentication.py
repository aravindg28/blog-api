from blog import models
from blog.auth.hash import verify_password
from blog.auth.token import create_access_token, validate_access_token
from blog.database import get_db
from blog.schemas import Token
from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

SECRET_KEY = "0c67ab5557eb60d831eac399366025fbdda1d41588527b4e248fb4cab5ffdc17"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_user_by_email(email: str, db):
      user = db.query(models.User).filter(models.User.email == email).first()
      return user

def get_token(request, db):
    # Get the user
    user = get_user_by_email(email=request.username, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"No user with username {request.username} exists")
    if not verify_password(request.password, user.password):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Incorrect password. Please try again")
    
    # Issue access token
    access_token = create_access_token(data={"sub":user.email})

    return Token(access_token=access_token, token_type="bearer")

def get_current_user(token: str = Depends(oauth2_scheme), 
                     db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
    token_data = validate_access_token(token, credentials_exception)
    print(f"token data: {token_data}")

    user = get_user_by_email(db=db, 
                             email=token_data.username)
    if user is None:
        raise credentials_exception
    return user
