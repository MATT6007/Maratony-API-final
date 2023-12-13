from sqlalchemy.orm import Session
import schemas.competition_schema as schemas
from fastapi_pagination import Page
from dependencies.database import get_db
from fastapi import Depends
from models.competition import Competition
from typing import Type
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload


from fastapi import FastAPI, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi_pagination.ext.sqlalchemy import paginate

class CompetitionRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_competition(self, create_competition: schemas.CompetitionCreate):
        try:
            db_competition = Competition(**create_competition.dict())
            self.db.add(db_competition)
            self.db.commit()
            self.db.refresh(db_competition)
            return db_competition
        except IntegrityError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Competition with this ID already exists")
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def get_competitions(self) -> Page[Competition]:
        query = self.db.query(Competition)
        return paginate(query)

    def get_competition(self, competition_id: int):
        return (
            self.db.query(Competition)
            .filter(Competition.ID_competition == competition_id)
            .options(
                joinedload(Competition.address),
                joinedload(Competition.competition_category)
            )
            .first()
        )



