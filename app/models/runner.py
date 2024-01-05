from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

from dependencies.database import Base

class Runner(Base):
    __tablename__ = 'runner'

    ID_runner = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    reset_token = Column(String)
    phone = Column(String)
    image_url = Column(String)
    disabled = Column(Boolean, default=False)
    club = Column(String(32))

    ID_address = Column(Integer, ForeignKey('addresses.ID_address'))
    address = relationship('Address', backref='runner')

  
