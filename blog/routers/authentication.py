
from fastapi import APIRouter , Depends ,HTTPException,status
from .. import schemas , database , models , token
from sqlalchemy.orm import Session
from ..hashing import Hash
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

 


router = APIRouter(
    tags=['Authentication']
)


@router.post('/Login')
def Login(request:schemas.Login , db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                detail=f'Invalid Credentials')
    
    if not Hash.verify(user.password, request.password):
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                detail=f'Incorrect password')

    return user

    access_token =token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}





