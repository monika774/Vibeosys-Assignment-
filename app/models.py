from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, Enum, func
from app.database import Base

# Added emun for the category and unit of mrasure
category_enum = Enum("finished", "semi-finished", "raw", name="category_enum", create_type=True)
unit_enum = Enum("mtr", "mm", "ltr", "ml", "cm", "mg", "gm", "unit", "pack", name="unit_enum", create_type=True)

class Product(Base):
    
    """  Product model to store the product details   """
    
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    category = Column(category_enum, nullable=False)  
    description = Column(String(250), nullable=True)
    product_image = Column(Text, nullable=True)
    sku = Column(String(100), unique=True, nullable=False)
    unit_of_measure = Column(unit_enum, nullable=False) 
    lead_time = Column(Integer, nullable=False)
    created_date = Column(TIMESTAMP, server_default=func.now())
    updated_date = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
