from sqlalchemy.orm import Session
from typing import Type
from fastapi import Depends
from dependencies.database import get_db
import schemas.runners_schema as schemas
from models.runner import Runner

class RunnerRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_runner(self, create_runner: schemas.RunnerCreate):
        db_runner = models.Runner(**runner.dict())
        self.db.add(db_runner)
        self.db.commit()
        self.db.refresh(db_runner)
        return db_runner

    def get_runner(self, runner_id: int):
        return db.query(models.Runner).filter(models.Runner.ID_runner == runner_id).first()

    def save(self, runner: Runner) -> Runner:
        self.db.add(runner)
        self.db.commit()
        self.db.refresh(runner)
        return runner

    def get_user_by_email(self, email: str) -> Runner | None:
        return self.db.query(Runner).filter(Runner.email == email).first()
