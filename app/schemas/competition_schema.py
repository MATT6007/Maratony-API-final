from pydantic import BaseModel
from datetime import date

class CompetitionBase(BaseModel):
    name: str
    date: date
    location: str
    entryfee: float
    organizer: str  
    body: str  
    image: str 

class CompetitionCreate(CompetitionBase):
    pass

class CompetitionUpdate(CompetitionBase):
    pass

class Competition(CompetitionBase):
    ID_competition: int

    class Config:
        orm_mode = True
