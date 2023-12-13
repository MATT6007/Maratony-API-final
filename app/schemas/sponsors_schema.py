from pydantic import BaseModel

class SponsorsBase(BaseModel):
    phone: str
    website: str
    email: str

class SponsorsCreate(SponsorsBase):
    pass

class SponsorsUpdate(SponsorsBase):
    pass

class Sponsors(SponsorsBase):
    ID_sponsor: int

    class Config:
        orm_mode = True
