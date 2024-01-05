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

class Competition(CompetitionBase):
    pass

class CompetitionUpdate(CompetitionBase):
    pass

class RunnerResultCreate(BaseModel):
    full_time: str
    half_time: str
    is_started: bool
    is_disqualified: bool

class Competition(CompetitionBase):
    ID_competition: int

    class Config:
        orm_mode = True
