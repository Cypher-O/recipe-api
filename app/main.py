from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import OpenAPI
from app.database import engine
from app.models import Base
from app.routers import recipes

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Recipe API",
    description="A simple API to manage recipes.",
    version="1.0.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Your Name",
        "email": "your.email@example.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
)

app.include_router(recipes.router, prefix="/v1/recipes", tags=["recipes"])