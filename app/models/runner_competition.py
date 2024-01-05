from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dependencies.database import Base
from sqlalchemy import String

class RunnerCompetition(Base):
    __tablename__ = 'runner_competition'

    ID_runner = Column(Integer, ForeignKey('runner.ID_runner'), primary_key=True)
    ID_competition = Column(Integer, ForeignKey('competition.ID_competition'), primary_key=True)
    is_started = Column(Boolean, nullable=False)
    is_disqualified = Column(Boolean, nullable=False)
    is_paid = Column(Boolean, nullable=False)
    ice_phone = Column(String, nullable=False)
    ice_first_name = Column(String, nullable=False)
    ice_last_name = Column(String, nullable=False)

    runner = relationship('Runner', backref='runner_competition')
    
    competition = relationship('Competition', backref='runner_competition')
