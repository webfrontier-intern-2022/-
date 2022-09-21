from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql://user:password@mysqlserver/db"

#sessionLocalクラス
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

#Baseクラス
Base = declarative_base()