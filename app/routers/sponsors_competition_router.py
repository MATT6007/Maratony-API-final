from typing import Type
from typing import List

from dependencies.auth import get_current_active_user
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi.responses import JSONResponse

from schemas.sponsors_competition_schema import SponsorCompetitionCreate, SponsorCompetitionUpdate, SponsorCompetition
from services.sponsors_competition_services import SponsorCompetitionService 
from models.runner import Runner

router = APIRouter(tags=["SponsorCompetition"])

@router.get("/competitions/{competition_name}/sponsors")
def get_sponsors_by_competition(
                  competition_name: str,
                  sponsors_competition_services: SponsorCompetitionService = Depends(), 
                  current_user: Runner = Depends(get_current_active_user)):

    sponsors = sponsors_competition_services.get_sponsors_by_competition(competition_name)
    return sponsors


@router.get("/competition/sponsors/all")
def get_addresses(sponsors_competition_services: SponsorCompetitionService = Depends(), 
                  current_user: Runner = Depends(get_current_active_user)):
    sponsors = sponsors_competition_services.get_sponsors_competition_all()
    return sponsors
    
@router.post("/assign-sponsorship/{ID_sponsor}/{ID_competition}/{amountUSD}")
def assign_sponsorship(sponsorship_create: SponsorCompetitionCreate, sponsors_competition_services: SponsorCompetitionService = Depends()):
    if sponsorship_create.amountUSD < 0:
        raise HTTPException(status_code=400, detail="AmountUSD must be non-negative")


    sponsorship = sponsors_competition_services.create_sponsor_competition(sponsorship_create)
    return {"message": "Sponsorship assigned successfully"}

    