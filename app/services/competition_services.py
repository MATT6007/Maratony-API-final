from typing import Type

from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_pagination import Page

from repositories import competition_repository
from models.competition import Competition
from schemas import competition_schema

class CompetitionService:
    def __init__(self, competition_repository: competition_repository.CompetitionRepository = Depends()):
        self.competition_repository = competition_repository

    def get_competition(self, competition_id: int) -> Type[Competition] | None:
        return self.competition_repository.get_competition(competition_id)

    def get_competitions(self) -> Page[Competition]:
        return self.competition_repository.get_competitions()

    def create_competition(self, competition_create: competition_schema.CompetitionCreate) -> Competition:
        return self.competition_repository.create_competition(competition_create)

    # def update_address(self, address_id: int, address_update: address_schema.AddressUpdate) -> Type[Address] | None:
    #     return self.address_repository.update_address(address_id, address_update)

    # def delete_address(self, address_id: int) -> Type[Address] | None:
    #     return self.address_repository.delete_address(address_id)


