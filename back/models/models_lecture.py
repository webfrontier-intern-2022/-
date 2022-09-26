from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#model.pyからModelBaseクラスをインポート
from model import ModelBase

# SQLAlchemyモデルでクラスを作成
# 講義モデル
class Lecture(ModelBase):
    __tablename__ = "lectures"

    #属性の作成
    id = Column(Integer, Index=True, Primary_kay=True)
    name = Column(String, Index=True)
    description = Column(String, Unique=True, Index=True)
    p_id = Column(Integer, ForeignKey("professor.id", Index=True))

    #関係を作成(教授モデルや履修モデルとの関係)
    owner = relationship("Professor", back_populates="lectures")
    lecture = relationship("Course",back_populates="corse_lecture")