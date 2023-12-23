from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.address import Address  

from dependencies.database import Base

# class Competition(Base):
#     __tablename__ = 'competition'

#     ID_competition = Column(Integer, primary_key=True, index=True)
#     name = Column(String(32), nullable=False)
#     date = Column(Date, nullable=False)
#     location = Column(String(32), nullable=False)
#     entryfee = Column(DECIMAL(7,2), nullable=False)
    
#     ID_address = Column(Integer, ForeignKey('addresses.ID_address'))
#     address = relationship('Address')
    
#     ID_competition_category = Column(Integer, ForeignKey('competition_category.ID_competition_category'))
#     competition_category = relationship('CompetitionCategory')


class Competition(Base):
    __tablename__ = 'competition'

    ID_competition = Column(Integer, primary_key=True, index=True   )
    name = Column(String(32), nullable=False)
    date = Column(Date, nullable=False)
    location = Column(String(32), nullable=False)
    entryfee = Column(DECIMAL(7,2), nullable=False)
    organizer = Column(String(64), nullable=False) 
    body = Column(String(256), nullable=True)  
    image = Column(String(256), nullable=True)  
    
    ID_address = Column(Integer, ForeignKey('addresses.ID_address'))
    address = relationship('Address')
    
    ID_competition_category = Column(Integer, ForeignKey('competition_category.ID_competition_category'))
    competition_category = relationship('CompetitionCategory')
    
    sponsor_competition = relationship('SponsorCompetition', back_populates='competition')
