from typing import Type
from typing import List
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi_pagination import Page, Params
from repositories import address_repository
from models.address import Address
from schemas import address_schema

class AddressService:
    def __init__(self, address_repository: address_repository.AddressRepository = Depends()):
        self.address_repository = address_repository

    def get_address(self, address_id: int) -> Type[Address] | None:
        return self.address_repository.get_address(address_id)

    def get_addresses(self):
        return self.address_repository.get_addresses()

    def create_address(self, address_create: address_schema.AddressCreate) -> Address:
        return self.address_repository.create_address(address_create)

    def update_address(self, address_id: int, address_update: address_schema.AddressUpdate) -> Type[Address] | None:
        return self.address_repository.update_address(address_id, address_update)

    def delete_address(self, address_id: int) -> Type[Address] | None:
        return self.address_repository.delete_address(address_id)


