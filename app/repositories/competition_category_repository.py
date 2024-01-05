from sqlalchemy.orm import Session
import schemas.competition_category_schema as schemas
from fastapi_pagination import Page
from dependencies.database import get_db
from fastapi import Depends
from models.competition_category import CompetitionCategory
from typing import Type
from fastapi_pagination.ext.sqlalchemy import paginate

class CompetitionCategoryRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def get_competition_category(self, competition_category_id: int) -> Type[CompetitionCategory] | None:
        return self.db.query(CompetitionCategory).filter(CompetitionCategory.ID_competition_category == competition_category_id).first()

    def get_competition_categories(self) -> Page[CompetitionCategory]:
        query = self.db.query(CompetitionCategory)
        return paginate(query)
        
    def create_competition_category(self, create_competition_category: schemas.CompetitionCategoryCreate):
        db_category = CompetitionCategory(**create_competition_category.dict())
        self.db.add(db_category)
        self.db.commit()
        self.db.refresh(db_category)
        return db_category

    def update_competition_category(self, competition_category_id: int, competition_category_update: schemas.CompetitionCategoryUpdate) -> Type[CompetitionCategory] | None:
          db_category = self.get_competition_category(competition_category_id_id)
          if db_category:
            for key, value in competition_category_update_update.dict().items():
                  setattr(db_address, key, value)
            self.db.commit()
            self.db.refresh(db_category)
          return db_category

    def delete_competition_category(self, competition_category_id: int):
        db_category = self.get_competition_category(competition_category_id)
        if db_category:
            self.db.delete(db_category)
            self.db.commit()
        return db_category

    def get_competition_categories(self, skip: int = 0, limit: int = 6):
        return self.db.query(CompetitionCategory).all()


    


    

   