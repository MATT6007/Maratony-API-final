from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from dependencies.database import Base

class Address(Base):
    __tablename__ = 'addresses'

    ID_address = Column(Integer, primary_key=True, index=True)
    street = Column(String(100), nullable=False)
    city = Column(String(50), nullable=False)
    postalCode = Column(String(10), nullable=False)



