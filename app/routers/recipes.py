from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, database
from ..controllers import recipe_controller

router = APIRouter()

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Recipe)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipe_controller.create_recipe(db, recipe)

@router.get("/", response_model=list[schemas.Recipe])
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return recipe_controller.read_recipes(db, skip=skip, limit=limit)

@router.get("/{recipe_id}", response_model=schemas.Recipe)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipe_controller.read_recipe(db, recipe_id)

@router.put("/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(recipe_id: int, recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return recipe_controller.update_recipe(db, recipe_id, recipe)

@router.delete("/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    return recipe_controller.delete_recipe(db, recipe_id)