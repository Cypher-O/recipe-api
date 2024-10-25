from fastapi import FastAPI
from database.database import engine
from app.models import Base
from app.routers import recipes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(recipes.router, prefix="/v1/recipes", tags=["recipes"])