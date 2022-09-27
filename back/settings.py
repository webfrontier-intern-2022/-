from datetime import datetime

from sqlalchemy import create_engine, Column, String, Integer, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base

# Engine の作成
Engine = create_engine(
    "mysql+pymysql://codeserver:rH8,KeGa@127.0.0.1:3306/test",
    encoding="utf-8",
    echo=False
)

'''
モデルの Base を作成
この Base を基にモデルを定義するとmetadataにモデルの情報が格納されていく
'''
ModelBase = declarative_base()

# class testModel(ModelBase):
#     """
#     testModel
#     """
#     __tablename__ = 'test'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     description = Column(Unicode(200))
#     created_at = Column(DateTime, default=datetime.now, nullable=False)
#     updated_at = Column(DateTime, default=datetime.now, nullable=False)