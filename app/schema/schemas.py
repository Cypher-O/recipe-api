from pydantic import BaseModel

class RecipeBase(BaseModel):
    title: str
    description: str
    ingredients: str
    instructions: str

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True