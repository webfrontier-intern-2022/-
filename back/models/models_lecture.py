from sqlalchemy import Boolean, column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#database.pyからBaseクラスをインポート
from .database import Base

# SQLAlchemyモデルでクラスを作成
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