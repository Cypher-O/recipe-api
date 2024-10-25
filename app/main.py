from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import recipes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(recipes.router, prefix="/v1/recipes", tags=["recipes"])