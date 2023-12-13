from sqlalchemy.orm import Session
import schemas.sponsors_schema as schemas
from pydantic import ValidationError
from dependencies.database import get_db
from models.sponsors import Sponsors
from typing import Type
from fastapi import Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from typing import List
from sqlalchemy import select

class SponsorsRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        
    def create_sponsor(self, create_sponsor: schemas.SponsorsCreate):
        db_sponsor = Sponsors(**create_sponsor.dict())
        self.db.add(db_sponsor)
        self.db.commit()
        self.db.refresh(db_sponsor)
        return db_sponsor

    def get_sponsor(self, sponsor_id: int):
        return db.query(models.Sponsors).filter(models.Sponsors.ID_sponsor == sponsor_id).first()

    def get_sponsors(self) -> Page[Sponsors]:
        query = self.db.query(Sponsors)
        return paginate(query)
