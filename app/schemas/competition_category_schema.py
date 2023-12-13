from pydantic import BaseModel

class CompetitionCategoryBase(BaseModel):
    name: str
    distance: float
    certificate: bool

class CompetitionCategoryCreate(CompetitionCategoryBase):
    pass

class CompetitionCategoryUpdate(CompetitionCategoryBase):
    pass

class CompetitionCategory(CompetitionCategoryBase):
    ID_competition_category: int

    class Config:
        orm_mode = True
