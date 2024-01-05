from typing import Type
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_pagination import Page
from repositories import competition_repository
from repositories import runners_repository
from models.competition import Competition
from schemas import competition_schema

class CompetitionService:
    def __init__(self, competition_repository: competition_repository.CompetitionRepository = Depends(), runners_repository: runners_repository.RunnerRepository = Depends()):
        self.competition_repository = competition_repository
        self.runners_repository = runners_repository

    def get_competition(self, competition_id: int) -> Type[Competition] | None:
        return self.competition_repository.get_competition(competition_id)

    def get_competitions(self) -> Page[Competition]:
        return self.competition_repository.get_competitions()

    def create_competition(self, competition_create: competition_schema.CompetitionCreate) -> Competition:
        return self.competition_repository.create_competition(competition_create)

    def delete_competition(self, competition_id: int) -> Type[Competition] | None:
        return self.competition_repository.delete_competition(competition_id)

    def add_runner_result(self, runner_id: int, competition_id: int, full_time, half_time, is_started, is_disqualified):
        runner = self.runners_repository.get_runner(runner_id)
        competition = self.competition_repository.get_competition(competition_id)

        if not runner or not competition:
            raise HTTPException(status_code=404, detail="Runner or competition not found")

        result = self.competition_repository.create_runner_result(
            runner=runner,
            competition=competition,
            full_time=full_time,
            half_time=half_time,
            is_started=is_started,
            is_disqualified=is_disqualified
        )

        return result

    def get_results_for_competition(self,competition_id: int):
        return self.competition_repository.get_results_for_competition(competition_id)


