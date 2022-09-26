from sqlalchemy import Boolean, column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#database.pyからBaseクラスをインポート
from .database import Base

# SQLAlchemyモデルでクラスを作成
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