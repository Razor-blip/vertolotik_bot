from models import SessionLocal, Users, Orders
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

def is_user_authenticated(username: str, password: str):
    db = SessionLocal()
    user = db.query(Users).filter(Users.username == username, Users.password == password).first()

    if user is not None:
        return user.account_type
    else:
        return False
    
def create_order(username: str, task_name: str, description: str, price: int, status: str):
    db = SessionLocal()
    user = Orders(username=username, task_name=task_name, description=description, price=price, status=status)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

def list_accepted_orders(username: str):
    db = SessionLocal()
    orders = db.query(Orders).filter(Orders.username == username, Orders.status == "active").all()

    return orders

def get_order_by_id(id):
    db = SessionLocal()
    order = db.query(Orders).filter(Orders.id == id).first()
    return order