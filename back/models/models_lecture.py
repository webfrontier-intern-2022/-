from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#model.pyからModelBaseクラスをインポート
from settings import ModelBase

# SQLAlchemyモデルでクラスを作成
# 講義モデル
class Lecture(ModelBase):
    __tablename__ = "lectures"

    #属性の作成
    l_id = Column("l_id", Integer, primary_key=True)
    name = Column("name", String(255), index=True)
    description = Column("description", String(255), unique=True, index=True)
    p_id = Column("p_id", Integer, ForeignKey("professor.id"))

    #関係を作成(教授モデルや履修モデルとの関係)
    owner = relationship("Professor", back_populates="lectures")
    lecture = relationship("Course",back_populates="corse_lecture")