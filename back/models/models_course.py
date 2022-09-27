from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

#model.pyからModelBaseクラスをインポート
from settings import ModelBase

# SQLAlchemyモデルでクラスを作成
# 履修モデル
class Course(ModelBase):
    __tablename__ = "courses"

    #属性の作成
    id = Column("course_id", Integer, primary_key=True)
    s_id = Column("s_id", Integer, ForeignKey("Student.id"))
    l_id = Column("l_id", Integer, ForeignKey("Lecture.id"))

    #関係を作成(学生モデルと講義モデルとの関係)
    course_student = relationship("students",back_populates="take_course")
    course_lecture = relationship("lectures",back_populates="lecture")