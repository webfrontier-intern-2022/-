from passlib.context import CryptContext
from sqlalchemy.orm import SessionLocal

from . import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context.hash("password")

def get_user_by_email(db: Session, email: str):
    return db.query(models.user).filter(models.users.email == email).first()

def get_user_by_password(db: Session, password: str):
    return db.query(models.user).filter(models.users.password == password).first()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(
        db: Session,
        email: str,
        password: str,
        expire: int,
        reuse: bool):
    user = get_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(plain_password, user.hashed_password):
        return False
    return True

def get_password_hash(password):
    return pwd_context.hash(password)