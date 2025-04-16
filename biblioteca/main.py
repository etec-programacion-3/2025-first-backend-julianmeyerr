from models import Libro
from fastapi import FastAPI

app=FastAPI()

libros_db = []

@app.post("/libros/",response_model=Libro)
def crear_libro(nuevo_libro:Libro):
    libros_db.append(nuevo_libro)
    return nuevo_libro

@app.get("/libros/",response_model=list[Libro])
def obtener_libros():
    return libros_db

@app.get("/libros/{libro_id}",response_model=Libro)
def obtener_libro(libro_id: int):
    for x in libros_db:
        if x.id == libro_id:
            return x
    return {"ERROR" : "Libro no encontrado"}

@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int):
    for x in libros_db:
        if x.id == libro_id:
            libros_db.remove(x)
            return {"Mensaje" : "Libro eliminado"}
    return {"ERROR" : "Libro no encontrado"}

