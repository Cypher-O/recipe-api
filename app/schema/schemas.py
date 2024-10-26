from pydantic import BaseModel, Field

class RecipeBase(BaseModel):
    title: str = Field(..., example="Spaghetti Carbonara")
    description: str = Field(..., example="A classic Italian pasta dish made with eggs, cheese, pancetta, and pepper.")
    ingredients: str = Field(..., example="Spaghetti, eggs, cheese, pancetta, pepper")
    instructions: str = Field(..., example="1. Boil water... 2. Cook spaghetti...")

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True
        
# from pydantic import BaseModel

# class RecipeBase(BaseModel):
#     title: str
#     description: str
#     ingredients: str
#     instructions: str

# class RecipeCreate(RecipeBase):
#     pass

# class Recipe(RecipeBase):
#     id: int

#     class Config:
#         orm_mode = True