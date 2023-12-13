from pydantic import BaseModel

class AddressBase(BaseModel):
    city: str
    street: str
    postalCode: str

class AddressCreate(AddressBase):
    pass 
    
class AddressUpdate(AddressBase):
    # city: str = None
    # street: str = None
    # postalCode: str = None
    pass

class Address(AddressBase):
    ID_address: int

    class Config:
        orm_mode = True
