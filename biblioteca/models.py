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
    token: int = None
    hist_prest : list = []

class IniciarSesion(BaseModel):
    id: int
    contrasena: str

class Prestamo(BaseModel):
    id: int
    libro_id: int
    usuario_id: int
    devuelto : bool