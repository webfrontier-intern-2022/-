from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#model.pyからModelBaseクラスをインポート
from settings import ModelBase

# SQLAlchemyモデルでクラスを作成
# # 教授モデル
class Professor(ModelBase):
    __tablename__ = "professors"

    #属性の作成
    id = Column("id", Integer, primary_key=True)
    email = Column("email", String(255), unique=True, index=True)
    name = Column("name", String(255), index=True)
    password = Column("password", String(255))
    hashed_password = Column("hashed_password", String(255))
    is_active = Column("is_active", Boolean, default=True)

    #関係を作成(講義モデルとの関係)
    lectures = relationship("Lecture", back_populates="owner")