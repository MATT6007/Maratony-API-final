from sqlalchemy import Column, Integer, String, Boolean, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from dependencies.database import Base

class CompetitionCategory(Base):
    __tablename__ = 'competition_category'

    ID_competition_category = Column(Integer, primary_key=True, index=True)
    name = Column(String(16), nullable=False)
    distance = Column(DECIMAL(5,3), nullable=False)
    certificate = Column(Boolean, nullable=False)

