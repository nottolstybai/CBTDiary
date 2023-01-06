from sqlalchemy import Column, String, Integer, Boolean
from db_manager.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
