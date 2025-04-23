from pydantic import BaseModel

class Libro(BaseModel):
    id: int
    titulo: str
    autor: str
    anio: int
    genero: str

class Usuario(BaseModel):
    id: int
    nombre: str
    contrasena: str
    rol: str
    status: str

class IniciarSesion(BaseModel):
    id: int
    contrasena: str