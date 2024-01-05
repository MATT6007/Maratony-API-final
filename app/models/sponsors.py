from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from dependencies.database import Base

class Sponsors(Base):
    __tablename__ = 'sponsors'

    ID_sponsor = Column(Integer, primary_key=True, index=True)
    phone = Column(String(9), nullable=False)
    website = Column(String(32))
    email = Column(String(32), nullable=False)
    
    ID_address = Column(Integer, ForeignKey('addresses.ID_address'))
    address = relationship('Address')
    
    sponsor_competition = relationship('SponsorCompetition', back_populates='sponsors')

