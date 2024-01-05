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

    def create_competition_category(self, competition_category_create: competition_category_schema.CompetitionCategoryCreate) -> CompetitionCategory:
        return self.competition_category_repository.create_competition_category(competition_category_create)
    
    def get_competition_categories(self, skip, limit):
        return self.competition_category_repository.get_competition_categories(skip, limit)

    def delete_competition_category(self, competition_category_id: int):
        return self.competition_category_repository.delete_competition_category(competition_category_id)

 

