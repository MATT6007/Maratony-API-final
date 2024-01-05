from fastapi import HTTPException, Depends
from repositories import runners_repository 
from repositories.runners_repository import RunnerRepository
from models.runner import Runner
from models.competition import Competition
from typing import Type
from schemas import runners_schema
from typing import List

class RunnerService:
    def __init__(self, runners_repository: runners_repository.RunnerRepository = Depends()):
        self.runners_repository = runners_repository

    def create_runner(self, runner_create: runners_schema.RunnerCreate) -> Runner:
        return self.runners_repository.create_runner(runner_create)

    def get_runners(self):
        return self.runners_repository.get_runners()

    def get_runner(self, runner_id: int) -> Type[Runner] | None:
        return self.runners_repository.get_runner(runner_id)

    def get_user_by_email(self, email: str) -> Runner | None:
        return self.runners_repository.get_user_by_email(email)

    def save(self, runner: Runner) -> Runner:
        return self.runners_repository.save(runner)

    def is_registered(self, runner_id: int, competition_id: int) -> bool:
        return self.runners_repository.is_registered(runner_id, competition_id)

    def create_runner_competition(self, runner_competition_create: runners_schema.RunnerCompetitionCreate):
        return self.runners_repository.create_runner_competition(runner_competition_create)

    def get_user_competitions(self, runner_id: int) -> List[Competition]:
        return self.runners_repository.get_user_competitions(runner_id)

    def get_top_runners(self, skip: int = 0, limit: int = 3):
        return self.runners_repository.get_top_runners(skip, limit)
    
    def update_address_club(self, competition_id: int, obj_in):
        return self.runners_repository.update_address_club(competition_id, obj_in)

    def update_profile_photo(self, runner_id: int, image_url: runners_schema.RunnerSchemaSetPhoto) -> Runner:
        return self.runners_repository.update_profile_photo(runner_id, image_url)