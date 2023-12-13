from typing import Type

from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_pagination import Page

from repositories import competition_category_repository
from models.competition_category import CompetitionCategory
from schemas import competition_category_schema


class CompetitionCategoryService:
    def __init__(self, competition_category_repository: competition_category_repository.CompetitionCategoryRepository = Depends()):
        self.competition_category_repository = competition_category_repository

    # def get_address(self, address_id: int) -> Type[Address] | None:
    #     return self.address_repository.get_address(address_id)

    def get_competition_categories(self) -> Page[CompetitionCategory]:
        return self.competition_category_repository.get_competition_categories()

    # def create_address(self, address_create: address_schema.AddressCreate) -> Address:
    #     return self.address_repository.create_address(address_create)

    # def update_address(self, address_id: int, address_update: address_schema.AddressUpdate) -> Type[Address] | None:
    #     return self.address_repository.update_address(address_id, address_update)

    # def delete_address(self, address_id: int) -> Type[Address] | None:
    #     return self.address_repository.delete_address(address_id)


