from sqlalchemy import Boolean, column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#database.pyからBaseクラスをインポート
from .database import Base

# SQLAlchemyモデルでクラスを作成
# 教授モデル
class Professor(Base):
    __tablename__ = "professors"

    #属性の作成
    id = Column(Integer, Primary_kay=True, Index=True)
    name = Column(String, Index=True)
    email = Column(String, Unique=True, Index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)

    #関係を作成(講義モデルとの関係)
    lectures = relationship("Lecture", back_populates="owner")

# 学生モデル
class Student(Base):
    __tablename__ = "students"

    #属性の作成
    id = Column(Integer, Primary_kay=True, Index=True)
    name = Column(String, Index=True)
    email = Column(String, Unique=True, Index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)

    #関係を作成(履修モデルとの関係)
    take_course = relationship("courses",back_populates="course_students")

# 講義モデル
class Lecture(Base):
    __tablename__ = "lectures"

    #属性の作成
    id = Column(Integer,primary_kay=True, Index=True)
    name = Column(String, Index=True)
    description = Column(String, Unique=True, Index=True)
    p_id = Column(Integer,ForeignKey("professor.id"))

    #関係を作成(教授モデルや履修モデルとの関係)
    owner = relationship("Professor", back_populates="lectures")
    lecture = relationship("Course",back_populates="corse_lecture")

# 履修モデル
class Course(Base):
    __tablename__ = "courses"

    #属性の作成
    id = Column(Integer, Primary_Key=True, index=True)
    s_id = Column(Integer, ForeignKey("Student.id"), Index=True)
    p_id = Column(Integer, ForeignKey("Lecture.id"), Index=True)

    #関係を作成(学生モデルと講義モデルとの関係)
    course_student = relationship("students",back_populates="take_course")
    course_lecture = relationship("lectures",back_populates="lecture")