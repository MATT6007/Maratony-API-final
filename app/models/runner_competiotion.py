from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dependencies.database import Base

class RunnerCompetition(Base):
    __tablename__ = 'runner_competition'

    ID_runner = Column(Integer, ForeignKey('runners.ID_runner'), primary_key=True)
    ID_competition = Column(Integer, ForeignKey('competition.ID_competition'), primary_key=True)
    is_paid = Column(Boolean, nullable=False)
    is_started = Column(Boolean, nullable=False)
    is_disqualified = Column(Boolean, nullable=False)
    
    runner = relationship('Runner', back_populates='runner_competitions')
    
    competition = relationship('Competition', back_populates='runner_competitions')
