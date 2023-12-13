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
    

# @router.get("/address/{address_id}", response_model=Address)
# def get_address(address_id: int, address_service: AddressService = Depends(),
#                current_user: Runner = Depends(get_current_active_user)) -> Address:
#     address = address_service.get_address(address_id)
#     if not address:
#         raise HTTPException(status_code=404, detail="Address not found")
#     return address

@router.post("/sponsors", response_model=Sponsors)
def create_sponsor(sponsor_create: SponsorsCreate, sponsor_service: SponsorsService = Depends(),
                    current_user: Runner = Depends(get_current_active_user)) -> Sponsors:
    sponsor = sponsor_service.create_sponsor(sponsor_create)
    return sponsor

# @router.put("/address/{address_id}", response_model=Address)
# def update_address(address_id: int, address_update: AddressUpdate, address_service: AddressService = Depends(),
#                   current_user: Runner = Depends(get_current_active_user)) -> Address:
#     address = address_service.update_address(address_id, address_update)
#     if not address:
#         raise HTTPException(status_code=404, detail="Address not found")
#     return address


# @router.delete("/address/{address_id}", response_model=Address)
# def delete_address(address_id: int, address_service: AddressService = Depends(),
#                   current_user: Runner = Depends(get_current_active_user)) -> Address:
#     address = address_service.delete_address(address_id)
#     if not address:
#         raise HTTPException(status_code=404, detail="Address not found")
#     return address


