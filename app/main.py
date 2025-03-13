from fastapi import FastAPI
from app.crud import router

app = FastAPI(title="Product - CRUDAPI")

app.include_router(router)

@app.get("/")
def root():
    return {"Welcome to the E-SMART Product API"}
