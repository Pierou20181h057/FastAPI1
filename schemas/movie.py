from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=2,  max_length=15)
    overview: str = Field(min_length=15,  max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=2, max_length=15)

    class Config:
        schema_extra = {
            "examen": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripción de la pelicula",
                "year": 2022,
                "rating": 9.8,
                "category": "Acción"
            }
        }