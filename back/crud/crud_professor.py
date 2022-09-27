from passlib.context import CryptContext
from sqlalchemy.orm import SessionLocal

from models import models_professor

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context.hash("password")

def get_professor_by_email(db: Session, email: str):
    return db.query(models_professor.Professor).filter(models_professor.Professor.email == email).first()

def get_professor_by_password(db: Session, password: str):
    return db.query(models_professor.Professor).filter(models_professor.Professor.password == password).first()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_professor(
        db: Session,
        email: str,
        password: str
    ):
    professor = get_professor_by_email(db, email)
    if not professor:
        return False
    if not verify_password(plain_password, professor.hashed_password):
        return False
    return True

def get_password_hash(password):
    return pwd_context.hash(password)