from sqlalchemy.orm import Session
import schemas.sponsors_competition_schema as schemas
from pydantic import ValidationError
from dependencies.database import get_db
from models.sponsor_competition import SponsorCompetition
from typing import Type
from fastapi import Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from typing import List
from sqlalchemy import select
from models.sponsor_competition import SponsorCompetition
from models.competition import Competition
from models.sponsors import Sponsors

from dependencies.database import Base, engine  

class SponsorCompetitionRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_sponsor_competition(self, sponsor_competition: schemas.SponsorCompetitionCreate):
        db_sponsor_competition = SponsorCompetition(**sponsor_competition.dict())   
        self.db.add(db_sponsor_competition)
        self.db.commit()
        self.db.refresh(db_sponsor_competition)
        return db_sponsor_competition

    def get_sponsor_competition(self, sponsor_competition_id: int):
        return self.db.query(models.SponsorCompetition).filter(models.SponsorCompetition.ID_sponsor_competition == sponsor_competition_id).first()

    def get_sponsors_by_competition(self, competition_name: str):
        
        with Session(engine) as session:
            competition = session.query(Competition).filter_by(name=competition_name).first()
          
            if not competition:
                return None  

            sponsors = (
                session.query(Sponsors)
                .join(SponsorCompetition, Sponsors.ID_sponsor == SponsorCompetition.ID_sponsor)
                .filter(SponsorCompetition.ID_competition == competition.ID_competition)
                .all()
            )

            return sponsors

    # def get_sponsors_competition_all(self):
    #     with Session(engine) as session:
    #         results = (
    #             session.query(SponsorCompetition, Sponsors, Competition)
    #             .join(Sponsors, SponsorCompetition.ID_sponsor == Sponsors.ID_sponsor)
    #             .join(Competition, SponsorCompetition.ID_competition == Competition.ID_competition)
    #             .all()
    #         )

    #         sponsors_with_competitions = []
    #         for sponsor_competition, sponsor, competition in results:
    #             sponsors_with_competitions.append({
    #                 "sponsor_id": sponsor.ID_sponsor,
    #                 "sponsor_name": sponsor.name,  # Dodaj odpowiednie pole, w zależności od struktury tabeli Sponsors
    #                 "competition_id": competition.ID_competition,
    #                 "competition_name": competition.name,  # Dodaj odpowiednie pole, w zależności od struktury tabeli Competition
    #                 "amount_usd": sponsor_competition.amountUSD
    #         })

    #         return sponsors_with_competitions


    def get_sponsors_competition_all(self):
        with Session(engine) as session:
            results = (
                session.query(SponsorCompetition, Sponsors, Competition)
                .join(Sponsors, SponsorCompetition.ID_sponsor == Sponsors.ID_sponsor)
                .join(Competition, SponsorCompetition.ID_competition == Competition.ID_competition)
                .all()
            )

            sponsors_with_competitions = []
            for sponsor_competition, sponsor, competition in results:
                sponsors_with_competitions.append({
                    "sponsor_competition_id": sponsor_competition.ID,
                    "sponsor_id": sponsor.ID_sponsor,
                    "sponsor_name": sponsor.email, 
                    "competition_id": competition.ID_competition,
                    "competition_name": competition.name,  
                    "amount_usd": sponsor_competition.amountUSD
                })

            return sponsors_with_competitions

        
