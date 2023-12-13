from pydantic import BaseModel

class SponsorCompetitionBase(BaseModel):
    amountUSD: int

class SponsorCompetitionCreate(SponsorCompetitionBase):
    ID_sponsor: int
    ID_competition: int

class SponsorCompetitionUpdate(SponsorCompetitionBase):
    pass

class SponsorCompetition(SponsorCompetitionBase):
    ID_sponsor: int
    ID_competition: int

    class Config:
        orm_mode = True

