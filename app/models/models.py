from sqlalchemy import Column, Integer, String, Text
from database.database import Base

class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    ingredients = Column(Text)
    instructions = Column(Text)