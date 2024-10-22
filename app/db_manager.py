from models import SessionLocal, Users
from keyboards import AccountType

MAPPING_DICT = {AccountType.CUSTOMER: "customer",
                AccountType.PERFORMER: "performer"}

def is_user_exists(username: str) -> bool:
    db = SessionLocal()
    return db.query(Users).filter(Users.username == username).first() is not None

def add_user_to_db(username: str, email: str, phone_number: str, account_type: str, password: str):
    db = SessionLocal()
    user = Users(username=username, email=email, phone_number=phone_number, account_type=MAPPING_DICT[account_type], password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user