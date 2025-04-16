from pydantic import BaseModel

class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    anio: int
    genero: str