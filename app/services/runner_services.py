from fastapi import HTTPException, Depends
from repositories import runners_repository 
from repositories.runners_repository import RunnerRepository
from models.runner import Runner

class RunnerService:
    def __init__(self, runners_repository: runners_repository.RunnerRepository = Depends()):
        self.runners_repository = runners_repository

    def get_user_by_email(self, email: str) -> Runner | None:
        return self.runners_repository.get_user_by_email(email)

    def save(self, runner: Runner) -> Runner:
        return self.runners_repository.save(runner)