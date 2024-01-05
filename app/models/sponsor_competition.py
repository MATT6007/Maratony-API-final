from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from dependencies.database import Base

class SponsorCompetition(Base):
    __tablename__ = 'sponsor_competition'

    ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ID_sponsor = Column(Integer, ForeignKey('sponsors.ID_sponsor'), nullable=False)
    ID_competition = Column(Integer, ForeignKey('competition.ID_competition'), nullable=False)
    amountUSD = Column(Integer, nullable=False)
    
    sponsors = relationship('Sponsors', back_populates='sponsor_competition')
    competition = relationship('Competition', back_populates='sponsor_competition')


