from typing import Type

from dependencies.auth import get_current_active_user
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page

# from models.competition_category import CompetitionCategory
from schemas.competition_category_schema import CompetitionCategoryCreate, CompetitionCategoryUpdate, CompetitionCategory
from services.competition_category_services import CompetitionCategoryService 
from models.runner import Runner


router = APIRouter(tags=["CompetitionCategory"])


@router.get("/competition_category", response_model=Page[CompetitionCategory])
def get_competition_category(competition_category_service: CompetitionCategoryService = Depends(), 
                  current_user: Runner = Depends(get_current_active_user)) -> Page[CompetitionCategory]:
    competition_categories = competition_category_service.get_competition_categories()
    return competition_categories
    

@router.get("/competition_category/{competition_category_id}", response_model=Type[CompetitionCategory])
def get_competition_category(competition_category_id: int, competition_category_service: CompetitionCategoryService = Depends(),
               current_user: Runner = Depends(get_current_active_user)) -> Type[CompetitionCategory]:
    category = competition_category_service.get_address(competition_category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Competition category not found")
    return category

@router.post("/competition_category", response_model=Type[CompetitionCategory])
def create_competition_category(competition_category_create: CompetitionCategoryCreate, competition_category_service: CompetitionCategoryService = Depends(),
                    current_user: Runner = Depends(get_current_active_user)) -> CompetitionCategory:
    category = competition_category_service.create_competition_category(competition_category_create)
    return category

@router.put("/competition_category/{competition_category_id}", response_model=Type[CompetitionCategory])
def update_competition_category(competition_category_id: int, competition_category_update: CompetitionCategoryUpdate, competition_category_service: CompetitionCategoryService = Depends(),
                  current_user: Runner = Depends(get_current_active_user)) -> Type[CompetitionCategory]:
    category = competition_category_service.update_competition_category(competition_category_id, competition_category_update)
    if not category:
        raise HTTPException(status_code=404, detail="Competition category not found")
    return category


@router.delete("/competition_category/{competition_category_id}", response_model=Type[CompetitionCategory])
def delete_competition_category(competition_category_id: int, competition_category_service: CompetitionCategoryService = Depends(),
                  current_user: Runner = Depends(get_current_active_user)) -> Type[CompetitionCategory]:
    category = competition_category_service.delete_competition_category(competition_category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Competition category not found")
    return category


