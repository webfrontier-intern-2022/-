from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#model.pyからModelBaseクラスをインポート
from model import ModelBase

# SQLAlchemyモデルでクラスを作成
# 学生モデル
class Student(ModelBase):
    __tablename__ = "students"

    #属性の作成
    id = Column(Integer, Index=True, Primary_key=True)
    name = Column(String, Index=True)
    email = Column(String, Unique=True, Index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean,default=True)

    #関係を作成(履修モデルとの関係)
    take_course = relationship("courses",back_populates="course_students")