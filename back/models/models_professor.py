from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#model.pyからModelBaseクラスをインポート
from model import ModelBase

# SQLAlchemyモデルでクラスを作成
# # 教授モデル
class Professor(ModelBase):
    __tablename__ = "professors"

    #属性の作成
    id = Column("id", Integer, primary_key=True)
    email = Column("email", String, unique=True, index=True)
    name = Column("name", String, index=True)    
    password = Column("password", String)
    hashed_password = Column("hashed_password", String)
    is_active = Column("is_active", Boolean, default=True)

    #関係を作成(講義モデルとの関係)
    lectures = relationship("Lecture", back_populates="owner")