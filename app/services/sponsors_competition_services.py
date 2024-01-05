from typing import Type
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_pagination import Page, Params
from repositories import sponsors_competition_repository
from models.sponsor_competition import SponsorCompetition
from schemas import sponsors_competition_schema

class SponsorCompetitionService:
    def __init__(self, sponsors_competition_repository: sponsors_competition_repository.SponsorCompetitionRepository = Depends()):
        self.sponsors_competition_repository = sponsors_competition_repository

    def get_sponsors_by_competition(self, competition_name: str):
        return self.sponsors_competition_repository.get_sponsors_by_competition(competition_name)

    def get_sponsors_competition_all(self):
        return self.sponsors_competition_repository.get_sponsors_competition_all()

    def create_sponsor_competition(self, sponsor_competition_create: sponsors_competition_schema.SponsorCompetitionCreate) -> SponsorCompetition:
        return self.sponsors_competition_repository.create_sponsor_competition(sponsor_competition_create)


