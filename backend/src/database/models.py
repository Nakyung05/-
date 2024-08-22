from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.ext.declarative import declarative_base

from src.database.database import engine

Base = declarative_base()

# 여기에 데이터베이스에 어떤 형태로 저장할지 정의해요.
# 이 User를 보고 더 추가해봐요.

class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    user_password = Column(String, index=True)
    user_name = Column(String, index=True)
    created_at = Column(DateTime, default=current_timestamp())

Base.metadata.create_all(bind=engine)
