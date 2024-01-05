from typing import Type
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_pagination import Page, Params
from repositories import sponsors_repository
from models.sponsors import Sponsors
from schemas import sponsors_schema

class SponsorsService:
    def __init__(self, sponsors_repository: sponsors_repository.SponsorsRepository = Depends()):
        self.sponsors_repository = sponsors_repository

    def get_sponsors(self):
        return self.sponsors_repository.get_sponsors()

    def create_sponsor(self, sponsor_create: sponsors_schema.SponsorsCreate) -> Sponsors:
        return self.sponsors_repository.create_sponsor(sponsor_create)

   

