from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

# Create an engine and a base class
engine = create_engine("sqlite:///./test.db")

if not database_exists(engine.url):
    print("Database does not exist, creating...")
    create_database(engine.url)
else:
    print("Database already exists.")

class Base(DeclarativeBase):
    pass

class Users(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(50))
    phone_number: Mapped[str] = mapped_column(String(50))
    account_type: Mapped[str] = mapped_column(String(10))
    password: Mapped[str] = mapped_column(String(8))

# Create tables
Base.metadata.create_all(bind=engine)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
