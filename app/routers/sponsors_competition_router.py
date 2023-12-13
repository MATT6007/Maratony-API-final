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
    
# @router.post("/assign-sponsorship/{sponsor_id}/{competition_id}")
# def assign_sponsorship(sponsor_id: int, competition_id: int):
#     sponsorship = SponsorCompetition(ID_sponsor=sponsor_id, ID_competition=competition_id)
#     db.add(sponsorship)
#     db.commit()
#     db.refresh(sponsorship)
#     return {"message": "Sponsorship assigned successfully"}


@router.post("/assign-sponsorship/{ID_sponsor}/{ID_competition}/{amountUSD}")
def assign_sponsorship(sponsorship_create: SponsorCompetitionCreate, sponsors_competition_services: SponsorCompetitionService = Depends()):
    if sponsorship_create.amountUSD < 0:
        raise HTTPException(status_code=400, detail="AmountUSD must be non-negative")

    print("---------------------------")
    print(sponsorship_create.amountUSD)
    print(sponsorship_create.ID_sponsor)
    print(sponsorship_create.ID_competition)

    sponsorship = sponsors_competition_services.create_sponsor_competition(sponsorship_create)
    return {"message": "Sponsorship assigned successfully"}

    # @router.post("/address", response_model=Address)
    # def create_address(address_create: AddressCreate, address_service: AddressService = Depends(),  
    #                 current_user: Runner = Depends(get_current_active_user)) -> Address:
    # address = address_service.create_address(address_create)
    # return address


    # address = address_service.create_address(address_create)
    # return address



    # if competition_name in sponsors:
    #     sponsors = competitions[competition_name]
    #     return {"competition": competition_name, "sponsors": sponsors}
    # else:
    #     raise HTTPException(status_code=404, detail="Competition not found")

# @router.get("/address/{address_id}", response_model=Address)
# def get_address(address_id: int, address_service: AddressService = Depends(),
#                current_user: Runner = Depends(get_current_active_user)) -> Address:
#     address = address_service.get_address(address_id)
#     if not address:
#         raise HTTPException(status_code=404, detail="Address not found")
#     return address

# @router.post("/address", response_model=Address)
# def create_address(address_create: AddressCreate, address_service: AddressService = Depends(),
#                     current_user: Runner = Depends(get_current_active_user)) -> Address:
#     address = address_service.create_address(address_create)
#     return address

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


