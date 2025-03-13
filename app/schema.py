from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):

    """ Base schema for product """

    name: str
    category: str
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: str
    unit_of_measure: str
    lead_time: int

class ProductCreate(ProductBase):

    """Schema for creating new product """

    pass

class ProductUpdate(ProductBase):

    """Schema for updating existing product"""

    pass

class ProductResponse(ProductBase):

    """Schema for product response"""

    id: int
    created_date: datetime
    updated_date: datetime

    class Config:
        """ ORM configuration """
        from_attributes = True 
