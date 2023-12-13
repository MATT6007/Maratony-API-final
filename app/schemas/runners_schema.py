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



class RunnerBase(BaseModel):
    # first_name: str = None
    # last_name: str = None
    # date_of_birth: datetime = None
    # email: str = None
    # phone: str | None = None
    # image_url: str | None = None

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
    # role: Role | None = None
    ID_runner: int
    disabled: bool = None

    class Config:
        orm_mode = True
