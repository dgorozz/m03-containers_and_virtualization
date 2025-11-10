from sqlalchemy import create_engine, Column, Integer, String

from .database import Base

class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    name = Column(String, nullable=False)