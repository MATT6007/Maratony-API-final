from sqlalchemy.orm import Session
from . import models
from ..schemas import runner_competition as schemas

def create_runner_competition(db: Session, runner_competition: schemas.RunnerCompetitionCreate):
    db_runner_competition = models.RunnerCompetition(**runner_competition.dict())
    db.add(db_runner_competition)
    db.commit()
    db.refresh(db_runner_competition)
    return db_runner_competition

def get_runner_competition(db: Session, runner_competition_id: int):
    return db.query(models.RunnerCompetition).filter(models.RunnerCompetition.ID_runner_competition == runner_competition_id).first()
