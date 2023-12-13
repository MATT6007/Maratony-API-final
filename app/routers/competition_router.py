from typing import Type

from dependencies.auth import get_current_active_user
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page

from schemas.competition_schema import CompetitionCreate, CompetitionUpdate, Competition
from services.competition_services import CompetitionService 
from models.runner import Runner

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