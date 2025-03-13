from fastapi import FastAPI
from app.crud import router
from app.database import engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Product API")

# Include the routes
app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Product API"}
