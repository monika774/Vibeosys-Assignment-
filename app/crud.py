from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Product
from app.schema import ProductResponse, ProductCreate, ProductUpdate

router = APIRouter(prefix="/product", tags=["Products"])

def get_products(db: Session, skip: int = 0, limit: int = 10):
    
    """ Get all product from the database """
    
    return db.query(Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    
    """Get a single product by id """
    
    return db.query(Product).filter(Product.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    
    """Create a new product in the databse """
    
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    
    """Update a product in the database """
    
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        for key, value in product.dict(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product



@router.get("/API/product/list –", response_model=List[ProductResponse])
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    
    """"List of all products"""
    
    return get_products(db, skip=skip, limit=limit)

@router.get("/API/product/{pid}/info", response_model=ProductResponse)
def product_info(pid: int, db: Session = Depends(get_db)):
    
    """"Get single product by id """
    
    product = get_product(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/API/product/add", response_model=ProductResponse)
def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    
    """"Create a new product and add into database"""
    
    return create_product(db, product)

@router.put("/API/product/{pid}/update", response_model=ProductResponse)
def update_product_api(pid: int, product: ProductUpdate, db: Session = Depends(get_db)):
    
    """Update product by id and add into database"""
    
    updated_product = update_product(db, pid, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product
