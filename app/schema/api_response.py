from pydantic import BaseModel
from typing import Optional, Generic, TypeVar, Dict

DataType = TypeVar('DataType')

class RecipeResponse(BaseModel):
    id: int
    title: str
    description: str
    ingredients: str
    instructions: str

class APIResponse(Generic[DataType], BaseModel):
    code: int
    status: str
    message: str
    data: Optional[DataType] 

    class Config:
        schema_extra = {
            "example": {
                "code": 0,
                "status": "success",
                "message": "Operation completed successfully",
                "data": {},  
            }
        }
