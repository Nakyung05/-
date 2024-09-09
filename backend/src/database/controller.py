from sqlalchemy.orm import Session

from src.database.models import User
# 아래 함수를 만들고 다 안써도 괜찮아요.
# 일단 만들어봐요.

def add_user(db: Session, user: User, commit: bool = True):
    db.add(user)
    if commit:
        db.commit()
    return user

def get_user_by_user_name(db: Session, user_name: str):
    return db.query(User).filter(User.user_name == user_name).first()

# 유저가 없으면 None을 반환해요.
def get_user_by_user_id(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()