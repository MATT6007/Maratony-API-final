from typing import Type
from typing import List
from dependencies.auth import get_current_active_user
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi.responses import JSONResponse
from schemas.runners_schema import RunnerCreate, RunnerUpdate
from schemas.runners_schema import Runner as RunnerSchema
from schemas.runners_schema import RunnerCompetitionCreate
from schemas.runners_schema import RunnerRegistrationData
from schemas.runners_schema import TopRunner
from schemas.runners_schema import RunnerAddressClubUpdate
from schemas.runners_schema import RunnerSchemaSetPhoto
from schemas.competition_schema import Competition as CompetitionSchema
from services.runner_services import RunnerService 
from services.competition_services import CompetitionService 
from models.runner import Runner

router = APIRouter(tags=["Runner"])

@router.get("/runners", response_model=Page[RunnerSchema])
def get_runners(runner_service: RunnerService = Depends(), 
                  current_user: Runner = Depends(get_current_active_user)) -> Page[Runner]:
    runners = runner_service.get_runners()
    return runners
    

@router.get("/runner/{runner_id}", response_model=RunnerSchema)
def get_address(runner_id: int, runner_service: RunnerService = Depends(),
               current_user: Runner = Depends(get_current_active_user)) -> Runner:
    runner = runner_service.get_runner(runner_id)
    if not runner:
        raise HTTPException(status_code=404, detail="Runner not found")
    return runner

@router.post("/competition/{competition_id}/register")
async def register_for_competition(
    competition_id: int,
    form_data: RunnerRegistrationData,  
    current_user: Runner = Depends(get_current_active_user),
    competition_service: CompetitionService = Depends(),
    runner_service: RunnerService = Depends(),
):
    competition = competition_service.get_competition(competition_id)

    if not competition:
        raise HTTPException(status_code=404, detail="Competition not found")

    if runner_service.is_registered(current_user.ID_runner, competition_id):
        raise HTTPException(status_code=400, detail="Runner is already registered for this competition")

    runner_competition_data = RunnerCompetitionCreate(
        ID_runner=current_user.ID_runner,
        ID_competition=competition_id,
        is_paid=form_data.is_paid,
        is_started=False,
        is_disqualified=False,
        ice_first_name = form_data.iceFirstName,
        ice_last_name = form_data.iceLastName,
        ice_phone = form_data.icePhone
    )

    runner_competition = runner_service.create_runner_competition(runner_competition_data)

    return runner_competition

@router.get("/users/me/competitions", response_model=List[CompetitionSchema])
async def get_user_competitions(
    current_user: Runner = Depends(get_current_active_user),
    runner_service: RunnerService = Depends()
):
    try:
        user_competitions = runner_service.get_user_competitions(current_user.ID_runner)
        return user_competitions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/top-runners")
def get_top_runners(runner_service: RunnerService = Depends()):
    top_runners = runner_service.get_top_runners()
    return top_runners

@router.post("/update-address-club", response_model=RunnerSchema)
def update_address_club(
    address_club_data: RunnerAddressClubUpdate,
    current_user: Runner = Depends(get_current_active_user),
    runner_service: RunnerService = Depends()
):
    return runner_service.update_address_club(current_user.ID_runner, address_club_data)

@router.post("/set-photo", response_model=RunnerSchema)
def set_profile_photo(
    image_url: RunnerSchemaSetPhoto,
    current_user: Runner = Depends(get_current_active_user),
    runner_service: RunnerService = Depends()
):
    updated_runner = runner_service.update_profile_photo(current_user.ID_runner, image_url)
    return updated_runner



