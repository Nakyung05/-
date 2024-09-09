from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config

# .env에서 로드한 DATABASE_URI를 사용해요.
engine = create_engine(config.DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    return db
