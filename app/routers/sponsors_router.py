from typing import Type
from typing import List
from dependencies.auth import get_current_active_user
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi.responses import JSONResponse
from schemas.sponsors_schema import SponsorsCreate, SponsorsUpdate, Sponsors
from services.sponsors_services import SponsorsService 
from models.runner import Runner

router = APIRouter(tags=["Sponsors"])

@router.get("/sponsors", response_model=Page[Sponsors])
def get_sponsors(sponsors_service: SponsorsService = Depends(), 
                  current_user: Runner = Depends(get_current_active_user)) -> Page[Sponsors]:
    sponsors = sponsors_service.get_sponsors()
    return sponsors

@router.post("/sponsors", response_model=Sponsors)
def create_sponsor(sponsor_create: SponsorsCreate, sponsor_service: SponsorsService = Depends(),
                    current_user: Runner = Depends(get_current_active_user)) -> Sponsors:
    sponsor = sponsor_service.create_sponsor(sponsor_create)
    return sponsor




