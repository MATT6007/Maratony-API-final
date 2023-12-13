from sqlalchemy.orm import Session
from . import models
from ..schemas import results as schemas

def create_results(db: Session, results: schemas.ResultsCreate):
    db_results = models.Results(**results.dict())
    db.add(db_results)
    db.commit()
    db.refresh(db_results)
    return db_results

def get_results(db: Session, results_id: int):
    return db.query(models.Results).filter(models.Results.ID_results == results_id).first()
