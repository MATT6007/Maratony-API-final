from sqlalchemy.orm import Session
import schemas.address_schema as schemas
from pydantic import ValidationError
from dependencies.database import get_db
from models.address import Address 
from typing import Type
from fastapi import Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from typing import List
from sqlalchemy import select

class AddressRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    
    def create_address(self, create_address: schemas.AddressCreate):
        db_address = Address(**create_address.dict())
        self.db.add(db_address)
        self.db.commit()
        self.db.refresh(db_address)
        return db_address

    def get_address(self, address_id: int) -> Address:
        return self.db.query(Address).filter(Address.ID_address == address_id).first()

    def get_addresses(self) -> Page[Address]:
        query = self.db.query(Address)
        return paginate(query)
        
    
    def update_address(self, address_id: int, address_update: schemas.AddressUpdate) -> Address | None:
        db_address = self.get_address(address_id)
        if db_address:
            for key, value in address_update.dict().items():
                setattr(db_address, key, value)
            self.db.commit()
            self.db.refresh(db_address)
        return db_address

    def delete_address(self, address_id: int) -> Address | None:
        db_address = self.get_address(address_id)
        if db_address:
            self.db.delete(db_address)
            self.db.commit()
        return db_address

    

