from http.client import HTTPException
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, database 
from app.controllers import recipe_controller
from app.schema.api_response import APIResponse, RecipeResponse

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
    response_model=APIResponse[RecipeResponse],
    summary="Create a new recipe",
    description="Create a new recipe with the provided details.",
)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    try:
        db_recipe = recipe_controller.create_recipe(db, recipe)

        response_data = RecipeResponse(
            id=db_recipe.id,
            title=db_recipe.title,
            description=db_recipe.description,
            ingredients=db_recipe.ingredients,
            instructions=db_recipe.instructions
        )

        return APIResponse[RecipeResponse](
            code=0,
            status="success",
            message="Recipe created successfully",
            data=response_data 
        )
    except Exception as e:
        print("Error creating recipe:", e)
        return APIResponse[RecipeResponse](
            code=1,
            status="error",
            message=str(e),
            data=None
        )

@router.get(
    "/",
    response_model=APIResponse[list[RecipeResponse]],
    summary="Get all recipes",
    description="Retrieve a list of all recipes.",
)
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        recipes = recipe_controller.read_recipes(db, skip=skip, limit=limit)
        
        response_data = [RecipeResponse(
            id=recipe.id,
            title=recipe.title,
            description=recipe.description,
            ingredients=recipe.ingredients,
            instructions=recipe.instructions
        ) for recipe in recipes]

        return APIResponse[list[RecipeResponse]](
            code=0,
            status="success",
            message="Recipes retrieved successfully",
            data=response_data
        )
    except Exception as e:
        print("Error retrieving recipes:", e)
        return APIResponse[list[RecipeResponse]](
            code=1,
            status="error",
            message=str(e),
            data=None
        )

@router.get(
    "/{recipe_id}",
    response_model=APIResponse[RecipeResponse],
    summary="Get a recipe by ID",
    description="Retrieve a specific recipe by its ID.",
)
def read_recipe(recipe_id: int, db: Session = Depends(get_db)):
    try:
        recipe = recipe_controller.read_recipe(db, recipe_id)
        
        response_data = RecipeResponse(
            id=recipe.id,
            title=recipe.title,
            description=recipe.description,
            ingredients=recipe.ingredients,
            instructions=recipe.instructions
        )

        return APIResponse[RecipeResponse](
            code=0,
            status="success",
            message="Recipe retrieved successfully",
            data=response_data
        )
    except HTTPException as e:
        return APIResponse[RecipeResponse](
            code=e.status_code,
            status="error",
            message=e.detail,
            data=None
        )
    except Exception as e:
        print("Error retrieving recipe:", e)
        return APIResponse[RecipeResponse](
            code=1,
            status="error",
            message=str(e),
            data=None
        )

@router.put(
    "/{recipe_id}",
    response_model=APIResponse[RecipeResponse],
    summary="Update a recipe",
    description="Update an existing recipe by its ID.",
)
def update_recipe(recipe_id: int, recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    try:
        updated_recipe = recipe_controller.update_recipe(db, recipe_id, recipe)
        
        response_data = RecipeResponse(
            id=updated_recipe.id,
            title=updated_recipe.title,
            description=updated_recipe.description,
            ingredients=updated_recipe.ingredients,
            instructions=updated_recipe.instructions
        )

        return APIResponse[RecipeResponse](
            code=0,
            status="success",
            message="Recipe updated successfully",
            data=response_data
        )
    except HTTPException as e:
        return APIResponse[RecipeResponse](
            code=e.status_code,
            status="error",
            message=e.detail,
            data=None
        )
    except Exception as e:
        print("Error updating recipe:", e)
        return APIResponse[RecipeResponse](
            code=1,
            status="error",
            message=str(e),
            data=None
        )

@router.delete(
    "/{recipe_id}",
    response_model=APIResponse[dict],
    summary="Delete a recipe",
    description="Delete a recipe by its ID.",
)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    try:
        recipe_controller.delete_recipe(db, recipe_id)
        
        return APIResponse[dict](
            code=0,
            status="success",
            message="Recipe deleted successfully",
            data={}
        )
    except HTTPException as e:
        return APIResponse[dict](
            code=e.status_code,
            status="error",
            message=e.detail,
            data=None
        )
    except Exception as e:
        print("Error deleting recipe:", e)
        return APIResponse[dict](
            code=1,
            status="error",
            message=str(e),
            data=None
        )
