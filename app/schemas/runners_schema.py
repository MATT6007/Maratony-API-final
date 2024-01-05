# from pydantic import BaseModel

# class RunnerBase(BaseModel):
#     Name: str
#     Surname: str
#     Age: int
#     Club: str

# class RunnerCreate(RunnerBase):
#     pass

# class Runner(RunnerBase):
#     ID_runner: int

#     class Config:
#         orm_mode = True

from datetime import datetime
from pydantic import BaseModel
from models.runner import Runner
from typing import Optional
from .competition_schema import Competition

class RunnerBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: datetime
    email: str
    phone: Optional[str] = None
    image_url: Optional[str] = None
    disabled: Optional[bool] = False
    club: Optional[str] = None

    class Config:
        orm_mode = True

class RunnerCreateRequest(RunnerBase):
    password: str = None

class RunnerCreate(RunnerBase):
    pass

class RunnerUpdate(RunnerBase):
    pass

class Runner(RunnerBase):
    ID_runner: int
    disabled: bool = None

    class Config:
        orm_mode = True

class RunnerCompetitionBase(BaseModel):
    ID_runner: int
    ID_competition: int
    is_paid: bool
    is_started: bool
    is_disqualified: bool

class RunnerRegistrationData(BaseModel):
    is_paid: bool
    iceFirstName: str
    iceLastName: str
    icePhone: str

class RunnerCompetitionCreate(RunnerCompetitionBase):
    ice_first_name: str
    ice_last_name: str
    ice_phone: str

class TopRunner(BaseModel):
    ID_runner: int
    first_name: str
    last_name: str
    date_of_birth: str
    club: str
    image_url: str
    races_participated: int

class RunnerAddressClubUpdate(BaseModel):
    club: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    postalCode: Optional[str] = None

class RunnerSchemaSetPhoto(BaseModel):
    image_url: str

class ResultWithRunner(BaseModel):
    ID_results: int
    full_time: str
    half_time: str
    runner_id: int
    runner: Runner
    competition_id: int
    competition: Competition

class RunnerCompetition(RunnerCompetitionBase):
    ID_runner_competition: int

    class Config:
        orm_mode = True



