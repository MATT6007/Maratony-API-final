from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from dependencies.database import Base

class Results(Base):
    __tablename__ = 'results'

    ID_results = Column(Integer, primary_key=True, index=True)
    full_time = Column(String(9), nullable=False)
    half_time = Column(String(9), nullable=False)
    
    ID_runner = Column(Integer, ForeignKey('runner.ID_runner'))
    runner = relationship('Runner', backref='results')
    
    ID_competition = Column(Integer, ForeignKey('competition.ID_competition'))
    competition = relationship('Competition', backref='results')
