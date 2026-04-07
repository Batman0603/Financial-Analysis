from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    date_of_birth = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    company_name = Column(String, nullable=True)