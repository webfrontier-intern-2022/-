from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#model.pyからModelBaseクラスをインポート
from model import ModelBase

# SQLAlchemyモデルでクラスを作成
# 学生モデル
class Student(ModelBase):
    __tablename__ = "students"

    #属性の作成
    s_id = Column("s_id", Integer, primary_key=True)
    name = Column("name", String, index=True)
    email = Column("email",String, unique=True, index=True)
    hashed_password = Column("hashed_password", String)
    is_active = Column("is_active", Boolean,default=True)

    #関係を作成(履修モデルとの関係)
    take_course = relationship("courses",back_populates="course_students")