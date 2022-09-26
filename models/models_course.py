from sqlalchemy import Boolean, column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#database.pyからBaseクラスをインポート
from .database import Base

# SQLAlchemyモデルでクラスを作成
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