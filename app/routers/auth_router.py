from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas.schemas import UserCreate, Token
from app.core.auth import hash_password, verify_password, create_access_token, oauth2_scheme, decode_token
from app.database.database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter_by(username=user.username).first():
        raise HTTPException(status_code=400, detail="Username taken")
    hashed_pw = hash_password(user.password)
    new_user = User(username=user.username, password=hashed_pw, is_admin=user.is_admin)
    db.add(new_user)
    db.commit()
    return {"msg": "User created"}

@router.post("/token", response_model=Token)
def login(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username=data.username).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_data = decode_token(token)
    user = db.query(User).filter_by(username=user_data.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user