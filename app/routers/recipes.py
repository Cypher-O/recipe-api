from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, database 
from app.controllers import recipe_controller

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(
    "/",
    response_model=schemas.Recipe,
    summary="Create a new recipe",
    description="Create a new recipe with the provided details.",
    response_description="The created recipe.",
)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipe_controller.create_recipe(db, recipe)

@router.get(
    "/",
    response_model=list[schemas.Recipe],
    summary="Get all recipes",
    description="Retrieve a list of all recipes.",
)
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return recipe_controller.read_recipes(db, skip=skip, limit=limit)

@router.get(
    "/{recipe_id}",
    response_model=schemas.Recipe,
    summary="Get a recipe by ID",
    description="Retrieve a specific recipe by its ID.",
)
@router.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipe_controller.read_recipe(db, recipe_id)

@router.put(
    "/{recipe_id}",
    response_model=schemas.Recipe,
    summary="Update a recipe",
    description="Update an existing recipe by its ID.",
)
def update_recipe(recipe_id: int, recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipe_controller.update_recipe(db, recipe_id, recipe)

@router.delete(
    "/{recipe_id}",
    summary="Delete a recipe",
    description="Delete a recipe by its ID.",
)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipe_controller.delete_recipe(db, recipe_id)