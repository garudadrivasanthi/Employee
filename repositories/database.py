from config import DATABASE_URL
from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import create_engine
class Base(DeclarativeBase):
    pass
engine=create_engine(DATABASE_URL)
session_local=sessionmaker(bind=engine)
def get_db():
    db=session_local()
    try:
        yield db
    finally:
        db.close()