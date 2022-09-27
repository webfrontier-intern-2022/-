from passlib.context import CryptContext
from sqlalchemy.orm import Session

from models import models_students

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
pwd_context.hash("password")

def get_students_by_email(db: Session, email: str):
    return db.query(models_students.Student).filter(models_students.Student.email == email).first()

def get_students_by_password(db: Session, password: str):
    return db.query(models_students.Student).filter(models_students.Student.password == password).first()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_students(
        db: Session,
        email: str,
        password: str,
    ):
    student = get_students_by_email(db, email)
    if not student:
        return False
    if not verify_password(plain_password, user.hashed_password):
        return False
    return True

def get_password_hash(password):
    return pwd_context.hash(password)