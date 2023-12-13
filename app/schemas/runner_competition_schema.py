from pydantic import BaseModel

class RunnerCompetitionBase(BaseModel):
    is_paid: bool
    is_started: bool
    is_disqualified: bool

class RunnerCompetitionCreate(RunnerCompetitionBase):
    pass

class RunnerCompetition(RunnerCompetitionBase):
    ID_runner: int
    ID_competition: int

    class Config:
        orm_mode = True
