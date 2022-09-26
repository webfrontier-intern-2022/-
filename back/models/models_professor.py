from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#model.pyからModelBaseクラスをインポート
from model import ModelBase

# SQLAlchemyモデルでクラスを作成
# # 教授モデル
class Professor(ModelBase):
    __tablename__ = "professors"

    #属性の作成
    id = Column(Integer, Index=True, Primary_key=True)
    email = Column(String, Unique=True, Index=True)
    name = Column(String, Index=True)    
    password = column(String)   #hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    #関係を作成(講義モデルとの関係)
    lectures = relationship("Lecture", back_populates="owner")