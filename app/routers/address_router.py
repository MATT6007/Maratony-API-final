from typing import Type
from typing import List

from dependencies.auth import get_current_active_user
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi.responses import JSONResponse

from schemas.address_schema import AddressCreate, AddressUpdate, Address
from services.address_services import AddressService 
from models.runner import Runner

router = APIRouter(tags=["Address"])

@router.get("/address", response_model=Page[Address])
def get_addresses(address_service: AddressService = Depends(), 
                  current_user: Runner = Depends(get_current_active_user)) -> Page[Address]:
    addresess = address_service.get_addresses()
    return addresess
    

@router.get("/address/{address_id}", response_model=Address)
def get_address(address_id: int, address_service: AddressService = Depends(),
               current_user: Runner = Depends(get_current_active_user)) -> Address:
    address = address_service.get_address(address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router.post("/address", response_model=Address)
def create_address(address_create: AddressCreate, address_service: AddressService = Depends(),
                    current_user: Runner = Depends(get_current_active_user)) -> Address:
    address = address_service.create_address(address_create)
    return address

@router.put("/address/{address_id}", response_model=Address)
def update_address(address_id: int, address_update: AddressUpdate, address_service: AddressService = Depends(),
                  current_user: Runner = Depends(get_current_active_user)) -> Address:
    address = address_service.update_address(address_id, address_update)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


@router.delete("/address/{address_id}", response_model=Address)
def delete_address(address_id: int, address_service: AddressService = Depends(),
                  current_user: Runner = Depends(get_current_active_user)) -> Address:
    address = address_service.delete_address(address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


