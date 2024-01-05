from sqlalchemy.orm import Session
from typing import Type
from typing import List
from fastapi import Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from dependencies.database import get_db
import schemas.runners_schema as schemas
from models.runner import Runner
from models.competition import Competition
from models.runner_competition import RunnerCompetition
from models.address import Address
from schemas import runners_schema
from sqlalchemy import func

class RunnerRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_runner(self, create_runner: schemas.RunnerCreate):
        db_runner = Runner(**create_runner.dict())
        self.db.add(db_runner)
        self.db.commit()
        self.db.refresh(db_runner)
        return db_runner

    def get_runners(self) -> Page[Runner]:
        query = self.db.query(Runner)
        return paginate(query)

    def get_runner(self, runner_id: int):
        return self.db.query(Runner).filter(Runner.ID_runner == runner_id).first()

    def save(self, runner: Runner) -> Runner:
        self.db.add(runner)
        self.db.commit()
        self.db.refresh(runner)
        return runner

    def get_user_by_email(self, email: str) -> Runner | None:
        return self.db.query(Runner).filter(Runner.email == email).first()

    def is_registered(self, runner_id: int, competition_id: int) -> bool:
        competition_registration = (
            self.db.query(RunnerCompetition)
            .filter_by(ID_runner=runner_id, ID_competition=competition_id)
            .first()
        )
        return competition_registration is not None

    def create_runner_competition(self, create_runner_competition: runners_schema.RunnerCompetitionCreate):
        db_runner_competition = RunnerCompetition(**create_runner_competition.dict())
        self.db.add(db_runner_competition)
        self.db.commit()
        self.db.refresh(db_runner_competition)
        return db_runner_competition

    def get_user_competitions(self, runner_id: int) -> List[Competition]:
        return self.db.query(Competition).join(RunnerCompetition).filter(RunnerCompetition.ID_runner == runner_id).all()

    def get_top_runners(self, skip: int = 0, limit: int = 3):
        top_runners = (
            self.db.query(
                Runner.ID_runner,
                Runner.first_name,
                Runner.last_name,
                Runner.date_of_birth,
                Runner.club, 
                Runner.image_url,
                func.count(Runner.ID_runner).label("races_participated"),
            )
            .outerjoin(RunnerCompetition)
            .group_by(Runner.ID_runner)
            .order_by(func.count(Runner.ID_runner).desc())
            .offset(skip)
            .limit(limit)
            .all()
        )
        return top_runners

    def update_address_club(self, runner_id: int, address_club_data: schemas.RunnerAddressClubUpdate):
        runner = self.db.query(Runner).filter(Runner.ID_runner == runner_id).first()
        
        if runner:
            if not runner.address:
                new_address = Address(
                    street=address_club_data.street,
                    city=address_club_data.city,
                    postalCode=address_club_data.postalCode
                )
                runner.address = new_address
            else:
                runner.address.street = address_club_data.street
                runner.address.city = address_club_data.city
                runner.address.postalCode = address_club_data.postalCode

            runner.club = address_club_data.club

            self.db.commit()
            self.db.refresh(runner)

        return runner


    def update_profile_photo(self, runner_id: int, image_url: schemas.RunnerSchemaSetPhoto) -> Runner:
        runner = self.db.query(Runner).filter(Runner.ID_runner == runner_id).first()
        if runner:
            runner.image_url = image_url.image_url
            self.db.commit()
            self.db.refresh(runner)
        return runner
