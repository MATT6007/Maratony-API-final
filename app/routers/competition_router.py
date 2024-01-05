from typing import Type
from dependencies.auth import get_current_active_user
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from schemas.competition_schema import CompetitionCreate, CompetitionUpdate, Competition
from schemas.runners_schema import Runner as RunnerSchema
from schemas.results_schema import Results as ResultsSchema
from schemas.runners_schema import ResultWithRunner
from services.competition_services import CompetitionService 
from services.runner_services import RunnerService
from models.runner import Runner
from models.results import Results
from schemas.competition_schema import RunnerResultCreate

router = APIRouter(tags=["Competition"])

@router.get("/competition", response_model=Page[Competition])
def get_competitions(competition_service: CompetitionService = Depends(),
                   current_user: Runner = Depends(get_current_active_user)) -> Page[Competition]:
    competitions = competition_service.get_competitions()
    return competitions

@router.get("/competition/{competition_id}", response_model=Competition)
def get_competition(competition_id: int, competition_service: CompetitionService = Depends(),
               current_user: Runner = Depends(get_current_active_user)) -> Competition:
    competition = competition_service.get_competition(competition_id)
    if not competition:
        raise HTTPException(status_code=404, detail="Address not found")
    return competition

@router.post("/competition", response_model=Competition)
def create_competition(competition_create: CompetitionCreate, competition_service: CompetitionService = Depends(),
                    current_user: Runner = Depends(get_current_active_user)) -> Competition:
    competition = competition_service.create_competition(competition_create)
    return competition

@router.delete("/competition/{competition_id}", response_model=Competition)
def delete_competition(competition_id: int, competition_service: CompetitionService = Depends(),
                  current_user: Runner = Depends(get_current_active_user)) -> Competition:
    competition = competition_service.delete_competition(competition_id)
    if not competition:
        raise HTTPException(status_code=404, detail="Competition not found")
    return competition

@router.post("/add-results/{competition_id}", response_model=RunnerSchema)
def add_results(
    competition_id: int,
    results_data: RunnerResultCreate,
    current_user: Runner = Depends(get_current_active_user),
    competition_service: CompetitionService = Depends(),
    runner_service: RunnerService = Depends(),
):
   
    competition_service.add_runner_result(
        runner_id=current_user.ID_runner,
        competition_id=competition_id,
        full_time=results_data.full_time,
        half_time=results_data.half_time,
        is_started=results_data.is_started,
        is_disqualified=results_data.is_disqualified,
    )

    return runner_service.get_runner(runner_id=current_user.ID_runner)


@router.get("/results/{competition_id}")
def get_results_for_competition(
    competition_id: int,
    current_user: Runner = Depends(get_current_active_user),
    competition_service: CompetitionService = Depends(),
):
    competition = competition_service.get_competition(competition_id=competition_id)
    if not competition:
        raise HTTPException(status_code=404, detail="Competition not found")

    results = competition_service.get_results_for_competition(competition_id=competition_id)
    return results


