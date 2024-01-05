from sqlalchemy.orm import Session
import schemas.competition_schema as schemas
from fastapi_pagination import Page
from dependencies.database import get_db
from fastapi import Depends
from models.competition import Competition
from models.results import Results
from models.runner_competition import RunnerCompetition
from typing import Type
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from fastapi import FastAPI, HTTPException, Depends, Body
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi_pagination.ext.sqlalchemy import paginate

from models.runner import Runner

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

    def delete_competition(self, competition_id: int) -> Competition | None:
        db_competition = self.get_competition(competition_id)
        if db_competition:
            self.db.delete(db_competition)
            self.db.commit()
        return db_competition

    def create_runner_result(self, runner: Runner, competition: Competition, full_time: str, half_time: str, is_started: bool, is_disqualified: bool):
        result = Results(full_time=full_time, half_time=half_time, runner=runner, competition=competition)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        runner_competition = (
            self.db.query(RunnerCompetition)
            .filter(RunnerCompetition.ID_runner == runner.ID_runner)
            .filter(RunnerCompetition.ID_competition == competition.ID_competition)
            .first()
        )

        if runner_competition:
            runner_competition.is_started = is_started
            runner_competition.is_disqualified = is_disqualified
        else:
            runner_competition = RunnerCompetition(
                ID_runner=runner.ID_runner,
                ID_competition=competition.ID_competition,
                is_started=is_started,
                is_disqualified=is_disqualified
            )
            self.db.add(runner_competition)


        self.db.commit()
        self.db.refresh(runner_competition)

        return result

    def get_results_for_competition(self, competition_id: int):
        results = (
            self.db.query(Results)
            .filter(Results.ID_competition == competition_id)
            .all()
        )

        result_data = []
        for result in results:
            runner_competition = (
                self.db.query(RunnerCompetition)
                .filter(RunnerCompetition.ID_runner == result.ID_runner)
                .filter(RunnerCompetition.ID_competition == result.ID_competition)
                .first()
            )

            result_data.append({
                "ID_results": result.ID_results,
                "full_time": result.full_time,
                "half_time": result.half_time,
                "runner_id": result.ID_runner,
                "runner": {
                    "ID_runner": result.runner.ID_runner,
                    "first_name": result.runner.first_name,
                    "second_name": result.runner.last_name,
                },
                "competition_id": result.ID_competition,
                "competition": {
                    "ID_competition": result.competition.ID_competition,
                    "name": result.competition.name,
                },
                "is_started": runner_competition.is_started if runner_competition else None,
                "is_disqualified": runner_competition.is_disqualified if runner_competition else None,
            })

        return result_data


        