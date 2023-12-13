from pydantic import BaseModel

class ResultsBase(BaseModel):
    full_time: str
    half_time: str

class ResultsCreate(ResultsBase):
    pass

class Results(ResultsBase):
    ID_results: int

    class Config:
        orm_mode = True
