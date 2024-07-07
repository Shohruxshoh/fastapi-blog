from fastapi import Depends, HTTPException
from user.bearer import JWTBearer
from database import SessionLocal
from user.models import User
import jwt


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(token: str = Depends(JWTBearer())) -> User:
    try:
        payload = jwt.decode(token, '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7',
                             algorithms=['HS256'])
        user_id = payload.get("sub")
        db = SessionLocal()
        return db.query(User).filter(User.id == user_id).first()
    except(jwt.PyJWTError, AttributeError):
        raise HTTPException(detail="Invalid token")
